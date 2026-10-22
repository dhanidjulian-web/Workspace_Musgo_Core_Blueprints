---
name: system.outage-communication-orchestrator
description: |
  Orchestrate communication during service outages across multiple audiences (customers, executives, support, public). Provides templates, timing guidance, and channel coordination for crisis communication. Use when an outage occurs and stakeholders need to be informed.
display_name: outage-communication-orchestrator
metadata:
  author: Agentman
  author_url: https://agentman.ai
  category: Software Development
  tags: [outage, incident, communication, status-page, crisis, customer-communication, SRE, DevOps, stakeholder]
---

# Outage Communication Orchestrator

## Overview

This skill focuses on WHAT TO SAY, TO WHOM, and WHEN during an outage—not how to fix it. Most teams improvise communication under pressure, leading to confused customers, nervous executives, and inconsistent messaging. This skill codifies communication patterns that build trust even when things break.

## Why Communication Fails During Outages

| Failure Mode | Result |
|--------------|--------|
| Too slow to communicate | Customers find out from Twitter, not you |
| Too technical | Customers don't understand, executives panic |
| Inconsistent across channels | Support says one thing, status page says another |
| Over-promising | "Fixed in 10 minutes" → still broken 2 hours later |
| Under-communicating severity | Customers surprised by data loss, billing impact |
| No internal alignment | Sales making promises engineering can't keep |

## Communication Audiences

```
┌─────────────────────────────────────────────────────────────────┐
│                    AUDIENCE MAP                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EXTERNAL                          INTERNAL                     │
│  ────────                          ────────                     │
│  • Customers (affected)            • Executives                 │
│  • Customers (all)                 • Support team               │
│  • Public (status page)            • Sales/CS team              │
│  • Press (if major)                • Engineering (other teams)  │
│  • Partners/integrations           • Legal/PR (if needed)       │
│                                                                 │
│  Different message for each. Never copy-paste across audiences. │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Communication Timing

### When to Communicate

| Trigger | Action | Timeline |
|---------|--------|----------|
| Outage confirmed | Internal alert to responders | Immediate |
| Impact assessed | Status page update | Within 5-10 minutes |
| Customer-facing impact | Support team enablement | Within 10 minutes |
| SEV1/major outage | Executive notification | Within 15 minutes |
| Extended outage (>30 min) | Customer email/notification | Within 30-45 minutes |
| Resolution | All-clear across all channels | Within 15 min of resolution |
| Post-incident | Follow-up communication | Within 24-48 hours |

### Communication Cadence During Outage

```
ONGOING OUTAGE CADENCE:
─────────────────────────
First 30 minutes: Update every 10-15 minutes
30 min - 2 hours: Update every 20-30 minutes
2+ hours: Update every 30-60 minutes

RULE: Never go silent for more than 30 minutes during active outage.
Even "still investigating" is better than silence.
```

## Status Page Communication

### Status Levels

| Level | Meaning | Use When |
|-------|---------|----------|
| **Operational** | All systems functioning | Normal state |
| **Degraded Performance** | Working but slow/impaired | Latency issues, partial functionality |
| **Partial Outage** | Some users/features affected | Regional issues, specific feature down |
| **Major Outage** | Widespread impact | Core functionality unavailable |

### Status Page Language Patterns

#### Initial Acknowledgment
```
INVESTIGATING: We are investigating reports of [symptom].
Some users may experience [user-visible impact].
We will provide updates as we learn more.

Posted: [time]
```

#### Investigation Update
```
IDENTIFIED: We have identified the cause of [symptom].
The issue is related to [general area - not technical jargon].
Our team is actively working on a fix.
[X]% of users are currently affected.

Posted: [time]
```

#### Mitigation in Progress
```
MONITORING: We have implemented a fix for [issue].
We are monitoring the results.
Some users may still experience [residual impact].
We expect full resolution within [timeframe or "the next X minutes"].

Posted: [time]
```

#### Resolved
```
RESOLVED: The issue affecting [service/feature] has been resolved.
All systems are operating normally.
Users should no longer experience [symptoms].

We apologize for any inconvenience.
A detailed post-incident summary will be shared within [timeframe].

Posted: [time]
Duration: [start time] - [end time] ([X] hours [Y] minutes)
```

### What NOT to Say on Status Page

| Avoid | Why | Instead |
|-------|-----|---------|
| "Database failover in progress" | Too technical | "We're restoring service" |
| "Should be fixed soon" | Vague, sets expectations | "Targeting resolution within 30 minutes" |
| "Minor issue" (when it's not) | Undermines trust | Be accurate about impact |
| Blame (vendor, team, person) | Unprofessional | Focus on resolution |
| "We don't know what's wrong" | Erodes confidence | "We're investigating the root cause" |

## Customer Communication Templates

### Email: Outage Notification (Major)

```
Subject: [Service Name] Service Disruption - [Date]

We're experiencing a service disruption affecting [specific functionality].

WHAT'S HAPPENING
[1-2 sentences describing user-visible impact, not technical cause]

WHAT WE'RE DOING
Our team identified the issue and is actively working to restore service.
We expect resolution within [timeframe] / as quickly as possible.

WHAT YOU CAN DO
[Any workarounds, or "No action needed from you at this time"]

We'll send another update [when: in 30 minutes / when resolved].
For real-time status: [status page URL]

We sincerely apologize for the disruption.

[Name]
[Title]
```

### Email: Resolution Notification

```
Subject: [RESOLVED] [Service Name] Service Disruption - [Date]

The service disruption affecting [functionality] has been resolved.

WHAT HAPPENED
On [date/time], [brief non-technical description of what users experienced].
The issue lasted approximately [duration].

IMPACT
[What was affected: data, transactions, access, etc.]
[Any data loss or required user action]

