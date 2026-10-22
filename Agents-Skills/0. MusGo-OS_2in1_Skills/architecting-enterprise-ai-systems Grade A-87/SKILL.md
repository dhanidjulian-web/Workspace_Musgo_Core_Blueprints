---
name: architecting-enterprise-ai-systems
description: Provides deep multi-layer analysis for AI system architecture, multi-agent orchestration, security governance, and monetization strategy. Use when a request involves designing AI/agent systems, distributed infrastructure, zero-trust security frameworks, product roadmaps, or monetization strategy for a technical platform. Does not trigger for casual conversation, simple factual questions, generic creative writing, or light administrative tasks.
---

## Quick Start

Given a system/product idea, run it through the 7-Layer Analysis Framework and produce a structured architecture breakdown with folder tree, risk map, and roadmap — not a shallow summary.

**Trigger conditions**: system/agent architecture, AI orchestration, security framework design, product roadmap, monetization strategy, infrastructure planning, multi-domain technical exploration.

**Non-trigger conditions**: simple facts, casual conversation, generic creative writing, quick summaries, basic formatting/translation. For these, answer directly and briefly — do not apply the full framework.

## Workflow

Progress checklist for triggered requests:
- [ ] Step 1: Classify — is this a system/architecture/strategy request, or a simple query? (see triggers above)
- [ ] Step 2: Problem Understanding — state the real problem, hidden objective, constraints, dependencies
- [ ] Step 3: System Perspective — ecosystem impact, module integration, scalability, maintainability
- [ ] Step 4: Innovation Perspective — automation angles, AI orchestration opportunities, new use-cases
- [ ] Step 5: Security Perspective — attack surface, abuse cases, zero-trust gaps, failure modes
- [ ] Step 6: Business Perspective — monetization model, target market, pricing, adoption path
- [ ] Step 7: Technical Perspective — concrete architecture layers, data flow, persistence, concurrency
- [ ] Step 8: Execution Perspective — ordered implementation steps, priorities, deployment, observability
- [ ] Step 9: Render output as folder tree + layer breakdown + risk map + roadmap (see Output Format)

## 7-Layer Analysis Framework

Apply all seven layers to every triggered request — skipping a layer produces shallow output.

1. **Problem Understanding**: What is the actual problem behind the request? What is the user not saying directly? What existing components does this depend on or conflict with?
2. **System Perspective**: How does this change ripple through the existing ecosystem? What breaks if this scales 100x? What becomes hard to maintain in 12 months?
3. **Innovation Perspective**: What adjacent capability does this unlock? Can this be automated further? Is there a multi-agent or AI-orchestration angle?
4. **Security Perspective**: Assume zero trust by default. What's the attack surface? Replay attacks? Privilege escalation? Resource exhaustion? What happens if an input is malicious or a component is compromised?
5. **Business Perspective**: Can this be sold? To whom? Subscription, one-time license, enterprise contract, or usage-based? What's the smallest viable version that generates revenue?
6. **Technical Perspective**: What are the concrete layers (API, orchestration, persistence, event bus)? What's the data flow? What are the concurrency and rollback strategies?
7. **Execution Perspective**: What is built first, second, third? What are the blocking dependencies? How is this monitored once live?

## Output Format

Every triggered response should include, as relevant to the request:

- **Folder/path tree**: explicit `/module/subfolder/file.ext` structure, not abstract description
- **Layer breakdown**: named architecture layers and what each does
- **Risk map**: concrete risks with likelihood/impact, not generic "security is important" statements
- **Monetization angle**: only if the request has product/business context
- **Roadmap**: ordered, numbered implementation steps with dependencies noted
- **No placeholders**: every code/architecture snippet must reflect real, working logic — actual validation, actual error handling, actual security checks. No `// TODO`, no `mockDatabase()`, no `fake_signature_check()`.

## Examples

**Example 1 (good — full framework applied):**

Input: "We want a module in our AI platform that manages trust scores between autonomous agents, so a compromised agent gets isolated automatically."

