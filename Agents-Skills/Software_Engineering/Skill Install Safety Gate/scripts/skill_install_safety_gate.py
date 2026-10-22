#!/usr/bin/env python3
"""Static pre-install safety gate for Codex/OpenClaw-style skill packages."""

from __future__ import annotations

import argparse
import ast
import csv
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


class SafetyGateError(Exception):
    pass


TOP_LEVEL_FIELDS = [
    "input",
    "package_summary",
    "compatibility_checks",
    "security_findings",
    "install_plan",
    "install_result",
    "gate_decision",
    "assumptions",
    "next_steps",
    "generated_at",
]

FINDING_CSV_FIELDS = [
    "id",
    "severity",
    "category",
    "title",
    "file",
    "evidence",
    "recommendation",
    "decision_impact",
]

COMPATIBILITY_CSV_FIELDS = ["id", "status", "check", "detail", "evidence"]

TEXT_SUFFIXES = {
    "",
    ".bat",
    ".cmd",
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".sh",
    ".toml",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}

BINARY_SUFFIXES = {
    ".7z",
    ".bin",
    ".dll",
    ".dmg",
    ".exe",
    ".iso",
    ".jar",
    ".msi",
    ".pyd",
    ".so",
}

RUNTIME_SUFFIXES = {".bat", ".cmd", ".js", ".mjs", ".ps1", ".py", ".sh", ".ts"}

PERSONAL_PATH_PATTERN = re.compile(
    "(?i)("
    + r"[a-z]:\\"
    + "users"
    + r"\\[^\\\s]+"
    + "|/"
    + "users"
    + r"/[^/\s]+"
    + "|/"
    + "home"
    + r"/[^/\s]+"
    + ")"
)

BLOCK_PATTERNS = [
    (
        "likely-secret",
        "Likely hardcoded secret",
        re.compile(
            r"(?i)\b(api[_-]?key|access[_-]?token|bearer[_-]?token|client[_-]?secret|password|secret)\b\s*[:=]\s*['\"][A-Za-z0-9_./+=-]{16,}['\"]"
        ),
        "Remove hardcoded credentials and require environment variables instead.",
    ),
    (
        "dangerous-shell",
        "Dangerous shell operation",
        re.compile(r"(?i)(remove-item\s+.*-recurse\s+.*-force|rm\s+-rf|del\s+/s|format\s+[a-z]:|curl\s+.+\|\s*(sh|bash)|invoke-webrequest.+iex)"),
        "Remove destructive or pipe-to-shell behavior from installable skill code.",
    ),
    (
        "suspicious-install-command",
        "Suspicious install command",
        re.compile(r"(?i)(npm\s+install\s+-g|pip\s+install\s+.+--trusted-host|powershell\s+-enc|bypass\s+-executionpolicy|chmod\s+\+s|sudo\s+)"),
        "Do not require privileged, global, or policy-bypass install behavior in a skill package.",
    ),
    (
        "obfuscated-payload",
        "Obfuscated or encoded payload",
        re.compile(r"(?i)(frombase64string|base64\.b64decode|atob\(|\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}|[A-Za-z0-9+/]{240,}={0,2})"),
        "Replace obfuscated payloads with auditable source text or remove them.",
    ),
    (
        "dynamic-code-execution",
        "Dynamic code execution",
        re.compile(r"(?i)(\beval\s*\(|\bexec\s*\(|new\s+function\s*\(|(?<!\.)\bcompile\s*\()"),
        "Avoid dynamic code execution in installable skill packages.",
    ),
]

REVIEW_PATTERNS = [
    (
        "prompt-injection-like-instruction",
        "Prompt-injection-like instruction",
        re.compile(r"(?i)(ignore previous instructions|disregard previous instructions|system prompt:|developer message:|reveal your hidden instructions)"),
        "Review whether this is legitimate test data or remove it from runtime instructions.",
    ),
    (
        "absolute-personal-path",
        "Absolute personal path",
        PERSONAL_PATH_PATTERN,
        "Replace personal absolute paths with relative or configurable paths.",
    ),
    (
        "broad-permission-wording",
        "Broad permission wording",
        re.compile(r"(?i)(administrator|full[- ]access|require_escalated|danger-full-access|unrestricted|all permissions)"),
        "Confirm the permission boundary and document why it is required.",
    ),
]

