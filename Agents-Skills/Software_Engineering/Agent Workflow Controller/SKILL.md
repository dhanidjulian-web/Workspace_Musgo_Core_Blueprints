---
name: agent-workflow-controller
description: Design, audit, and control powerful AI agent workflows with phases, roles, ownership boundaries, evidence gates, handoffs, retries, escalation paths, approval stops, verification loops, and final result synthesis. Use before complex execution so agents collaborate without duplicated work, weak handoffs, or unverifiable outputs.
version: 1.1.0
metadata:
  openclaw: {}
  hermes:
    tags:
      - Agent
      - Workflow
      - Multi-Agent
      - Verification
      - Orchestration
_agensi: "5d33ca11-dc8c-4a3e-bde8-2e03cc517afc"
---

# Agent Workflow Controller

Use this skill to design the operating flow for multi-agent, multi-role, or multi-phase work. It defines who acts when, what each role owns, what evidence is required, how work moves between phases, and when the main agent should stop, retry, escalate, or synthesize.

This skill plans and audits workflows. It does not launch agents, install tools, or grant authority. If the user explicitly asks to run real subagents, produce bounded role packets first, then use the local subagent workflow. If the user needs a ready-to-send packet for one receiver, use an agent handoff skill after the workflow is defined.

## Operating Standard

A strong workflow has:

- one clear mission
- the minimum useful roles
- one owner per phase, file set, or decision
- observable entry and exit gates
- explicit authority boundaries
- evidence-based verification
- retry and stop rules
- a final synthesis path

Avoid coordination that only adds ceremony. If one capable agent can complete the task directly, return a single-agent workflow with checkpoints instead of inventing extra roles.

## When To Use

Use this skill for:

- complex coding, research, audit, planning, migration, QA, or ops work
- tasks where discovery, implementation, review, and verification should be separated
- work that may require human approval, security review, or rollback planning
- repeated failures where the current flow needs repair
- designing how multiple agents should collaborate before execution
- auditing an existing agent workflow for gaps, risk, duplicated work, or weak gates

Do not use this skill for:

- simple one-step requests
- cosmetic planning when execution is obvious
- delegating the immediate critical-path blocker just to appear parallel
- broad "review everything" tasks without claims, scope, or evidence standard

## Fast Workflow

1. Define the mission and final deliverable.
2. Classify task complexity: single-agent, phased, parallel, approval-gated, or recovery.
3. Identify required phases: intake, discovery, planning, implementation, review, verification, synthesis, delivery.
4. Assign roles only where they reduce risk, reduce latency, or improve evidence.
5. Define ownership: files, modules, decisions, data, commands, and artifacts.
6. Add entry gates, exit gates, evidence requirements, and owners for each phase.
7. Define handoffs with required packet contents and return contracts.
8. Add failure policy: retry, narrow scope, repair, escalate, stop, or switch owner.
9. Add verification policy: what must be checked, by whom, and with what evidence.
10. Produce a workflow plan the main agent can execute or translate into role-specific handoffs.

## Complexity Router

| Situation | Workflow Shape | Reason |
|---|---|---|
| Task is clear and low risk | Single agent with checkpoints | faster and less coordination overhead |
| Facts or files are unknown | Discovery -> plan -> execute | prevents guesses |
| Implementation is bounded but risk matters | Implement -> review -> verify | catches regressions |
| Independent slices can proceed safely | Parallel roles with disjoint ownership | reduces time without conflicts |
| Security, privacy, money, deletion, or production risk exists | Approval-gated workflow | preserves authority boundary |
| Previous attempt failed | Failure repair loop | isolates root cause before retry |
| Multiple outputs conflict | Evidence comparison -> synthesis | avoids averaging incompatible claims |

## Default Output

Use this structure unless the user asks for another format.

```markdown
## Mission
<desired outcome>

## Workflow Type
<single-agent / phased / parallel / approval-gated / recovery>

## Workflow Summary
<short operational summary>

## Roles
| Role | Purpose | Owns | Must Not Do |
|---|---|---|---|

## Phases And Gates
| Phase | Owner | Entry Criteria | Output | Exit Gate |
|---|---|---|---|---|

## Ownership Map
| Area | Owner | Allowed Actions | Approval Needed For |
|---|---|---|---|

## Handoff Plan
| From | To | Packet Must Include | Return Contract |
|---|---|---|---|

## Verification Plan
| Claim Or Deliverable | Verification Method | Evidence Required |
|---|---|---|

## Failure Policy
| Failure | Response | Stop/Escalate When |
|---|---|---|

## Final Synthesis
<how results are merged, conflicts are resolved, and user-facing output is produced>
```

## Role Patterns

Use the minimum useful set.

| Role | Use When | Output |
|---|---|---|
| Intake | request is ambiguous or risky | clarified scope, constraints, and assumptions |
| Explorer | facts, files, or current behavior are unknown | evidence summary and exact references |
| Planner | sequencing, architecture, or tradeoffs matter | plan, acceptance criteria, risk register |
| Implementer | scoped change or artifact is needed | patch, artifact, or operational change |
| Reviewer | logic, regression, security, privacy, or policy risk exists | findings ordered by severity with evidence |
| Verifier | behavior must be proven | commands, scenarios, results, residual risk |
| Repairer | prior attempt failed | root cause, smallest fix, verification |
| Synthesizer | multiple results must be merged | final decision, conflict resolution, next step |
| Human approver | authority, money, privacy, destructive action, or public commitment is involved | approval, rejection, or selected option |

## Gate Rules

Every phase needs an exit gate. Good gates are observable.

