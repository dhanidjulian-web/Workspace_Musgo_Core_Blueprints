---
name: "skill-install-safety-gate"
description: "Pre-install safety gate for Codex/OpenClaw-style skills. Use before installing a new skill folder or ZIP to check compatibility, metadata, target-folder conflicts, suspicious code patterns, ZIP safety, and install readiness, then optionally install only when the gate decision is allow."
version: "1.0.0"
metadata:
  openclaw:
    requires:
      anyBins:
        - "python"
        - "python3"
      config:
        - ".env"
        - "compatibility-checks.csv"
        - "install-receipt.json"
        - "install-safety-report.md"
        - "output.json"
        - "security-findings.csv"
_agensi: "5bc3869c-c562-41a8-acef-b44f1938b39b"
---


# Skill Install Safety Gate

Use this skill before installing a new skill from a folder or ZIP.

The workflow statically checks package shape, Codex/OpenClaw-style compatibility, suspicious install risk, and target-folder conflicts. It never executes untrusted package code. It only installs when `--install-on-pass` is supplied and the final gate decision is exactly `allow`.

## Quick Start

```text
python scripts/skill_install_safety_gate.py `
  --skill-source ".\downloaded-skill.zip" `
  --target-dir "%USERPROFILE%\.codex\skills" `
  --target-runtime codex-openclaw `
  --install-on-pass `
  --out-json output.json `
  --out-md install-safety-report.md `
  --out-findings-csv security-findings.csv `
  --out-compatibility-csv compatibility-checks.csv `
  --out-install-receipt install-receipt.json
```

## Inputs

Required:

- `--skill-source`

Optional:

- `--target-dir`
- `--target-runtime codex-openclaw`
- `--install-on-pass`
- `--out-json`
- `--out-md`
- `--out-findings-csv`
- `--out-compatibility-csv`
- `--out-install-receipt`

## Workflow

### 1. Normalize the Source

- Accept a folder or ZIP.
- Extract ZIP files only into a temporary scan directory.
- Block ZIP path traversal.
- Locate exactly one installable skill root, or use a root-level `SKILL.md`.
- Reject missing or ambiguous `SKILL.md`.

### 2. Check Compatibility

- Validate skill name slug, frontmatter, description, and version.
- Parse `metadata.openclaw.requires` for `bins`, `anyBins`, `env`, and `config`.
- Check required binaries with `shutil.which`.
- Pass `anyBins` when at least one listed binary exists.
- Mark missing environment variables as `review`.
- Block when the target skill folder already exists.

### 3. Scan Security Surface

- Block likely real secrets, ZIP traversal, binary payloads, suspicious install commands, obfuscated payloads, dangerous shell patterns, dynamic code execution, and environment-read plus network-send patterns.
- Mark prompt-injection-like instructions, personal absolute paths, broad permission wording, generated caches, runtime command surfaces, and hidden files as `review`.
- Mark ordinary network URLs as `warn` unless combined with credential access or executable download behavior.

### 4. Decide and Install

Gate decisions:

- `allow`: no blockers and no review findings.
- `review`: no blockers but at least one review item.
- `block`: at least one blocker.

Install behavior:

- `--install-on-pass` copies the scanned skill root only for `allow`.
- `review` and `block` never install.
- Existing target folders are never overwritten in V1.
- The install receipt records the final decision and copy result.

## Output Contract

Read `references/output-contract.md` for JSON fields, report sections, CSV columns, and install receipt expectations.

Preserve the top-level JSON fields:

- `input`
- `package_summary`
- `compatibility_checks`
- `security_findings`
- `install_plan`
- `install_result`
- `gate_decision`
- `assumptions`
- `next_steps`
- `generated_at`

## Guardrails

- Never execute package code, install hooks, dependency commands, post-install scripts, or bundled binaries.
- Do not install on `review` or `block`.
- Do not overwrite existing skills.
- Treat findings as static evidence, not proof of malicious intent.
- Keep token values and secrets out of outputs.

## Commercial License Notice

This skill is a proprietary commercial product. Purchase grants a non-transferable license for personal or internal business use only. Redistribution, resale, sublicensing, republishing, and bundle-sharing are not permitted without separate written permission from the author.
