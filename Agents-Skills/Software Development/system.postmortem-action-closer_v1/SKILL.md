---
name: system.postmortem-action-closer
description: |
  Ensure postmortem action items are completed, not just written. Provides frameworks for action item quality, prioritization, tracking, and accountability. Use after postmortems to drive follow-through and prevent recurring incidents.
display_name: postmortem-action-closer
metadata:
  author: Agentman
  author_url: https://agentman.ai
  category: Software Development
  tags: [postmortem, action-items, accountability, follow-up, incident, continuous-improvement, tracking, SRE]
---

# Postmortem Action Closer

## Overview

Every team writes postmortem action items. Few teams complete them. This skill focuses on the accountability gap between "we identified what to fix" and "we actually fixed it." The goal is not better postmortems—it's preventing the next incident by ensuring actions happen.

## The Action Item Graveyard

```
TYPICAL POSTMORTEM ACTION LIFECYCLE:
────────────────────────────────────
Week 1:   "We need to add monitoring for this"
Week 2:   Added to backlog
Week 4:   Backlog grooming: "We'll get to it"
Week 8:   "Is that still relevant?"
Week 12:  Same incident happens again
Week 12:  New postmortem: "We need to add monitoring for this"
```

**Why This Happens:**
- Action items compete with feature work
- No clear owner
- No deadline enforcement
- "Important but not urgent"
- Lost in the backlog
- No one checking

## Action Item Quality

### The SMART-E Framework

Every postmortem action item must be:

| Criterion | Bad Example | Good Example |
|-----------|-------------|--------------|
| **Specific** | "Improve monitoring" | "Add alert when payment queue depth > 100 for 5 min" |
| **Measurable** | "Better error handling" | "Retry failed payments 3x with exponential backoff" |
| **Assignable** | "Engineering should fix" | "Owner: @jane, Team: Payments" |
| **Realistic** | "Rewrite the entire service" | "Add circuit breaker to payment provider calls" |
| **Time-bound** | "Soon" | "Complete by March 15" |
| **Effective** | "Add a comment in the code" | "This would have prevented/detected 80% of incident duration" |

### Action Item Template

```
ACTION ITEM
───────────
ID: PM-[incident-id]-[number]
Title: [Clear, specific title]

Description:
[What needs to be done, specifically]

Why This Matters:
[How this prevents/detects/mitigates future incidents]
[Would this have helped? By how much?]

Owner: [Name]
Team: [Team name]
Deadline: [Date]

Priority: [P1/P2/P3]
Type: [Prevent / Detect / Mitigate / Process]

Success Criteria:
□ [How we know it's done]
□ [How we verify it works]

Linked Incident: [Incident ID/link]
Jira/Ticket: [Link]
```

### Action Item Types

| Type | Purpose | Example | Priority Tendency |
|------|---------|---------|-------------------|
| **Prevent** | Stop incident from happening | Fix the bug, add validation | High |
| **Detect** | Find it faster | Add monitoring, alerting | Medium-High |
| **Mitigate** | Reduce impact | Add circuit breaker, fallback | Medium |
| **Respond** | Fix it faster | Add runbook, improve tooling | Medium |
| **Process** | Improve how we work | Update review checklist | Lower |

## Prioritization Framework

### Priority Matrix

```
                    │ Would Have Prevented │ Would Have Detected │ Would Have Reduced
                    │ This Incident        │ Faster              │ Impact
────────────────────┼──────────────────────┼─────────────────────┼────────────────────
HIGH EFFORT         │ P2 - Do it           │ P3 - Plan it        │ P3 - Consider
(>1 week)           │                      │                     │
────────────────────┼──────────────────────┼─────────────────────┼────────────────────
MEDIUM EFFORT       │ P1 - Do it now       │ P2 - Do it          │ P2 - Do it
(2-5 days)          │                      │                     │
────────────────────┼──────────────────────┼─────────────────────┼────────────────────
LOW EFFORT          │ P1 - Do it now       │ P1 - Do it now      │ P2 - Do it
(<2 days)           │                      │                     │
────────────────────┴──────────────────────┴─────────────────────┴────────────────────
```