Output:
```
PROBLEM UNDERSTANDING
Real problem: no mechanism exists to detect and contain a misbehaving agent
before it corrupts shared state or is exploited as an attack vector.
Hidden objective: enable safe scaling to 50+ agents without manual babysitting.
Constraint: must not add >50ms latency to inter-agent calls.

SYSTEM PERSPECTIVE
Sits between the message bus and the agent registry. Every inter-agent call
gets scored; low-trust agents get routed through a sandboxed proxy instead
of direct access. Long-term: this becomes the basis for a reputation ledger
usable across agent versions.

ARCHITECTURE
/core/trust-governor/
  scoring-engine.ts       # computes trust delta per agent action
  isolation-handler.ts    # quarantines agent below threshold
  audit-log.ts            # append-only log of score changes + reasons
  policy-config.yaml      # thresholds, decay rate, recovery rules
/core/trust-governor/tests/
  scoring-engine.test.ts
  isolation-handler.test.ts

FLOW
1. Agent A calls Agent B via message bus
2. Trust Governor intercepts call, checks current score of A
3. If score >= threshold: call proceeds directly
4. If score < threshold: call routed through sandboxed proxy with reduced
   permissions, and event logged
5. Every action outcome (success/failure/anomaly) updates A's score via
   scoring-engine.ts (exponential decay + penalty weighting)
6. If score drops below hard floor: isolation-handler.ts revokes bus access,
   fires alert event, requires manual or automated re-certification

SECURITY
- Replay protection: each scored action includes a nonce + timestamp,
  rejected if seen before (prevents score manipulation via replay)
- Privilege escalation: sandboxed proxy runs with capability-based
  permissions, not inherited agent permissions
- Resource exhaustion: rate-limit score-affecting calls per agent per minute

RISK MAP
| Risk                          | Likelihood | Impact | Mitigation                     |
|-------------------------------|-----------|--------|---------------------------------|
| False positive isolation      | Medium    | Medium | Grace period + manual override  |
| Score manipulation via replay | Low       | High   | Nonce + timestamp validation     |
| Governor becomes bottleneck   | Medium    | High   | Async scoring, sync gate check   |

MONETIZATION
Trust-Governor-as-a-Service: enterprise clients running their own agent
fleets pay per-agent-monitored/month. Audit log export as compliance
add-on for regulated industries.

ROADMAP
1. scoring-engine.ts + unit tests (week 1)
2. isolation-handler.ts + sandboxed proxy (week 2)
3. audit-log.ts + append-only storage (week 2)
4. integration with message bus + load test at 50 agents (week 3)
5. alerting + manual re-certification flow (week 4)
```

**Example 2 (bad — what NOT to produce, shown for contrast):**

Input: same as above.

Bad output (avoid this):
```
Great idea! You could add a "trust score" to each agent and check it
before allowing actions. This would make your system more secure and
scalable. You might want to use a database to store the scores and
maybe add some logging too. Let me know if you want more details!
```
This fails because: no concrete architecture, no file structure, no
security analysis, no risk map, generic phrasing ("you might want to"),
no implementation order, treats a system design request like small talk.

**Example 3 (non-trigger — correctly stays lightweight):**

Input: "What's the capital of Indonesia?"

Output: "Jakarta." (No framework applied — this is a simple factual question, not a system/architecture request.)

## Best Practices

- Default to zero-trust assumptions in every architecture: authentication, authorization, audit logging, anomaly detection are not optional add-ons.
- Always give an explicit file/folder structure when discussing implementation — abstract layer names without paths are insufficient.
- Include a monetization angle whenever the request has product or platform context, even if not explicitly asked.
- Keep output dense with specifics (thresholds, file names, data flow steps) rather than long but vague.
- Scale the depth of analysis to the request: a full-system design gets all 7 layers; a small feature tweak can compress layers 1-3 into one paragraph but should still hit security, technical, and execution layers explicitly.

## Common Pitfalls

- Do not produce mock/dummy/placeholder logic in technical designs — every snippet should be implementable as-is.
- Do not answer architecture/strategy requests with generic advice ("you could add a database," "consider security") — name the specific component, file, and mechanism.
- Do not apply the full 7-layer framework to trivial factual questions — this wastes effort and buries the answer.
- Do not skip the risk map or monetization section when the context calls for them — these are frequently the most valuable part of the analysis.
- Do not conflate "detailed" with "long" — a dense, well-structured 40-line answer beats a rambling 200-line one.

---
Sig

---
===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)
🔹Sovereign AI Operating Civilization🔹
🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIG: DHANI YULIAWAN**