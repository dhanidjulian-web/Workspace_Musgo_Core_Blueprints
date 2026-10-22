# References — AI Coding Checklist

## Source 1: "Accelerate" (Forsgren, Humble, Kim — 2018, IT Revolution Press)

**ISBN:** 978-1942788331

### Context loading and blast radius — why they matter for delivery

The DORA research behind *Accelerate* directly informs Gates G3 and G5 of this skill:

> "High-performing teams have a comprehensive understanding of how their systems work end-to-end. Low performers frequently report that they do not have a good understanding of the systems they work on."

The research found that teams with unclear system understanding had 4× higher change failure rates. Gate G3 (Context Loaded) operationalizes this finding: an AI agent that hasn't read the relevant code is in the same failure mode as a developer who doesn't understand the system.

**On change failure rate and blast radius:**
> "The single most common cause of production incidents is not bugs — it is unintended side effects of changes that developers believed were isolated."

Gate G5 (Blast Radius) is derived directly from this finding. The checklist forces explicit mapping of what could be affected before writing code.

---

## Source 2: "A Philosophy of Software Design" (John Ousterhout — 2nd ed., 2021, Yaknyam Press)

**ISBN:** 978-1732102217

### Requirements clarity and deep modules

Ousterhout's argument for requirement clarity maps directly to Gate G1:

> "One of the most important factors in determining whether code is simple or complex is whether its behavior matches the developer's mental model. Complexity arises when the implementation diverges from expectations — and this divergence almost always starts with unclear requirements."

**On scope creep (Gate G2):**
> "The greatest danger in writing software is not that it will fail to do what you intended — it is that it will do more than you intended. Every feature added beyond the minimum necessary adds complexity disproportionate to its size."

This directly motivates forcing an explicit OUT-OF-SCOPE list before coding begins.

---

## Source 3: "Test-Driven Development: By Example" (Kent Beck — 2002, Addison-Wesley)

**ISBN:** 978-0321146533

### Test strategy as a forcing function for clarity (Gate G4)

> "If you can't describe how you'll know the code is right before you write it, you don't yet understand what you're trying to build."

This is the single most important insight behind Gate G4. If a developer cannot describe the test strategy before coding, the requirements (G1) are effectively also incomplete. The gates are intentionally ordered so G4 failures imply a G1 review.

**On the cost of missing tests:**
> "The time to write the test is not the time lost — it is the time you save on debugging, on rework, on explaining to stakeholders why it doesn't work."

---

## Behavioral Patterns: Why AI Coding Sessions Fail

Research from developer productivity studies (2022–2024) consistently identifies 5 failure modes for AI-assisted coding:

| Failure Mode | Gate That Prevents It |
|-------------|----------------------|
| Agent builds the wrong feature | G1 — Requirements Clarity |
| Agent refactors out-of-scope code | G2 — Scope Boundary |
| Agent uses wrong API/schema version | G3 — Context Loaded |
| Output cannot be verified | G4 — Test Strategy |
| Working features break silently | G5 — Blast Radius |

Each gate in this skill was designed to block exactly one failure mode. A GO verdict means all 5 failure modes have been explicitly addressed before coding begins.

---

## Comparison: Checklist vs. Ad-Hoc Prompting

| Approach | Coverage | Consistency | Time |
|----------|----------|-------------|------|
| Ad-hoc prompting | Depends on developer | Variable | 0–5 min (often skipped) |
| This checklist | All 5 gates, always | Consistent | 2–3 min |
| Full spec doc | Complete | High | 30–60 min |

The 5-gate checklist sits in the optimal position: fast enough to run before every session, thorough enough to prevent the top 5 failure modes. It is not a replacement for full specifications on large projects — it is a pre-flight check for AI-assisted coding tasks.
