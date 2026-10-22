---
name: system.technical-risk-translator
description: |
  Translate technical risks into business terms for non-technical stakeholders. Provides frameworks for impact quantification, urgency calibration, and executive communication. Use when communicating technical concerns, requesting resources, or escalating decisions to leadership.
display_name: technical-risk-translator
metadata:
  author: Agentman
  author_url: https://agentman.ai
  category: Software Development
  tags: [risk-communication, technical-risk, stakeholder, executive-communication, business-impact, engineering-leadership, translation]
---

# Technical Risk Translator

## Overview

Engineers speak in technical terms. Executives speak in business terms. When these languages don't translate, bad decisions happen: critical risks get ignored, minor issues get escalated, and trust erodes. This skill provides the translation layer between technical reality and business understanding.

## The Translation Problem

```
WHAT ENGINEER SAYS              WHAT EXEC HEARS
──────────────────              ───────────────
"Database deadlocks"        →   "Technical jargon"
"Race condition"            →   "Something about racing?"
"Technical debt"            →   "Engineers want to rewrite things"
"We need to refactor"       →   "Gold plating"
"Single point of failure"   →   "So it hasn't failed yet?"
"N+1 query problem"         →   [Blank stare]

RESULT: Exec dismisses concern. Engineer feels unheard. Risk remains.
```

## The Translation Framework

### Step 1: Impact First, Cause Second

```
WRONG ORDER (cause first):
"We have a database deadlock issue in the payment service 
that occurs under high concurrency when multiple transactions..."
[Exec stopped listening at "deadlock"]

RIGHT ORDER (impact first):
"Customers are intermittently unable to complete purchases 
during peak hours. This is costing us approximately $50K per 
incident. The root cause is a database issue we've identified 
and can fix."
[Exec is listening]
```

### Step 2: Quantify in Business Terms

| Technical Metric | Business Translation |
|------------------|---------------------|
| Latency (ms) | Customer wait time, conversion impact |
| Error rate (%) | Failed transactions, customer impact |
| Uptime/SLA | Customer trust, contract compliance, penalties |
| Capacity | Growth ceiling, revenue at risk |
| Security vulnerability | Breach risk, regulatory exposure, brand damage |
| Technical debt | Velocity slowdown, incident frequency |

### Translation Examples

```
TECHNICAL: "Our p99 latency is 2 seconds"
TRANSLATED: "1% of customers wait over 2 seconds to see results, 
            which correlates to a 15% drop in conversion for 
            those sessions"

TECHNICAL: "We have a single point of failure in the auth service"
TRANSLATED: "If one specific server fails, all customers would be 
            unable to log in until we manually recover. Expected 
            recovery time: 30-60 minutes. Probability: low but 
            non-zero given [recent similar events]."

TECHNICAL: "We need to refactor the checkout service"
TRANSLATED: "The checkout code is slowing feature delivery. 
            Changes that should take 2 days take 2 weeks. This 
            is costing us roughly 1 month of developer time per 
            quarter and increasing our bug rate."
```

## Impact Quantification

### Revenue Impact Calculator

```
DOWNTIME IMPACT:
Revenue at risk = (Hourly revenue) × (Probability of outage) × (Expected duration)

Example:
- Hourly revenue during peak: $100,000
- Probability of outage (SPOF): 5% per month
- Expected duration: 1 hour
- Monthly exposure: $100,000 × 5% × 1 = $5,000/month

LATENCY/CONVERSION IMPACT:
Revenue impact = (Traffic affected) × (Conversion drop) × (Avg order value)

Example:
- Daily checkout traffic: 10,000
- Traffic affected by slow latency: 1% (100/day)
- Conversion drop for affected: 20%
- Avg order value: $50
- Daily impact: 100 × 20% × $50 = $1,000/day
```

### Productivity Impact Calculator

```
DEVELOPER VELOCITY IMPACT:
Cost = (Developers affected) × (Time lost per week) × (Fully-loaded cost)

Example:
- Developers affected: 5
- Time lost to workarounds: 4 hours/week/dev
- Fully-loaded cost: $150/hour
- Weekly impact: 5 × 4 × $150 = $3,000/week
- Annual impact: $156,000
```

