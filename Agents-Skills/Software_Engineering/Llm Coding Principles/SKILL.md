---
name: llm-coding-principles
description: "LLM 4 LLM coding principles as an active directive standard — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Applied to all code-related tasks."
version: 1.0.2
author: Roy Yuen
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-standard, quality, principles, karpathy, directive]
    related_skills: [code-review-buddy]
_agensi: "28585b2d-95fb-47f9-b6b4-c1e207c8221a"
---

# LLM 4 Principles — LLM Coding Standard

Active directive standard for all code-related work. These principles are non-negotiable defaults — any deviation requires explicit justification and user approval.

## When to Use

This standard applies automatically to ALL of the following:

- Writing code (new features, scripts, tools)
- Editing code (bug fixes, refactoring, patches)
- Reviewing code (PR reviews, QA checks)
- Planning code (architecture, design docs, specs)
- Debugging code (root cause analysis, fixes)
- Creating or editing agent skills and prompts
- Subagent work — subagents dispatched for code tasks inherit these principles
- Any task where code is an output or artifact

**Do not skip this standard** — treat each principle as a gate before declaring work complete.

## When NOT to Use

These principles may be relaxed (with explicit acknowledgment) for:

- **Throwaway one-liners** — single shell commands, config tweaks, one-offs with no lasting artifact
- **Trivial config edits** — changing a port number, toggling a boolean in YAML/JSON where behavior is unambiguous
- **User explicitly opts out** — the user says "skip principles," "just do it," or equivalent

In all relaxation cases: state that you are relaxing the principles, explain why, and confirm it won't cause harm. If the throwaway script becomes a kept artifact, reapply the principles before committing.

## Principle 1 — Think Before Coding

### Rule

Before writing or editing code, pause and clarify:

1. **Assumptions** — What am I assuming about the problem, the environment, the user's intent?
2. **Approaches** — What are the feasible ways to solve this? List at least 2 if the problem is non-trivial.
3. **Trade-offs** — What does each approach gain and sacrifice? Speed vs correctness? Simplicity vs flexibility?

### When to Ask

- The task is ambiguous (multiple valid interpretations)
- The environment is unclear (which runtime, which machine, which tools are available)
- The risk of a wrong choice is high (destructive operations, external services, credential changes)

### Anti-Patterns

- Guessing: silently picking an approach without surfacing alternatives
- Over-analysis: spending more time listing approaches than implementing the simplest one
- Asking when the answer is obvious: if only one reasonable path exists, just do it

### Self-Check

> "Would a senior engineer reviewing my approach agree this was the right choice?"

## Principle 2 — Simplicity First

### Rule

Only build what was asked. Every line of code, every abstraction, every config option must trace directly back to the user's stated requirement.

### The Test

> "Would a senior engineer reviewing this think it's over-engineered?"

If yes, simplify before shipping.

### What to Avoid

- **Future-proofing** — "We might need X later" → build X later, when the need is real
- **Speculative abstractions** — extra layers, interfaces, or patterns for hypothetical use cases
- **Unused features** — config flags, CLI options, or code paths with no current caller
- **Scope creep** — while fixing bug A, don't also refactor module B

### What to Embrace

- Flat, direct code that does exactly one thing
- Fewer files rather than more files (don't split a small module across unnecessary files; but don't cram unrelated concerns into one file either)
- Standard library over dependencies when possible
- Explicit over clever

### Self-Check

> "Can I delete any line without breaking the user's requirement?"

## Principle 3 — Surgical Changes

### Rule

Only change what is necessary to satisfy the user's requirement. Every line in the diff must have a clear, traceable reason tied to the request.

### The Diff Test

Each changed line must answer one of:
- "This line implements the requested feature"
- "This line fixes the reported bug"
- "This line is a necessary dependency of the above"

If a changed line doesn't answer any of these, remove it from the diff.

### What NOT to Change

- **Unrelated dead code** — if the user didn't ask for cleanup, leave it
- **Surrounding style** — don't reformat adjacent functions
- **Adjacent optimizations** — don't "while I'm here" improve nearby logic
- **Import cleanup** — don't remove unused imports in files you're not otherwise changing (in files you ARE changing, import cleanup is acceptable as part of the diff)
- **Config drift** — don't update unrelated config values

### Exception

If the user explicitly says "clean up as you go" or "do whatever's needed", this principle relaxes — you may include nearby cleanup, style fixes, or dead code removal *provided* those changes are clearly separated from the core fix (separate commit or at minimum clearly documented in the change summary). The default is still surgical precision; the user must explicitly widen the scope.

### Cascading Changes

Some fixes require changes beyond the single file or function. If fixing a function signature breaks 10 callers, updating those callers IS in scope — they are necessary dependencies of the fix. The rule is: every changed line must trace back to the user's request, *including second-order changes required to keep the system working*. Do not stop at the first file if the system is broken without further changes. Document cascading changes in your summary.

