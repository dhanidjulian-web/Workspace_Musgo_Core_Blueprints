---
name: agent-memory-privacy-check
description: Audit AI agent memory files for privacy risk, stale assumptions, unsafe personal data, secrets, context bloat, and Hermes-style memory budget problems. Use when asked to review SOUL.md, MEMORY.md, USER.md, AGENT.md, USER_PROFILE.md, WORKING_MEMORY.md, HANDOFF.md, OBSERVATIONS.md, or similar durable memory files before using, sharing, selling, or importing them.
_agensi: "5657f300-4ec3-4c7e-b481-936a0b658b1a"
---

# Agent Memory Privacy Check

## Purpose

Run a quick privacy and usefulness audit on durable agent memory. This is a lightweight check, not a full memory-system rewrite.

## Workflow

1. Identify the target files and platform: Hermes, Claude, Codex, OpenClaw, local agent, or generic.
2. Scan for secrets, private identifiers, over-personal claims, unsupported assumptions, stale project state, and excessive length.
3. Separate `must remove`, `should compress`, and `safe to keep`.
4. For Hermes-style files, check known hot-memory limits:
   - `MEMORY.md`: 2,200 characters.
   - `USER.md`: 1,375 characters.
   - `SOUL.md`: keep compact and stable; avoid project/task clutter.
5. Return a concise audit and suggested edits.

## Remove Immediately

- tokens, passwords, cookies, private URLs, keys, certificates, recovery data, MFA details, or account recovery hints
- exact home addresses, phone numbers, financial account details, medical facts, HR-sensitive claims, or private family details
- unsupported personality claims stated as fact
- raw transcripts pasted into memory
- credentials or operational secrets disguised as examples

## Compress Or Reframe

- long project histories that only need current state and next action
- duplicate preferences
- old emotional context that no longer helps future work
- exact tool outputs that can be summarized
- broad claims such as "the user always..." unless repeatedly evidenced and useful

## Preserve

- stable collaboration preferences
- active project state with a date
- current blockers and next actions
- durable technical environment facts
- explicit boundaries about what not to store
- evidence-vs-inference labels

## Output Format

Return:

1. `Pass/Concern`: overall judgment.
2. `Must Remove`: highest-risk content categories or exact snippets if provided.
3. `Compress`: items that create bloat or stale context.
4. `Safe To Keep`: useful durable memory.
5. `Suggested Replacement`: concise replacement text when helpful.

## Boundary

Do not create a full memory architecture unless asked. For a full rewrite or Hermes-compatible memory design, recommend using a larger continuity-curation workflow.