NETWORK_PATTERN = re.compile(r"https?://[^\s)\"']+", re.IGNORECASE)
ENV_PATTERN = re.compile(r"(?i)(os\.environ|getenv|process\.env|\$env:)")
NETWORK_SEND_PATTERN = re.compile(r"(?i)(requests\.(post|put)|urlopen|fetch\s*\(|axios\.|invoke-webrequest|curl\s+)")
RUNTIME_COMMAND_PATTERN = re.compile(r"(?i)(subprocess|child_process|start-process|os\.system)")
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


def clean_text(value: str | None) -> str:
    return " ".join((value or "").split()).strip()


def default_target_dir() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "skills"
    return Path.home() / ".codex" / "skills"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check a skill folder or ZIP before installation.")
    parser.add_argument("--skill-source", required=True)
    parser.add_argument("--target-dir", default=str(default_target_dir()))
    parser.add_argument("--target-runtime", choices=("codex-openclaw",), default="codex-openclaw")
    parser.add_argument("--install-on-pass", action="store_true")
    parser.add_argument("--out-json", default="output.json")
    parser.add_argument("--out-md", default="install-safety-report.md")
    parser.add_argument("--out-findings-csv", default="security-findings.csv")
    parser.add_argument("--out-compatibility-csv", default="compatibility-checks.csv")
    parser.add_argument("--out-install-receipt", default="")
    return parser.parse_args(argv)


def finding(
    severity: str,
    category: str,
    title: str,
    file: str,
    evidence: str,
    recommendation: str,
    decision_impact: str,
) -> dict[str, Any]:
    return {
        "id": "",
        "severity": severity,
        "category": category,
        "title": title,
        "file": file,
        "evidence": clean_text(evidence)[:240],
        "recommendation": recommendation,
        "decision_impact": decision_impact,
    }


def check(status: str, name: str, detail: str, evidence: list[str] | str) -> dict[str, Any]:
    return {
        "id": "",
        "status": status,
        "check": name,
        "detail": detail,
        "evidence": evidence if isinstance(evidence, list) else [evidence],
    }


def number_rows(rows: list[dict[str, Any]], prefix: str) -> list[dict[str, Any]]:
    for index, row in enumerate(rows, start=1):
        row["id"] = f"{prefix}-{index:03d}"
    return rows


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def analysis_text_for_path(path: Path, text: str) -> str:
    if path.suffix.lower() != ".py":
        return text
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    lines = text.splitlines(keepends=True)

    def blank_span(start_line: int, start_col: int, end_line: int, end_col: int) -> None:
        for line_number in range(start_line, end_line + 1):
            line = lines[line_number - 1]
            span_start = start_col if line_number == start_line else 0
            span_end = end_col if line_number == end_line else len(line)
            lines[line_number - 1] = line[:span_start] + (" " * (span_end - span_start)) + line[span_end:]

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Attribute) or node.func.attr != "compile":
            continue
        if not isinstance(node.func.value, ast.Name) or node.func.value.id != "re":
            continue
        for arg in node.args:
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str) and hasattr(arg, "end_lineno"):
                # Regex literals often contain dangerous examples as detection rules, not executable behavior.
                blank_span(arg.lineno, arg.col_offset, arg.end_lineno, arg.end_col_offset)
    return "".join(lines)


def is_safe_zip_member(name: str) -> bool:
    normalized = name.replace("\\", "/")
    if not normalized or normalized.startswith("/") or re.match(r"^[A-Za-z]:", normalized):
        return False
    parts = PurePosixPath(normalized).parts
    return ".." not in parts


