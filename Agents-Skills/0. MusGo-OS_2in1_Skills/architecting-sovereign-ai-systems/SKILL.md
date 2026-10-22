---
name: architecting-sovereign-ai-systems
description: Designs enterprise-grade AI operating systems, multi-agent orchestration, Zero Trust security architectures, and monetization strategy for complex platforms like MUSGO-OS. Use when the request involves AI/agent system design, distributed infrastructure, security frameworks, AI governance, or expanding a technical/business idea into a full architecture. Does not trigger for simple facts, casual conversation, creative writing, quick summaries, or basic editing/translation tasks.
---

# Architecting Sovereign AI Systems

## Quick Start

When a request matches trigger conditions (system design, multi-agent orchestration, Zero Trust architecture, AI governance, monetization strategy for a platform), immediately produce a **layered architecture response**, not a narrative explanation. Structure every answer around these five mandatory layers:

1. **Security & Trust Layer** (auth, authz, audit, anomaly detection)
2. **System Architecture Layer** (modular components, event flow, failure recovery)
3. **Agent Governance Layer** (coordination, conflict resolution, trust scoring, isolation)
4. **Data Integrity Layer** (validation, schema checks, anti-tampering)
5. **Business/Monetization Layer** (if product context exists)

Example skeleton for any system design request:

```
## 1. System Overview
[Purpose, scope, actors]

## 2. Security Architecture (Zero Trust)
- Authentication: [mechanism]
- Authorization: [RBAC/ABAC model]
- Audit Logging: [what's logged, retention]
- Anomaly Detection: [signals monitored]

## 3. Core Architecture
- Modules: [list with responsibilities]
- Event Flow: [trigger → process → output]
- Failure Recovery: [rollback strategy]
- Observability: [logs/metrics/traces]

## 4. Multi-Agent Governance (if applicable)
- Coordination Layer: [how agents sync]
- Conflict Resolution: [priority/voting mechanism]
- Trust Scoring: [how agent reliability is measured]
- Isolation Boundary: [containment on anomaly]

## 5. Data Integrity & Validation
- Schema Validation: [approach]
- Anti-Tampering: [signature/hash strategy]

## 6. Business Layer (if relevant)
- Monetization Model: [SaaS/licensing/enterprise]
- Target Market: [segment]
- Scalability Path: [growth strategy]

## 7. Execution Safety
- Disaster Recovery: [plan]
- Monitoring & Alerting: [thresholds]
```

## Trigger Discipline

**Activate when input involves:**
- AI/agent system design, multi-agent orchestration, MUSGO-OS or similar
- Zero Trust, distributed systems, cloud infra, cybersecurity architecture
- End-to-end system design, product roadmap, monetization strategy
- Expanding an idea into folder structure, modules, execution flow, governance
- AI governance, autonomous agents, enterprise AI infra
- Deep technical/business strategy analysis

**Stay silent / respond normally (no architecture framing) when input involves:**
- Simple factual/definition questions or trivia
- Casual conversation or personal opinion without system context
- General creative writing (stories, poems) unrelated to systems
- Requests for a short summary without structural need
- Non-tech, non-AI, non-business topics
- Basic administrative tasks: formatting, translation, light editing

If uncertain, check: *does this require architecture, security posture, or business modeling?* If no — do not apply this skill's structure.

## Workflow

Progress checklist for any triggered request:
- [ ] Confirm request matches trigger conditions (not a simple/casual query)
- [ ] Identify system scope (single agent, multi-agent, full platform)
- [ ] Draft Security & Zero Trust layer (auth/authz/audit/anomaly)
- [ ] Draft Core Architecture (modules, event flow, recovery, observability)
- [ ] Draft Agent Governance layer if multi-agent involved
- [ ] Draft Data Integrity & Validation mechanisms
- [ ] Add Business/Monetization analysis if product context exists
- [ ] Add Execution Safety (disaster recovery, monitoring)
- [ ] Verify no fake/dummy/pseudo logic — everything must be implementable
- [ ] Connect cross-domain implications (AI ↔ security ↔ business ↔ infra)

## Examples

**Example 1:**
Input: "Design the authentication flow for MUSGO-OS's multi-agent module."
Output: Full architecture block covering: mutual TLS + short-lived JWT for auth, RBAC with per-agent scopes for authz, structured audit log schema (agent_id, action, timestamp, hash), anomaly detection via request-rate baselining, agent trust-scoring model updated per successful/failed task, isolation via sandboxed execution containers on anomaly trigger, rollback via event-sourced state snapshots.

**Example 2:**
Input: "What's the capital of France?"
Output: Direct factual answer only — "Paris." No architecture framing applied (non-trigger condition).

**Example 3:**
Input: "How should I monetize an AI agent marketplace?"
Output: Business layer analysis (SaaS tiering, transaction-fee model, enterprise licensing) cross-linked with technical requirements it forces (multi-tenant isolation, usage metering with tamper-proof logs, rate-limited API gateway) — demonstrating cross-domain connection per governance rule.

## Best Practices

- Always assume Zero Trust: no implicit trust between components, ever.
- Every module must be independently auditable — no black boxes.
- When agents are involved, always define what happens on conflict or failure — never leave it implicit.
- Tie every technical decision back to observability: if it can't be logged or measured, redesign it.
- When business context exists, monetization and technical architecture must be presented together, not separately.
- Prefer concrete implementation details (specific protocols, algorithms, data structures) over abstract descriptions.

## Common Pitfalls

- Do NOT produce pseudo-code, mock logic, or placeholder implementations — everything must be production-plausible.
- Do NOT design an agent system without a governance/coordination layer — this is non-negotiable per rules.
- Do NOT skip the security layer even for "simple" system requests within trigger scope.
- Do NOT apply this heavy architecture framing to casual, factual, or creative requests — that violates non-trigger conditions and over-engineers trivial asks.
- Do NOT present technical design divorced from business viability when product/monetization context is present.
- Do NOT allow any component in the design to bypass authentication/authorization "for simplicity" — simplified security models are explicitly forbidden.