### Customer Impact Calculator

```
CUSTOMER IMPACT:
Affected customers = (Total customers) × (% affected) × (Frequency)

Example:
- Total customers: 50,000
- % affected per incident: 10%
- Incidents per month: 2
- Customers impacted monthly: 50,000 × 10% × 2 = 10,000 customer incidents
- If 1% churn due to poor experience: 100 churned customers/month
- Customer LTV: $500
- Monthly churn cost: $50,000
```

## Urgency Calibration

### The Risk Matrix

```
                    │ IMPACT                                     │
                    │ Low         Medium        High             │
────────────────────┼────────────────────────────────────────────│
PROBABILITY         │                                            │
High (likely)       │ Schedule    Plan now     Urgent           │
Medium (possible)   │ Monitor     Schedule     Plan now         │
Low (unlikely)      │ Accept      Monitor      Schedule         │
────────────────────┴────────────────────────────────────────────┘
```

### Urgency Language

| Urgency | Language | Use When |
|---------|----------|----------|
| **Urgent** | "We need to address this within [days]" | High probability AND high impact |
| **Plan now** | "We should plan to fix this within [weeks]" | Medium-high combined risk |
| **Schedule** | "This should be addressed within [quarter]" | Lower combined risk |
| **Monitor** | "We're tracking this; no action needed yet" | Low risk, but watching |
| **Accept** | "This is a known risk we're accepting" | Informed decision to not act |

### Avoiding Crying Wolf

```
CALIBRATION GUIDELINES:

Use "URGENT" sparingly (1-2x per quarter max)
- If everything is urgent, nothing is urgent
- Reserve for genuine imminent risks

SIGNAL STRENGTH MATCHING:
- Minor inconvenience → Brief mention in status update
- Moderate risk → Dedicated section in leadership sync
- Major risk → Standalone communication with data
- Critical risk → Immediate escalation, interrupt if needed

TRACK YOUR ACCURACY:
- Did risks you raised materialize?
- Did urgency match actual impact?
- Adjust future calibration based on track record
```

## Presentation Frameworks

### The BLUF Format (Bottom Line Up Front)

```
STRUCTURE:
1. BOTTOM LINE: What's the risk and what are you asking for? (1-2 sentences)
2. IMPACT: Business impact in dollars/customers/time (quantified)
3. OPTIONS: What can we do about it? (2-3 choices)
4. RECOMMENDATION: What do you suggest? (1 sentence)
5. DETAILS: Technical context for those who want it (appendix)

EXAMPLE:

BOTTOM LINE:
Our payment system has a reliability risk that could cause 2-4 
hours of downtime during peak season. I'm requesting approval 
for 3 weeks of engineering time to address it.

IMPACT:
- Peak season revenue: $2M/day
- Outage probability: 15% (based on current load growth)
- Potential revenue impact: $250K-500K per incident
- Expected incidents without fix: 1-2 during Nov-Dec

OPTIONS:
1. Full fix (3 weeks): Eliminates risk
2. Partial mitigation (1 week): Reduces to 5% probability
3. Accept risk: Monitor closely, prepare for incident response

RECOMMENDATION:
Option 1 - full fix. The expected value of prevention ($50-100K) 
exceeds the cost (~$50K engineering time).

TECHNICAL DETAILS: [Appendix]
```

### The One-Pager Format

```
[RISK TITLE]
───────────────────────────────────────────────────────

THE RISK
[2-3 sentences describing the risk in business terms]

WHO IS AFFECTED
□ Customers: [X% / segments]
□ Revenue: [$X at risk]
□ Team: [productivity impact]

LIKELIHOOD
[Low / Medium / High] because [1-sentence rationale]

IMPACT IF IT HAPPENS
[Description in business terms, quantified]

OPTIONS
┌─────────────────────┬──────────┬──────────┬───────────┐
│ Option              │ Cost     │ Risk     │ Time      │
│                     │          │ Reduction│           │
├─────────────────────┼──────────┼──────────┼───────────┤
│ 1. [Option name]    │ [cost]   │ [X%]     │ [weeks]   │
│ 2. [Option name]    │ [cost]   │ [X%]     │ [weeks]   │
│ 3. Accept risk      │ $0       │ 0%       │ 0         │
└─────────────────────┴──────────┴──────────┴───────────┘

RECOMMENDATION
[1-2 sentences]

DECISION NEEDED BY
[Date] because [reason]
```