def safe_extract_zip(zip_path: Path, destination: Path) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            if not is_safe_zip_member(info.filename):
                findings.append(
                    finding(
                        "high",
                        "zip-path-traversal",
                        "ZIP entry attempts to write outside the extraction root",
                        info.filename,
                        info.filename,
                        "Reject the archive and request a clean package without traversal paths.",
                        "block",
                    )
                )
                continue
            target = destination / info.filename.replace("\\", "/")
            resolved = target.resolve()
            if destination.resolve() not in resolved.parents and resolved != destination.resolve():
                findings.append(
                    finding(
                        "high",
                        "zip-path-traversal",
                        "ZIP entry resolves outside the extraction root",
                        info.filename,
                        info.filename,
                        "Reject the archive and request a clean package without traversal paths.",
                        "block",
                    )
                )
                continue
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, target.open("wb") as handle:
                    shutil.copyfileobj(source, handle)
    return findings


def find_skill_root(scan_root: Path) -> tuple[Path | None, list[dict[str, Any]]]:
    skill_files = [path for path in scan_root.rglob("SKILL.md") if "__MACOSX" not in path.parts]
    if (scan_root / "SKILL.md").exists():
        return scan_root, []
    if len(skill_files) == 1:
        return skill_files[0].parent, []
    if not skill_files:
        return None, [
            finding(
                "high",
                "missing-skill-md",
                "Missing SKILL.md",
                "",
                "No SKILL.md found in the supplied package.",
                "Provide an installable skill root containing SKILL.md.",
                "block",
            )
        ]
    return None, [
        finding(
            "high",
            "ambiguous-skill-root",
            "Multiple skill roots found",
            "",
            ", ".join(str(path.relative_to(scan_root)) for path in skill_files[:10]),
            "Install one skill package at a time or provide the exact skill root.",
            "block",
        )
    ]


def prepare_source(source: Path, temp_root: Path) -> tuple[str, Path, Path | None, list[dict[str, Any]]]:
    findings: list[dict[str, Any]] = []
    if not source.exists():
        raise SafetyGateError(f"Skill source not found: {source}")
    if source.is_file():
        if source.suffix.lower() != ".zip":
            raise SafetyGateError("Skill source must be a folder or .zip file.")
        scan_root = temp_root / "extracted"
        scan_root.mkdir(parents=True, exist_ok=True)
        try:
            findings.extend(safe_extract_zip(source, scan_root))
        except zipfile.BadZipFile as exc:
            raise SafetyGateError("Skill ZIP is malformed or unreadable.") from exc
        skill_root, root_findings = find_skill_root(scan_root)
        findings.extend(root_findings)
        return "zip", scan_root, skill_root, findings
    skill_root, root_findings = find_skill_root(source)
    findings.extend(root_findings)
    return "folder", source, skill_root, findings


def parse_frontmatter(skill_text: str) -> tuple[dict[str, str], list[str], bool]:
    if not skill_text.startswith("---"):
        return {}, [], False
    lines = skill_text.splitlines()
    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, [], False
    frontmatter = lines[1:end_index]
    scalars: dict[str, str] = {}
    for line in frontmatter:
        match = re.match(r"^([A-Za-z0-9_.-]+):\s*(.+?)\s*$", line)
        if match and not line.startswith(" "):
            scalars[match.group(1)] = unquote_yaml(match.group(2))
    return scalars, frontmatter, True


def unquote_yaml(value: str) -> str:
    text = value.strip()
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
        return text[1:-1]
    return text


def parse_requires(frontmatter: list[str]) -> dict[str, list[str]]:
    requires = {"bins": [], "anyBins": [], "env": [], "config": []}
    active: str | None = None
    active_indent = 0
    for raw in frontmatter:
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key = stripped[:-1] if stripped.endswith(":") else ""
        if key in requires:
            active = key
            active_indent = indent
            continue
        if active and indent > active_indent and stripped.startswith("- "):
            requires[active].append(unquote_yaml(stripped[2:].strip()))
            continue
        if active and indent <= active_indent and not stripped.startswith("- "):
            active = None
    return {key: sorted(set(value)) for key, value in requires.items()}


def relpath(path: Path, root: Path | None) -> str:
    if root is None:
        return path.name
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.name


