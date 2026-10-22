#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MusGo-OS 2in1 — Project Progress Configuration Loader & Resolver
File    : /home/Project-Progress/config/scripts/musgo_config.py
Founder : Dhani Yuliawan
License : © 2026 — Dhani Yuliawan | All Rights Reserved

Fungsi:
  1. Load konfigurasi kanonik (paths, founder_rules, workflow, registry, config).
  2. Resolve placeholder {key} pada paths -> path absolut nyata.
  3. Enforce write-policy zero-trust (write_scopes, immutable, max size).
  4. Merge env override (MUSGO_*) tanpa mengubah file.

Dependensi: PyYAML (opsional). Jika tidak tersedia, dipakai parser YAML
mini terbatas yang tetap VALID untuk struktur config ini (mapping bersarang,
list skalar, list of map inline). Tidak ada mock: bila file gagal dibaca,
fungsi mengangkat exception.
"""

from __future__ import annotations

import json
import os
import re
import sys

CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(CONFIG_DIR)

FILES = {
    "paths": "paths.yaml",
    "founder": "founder_rules.yaml",
    "workflow": "canonical_workflow.yaml",
    "registry": "agents_skills_registry.yaml",
    "project": "project_progress.config.yaml",
}

try:  # pragma: no cover - tergantung environment
    import yaml as _yaml  # type: ignore
    HAS_PYYAML = True
except Exception:  # noqa: BLE001
    _yaml = None
    HAS_PYYAML = False


# ---------------------------------------------------------------------------
# FALLBACK YAML PARSER (subset yang dipakai config ini)
# ---------------------------------------------------------------------------
def _strip_comment(line: str) -> str:
    out, quote = [], None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ("'", '"'):
            quote = ch
            out.append(ch)
            continue
        if ch == "#":
            break
        out.append(ch)
    return "".join(out).rstrip()


def _cast(value: str):
    v = value.strip()
    if v == "" or v in ("~", "null", "NULL"):
        return None
    if v in ("true", "True", "TRUE"):
        return True
    if v in ("false", "False", "FALSE"):
        return False
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_cast(x) for x in re.split(r",(?![^\[\]{}]*[\]}])", inner)]
    if v.startswith("{") and v.endswith("}"):
        inner = v[1:-1].strip()
        obj = {}
        if not inner:
            return obj
        for part in re.split(r",(?![^{}]*\})", inner):
            if ":" not in part:
                raise ValueError(f"inline map tidak valid: {part!r}")
            k, val = part.split(":", 1)
            obj[k.strip().strip("'\"")] = _cast(val)
        return obj
    return v


def _mini_yaml(text: str):
    """Parser YAML subset: mapping, nested mapping, list skalar, list of inline map."""
    root: dict = {}
    stack = [(-1, root)]
    pending_key = None
    pending_indent = 0

    for raw in text.splitlines():
        if not raw.strip():
            continue
        line = _strip_comment(raw)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            stack = [(-1, root)]

        # item list
        if content.startswith("- "):
            value = content[2:].strip()
            parent = stack[-1][1]
            if isinstance(parent, dict):
                # list di bawah key kosong: konversi
                if pending_key and parent.get(pending_key) is None:
                    parent[pending_key] = []
                    stack.append((pending_indent, parent[pending_key]))
                target = stack[-1][1]
                if isinstance(target, list):
                    target.append(_cast(value))
                    continue
                raise ValueError(f"list tanpa parent pada: {content!r}")
            if isinstance(parent, list):
                parent.append(_cast(value))
                continue
            raise ValueError(f"struktur tidak dikenali: {content!r}")

        if content.endswith(":"):
            key = content[:-1].strip().strip("'\"")
            parent = stack[-1][1]
            if not isinstance(parent, dict):
                raise ValueError(f"key di dalam list tidak didukung: {key}")
            parent[key] = {}
            pending_key, pending_indent = key, indent
            stack.append((indent, parent[key]))
            continue

        if ":" in content:
            key, value = content.split(":", 1)
            key = key.strip().strip("'\"")
            parent = stack[-1][1]
            if not isinstance(parent, dict):
                raise ValueError(f"key di dalam list tidak didukung: {key}")
            parent[key] = _cast(value)
            pending_key, pending_indent = key, indent
            continue

        raise ValueError(f"baris tidak dikenali: {content!r}")

    return root


def parse_yaml_file(path: str):
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if HAS_PYYAML:
        return _yaml.safe_load(text) or {}
    return _mini_yaml(text)


# ---------------------------------------------------------------------------
# LOADER
# ---------------------------------------------------------------------------
def load_config(config_dir: str | None = None) -> dict:
    cdir = config_dir or CONFIG_DIR
    cfg = {"_meta": {"config_dir": cdir, "project_dir": os.path.dirname(cdir),
                     "yaml_engine": "PyYAML" if HAS_PYYAML else "mini-parser"}}
    for key, fname in FILES.items():
        fpath = os.path.join(cdir, fname)
        if not os.path.isfile(fpath):
            raise FileNotFoundError(f"[musgo_config] config wajib tidak ada: {fpath}")
        cfg[key] = parse_yaml_file(fpath)
    rules = cfg["founder"]
    if rules.get("priority") != 0 or rules.get("immutable") is not True:
        raise ValueError("[musgo_config] founder_rules.yaml harus priority:0 & immutable:true")
    return cfg


# ---------------------------------------------------------------------------
# PATH RESOLVER
# ---------------------------------------------------------------------------
def _apply_env_overrides(cfg: dict) -> dict:
    paths_cfg = cfg["paths"]
    roots = dict(paths_cfg.get("root_dirs", {}))
    env_map = paths_cfg.get("env_overrides", {}) or {}
    for env_name, root_key in env_map.items():
        val = os.environ.get(env_name)
        if val:
            roots[root_key] = os.path.abspath(val)
    merged = dict(paths_cfg)
    merged["root_dirs"] = roots
    merged["paths"] = {**roots, **dict(paths_cfg.get("paths", {}))}
    return merged


def resolve(cfg: dict, key: str, _depth: int = 0) -> str:
    """Resolve key (mis. 'memory', 'paths.memory', atau '{memory}/x') -> absolut."""
    if _depth > 12:
        raise RecursionError(f"[musgo_config] resolusi path terlalu dalam: {key}")
    pcfg = _apply_env_overrides(cfg)
    table = pcfg["paths"]
    if key.startswith("{"):
        template = key
    elif key in table:
        template = table[key]
    else:
        raise KeyError(f"[musgo_config] key path tidak dikenal: {key}")
    if not isinstance(template, str):
        raise TypeError(f"[musgo_config] nilai path bukan string: {key}")

    def repl(match):
        name = match.group(1)
        if name in table and isinstance(table[name], str):
            return resolve(cfg, name, _depth + 1)
        raise KeyError(f"[musgo_config] placeholder tidak terdefinisi: {{{name}}}")

    resolved = re.sub(r"\{([a-zA-Z0-9_]+)\}", repl, template)
    return resolved


def generated_path(cfg: dict, key: str) -> str:
    table = cfg["paths"].get("generated", {})
    if key not in table:
        raise KeyError(f"[musgo_config] generated path tidak dikenal: {key}")
    return resolve(cfg, table[key])


# ---------------------------------------------------------------------------
# WRITE GUARD (zero-trust filesystem)
# ---------------------------------------------------------------------------
def _norm(path: str) -> str:
    return os.path.realpath(os.path.abspath(path))


def write_denial(cfg: dict, target: str) -> str | None:
    """Return alasan penolakan, atau None bila boleh ditulis."""
    integ = cfg["paths"].get("integrity", {}) or {}
    real = _norm(target)
    scopes = [resolve(cfg, s) for s in integ.get("write_scopes", [])]
    allowed = any(_norm(real).startswith(_norm(s) + os.sep) or _norm(real) == _norm(s)
                  for s in scopes)
    if not allowed:
        return f"di luar write_scopes: {real}"
    base = os.path.basename(real)
    if base.startswith(str(integ.get("immutable_prefix", "FOUNDER-"))):
        return f"file immutable (prefix {integ.get('immutable_prefix')}): {base}"
    max_bytes = int(integ.get("max_file_write_bytes", 2 * 1024 * 1024))
    if os.path.isfile(real) and os.path.getsize(real) > max_bytes:
        return f"melebihi batas {max_bytes} byte"
    return None


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _cli(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print("Pakai: musgo_config.py {get <key>|show-paths|check-write <path>|"
              "generated <key>|registry-summary}")
        return 0 if argv else 2
    cfg = load_config()
    cmd = argv[0]
    if cmd == "get":
        print(resolve(cfg, argv[1]))
        return 0
    if cmd == "generated":
        print(generated_path(cfg, argv[1]))
        return 0
    if cmd == "show-paths":
        pcfg = _apply_env_overrides(cfg)
        for k, v in pcfg["paths"].items():
            try:
                print(f"{k:22s} {resolve(cfg, k)}")
            except KeyError as exc:  # noqa: PERF203
                print(f"{k:22s} <ERROR: {exc}>")
        return 0
    if cmd == "check-write":
        reason = write_denial(cfg, argv[1])
        if reason:
            print(f"DENIED: {reason}")
            return 1
        print("ALLOWED")
        return 0
    if cmd == "registry-summary":
        reg = cfg["registry"]
        groups = reg.get("catalog", {})
        total = sum(len(v) for v in groups.values())
        print(json.dumps({"catalog_domains": len(groups), "pairs_listed": total,
                          "total_groups": reg.get("total_groups"),
                          "yaml_engine": cfg["_meta"]["yaml_engine"]}, indent=2))
        return 0
    print(f"Perintah tidak dikenal: {cmd}")
    return 2


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