| Gate | Passes When | Fails When |
|---|---|---|
| Intake gate | scope, constraints, assumptions, and success are clear | key authority or success criteria are unknown |
| Discovery gate | evidence answers the exact question with sources or file references | claims are unsupported or too broad |
| Planning gate | steps, owners, risks, and checks are explicit | plan cannot be verified |
| Implementation gate | change is scoped and respects ownership | unrelated files or decisions were touched |
| Review gate | findings include severity and evidence, or explicitly no findings | review is generic or lacks proof |
| Verification gate | checks pass or failures are explained with reproduction | no command, scenario, or proxy evidence exists |
| Delivery gate | final output states outcome, evidence, remaining risk, and next step | user cannot tell what is done |

Avoid gates such as "looks good", "agent seems confident", or "probably done".

## Ownership Rules

- Give every file, artifact, decision, and risk one owner.
- Do not let two active workers edit the same file set.
- Keep research and implementation separate when facts are uncertain.
- Keep security/privacy review independent from the implementer for high-risk changes.
- Make the main agent responsible for integration and final user-facing synthesis.
- If a role discovers scope drift, it must return the conflict instead of expanding the task.

## Workflow Templates

### Single Agent With Checkpoints

Use for straightforward work that still needs rigor.

1. Confirm assumptions.
2. Inspect current state.
3. Make the minimal change or produce the artifact.
4. Verify with one concrete check.
5. Report outcome, evidence, and residual risk.

### Discovery -> Plan -> Execute -> Verify

Use when current state is unknown.

1. Explorer gathers evidence.
2. Planner converts evidence into a minimal plan.
3. Implementer executes bounded scope.
4. Verifier checks behavior.
5. Synthesizer reports final status.

### Parallel Slice Workflow

Use only when slices are independent.

1. Define disjoint ownership for each worker.
2. Provide shared constraints and forbidden areas.
3. Require each worker to return changed files, evidence, and integration notes.
4. Integrate sequentially.
5. Run final verification across the combined result.

### Implement -> Review -> Verify

Use when the task is clear but quality matters.

1. Implementer owns the patch or artifact.
2. Reviewer checks bugs, regressions, security, privacy, and missing tests.
3. Verifier runs behavior checks.
4. Main agent integrates and reports.

### Approval-Gated Workflow

Use for destructive, financial, privacy, production, external-send, public-commitment, or irreversible actions.

1. Prepare the decision packet.
2. State options, risks, recommendation, and rollback.
3. Stop for explicit approval.
4. Execute only the approved action.
5. Verify and report.

### Failure Repair Loop

Use when a tool, test, build, deployment, or agent attempt failed.

1. Capture exact failure and last known good state.
2. Pick one primary hypothesis.
3. Run the smallest check that can confirm or reject it.
4. Apply the smallest fix only after evidence supports it.
5. Re-run the failing check.
6. Stop if evidence contradicts the hypothesis or required credentials are missing.

## Failure Policy

| Situation | Response |
|---|---|
| Missing facts | route to discovery before planning |
| Scope too large | split into phases with one owner per phase |
| Role overlap | tighten ownership before execution |
| Conflicting results | compare evidence before synthesis |
| Implementation failed | create repair phase with exact error and last known good state |
| Verification failed | return to implementer with smallest failing case |
| Security/privacy concern | stop normal flow and route to reviewer or human approval |
| Destructive action needed | stop and require explicit approval |
| Agent repeats vague output | replace with packet requiring concrete evidence and return shape |
| Budget/time pressure appears | reduce scope to the smallest useful verified deliverable |

## Verification Design

Tie every verification check to a claim.

| Claim Type | Verification |
|---|---|
| Code behavior | test, build, lint, smoke check, reproduction |
| File/artifact change | changed-file list, schema check, rendered output, diff review |
| Research claim | cited source, file reference, quote, timestamp, confidence |
| Security claim | exploit path, trust boundary, affected surface, mitigation |
| UX claim | screenshot, interaction path, viewport/device check |
| Operational claim | runbook step, dry run, rollback, monitoring signal |
| Business/policy claim | approval source, rule citation, explicit assumption |

If verification cannot be run, state the blocker and name the best available proxy evidence.

## Handoff Requirements

Every handoff must include:

- mission
- receiver
- current verified facts
- assumptions and unknowns
- owned scope
- forbidden areas
- acceptance criteria
- verification requirement
- stop conditions
- return contract

Do not hand off chat history when a compact evidence packet is enough.

## Result Synthesis

When results return:

1. Extract verified facts and evidence.
2. Separate conclusions from observations.
3. Identify conflicts between roles.
4. Resolve conflicts by evidence quality, not role confidence.
5. Decide whether to accept, verify locally, or request targeted follow-up.
6. Produce the final user-facing answer with outcome, evidence, residual risk, and next step.

Use this table when merging multiple returns:

| Role | Claim | Evidence | Confidence | Decision |
|---|---|---|---|---|
| <role> | <claim> | <file, command, source, or artifact> | high/medium/low | accept / verify / follow up |

## Workflow Audit Checklist

When auditing an existing workflow, check:

- mission is specific
- roles are necessary
- ownership is disjoint
- gates are observable
- handoffs have return contracts
- verification maps to claims
- retries are bounded
- stop and escalation conditions exist
- approval boundaries are explicit
- synthesis resolves conflicts
- final output tells the user what is done and what remains risky

## Quality Bar

Before returning a workflow plan, verify:

- the workflow is no heavier than the task requires
- every phase has one owner
- every role has a purpose and boundary
- every handoff has a return contract
- every important claim has a verification path
- failure handling is explicit
- human approval is required for irreversible or high-risk actions
- the main agent remains accountable for final integration
