# Health-Gated Autonomous Operator

Developed through extended agent autonomy calibration work. Ready for use as an internal sub-agent skill.

Reliable, health-gated autonomous operations for Grok agents in restricted or sandboxed terminal environments.

This is the practical "how to act" companion to “Making Complex Systems Agent-Readable with Grok”.

## Quick Start (Internal Use)

1. A parent agent decides it wants to delegate autonomous work.
2. It loads this skill and spawns the `HealthGatedOperator` persona.
3. The operator is given a clear charter + the target repository.
4. It operates using the patterns defined in this skill (health gating + Direct Launchers + structured reporting).

See `SKILL.md` for the full specification, `agents/grok.yaml` for Agensi metadata & interface definition, and `agents/HealthGatedOperator.md` (preferred) or `personas/HealthGatedOperator.md` for the persona definition.

Supporting reference material (highly recommended when using this skill for real work):
- `references/health-gating-patterns.md`
- `references/sub-agent-delegation.md`
- `references/resumption-patterns.md`

## Current Status

- Validated in production calibration work
- 11+ successful health-gated autonomous pushes under real `run_terminal_command` restrictions
- Designed for easy extraction into a public Agensi skill later

## Directory Structure

```
health-gated-autonomous-operator/
├── SKILL.md
├── README.md
└── personas/
    └── HealthGatedOperator.md
```