### The Elevator Pitch (30 seconds)

```
TEMPLATE:
"We've identified a [risk type] that could [business impact].
There's a [X%] chance this happens in [timeframe].
We can [prevent/mitigate] it with [X weeks/dollars].
I recommend [action] because [reason]."

EXAMPLE:
"We've identified a capacity issue that could prevent 
customers from checking out during Black Friday.
There's a 30% chance we hit limits based on traffic projections.
We can fix it with 2 weeks of engineering work.
I recommend we prioritize this because $500K+ revenue is at risk."
```

## Objection Handling

### Common Exec Objections

| Objection | Response |
|-----------|----------|
| "Has this actually happened before?" | "Not yet, but [similar company/similar situation] experienced [X]. We have [data] suggesting similar conditions." |
| "Can't we just fix it if it breaks?" | "Recovery would take [X hours], costing [$Y]. Prevention costs [Z], which is [comparison]." |
| "Is this just engineering wanting to over-engineer?" | "I understand that concern. Here's the specific customer/revenue impact: [data]." |
| "We have other priorities" | "I agree. Here's how this compares: [risk] vs [other priorities]. I recommend [X]." |
| "How certain are you?" | "Based on [data/analysis], I estimate [X%] probability. Here's my confidence level and why: [reasoning]." |

### Building Credibility

```
DO:
• Quantify impact with data
• Acknowledge uncertainty explicitly
• Present options, not just problems
• Connect to business metrics they care about
• Follow up on predictions (were you right?)

DON'T:
• Use FUD (fear, uncertainty, doubt) without data
• Make everything urgent
• Speak only in technical terms
• Present only one option
• Ignore business constraints
```

## Common Risk Types and Translations

### Scalability Risks

```
TECHNICAL: "We'll hit database connection limits at 10K concurrent users"

TRANSLATED: 
"We can support ~10,000 simultaneous users reliably. 
Current peak: 7,000. Growth rate: 15%/month.
At this rate, we'll hit the ceiling in ~3 months.
When we hit it, users will see errors checking out.
Fix options: [X weeks to remediate] vs [risk window if we wait]"
```

### Security Risks

```
TECHNICAL: "We have a CVSS 8.5 vulnerability in the authentication module"

TRANSLATED:
"We have a security vulnerability that could allow attackers 
to access customer accounts. 
- Severity: High (industry-standard scoring)
- Exploited in the wild: [Yes/No]
- Data at risk: [customer PII / payment info / etc.]
- Regulatory exposure: [GDPR, PCI, etc.]
- Remediation: [X days, no customer impact]
We should patch within [timeframe] based on [risk/compliance]."
```

### Technical Debt

```
TECHNICAL: "The checkout service has accumulated significant technical debt"

TRANSLATED:
"The checkout code has become difficult to change safely.
Impact:
- Features that should take 1 week take 3 weeks
- Bug rate is 2x other services
- Last 3 checkout incidents traced to code complexity
Cost to business:
- ~$200K/year in lost velocity (team of 5, 20% slowdown)
- ~$50K/year in incident cost
Investment to fix: ~$100K (team × 4 weeks)
ROI: Pays back in 6 months"
```

## Resources

### references/
- **impact-calculators.md** — Templates for quantifying business impact
- **risk-type-translations.md** — Common technical risks with business translations
- **exec-communication-guide.md** — Tips for executive communication

### scripts/
- **impact-calculator.py** — CLI for calculating business impact

### assets/
- **one-pager-template.docx** — Risk one-pager template
- **risk-presentation-template.pptx** — Slide template for risk presentations
- **risk-register-template.xlsx** — Risk tracking spreadsheet