def scan_security(skill_root: Path | None, prep_findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    findings = list(prep_findings)
    if skill_root is None:
        return number_rows(findings, "FINDING")
    for path in skill_root.rglob("*"):
        if not path.is_file():
            continue
        relative = relpath(path, skill_root)
        lowered = relative.lower()
        suffix = path.suffix.lower()
        if "__pycache__" in lowered or suffix in {".pyc", ".pyo"}:
            findings.append(
                finding(
                    "medium",
                    "generated-cache",
                    "Generated cache file included",
                    relative,
                    relative,
                    "Remove generated caches before installing the skill.",
                    "review",
                )
            )
            continue
        if any(part.startswith(".") for part in Path(relative).parts):
            findings.append(
                finding(
                    "medium",
                    "hidden-file",
                    "Hidden file included",
                    relative,
                    relative,
                    "Review hidden files and remove local metadata from the package.",
                    "review",
                )
            )
        if suffix in BINARY_SUFFIXES or suffix not in TEXT_SUFFIXES:
            findings.append(
                finding(
                    "high",
                    "binary-payload",
                    "Binary or non-text payload included",
                    relative,
                    suffix or "no extension",
                    "Remove binary payloads or distribute them through a separately signed channel.",
                    "block",
                )
            )
            continue
        text = read_text(path)
        if not text:
            continue
        analysis_text = analysis_text_for_path(path, text)
        for category, title, pattern, recommendation in BLOCK_PATTERNS:
            match = pattern.search(analysis_text)
            if match:
                findings.append(finding("high", category, title, relative, match.group(0), recommendation, "block"))
        if ENV_PATTERN.search(analysis_text) and NETWORK_SEND_PATTERN.search(analysis_text):
            findings.append(
                finding(
                    "high",
                    "env-read-network-send",
                    "Environment credential access appears near network-send capable code",
                    relative,
                    "environment access and network send API appear in same file",
                    "Review for exfiltration risk and require explicit user-controlled endpoints.",
                    "block",
                )
            )
        for category, title, pattern, recommendation in REVIEW_PATTERNS:
            match = pattern.search(analysis_text)
            if match:
                findings.append(finding("medium", category, title, relative, match.group(0), recommendation, "review"))
        network_match = NETWORK_PATTERN.search(analysis_text)
        if network_match and not (ENV_PATTERN.search(analysis_text) and NETWORK_SEND_PATTERN.search(analysis_text)):
            findings.append(
                finding(
                    "low",
                    "ordinary-network-url",
                    "Network URL present",
                    relative,
                    network_match.group(0),
                    "Confirm this URL is documentation or an intended official endpoint.",
                    "warn",
                )
            )
        if suffix in RUNTIME_SUFFIXES and RUNTIME_COMMAND_PATTERN.search(analysis_text):
            findings.append(
                finding(
                    "medium",
                    "runtime-command-surface",
                    "Runtime command surface present",
                    relative,
                    "command execution API found",
                    "Review whether this command surface is necessary and bounded.",
                    "review",
                )
            )
    return number_rows(findings, "FINDING")


def build_package_summary(source_kind: str, scan_root: Path, skill_root: Path | None, scalars: dict[str, str], requires: dict[str, list[str]]) -> dict[str, Any]:
    files = [path for path in skill_root.rglob("*") if path.is_file()] if skill_root else []
    total_size = sum(path.stat().st_size for path in files)
    skill_name = scalars.get("name", "")
    return {
        "source_kind": source_kind,
        "skill_root_found": skill_root is not None,
        "skill_root_name": skill_root.name if skill_root else "",
        "skill_name": skill_name,
        "description": scalars.get("description", ""),
        "version": scalars.get("version", ""),
        "file_count": len(files),
        "total_size_bytes": total_size,
        "has_scripts": any(relpath(path, skill_root).startswith("scripts/") for path in files) if skill_root else False,
        "declared_requires": requires,
        "scan_root": scan_root.name,
    }


def build_compatibility_checks(
    skill_root: Path | None,
    scalars: dict[str, str],
    frontmatter_present: bool,
    requires: dict[str, list[str]],
    target_dir: Path,
    target_runtime: str,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    checks.append(check("pass", "target-runtime-supported", f"Runtime target is {target_runtime}.", f"target_runtime: {target_runtime}"))
    if skill_root is None:
        checks.append(check("block", "skill-root", "No installable skill root was found.", "SKILL.md missing or ambiguous."))
        return number_rows(checks, "COMPAT")
    skill_md = skill_root / "SKILL.md"
    checks.append(check("pass" if skill_md.exists() else "block", "skill-md-present", "SKILL.md exists." if skill_md.exists() else "SKILL.md is missing.", relpath(skill_md, skill_root)))
    checks.append(
        check(
            "pass" if frontmatter_present else "block",
            "frontmatter-present",
            "YAML frontmatter is present." if frontmatter_present else "SKILL.md must start with YAML frontmatter.",
            "frontmatter delimiter",
        )
    )
    name = scalars.get("name", "")
    if not name:
        checks.append(check("block", "skill-name", "Skill name is missing.", "name: missing"))
    elif not SKILL_NAME_PATTERN.match(name):
        checks.append(check("block", "skill-name", f"Skill name is not a valid slug: {name}", f"name: {name}"))
    else:
        checks.append(check("pass", "skill-name", f"Skill name slug is valid: {name}", f"name: {name}"))
    description = scalars.get("description", "")
    checks.append(check("pass" if description else "block", "description", "Description is present." if description else "Description is missing.", "description frontmatter"))
    version = scalars.get("version", "")
    checks.append(check("pass" if version else "review", "version", f"Version is present: {version}" if version else "Version is missing; Codex can load it, but marketplace metadata should declare it.", "version frontmatter"))
    metadata_present = any("metadata:" == line.strip() for line in parse_frontmatter(read_text(skill_md))[1]) if skill_md.exists() else False
    checks.append(
        check(
            "pass" if metadata_present else "review",
            "openclaw-metadata",
            "metadata.openclaw surface is declared or metadata exists." if metadata_present else "No metadata block found; OpenClaw-style requirements may be implicit.",
            "metadata block",
        )
    )
    target_skill_dir = target_dir / name if name else target_dir / (skill_root.name if skill_root else "unknown-skill")
    checks.append(
        check(
            "block" if target_skill_dir.exists() else "pass",
            "target-folder-available",
            f"Target folder already exists: {target_skill_dir}" if target_skill_dir.exists() else f"Target folder is available: {target_skill_dir}",
            str(target_skill_dir),
        )
    )
    for binary in requires.get("bins", []):
        checks.append(
            check(
                "pass" if shutil.which(binary) else "block",
                "required-binary",
                f"Required binary found: {binary}" if shutil.which(binary) else f"Required binary missing: {binary}",
                f"bins: {binary}",
            )
        )
    any_bins = requires.get("anyBins", [])
    if any_bins:
        available = [binary for binary in any_bins if shutil.which(binary)]
        checks.append(
            check(
                "pass" if available else "block",
                "any-binary",
                f"At least one anyBins option is available: {', '.join(available)}" if available else f"No anyBins option is available: {', '.join(any_bins)}",
                [f"anyBins: {binary}" for binary in any_bins],
            )
        )
    for env_name in requires.get("env", []):
        checks.append(
            check(
                "pass" if os.environ.get(env_name) else "review",
                "required-env",
                f"Environment variable is set: {env_name}" if os.environ.get(env_name) else f"Environment variable is not set: {env_name}",
                f"env: {env_name}",
            )
        )
    return number_rows(checks, "COMPAT")


def gate_decision(compatibility_checks: list[dict[str, Any]], security_findings: list[dict[str, Any]]) -> dict[str, Any]:
    blocking_checks = [item for item in compatibility_checks if item["status"] == "block"]
    review_checks = [item for item in compatibility_checks if item["status"] == "review"]
    blocking_findings = [item for item in security_findings if item["decision_impact"] == "block"]
    review_findings = [item for item in security_findings if item["decision_impact"] == "review"]
    if blocking_checks or blocking_findings:
        decision = "block"
    elif review_checks or review_findings:
        decision = "review"
    else:
        decision = "allow"
    return {
        "decision": decision,
        "blocker_count": len(blocking_checks) + len(blocking_findings),
        "review_count": len(review_checks) + len(review_findings),
        "warning_count": len([item for item in security_findings if item["decision_impact"] == "warn"]),
        "policy": "allow installs only; review and block never install",
        "evidence": [
            f"blocking_checks: {len(blocking_checks)}",
            f"blocking_findings: {len(blocking_findings)}",
            f"review_checks: {len(review_checks)}",
            f"review_findings: {len(review_findings)}",
        ],
    }


def build_install_plan(args: argparse.Namespace, skill_root: Path | None, skill_name: str, decision: dict[str, Any]) -> dict[str, Any]:
    target_dir = Path(args.target_dir).expanduser()
    target_skill_dir = target_dir / (skill_name or (skill_root.name if skill_root else "unknown-skill"))
    will_install = bool(args.install_on_pass and decision["decision"] == "allow")
    return {
        "requested_install_on_pass": bool(args.install_on_pass),
        "target_dir": str(target_dir),
        "target_skill_dir": str(target_skill_dir),
        "will_install": will_install,
        "reason": "clean allow decision" if will_install else f"install skipped because decision is {decision['decision']} or install was not requested",
        "preconditions": [
            "skill root exists",
            "gate decision is allow",
            "target folder does not already exist",
            "--install-on-pass is supplied",
        ],
    }


def perform_install(skill_root: Path | None, install_plan: dict[str, Any]) -> dict[str, Any]:
    if not install_plan["will_install"]:
        return {
            "status": "skipped",
            "installed": False,
            "target": install_plan["target_skill_dir"],
            "message": install_plan["reason"],
        }
    if skill_root is None:
        return {
            "status": "blocked",
            "installed": False,
            "target": install_plan["target_skill_dir"],
            "message": "No skill root was available to install.",
        }
    target = Path(install_plan["target_skill_dir"])
    if target.exists():
        return {
            "status": "blocked",
            "installed": False,
            "target": str(target),
            "message": "Target folder already exists.",
        }
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill_root, target)
    return {
        "status": "installed",
        "installed": True,
        "target": str(target),
        "message": "Skill copied after clean allow decision.",
    }


def next_steps(decision: dict[str, Any], install_result: dict[str, Any]) -> list[str]:
    if decision["decision"] == "allow" and install_result["installed"]:
        return ["Restart or refresh the skill runtime if required by the host.", "Keep the JSON report and install receipt with the package record."]
    if decision["decision"] == "allow":
        return ["Run again with --install-on-pass if you want the clean package copied into the target skills directory."]
    if decision["decision"] == "review":
        return ["Review all review findings and missing environment variables before installing.", "Rerun the gate after the package or host environment is updated."]
    return ["Do not install this package until blockers are removed.", "Request a clean package from the skill author and rerun the gate."]


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    source = Path(args.skill_source).expanduser()
    target_dir = Path(args.target_dir).expanduser()
    with tempfile.TemporaryDirectory(prefix="skill-install-safety-gate-") as temp_name:
        temp_root = Path(temp_name)
        source_kind, scan_root, skill_root, prep_findings = prepare_source(source, temp_root)
        skill_text = read_text(skill_root / "SKILL.md") if skill_root else ""
        scalars, frontmatter, frontmatter_present = parse_frontmatter(skill_text)
        requires = parse_requires(frontmatter)
        compatibility = build_compatibility_checks(skill_root, scalars, frontmatter_present, requires, target_dir, args.target_runtime)
        security = scan_security(skill_root, prep_findings)
        decision = gate_decision(compatibility, security)
        install_plan = build_install_plan(args, skill_root, scalars.get("name", ""), decision)
        install_result = perform_install(skill_root, install_plan)
        result = {
            "input": {
                "skill_source": args.skill_source,
                "target_dir": args.target_dir,
                "target_runtime": args.target_runtime,
                "install_on_pass": bool(args.install_on_pass),
            },
            "package_summary": build_package_summary(source_kind, scan_root, skill_root, scalars, requires),
            "compatibility_checks": compatibility,
            "security_findings": security,
            "install_plan": install_plan,
            "install_result": install_result,
            "gate_decision": decision,
            "assumptions": [
                "The gate is static analysis only and does not execute untrusted skill code.",
                "A clean allow decision is required before install-on-pass can copy files.",
                "Missing environment variables require review but do not prove the package is unsafe.",
                "Existing target folders are never overwritten in v1.",
                "The gate targets Codex local skill installation with OpenClaw-style metadata compatibility checks.",
            ],
            "next_steps": next_steps(decision, install_result),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }
    if list(result.keys()) != TOP_LEVEL_FIELDS:
        raise SafetyGateError("Internal output contract mismatch.")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    package = result["package_summary"]
    decision = result["gate_decision"]
    lines = [
        "# Skill Install Safety Gate",
        "",
        "## Package Summary",
        "",
        f"- Source kind: {package['source_kind']}",
        f"- Skill root found: {package['skill_root_found']}",
        f"- Skill name: {package['skill_name'] or 'Unknown'}",
        f"- Description: {package['description'] or 'Missing'}",
        f"- Version: {package['version'] or 'Missing'}",
        f"- Files: {package['file_count']}",
        f"- Total size bytes: {package['total_size_bytes']}",
        "",
        "## Gate Decision",
        "",
        f"- Decision: {decision['decision']}",
        f"- Blockers: {decision['blocker_count']}",
        f"- Review items: {decision['review_count']}",
        f"- Warnings: {decision['warning_count']}",
        f"- Policy: {decision['policy']}",
        "",
        "## Compatibility Checks",
        "",
    ]
    for item in result["compatibility_checks"]:
        lines.append(f"- {item['id']} [{item['status']}] {item['check']}: {item['detail']}")
    lines.extend(["", "## Security Findings", ""])
    if result["security_findings"]:
        for item in result["security_findings"]:
            lines.append(f"- {item['id']} [{item['decision_impact']}] {item['category']} in {item['file'] or 'package'}: {item['title']}. Evidence: {item['evidence']}")
    else:
        lines.append("- No security findings detected.")
    plan = result["install_plan"]
    install = result["install_result"]
    lines.extend(
        [
            "",
            "## Install Plan",
            "",
            f"- Requested install-on-pass: {plan['requested_install_on_pass']}",
            f"- Target directory: {plan['target_dir']}",
            f"- Target skill directory: {plan['target_skill_dir']}",
            f"- Will install: {plan['will_install']}",
            f"- Reason: {plan['reason']}",
            "",
            "## Install Result",
            "",
            f"- Status: {install['status']}",
            f"- Installed: {install['installed']}",
            f"- Target: {install['target']}",
            f"- Message: {install['message']}",
            "",
            "## Assumptions",
            "",
        ]
    )
    for item in result["assumptions"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Next Steps", ""])
    for item in result["next_steps"]:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def write_csv(path: str, fields: list[str], rows: list[dict[str, Any]]) -> None:
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: " | ".join(row[field]) if isinstance(row.get(field), list) else row.get(field, "") for field in fields})


def write_outputs(result: dict[str, Any], args: argparse.Namespace) -> None:
    output_paths = [args.out_json, args.out_md, args.out_findings_csv, args.out_compatibility_csv, args.out_install_receipt]
    for raw_path in output_paths:
        if not raw_path:
            continue
        path = Path(raw_path)
        if path.parent != Path("."):
            path.parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    Path(args.out_md).write_text(render_markdown(result), encoding="utf-8")
    write_csv(args.out_findings_csv, FINDING_CSV_FIELDS, result["security_findings"])
    write_csv(args.out_compatibility_csv, COMPATIBILITY_CSV_FIELDS, result["compatibility_checks"])
    if args.out_install_receipt:
        receipt = {
            "gate_decision": result["gate_decision"]["decision"],
            "install_result": result["install_result"],
            "package_summary": result["package_summary"],
            "generated_at": result["generated_at"],
        }
        Path(args.out_install_receipt).write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        result = build_result(args)
        write_outputs(result, args)
    except (SafetyGateError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
