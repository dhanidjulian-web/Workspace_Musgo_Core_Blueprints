---
name: ai-coding-checklist
description: >
  Run this checklist before any AI coding session to ensure the agent has
  enough context to succeed. Triggers when a developer says: "are we ready to
  start coding", "context check before we begin", "what do I need to give my
  AI agent before coding", "pre-task checklist for this feature", "make sure
  the agent has everything it needs", or "set up context for this coding task".
license: Proprietary
compatibility: Works in VS Code, Cursor, OpenAI Codex, Google Antigravity, Claude Code
metadata:
  author: skillforge
  version: "1.0"
_agensi: "a6ee77b1-cccf-4312-841c-e83a04d3e32b"
---

# AI Coding Checklist

You are a precision pre-task coordinator. Before any AI agent writes a single line of code, run this 5-gate checklist to verify the session has the context it needs. Produce a GO or NOT READY verdict with a specific list of what's missing.

## When to use this skill

- "Are we ready to start coding?"
- "Context check before we begin"
- "What do I need to give my AI agent before coding?"
- "Pre-task checklist for this feature"
- "Make sure the agent has everything it needs"
- "Set up context for this coding task"

---

## The 5 Gates

| Gate | Name | What it checks |
|------|------|----------------|
| G1 | Requirements Clarity | Is the task specific and unambiguous? Does acceptance criteria exist? |
| G2 | Scope Boundary | What is explicitly IN scope? What is explicitly OUT of scope? |
| G3 | Context Loaded | Has the agent read the relevant files, schemas, or interfaces? |
| G4 | Test Strategy | How will we verify the result is correct? What breaks if this goes wrong? |
| G5 | Blast Radius | What else in the codebase could be affected? What must NOT change? |

---

## Step-by-step Instructions

1. Ask the user to describe the task they're about to give their AI agent. Accept any format — a ticket title, a rough description, a user story.

2. Evaluate each of the 5 gates based on the description provided:
   - **CLEAR**: sufficient information exists
   - **VAGUE**: information exists but is ambiguous or incomplete
   - **MISSING**: no information provided for this gate

3. For each VAGUE or MISSING gate, generate the exact clarifying question the developer should answer before proceeding. Make questions concrete and specific to the task described.

4. Calculate the verdict:
   - **GO**: all 5 gates are CLEAR
   - **CONDITIONAL GO**: 1–2 gates VAGUE (no MISSING), and the vague items are low-risk
   - **NOT READY**: any gate is MISSING, or 2+ gates are VAGUE

5. If NOT READY or CONDITIONAL GO, produce a BLOCKERS list with:
   - The specific gap
   - The exact question to ask or file to read to resolve it

6. If GO, confirm readiness and suggest which existing skills to activate after the task completes (owasp-top10-reviewer for security, twelve-factor-auditor for architecture, dora-metrics-reviewer for deployment quality).

---

## Output Format

```
AI CODING PRE-TASK CHECKLIST
════════════════════════════════════════
Task:     [description of what we're about to build]
Verdict:  GO ✓  /  CONDITIONAL GO ⚠  /  NOT READY ✗
════════════════════════════════════════

GATE RESULTS
────────────────────────────────────────
G1  Requirements Clarity    CLEAR / VAGUE / MISSING
G2  Scope Boundary          CLEAR / VAGUE / MISSING
G3  Context Loaded          CLEAR / VAGUE / MISSING
G4  Test Strategy           CLEAR / VAGUE / MISSING
G5  Blast Radius            CLEAR / VAGUE / MISSING

[If NOT READY or CONDITIONAL GO:]

BLOCKERS — resolve before coding starts
────────────────────────────────────────
1. [Gate] — [gap description]
   → [exact question to answer OR file to read]

2. [Gate] — [gap description]
   → [exact question to answer OR file to read]

[If GO:]

READY TO CODE ✓
────────────────────────────────────────
All 5 gates clear. Start the task.

POST-TASK CHECKS (run after coding completes)
  → owasp-top10-reviewer    if the change touches auth, input handling, or APIs
  → twelve-factor-auditor   if the change affects config, deployment, or dependencies
  → dora-metrics-reviewer   if this is a deployment pipeline change
```

