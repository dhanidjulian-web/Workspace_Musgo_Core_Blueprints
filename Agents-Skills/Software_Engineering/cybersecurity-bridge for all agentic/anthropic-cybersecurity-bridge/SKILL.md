---
name: anthropic-cybersecurity-bridge
description: Connect directly to a local checkout of Anthropic-Cybersecurity-Skills and route a security task to the best matching external skill. Use when the external repo is installed and you want a repo-specific wrapper instead of a generic agentskills bridge.
_agensi: "66969edc-df51-4757-8dea-4298538128df"
---

# Anthropic Cybersecurity Bridge

Use this skill when the external library is specifically `Anthropic-Cybersecurity-Skills`.

This wrapper is thinner and more direct than `cybersecurity-skill-bridge`:

- it assumes the target repo shape
- it searches common Anthropic-Cybersecurity-Skills paths first
- it narrows the query flow to that library

## Workflow

1. resolve the local repo root
2. query its `index.json`
3. shortlist the most relevant external skills
4. open only those external `SKILL.md` files
5. continue the task using the matched external guidance

## Query Helper

Use:

```bash
python3 scripts/query_anthropic_index.py --query "memory dump credential theft"
```

The wrapper will search common locations such as:

- `/tmp/Anthropic-Cybersecurity-Skills`
- `~/Anthropic-Cybersecurity-Skills`
- `AGENTSKILLS_LIB_ROOT`

## Boundary

This wrapper does not bundle the third-party repo. It only connects to a separately installed checkout at runtime.

Read [`references/install-notes.md`](references/install-notes.md) before packaging or sharing.