WHAT WE'RE DOING
We're conducting a thorough review to prevent similar issues.
[Any remediation: credits, extended access, etc.]

We apologize for the inconvenience and thank you for your patience.

[Name]
[Title]
```

### Email: Follow-Up (Post-Incident Summary)

```
Subject: Post-Incident Summary: [Service] Disruption on [Date]

SUMMARY
On [date], [service] experienced a [duration] disruption affecting 
[scope: all users / X% of users / specific regions].

TIMELINE
[Time] - Issue began
[Time] - Issue detected
[Time] - Investigation started
[Time] - Root cause identified
[Time] - Fix implemented
[Time] - Service restored

ROOT CAUSE
[Non-technical explanation of what went wrong]

REMEDIATION
To prevent this from happening again, we are:
• [Action 1]
• [Action 2]
• [Action 3]

We take reliability seriously and apologize for the impact to your operations.

[Name]
[Title]
```

## Internal Communication

### Executive Notification Template

```
INCIDENT BRIEF - [SEV LEVEL] - [Time]
────────────────────────────────────

STATUS: [Investigating / Identified / Mitigating / Resolved]

IMPACT:
• Customer impact: [X users affected / Y% of traffic / $Z revenue at risk]
• Duration so far: [X minutes/hours]
• Services affected: [list]

WHAT HAPPENED:
[2-3 sentences, business terms not technical]

WHAT WE'RE DOING:
• [Current action]
• [Next step]
• ETA to resolution: [time or "unknown, investigating"]

CUSTOMER COMMUNICATION:
• Status page: [Updated / Pending]
• Customer notification: [Sent / Drafting / Not yet needed]

NEXT UPDATE: [Time]

INCIDENT COMMANDER: [Name]
CONTACT: [Slack channel / phone]
```

### Support Team Enablement

```
🚨 ACTIVE INCIDENT - [Service] - [Time]
──────────────────────────────────────

CUSTOMER-FACING SCRIPT:

"We're aware of an issue affecting [feature/service]. Our engineering 
team is actively working on it. Based on current information, we 
expect [resolution timeframe / to have an update within X minutes]."

WHAT CUSTOMERS ARE EXPERIENCING:
• [Symptom 1]
• [Symptom 2]
• [Symptom 3]

WORKAROUNDS:
• [Workaround if any, or "None available at this time"]

DO NOT SAY:
• [Anything about root cause if not confirmed]
• [Specific timeframes unless approved]
• [Technical details]

ESCALATION:
• For VIP/Enterprise customers: [escalation path]
• For press inquiries: [PR contact]

UPDATES: Watch [Slack channel] for real-time updates
```

## Channel Coordination

### Channel Priority by Audience

| Audience | Primary Channel | Secondary |
|----------|-----------------|-----------|
| Public | Status page | Twitter/X |
| Affected customers | In-app banner + email | Status page |
| All customers | Email (if major) | Status page |
| Support team | Slack/internal tool | Email |
| Executives | Slack + brief | Email summary |
| Sales/CS | Slack + talking points | Email |
| Press | PR team only | — |

### Coordination Checklist

```
COMMUNICATION COORDINATION
──────────────────────────

□ Status page updated
□ In-app banner (if applicable)
□ Support team enabled (script + Slack)
□ Exec brief sent
□ Sales/CS notified with talking points
□ Customer email drafted (if needed)
□ Customer email approved (if needed)
□ Customer email sent
□ Twitter/social updated (if major)
□ Press statement ready (if needed)

ALL CHANNELS CONSISTENT: □ Yes
```

## Decision Framework

### When to Send Customer Email

```
SEND EMAIL IF:
□ Outage > 30 minutes AND customer-impacting
□ Data loss or integrity issue (any duration)
□ Security incident affecting customer data
□ Billing/payment system affected
□ SLA breach likely/occurred

DON'T SEND EMAIL IF:
□ Resolved quickly (<15-20 min) with minimal impact
□ Very limited scope (single customer, handled directly)
□ Internal-only impact
```

### When to Involve PR/Legal

| Situation | Involve |
|-----------|---------|
| Data breach / security incident | Legal + PR |
| Potential press coverage | PR |
| Customer data exposed | Legal + PR |
| Regulatory implications | Legal |
| Major customer threatening public statement | PR |
| >4 hour outage of critical service | PR (standby) |

### When to Offer Credits/Remediation

| Situation | Typical Response |
|-----------|------------------|
| Brief outage, no data impact | Apology only |
| Extended outage (>2 hrs), SLA breach | Service credit |
| Data loss | Credit + direct outreach |
| Repeated incidents | Credit + exec apology + remediation plan |

## Post-Incident Communication

### Timeline for Follow-Up

| Communication | Timeline |
|---------------|----------|
| Resolution notification | Within 15 min of resolution |
| Initial "what happened" (if major) | Within 24 hours |
| Detailed post-incident summary | Within 48-72 hours |
| Remediation update | Within 1-2 weeks |

### What to Include in Public Post-Incident

```
INCLUDE:
• What happened (user perspective)
• Timeline of events
• Impact scope
• What we're doing to prevent recurrence

DO NOT INCLUDE:
• Blame (individuals, vendors, teams)
• Excessive technical detail
• Security-sensitive information
• Speculation about cause
```

## Resources

### references/
- **message-templates.md** — Full template library by scenario
- **channel-guide.md** — When to use which communication channel
- **severity-communication-matrix.md** — What to communicate at each severity level

### scripts/
- **timeline-formatter.py** — Formats incident timeline for communications

### assets/
- **email-templates.docx** — Editable customer email templates
- **exec-brief-template.docx** — Executive notification template
- **support-script-template.md** — Support team enablement template