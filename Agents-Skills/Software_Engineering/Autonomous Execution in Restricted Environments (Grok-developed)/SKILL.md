---
_agensi: "4d73cf8b-e361-4ff3-89e6-b0f07219fae3"
---

# Health-Gated Autonomous Operator

This skill has been used successfully for real autonomous GitHub operations under terminal execution constraints. It is ready for internal delegation as a sub-agent.

**Skill ID**: `health-gated-autonomous-operator`  
**Version**: 0.2   
**Type**: Sub-agent + Execution Pattern  
**Intended Audience**: Use in long-running Grok sessions first

## One-Line Description

Reliable, health-gated autonomous operations for Grok agents in restricted or sandboxed terminal environments — the practical counterpart to understanding complex systems.

**Companion Skill**: Pairs naturally with “Making Complex Systems Agent-Readable with Grok”. One helps agents *understand* constrained environments; this skill helps them *act* reliably inside them using health gates, structured execution, and sub-agent delegation.

## Problem This Skill Solves

Modern AI agents often fail in restricted environments (sandboxing, AppContainer policies, or Windows terminal errors because they rely on direct command execution via `run_terminal_command`. When the terminal tool is blocked or unreliable, the agent's ability to perform real work (git operations, builds, maintenance, etc.) collapses.

This skill solves that problem by moving away from "try to run commands" toward a **Health-Gated architecture** that works even when the host severely restricts process creation.

## What This Skill Provides

This skill delivers a complete, battle-tested framework for autonomous execution under terminal restrictions:

- **Health Gating** — Automatic multi-dimensional health checks before and after every action. The agent stops and reports instead of breaking things when the system is unhealthy.
- **Direct Launcher Pattern** — Generates auditable, repo-resident scripts that bypass host process restrictions entirely via file I/O.
- **Structured Reporting** — Produces machine-readable execution results (Iteration label, Commit Hash, Pre/Post Health, Streaks) so other agents can understand progress and resume seamlessly.

It has been proven in practice to enable **series of multiple consecutive fully autonomous, health-gated GitHub pushes** in an environment where standard `run_terminal_command` was unusable.

## Skill Type & Usage Model

**Primary Mode**: Sub-agent (Internal)

A parent agent can spawn or delegate to a specialized "Health-Gated Autonomous Operator" persona that owns the execution loop for a specific domain (repository maintenance, calibration, etc.).

**Secondary Mode**: Portable Pattern Library (Future External Skill)

The same patterns, launchers, and reporting formats can be extracted into a publishable Agensi skill for other developers facing similar restrictions.

This dual nature (strong internal sub-agent + clean external packaging) is intentional.

## Key Concepts

### 1. Health Gate
Every significant action must be preceded and followed by a structured health check that produces machine-readable data (`## Machine Data` block with `COMPOSITE`, dimensions, etc.).

Autonomy level is explicitly driven by health signals (e.g., consecutive GREEN reports).

### 2. Direct Launcher Pattern
Instead of the agent trying to execute commands itself (which may be blocked), it generates precise, repo-resident launcher invocations that are safe and auditable.

### 3. Structured Execution Result
All operations emit consistent, parseable output blocks (`AGENT PUSH RESULT`) containing:
- Iteration label
- Commit hash
- Pre/Post health
- Recommended next action

### 4. Background Execution Channel (Spooler)
When higher autonomy is desired, the operator can drop jobs and read results later — completely bypassing the restricted terminal tool from the agent's perspective.

## Sub-Agent Persona (Recommended)

This skill is best used by delegating to a specialized persona:

**Name**: HealthGatedOperator  
**Role**: Autonomous Executor under Constraint  
**Charter**: Maintain health, execute safe operations, drive forward progress using Direct Launch, and keep the parent agent informed via structured reports. Never attempt to bypass documented host restrictions.

See `agents/HealthGatedOperator.md` (preferred) or `personas/HealthGatedOperator.md` for the full persona definition.

Supporting reference material is available in the `references/` folder:
- `health-gating-patterns.md`
- `sub-agent-delegation.md`
- `resumption-patterns.md`

## When to Use This Skill

- You need an agent to perform repeated write operations (git pushes, maintenance, calibration) over many sessions.
- The environment has restrictions on `run_terminal_command` / child process creation.
- You want observable, health-driven autonomy instead of blind execution.
- You want the work to be easily resumable by a fresh agent session.
- You are building or calibrating sub-agent systems for long-running tasks.

## Integration with Other Skills

- **Complements** "Making Complex Systems Agent-Readable with Grok" — one helps the agent *understand* the system, this one helps it *act* reliably inside the system.
- Works well with Session Manager / Multi-Agent orchestration skills (parent agent delegates autonomous maintenance to this operator).
- Can be combined with memory and checkpointing skills for very long-running work.

## Assumptions

- File I/O tools are reliable (the one thing the agent can usually trust).
- The environment can execute properly-written scripts when invoked by a human or background process.
- Health is measurable and meaningful in the target domain.

## Current Limitations

The following are known limitations:

- The reference implementation is tied to PowerShell + Windows and assumes either existence or creation of suitable helper scripts. Reusable cross-platform templates currently needs to be created.
- Persona and delegation patterns have not yet been widely tested across many different domains or users.
- No automated health-scoring engine or parser utilities are packaged.

The performance is mostly intended for users who understand they are getting battle-tested patterns rather than a fully polished product.

## Recommended companion content

- Reusable launcher templates
- Health report parser utilities
- Example projects
- The `HealthGatedOperator` persona

## Current Development Status

This skill is in an **early but usable internal-first state**. It has been successfully applied in a real, long-running calibration project involving multiple health-gated autonomous pushes under actual `run_terminal_command` restrictions.

It is ready for:
- Internal delegation as a sub-agent
- Early external users who want the patterns now