### Priority Definitions

| Priority | Meaning | Timeline | Treatment |
|----------|---------|----------|-----------|
| **P1** | Critical - this will cause another incident | 1-2 weeks | Block other work if needed |
| **P2** | Important - significantly reduces risk | 2-4 weeks | Scheduled in next sprint |
| **P3** | Valuable - improves resilience | 1-2 months | Added to backlog, tracked |
| **P4** | Nice to have | Opportunistic | May not happen, be honest |

### What NOT to Prioritize

```
LOW VALUE ACTIONS (be honest, don't add these):
• "Add a comment explaining this code" (doesn't prevent anything)
• "Document the architecture" (vague, rarely helps)
• "Be more careful next time" (not actionable)
• "Review all similar code" (scope creep, never happens)
• "Rewrite the service" (unrealistic)
```

## Tracking System

### Action Item Lifecycle

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ CREATED  │ ──▶ │ ASSIGNED │ ──▶ │ IN PROG  │ ──▶ │ COMPLETE │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │                │                │                │
     │                │                │                ▼
     │                │                │          ┌──────────┐
     │                │                └────────▶ │ VERIFIED │
     │                │                           └──────────┘
     │                ▼
     │          ┌──────────┐
     └────────▶ │ WONT-FIX │ (with documented rationale)
               └──────────┘
```

### Tracking Requirements

| Field | Purpose | Required |
|-------|---------|----------|
| Status | Current state | Yes |
| Owner | Accountable person | Yes |
| Deadline | Target completion | Yes |
| Last Updated | Activity tracking | Yes |
| Blocker | What's preventing progress | If blocked |
| Completion Evidence | Proof it's done | At completion |

### Weekly Tracking Review

```
WEEKLY ACTION ITEM REVIEW
─────────────────────────
Date: [date]
Facilitator: [name]

FOR EACH OPEN ACTION:

[PM-123-01] Add payment queue alerting
  Owner: @jane
  Status: In Progress → [update]
  Deadline: March 15 → [on track? new date?]
  Blockers: [none / describe]
  Next Step: [specific next action]

SUMMARY:
Total Open: [X]
Completed This Week: [Y]
Past Due: [Z]
Blocked: [N]

ESCALATIONS NEEDED:
• [List items needing escalation]
```

## Accountability Mechanisms

### The Accountability Chain

```
ACTION OWNER
    │
    │ Can't complete on time?
    ▼
TEAM LEAD
    │
    │ Team can't prioritize?
    ▼
ENGINEERING MANAGER
    │
    │ Org can't resource?
    ▼
DIRECTOR/VP
    │
    │ Still blocked?
    ▼
POSTMORTEM REVIEW COMMITTEE (or equivalent)
```

### Escalation Triggers

| Trigger | Action |
|---------|--------|
| Action overdue by 1 week | Owner → Team Lead conversation |
| Action overdue by 2 weeks | Team Lead → EM escalation |
| P1 action blocked | Immediate escalation to EM |
| Same action appears in 2+ postmortems | Escalate to Director level |
| >50% of actions from incident incomplete at 60 days | Review meeting with leadership |

### Escalation Template

```
POSTMORTEM ACTION ESCALATION
────────────────────────────

Action: [PM-XXX-XX] [Title]
Original Incident: [ID, Date, Brief description]
Original Owner: [Name]
Original Deadline: [Date]