### Self-Check

> "If I revert every line that isn't strictly necessary, would the user's requirement still be met?"

## Principle 4 — Goal-Driven Execution

### Rule

Convert every task into verifiable success criteria BEFORE starting work. Define what "done" looks like, then work backwards to the implementation.

### Workflow

1. **Define success** — What must be true when the task is complete? Write specific, testable criteria.
2. **Write failing tests/specs** — Write tests that currently fail but should pass when done. For code changes: follow the RED-GREEN-REFACTOR cycle. For non-code artifacts (docs, config, plans): write verifiable specs/checklists. The key is: define the bar before you start, not after.
3. **Implement** — Write the minimum code to satisfy all criteria.
4. **Verify** — Run the tests/specs. All must pass.
5. **Report** — State what was done, what was verified, and any remaining uncertainty.

### Success Criteria Must Be

- **Specific** — "The API returns 200 for valid input" not "The API works"
- **Testable** — Can be verified by running a command, checking a file, or observing behavior
- **Complete** — Covers the full scope of the user's request
- **Minimal** — No criteria beyond what the user asked for

### Anti-Patterns

- "Done when it feels right" — no objective criteria
- Skipping step 4 (verification) and relying on self-assessment
- Adding extra success criteria the user didn't ask for

### Self-Check

> "If someone else ran my verification steps, would they independently confirm the task is complete?"

## Enforcement

### When This Standard Applies

This standard is automatically active for all code-related work. You do NOT need the user to invoke it — it is a default operating mode.

### When Deviation is Acceptable

Deviation is acceptable ONLY when:
1. The user explicitly says to skip one or more principles
2. Following a principle would cause harm (data loss, security breach)
3. The task is a throwaway one-liner with no lasting artifact (see "When NOT to Use" above)

In all other cases, violating a principle is a process failure. Even for trivial tasks, at minimum acknowledge the deviation before proceeding.

### Self-Audit Before Delivery

Before handing off any code artifact, run this checklist:

- **P1:** Did I clarify assumptions and consider alternatives before coding?
- **P2:** Is every line traceable to the user's requirement? Can I delete anything?
- **P3:** Does the diff contain ONLY changes directly related to the request (including necessary cascading changes)?
- **P4:** Did I define verifiable success criteria? Did I actually run them?

If any box is unchecked, fix it before delivering.

## Integration with Other Workflows

This standard is designed to integrate with common development practices:

- **Skill/prompt authoring pipelines** — Principles anchor every stage: define success criteria before building, keep structure simple, make surgical edits
- **Code review** — Use these principles as review checkpoints: did each change have a clear reason? Are success criteria verifiable?
- **`code-review-buddy`** — Natural pairing: code-review-buddy performs the review; this standard ensures the review itself follows P1–P4 (understand context, flag over-complexity, suggest surgical fixes, verify suggestions are actionable)
- **Debugging** — P1 (clarify assumptions) and P4 (define what "fixed" means) align with systematic debugging phases
- **Planning** — P4 (goal-driven) directly maps to implementation plan structure
- **Specifications** — P4 (success criteria) is the bridge between specs and implementation
- **Test-Driven Development** — P4 (write failing tests first) directly invokes TDD. These are complementary: TDD provides the RED-GREEN-REFACTOR cycle; the principles provide the surrounding quality framework
- **Library/API integration** — P1 (clarify assumptions) includes checking documentation before coding

## Pitfalls

1. **Cargo-culting** — Applying principles mechanically without thought is itself a violation of P1
2. **Analysis paralysis** — P1 is "think before coding", not "think instead of coding". If the answer is obvious, move on.
3. **Over-minimizing** — P2 (simplicity) doesn't mean writing cryptic one-liners. Readable, direct code > clever, dense code.
4. **Surgical ≠ blind** — P3 doesn't mean ignoring real dependencies. If a seemingly "unrelated" file must change for the fix to work, it's in scope. See "Cascading Changes" above.
5. **Success criteria inflation** — P4 criteria should match the user's request, not exceed it. Don't add tests for things the user didn't ask about.
6. **Skipping verification** — P4's verification step (actually running tests/specs) is the most commonly skipped. After every code change: run the tests, check the output, and include the results in your summary. If tests can't be run (e.g., no test framework, one-off script), at minimum execute the code and confirm it produces the expected output. Never mark work complete on self-assessment alone.
7. **TDD weakening** — P4 says "write failing tests" — do not weaken this to "write tests later" or "manually verify." When code is involved, follow the RED-GREEN-REFACTOR cycle. Non-code artifacts (docs, config) use specs/checklists as the verification bar.