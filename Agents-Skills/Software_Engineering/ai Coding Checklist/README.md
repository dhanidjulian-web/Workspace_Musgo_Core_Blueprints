# AI Coding Checklist — For AI Coding Agents

**Stop your AI agent from coding in the wrong direction.**

Most wasted AI coding sessions have one thing in common: the agent started before the developer had a clear picture of what they actually wanted. This free skill runs a 5-gate pre-task checklist before any coding session begins, flags exactly what's missing, and produces a GO / NOT READY verdict.

---

## What You Get

- A **GO / CONDITIONAL GO / NOT READY** verdict before your AI agent writes a single line
- CLEAR / VAGUE / MISSING status for each of 5 critical context gates
- A **BLOCKERS list** for anything missing — with the exact question to answer or file to read
- Post-task pointers to deeper audit skills (OWASP, 12-factor, DORA) based on what you built

---

## The 5 Gates

| Gate | Name | What goes wrong without it |
|------|------|--------------------------|
| **G1** | Requirements Clarity | Agent builds to the wrong spec; rework takes longer than building from scratch |
| **G2** | Scope Boundary | "Simple" tasks expand; agent refactors things it shouldn't touch |
| **G3** | Context Loaded | Agent makes incorrect assumptions about existing code structure |
| **G4** | Test Strategy | No way to verify the result is correct; bugs ship |
| **G5** | Blast Radius | Working features break silently; production incidents follow |

---

## Who It's For

Any developer using an AI coding agent (Cursor, Copilot, Claude Code, Codex, Antigravity) who has ever:

- Spent 20 minutes reviewing AI output that missed the point entirely
- Watched an AI agent refactor something it wasn't supposed to touch
- Shipped a feature that broke an unrelated flow because nobody mapped the dependencies
- Asked an AI to "add login" and got a 400-line implementation of the wrong thing

---

## Sample Output

```
AI CODING PRE-TASK CHECKLIST
════════════════════════════════════════
Task:     Add a login feature to my app
Verdict:  NOT READY ✗
════════════════════════════════════════

G1  Requirements Clarity    VAGUE
G2  Scope Boundary          MISSING
G3  Context Loaded          MISSING
G4  Test Strategy           MISSING
G5  Blast Radius            VAGUE

BLOCKERS — resolve before coding starts
────────────────────────────────────────
1. G2 Scope Boundary — "login feature" is undefined scope
   → Does this include sign-up, password reset, OAuth, session management?
     List what is IN and OUT explicitly.

2. G3 Context Loaded — agent has not read relevant files
   → Read the existing user/auth model and session handling code first.
```

---

## How It Works

Tell the skill what you're about to build. It evaluates each gate based on the information available, identifies what's vague or missing, and asks the exact questions you need to answer before starting. Takes 2 minutes. Prevents multi-hour rework.

---

## Requirements

Works with VS Code / GitHub Copilot, Cursor, OpenAI Codex, Google Antigravity, Claude Code, and any agent supporting the AgentSkills open standard.

**Install:** `.agents/skills/ai-coding-checklist/SKILL.md`

---

**Free** — part of the Skillforge library.