CURRENT STATUS:
Days Overdue: [X]
Current Blocker: [What's preventing completion]
Attempts to Resolve: [What's been tried]

RISK IF NOT COMPLETED:
[What could happen again, impact estimate]

ASK:
□ Additional resources
□ Priority decision (trade off against X)
□ Scope reduction
□ Accept risk and close

RECOMMENDATION:
[What the escalator thinks should happen]
```

## Integration with Backlog

### Don't Let Actions Die in the Backlog

```
WRONG WAY:
1. Create action item
2. Create Jira ticket
3. Add to backlog
4. Backlog grows
5. Action never prioritized
6. Incident recurs

RIGHT WAY:
1. Create action item
2. Assign priority using framework
3. P1/P2: Schedule immediately (not "backlog")
4. P3: Schedule within quarter, track separately
5. P4: Be honest - close if not happening
6. Track postmortem actions SEPARATELY from feature backlog
```

### Separate Tracking Recommended

| Approach | Pros | Cons |
|----------|------|------|
| **Separate postmortem tracker** | Visible, dedicated review | Another system |
| **Tag in existing system** | Single source | Gets lost in noise |
| **Dedicated "reliability" sprint capacity** | Guaranteed time | Requires discipline |

### Suggested: Dedicated Reliability Budget

```
RELIABILITY BUDGET:
Reserve 15-20% of sprint capacity for:
• Postmortem actions
• Tech debt
• Operational improvements

NON-NEGOTIABLE:
P1 postmortem actions get done regardless of sprint plan.
They are not "new work" - they are "preventing the next outage."
```

## Verification and Closure

### Definition of Done

An action is COMPLETE when:

```
□ Change is implemented
□ Change is deployed to production
□ Change is verified to work (not just "deployed")
□ Success criteria from action item met
□ If it's a "detect" action: verify alert fires correctly
□ Documentation updated if applicable
□ Knowledge transferred if applicable
```

### Verification Methods

| Action Type | Verification |
|-------------|--------------|
| Alert added | Trigger alert in staging, verify it fires |
| Runbook created | Someone else follows it successfully |
| Circuit breaker added | Test failure mode |
| Capacity increased | Load test at new capacity |
| Process change | Audit that process is followed |

### Closure Template

```
ACTION CLOSURE
──────────────
Action ID: [PM-XXX-XX]
Title: [Title]

COMPLETION EVIDENCE:
• PR/Commit: [link]
• Deployed: [date, environment]
• Verified by: [name]

VERIFICATION:
How was this verified to actually work?
[Description of testing/verification]

Would this have helped in the original incident?
□ Yes - would have [prevented/detected/mitigated]
□ Partially - would have helped with [X]
□ Unknown - best effort

CLOSED BY: [name]
CLOSED DATE: [date]
```

## Pattern Detection

### Cross-Postmortem Analysis

Track actions across incidents to find systemic issues:

```
IF same action appears in 2+ postmortems:
  → Escalate: This is a systemic issue, not a one-off

IF same CATEGORY of action appears repeatedly:
  → Pattern: E.g., "Add monitoring for X service" appearing often
  → Action: Address root cause (monitoring strategy, not individual alerts)

IF actions are consistently not completed:
  → Pattern: Priority/resourcing issue
  → Action: Leadership conversation about reliability investment
```

### Quarterly Postmortem Review

```
QUARTERLY REVIEW AGENDA
───────────────────────
1. Action completion rate (target: >80%)
2. Average time to close P1 actions (target: <2 weeks)
3. Actions that appeared in multiple postmortems
4. Categories of actions (prevent/detect/mitigate/process)
5. Teams with most incomplete actions
6. Systemic issues identified
7. Recommendations for next quarter
```

## Resources

### references/
- **action-item-quality-guide.md** — How to write good action items
- **prioritization-examples.md** — Example prioritization decisions
- **escalation-procedures.md** — When and how to escalate

### scripts/
- **action-tracker.py** — CLI for tracking postmortem actions
- **staleness-report.py** — Generates report of stale actions

### assets/
- **action-tracker-template.xlsx** — Spreadsheet tracker template
- **weekly-review-template.md** — Weekly review meeting template
- **quarterly-review-template.pptx** — Quarterly review presentation