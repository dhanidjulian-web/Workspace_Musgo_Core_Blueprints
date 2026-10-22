---
name: "Agensi Skill Authoring"
description: "A practical, step-by-step process for writing SKILL.md files that follow the Agensi open standard, stay usable across coding agents, and load cleanly in Grok Build when that is the target runtime."
version: 1.4.0
author: Markus Isaksson
license: MIT
price: 0
tags:
  - agensi
  - skill-authoring
  - meta
  - documentation
  - best-practices
  - free
  - grok
_agensi: "501fc69f-95da-4274-8caf-9b9f7c55c7b8"
---

# Agensi Skill Authoring

**Why This Skill Exists**  
A skill is not a long prompt. It is a small operating procedure an agent can load and follow. Vague skills get ignored; rigid skills fail on the next model or folder layout. This skill is the authoring pass: purpose, boundaries, procedure, output contract, then packaging for Agensi and for Grok when Grok is in play.

It does not replace Grok’s built-in skill creator. Use that when you only need a Grok-local `SKILL.md` under `~/.grok/skills` or `.grok/skills`. Use this skill when the artifact should be publishable on Agensi, portable to other agents, or both.

## What You'll Gain

- A repeatable authoring sequence with an explicit stop after purpose and scope
- Skills other people (and later sessions) can follow without you in the room
- Packaging that matches Agensi listings and, when relevant, Grok Build

## When to Use This Skill

Use this skill when:
- Writing a new `SKILL.md` you intend to share, publish, or reuse
- Standardizing how a team writes agent instructions
- Preparing an Agensi marketplace listing (frontmatter, permissions, agent adapter)
- Teaching skill shape, not just dumping a prompt into a file

**When You DON’T Need This Skill**
- One-off prompts you will not reuse
- A Grok-only personal skill with no listing — use Grok’s create-skill flow
- Harvesting a prompt you already run on repeat — that is Prompt-to-Skill Converter
- Scoring or rewriting a skill that already has a solid structure — evaluation/iteration, not this

## Token Cost Profile

Authoring is usually a medium-cost session (several reads, one coherent write). Under tight credits: finish Phase 1 with the user, then draft only frontmatter + procedure + output template; defer examples and adapters. See `references/token-economy-patterns.md` if the session is credit-constrained.

## Agent Operating Procedure

Follow these phases in order. The procedure is model-agnostic. Apply the Grok notes in Phase 5 only when the user cares about Grok Build.

### Phase 1: Define Purpose and Boundaries

Capture:
- The specific problem the skill solves (one job, not a toolbox)
- Who it is for
- When it **should** be used (triggers a later agent can match)
- When it should **not** be used
- What “done” looks like for a run of the skill

**Stop here.** Confirm purpose and scope with the user before writing the rest.

### Phase 2: Design the Core Procedure

Break the work into ordered phases the agent must follow. For each phase:
- State what the agent must do
- Name the tools or inputs it needs, if any
- Put a stop where the user should review (not after every sentence)
- Use direct language (“Do this.” “Do not proceed until…”)

Keep each fact in one place. Do not restate the same rule in procedure, pitfalls, and notes.

### Phase 3: Define Expected Output

Specify the artifact the agent must produce. Prefer:
- A fill-in template with named sections
- One short completed example
- Structured forms (tables, checklists) only when they reduce ambiguity

This is usually the highest-leverage part of the skill.

### Phase 4: Guardrails

Document only failure modes that the procedure does not already prevent:
- Common mistakes
- Hard “never” rules
- When to abandon the skill

Skip no-op restatements of Phase 2.

### Phase 5: Metadata, Grok notes, Polish

Finalize the bundle:

1. **YAML frontmatter** — valid YAML. Include `name`, `description`, `version`, `author`, `license`, `price`, `tags`. Description: what the skill does, plus trigger phrases.
2. **Permissions** — honest tool use, file scopes, hosts, env vars. Do not claim “no write” if the procedure writes files.
3. **Quick Start prompt** — copy-pasteable.
4. **Works Well With** — only skills that still exist and complement this one. No catalog padding.
5. **Grok, when it matters**
   - Description should be specific enough for auto-invoke.
   - Grok-local installs often use kebab-case `name` (e.g. `agensi-skill-authoring`); Agensi listings may keep a human display name. Put the listing name in frontmatter `name` and the kebab slug in `agents/grok.yaml` (`agensi_slug` / notes), not twice in the body.
   - If the skill is meant to run in Grok Build, include `agents/grok.yaml` (display name, default prompt, permissions, tags). Other agents: add an adapter file only if the user asked for that agent.
   - Do not duplicate Grok platform policy (browser verification, no exploits, etc.) inside the skill. Point at the host. Put only skill-specific rules here.
6. **Verify the write** — after creating or updating files, re-read them and confirm frontmatter parses and fences are balanced.

**Hard stop:** Do not call the skill complete until Phases 1–5 are done and the user has seen the draft.

## Expected Output (Fill-in Template)

Produce a structured draft the user can save as `SKILL.md` (and `agents/grok.yaml` when Grok is a target):

```markdown
## Skill Name
[Listing / display name]

## Purpose
[Why it exists and who it is for]

## When to Use / When Not to Use
- Use when: ...
- Do not use when: ...

## Agent Operating Procedure
### Phase 1: ...
### Phase 2: ...

## Expected Output Template
[Template the consuming agent should fill in]

## Common Pitfalls
[Only rules not already in the procedure]

## Quick Start Prompt
[Ready-to-copy prompt]

## Packaging
- Frontmatter fields: ...
- agents/grok.yaml: yes/no
- Extra files: ...
```

## Common Pitfalls to Avoid

| Don’t | Do |
|-------|----|
| Encode a whole product suite in one skill | One job per skill |
| Copy host-agent policy into every SKILL.md | Skill-specific rules only |
| Nested identical markdown fences | Outer fence longer than inner |
| Invalid YAML (`name: Foo:` without quotes, stray backticks) | Quote strings that need it; close the frontmatter |
| “Works Well With” as a storefront | Link only real companions |
| Skipping the Phase 1 stop | Confirm scope before drafting the full file |

## Quick Start Prompt

```
I want to write a new SKILL.md for [what the agent should do].

Apply Agensi Skill Authoring. Start with Phase 1 (purpose and boundaries). Target Agensi packaging; include Grok Build notes if I will load it in Grok.
```

## Works Well With

- **Prompt-to-Skill Converter with Grok** — when the input is an existing repetitive prompt, not a blank design
- **PromptMaster with Grok** — when you need a strong prompt *before* it becomes a skill
- **Getting Started with Agensi MCP** — when the new skill will call the Agensi marketplace
- Grok bundled **create-skill** / **skill-design-principles** — Grok-local install and writing hygiene; this skill stays the Agensi + portable authoring path

## Compatibility

Agensi skills use the open `SKILL.md` standard and should remain readable by Claude Code, Codex CLI, Cursor, Copilot, Gemini CLI, and Grok Build.

Authoring rules in Phases 1–4 are agent-agnostic. Phase 5 Grok notes apply only when Grok Build is a target runtime.

---

## Permissions

**Permission Profile**: Documentation and Skill Creation (Read + Write)

**Tools Used**

- **Terminal / Shell**: Sometimes — inspect example skills or confirm files exist
- **Read Files**: Yes — existing skills and drafts
- **Write Files**: Yes — `SKILL.md`, optional `agents/*.yaml`, optional `references/`
- **Browser**: No
- **Network Access**: No

**Environment Variables**: None required

**Allowed Hosts**: None

**File Scopes**:
- `**/*.md`
- `agents/**`
- `references/**`

**Notes**:
Writes skill source, not unrelated project code. Prefer the user’s chosen skill folder. Do not invent marketplace IDs.