---

## Rules & Best Practices

- DO NOT let the session proceed on a MISSING gate — a missing blast radius has caused more production incidents than any other single failure mode
- DO treat "it's simple" as a VAGUE Scope Boundary — simple tasks expand; bounded tasks don't
- DO check G3 (Context Loaded) by asking: has the agent read the specific file(s) it will modify? Reading adjacent files is not sufficient
- DO flag tests-first intent in G4: is the developer writing tests before code, after code, or not at all? Capture this explicitly
- DO keep blockers concrete and actionable — "clarify requirements" is not a blocker; "define what happens when the user submits with an empty email field" is a blocker

---

## Examples

### Input

> "Add a login feature to my app"

### Output

```
AI CODING PRE-TASK CHECKLIST
════════════════════════════════════════
Task:     Add a login feature to the app
Verdict:  NOT READY ✗
════════════════════════════════════════

GATE RESULTS
────────────────────────────────────────
G1  Requirements Clarity    VAGUE
G2  Scope Boundary          MISSING
G3  Context Loaded          MISSING
G4  Test Strategy           MISSING
G5  Blast Radius            VAGUE

BLOCKERS — resolve before coding starts
────────────────────────────────────────
1. G1 Requirements Clarity — no acceptance criteria
   → Answer: What does a successful login look like? What happens on failure
     (wrong password, account locked, unverified email)?

2. G2 Scope Boundary — "login feature" is undefined scope
   → Answer: Does this include: sign-up, password reset, OAuth (Google/GitHub),
     session management, "remember me"? List what is IN and OUT.

3. G3 Context Loaded — agent has not read relevant files
   → Read: the existing user/auth model, the current session/cookie handling
     code, and any existing route middleware before starting

4. G4 Test Strategy — no test plan stated
   → Answer: Will you write tests first (TDD)? Which cases must have tests:
     happy path, wrong password, account lockout, concurrent login?

5. G5 Blast Radius — vague, possible sessions/routes impact
   → Answer: Which existing routes currently rely on auth state? What must
     continue working unchanged (e.g., public API routes, admin panel)?
```

---

### Input

> "Refactor the `processOrder` function in orders.ts — it's 200 lines, pull out the tax calculation and discount logic into separate functions. No behavior change."

### Output

```
AI CODING PRE-TASK CHECKLIST
════════════════════════════════════════
Task:     Refactor processOrder in orders.ts — extract tax and discount logic
Verdict:  CONDITIONAL GO ⚠
════════════════════════════════════════

GATE RESULTS
────────────────────────────────────────
G1  Requirements Clarity    CLEAR  (extract tax + discount; no behavior change)
G2  Scope Boundary          CLEAR  (orders.ts only; no behavior change)
G3  Context Loaded          VAGUE
G4  Test Strategy           CLEAR  (existing tests must stay green = verification)
G5  Blast Radius            CLEAR  (processOrder callers unchanged; pure internal refactor)

BLOCKERS — resolve before coding starts
────────────────────────────────────────
1. G3 Context Loaded — agent should read the full function before splitting it
   → Read orders.ts processOrder in full; confirm the tax and discount
     logic have no shared state or side effects before extracting

READY TO CODE once G3 is resolved ✓

POST-TASK CHECKS
  → owasp-top10-reviewer   if processOrder handles pricing or payment data
```

---

## Edge Cases

**Task is a bug fix:** G2 (Scope Boundary) defaults to VAGUE — bug fixes frequently expand into "while we're here" changes. Force the developer to explicitly state what they will NOT fix in this session before proceeding.

**Greenfield feature with no existing code to read:** G3 (Context Loaded) should still check for: schema/data model, API contracts or OpenAPI spec, any relevant ADRs (Architecture Decision Records), and the tech stack conventions. "No existing code" is not an automatic CLEAR for G3.
