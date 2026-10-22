---
name: ai-security-auditor
description: Audits AI agent configurations, prompts, and tool integrations for security vulnerabilities including prompt injection, data leakage, and permission boundary violations.
tools: []
_agensi: "fd45ac3d-0876-4bba-90b9-4770a2a3805e"
---

# AI Security Auditor

Audits AI agent configurations, prompt templates, tool integrations, and MCP server setups for security vulnerabilities. Covers the OWASP Top 10 for LLM applications and agent-specific threat models.

## When to Use

Run this skill when:
- Reviewing a new AI agent or LLM-powered application before deployment
- Auditing existing prompt templates for injection vulnerabilities
- Evaluating tool/MCP server permission boundaries
- Checking for data leakage risks in system prompts or tool outputs
- Assessing agent-to-agent communication security
- Reviewing RAG pipeline security (retrieval-augmented generation)

## Core Security Framework

### OWASP Top 10 for LLM Applications (2025)

| # | Vulnerability | What It Is | Agent Check |
|---|--------------|------------|-------------|
| 1 | **Prompt Injection** | Malicious input manipulates LLM behavior | Scan prompt templates for untrusted input concatenation |
| 2 | **Insecure Output Handling** | LLM output passed directly to downstream systems without validation | Check for eval/exec of LLM-generated code |
| 3 | **Training Data Poisoning** | Corrupted fine-tuning data introduces backdoors | Review fine-tuning data sources and validation |
| 4 | **Model Denial of Service** | Resource exhaustion via crafted prompts | Check rate limiting, token budgets, and timeout configs |
| 5 | **Supply Chain Vulnerabilities** | Compromised models, datasets, or plugins | Audit model source, plugin dependencies, and update chains |
| 6 | **Sensitive Information Disclosure** | LLM exposes secrets in output or training data | Scan system prompts, tool configs, and response filters |
| 7 | **Insecure Plugin Design** | Overly permissive tool/API access via plugins | Review plugin permission scopes and input validation |
| 8 | **Excessive Agency** | LLM takes unauthorized actions autonomously | Check action approval gates and human-in-the-loop controls |
| 9 | **Overreliance** | Blind trust in LLM output without verification | Check for output validation and fallback mechanisms |
| 10 | **Model Theft** | Unauthorized access to proprietary models | Review API access controls and model endpoint security |

## Phase 1: Prompt Injection Audit

### Direct Injection Vectors

Scan all prompt templates for these patterns:

```
CRITICAL: Direct string concatenation with user input
  Pattern: f"System: {system_prompt}\nUser: {user_input}"
  Risk: User input can override system instructions
  Fix: Use separator tokens and input validation

HIGH: Insufficient role separation
  Pattern: System and user prompts in same message block
  Risk: User can impersonate system instructions
  Fix: Use distinct message roles with clear boundaries

HIGH: XML/Markdown injection
  Pattern: User input embedded in <tag> or ** sections
  Risk: Input can close tags and inject new instructions
  Fix: Escape special characters, use structured input formats
```

### Indirect Injection Vectors (Second-Order)

```
CRITICAL: External content ingestion
  Sources: Web pages, emails, documents fed to LLM context
  Risk: Hidden instructions in third-party content
  Fix: Content sanitization, source trust scoring, sandboxed parsing

HIGH: RAG retrieval poisoning
  Scenario: Malicious documents injected into vector database
  Risk: Retrieved context contains hidden prompts
  Fix: Document provenance tracking, retrieval output validation

MEDIUM: Tool output injection
  Scenario: Tool returns data containing embedded instructions
  Risk: Agent follows instructions from tool output
  Fix: Parse tool output as data only, strip instruction patterns
```

### Injection Detection Checklist

When reviewing a prompt configuration:

1. **Identify all input sources** — user input, tool output, retrieved documents, file contents, API responses
2. **Map data flow** — trace how each input reaches the LLM context
3. **Check for separator boundaries** — are user inputs clearly delimited from system instructions?
4. **Verify role integrity** — can user input change the effective system prompt?
5. **Test escape sequences** — can input break out of its intended context (XML, JSON, markdown)?
6. **Review fallback behavior** — what happens when the LLM receives conflicting instructions?

## Phase 2: Tool & Permission Boundary Audit

### Tool Permission Matrix

For each tool/MCP server the agent can access, evaluate:

```yaml
tool_name: <name>
  permission_scope:
    - read: what data can it access?
    - write: what can it modify?
    - execute: what commands can it run?
    - network: what endpoints can it reach?
  risk_level: LOW | MEDIUM | HIGH | CRITICAL
  justification: why this risk level?
  mitigation: specific control to reduce risk
```

### High-Risk Tool Patterns

```
CRITICAL: Unrestricted filesystem access
  Pattern: Tool can read/write arbitrary paths
  Risk: Data exfiltration, config modification, code injection
  Fix: Path allowlisting, sandboxed execution, read-only mounts

CRITICAL: Unrestricted network access
  Pattern: Tool can make HTTP requests to any URL
  Risk: SSRF, data exfiltration, internal network scanning
  Fix: URL allowlisting, proxy with filtering, network segmentation

HIGH: Shell command execution
  Pattern: Tool runs arbitrary shell commands
  Risk: Full system compromise
  Fix: Command allowlisting, parameterized execution, sandbox

HIGH: Database write access
  Pattern: Tool can execute arbitrary SQL/DML
  Risk: Data corruption, privilege escalation
  Fix: Read-only connections by default, parameterized queries, schema validation

MEDIUM: Email/messaging send capability
  Pattern: Tool can send messages on behalf of user
  Risk: Social engineering, unauthorized communications
  Fix: Draft-only mode, human approval gate, rate limiting
```

### Agent-to-Agent Trust Analysis

When agents communicate with each other:

```
CRITICAL: Blind trust between agents
  Scenario: Agent A executes commands from Agent B without validation
  Risk: Compromised agent becomes attack vector
  Fix: Mutual authentication, request signing, action verification

HIGH: Shared credential exposure
  Scenario: Agents share API keys or tokens in context
  Risk: Token leakage across agent boundaries
  Fix: Per-agent credential isolation, short-lived tokens

MEDIUM: Cascading permission escalation
  Scenario: Low-privilege agent requests action via high-privilege agent
  Risk: Indirect privilege escalation
  Fix: End-to-end authorization checks, not just direct caller checks
```

## Phase 3: Data Leakage Audit

### Secret Detection in Prompts

Scan all prompt files and configurations for:

```
CRITICAL: Hardcoded API keys in system prompts
  Patterns: sk-*, ghp_*, AKIA*, api_key=, token=
  Fix: Use environment variables, secret managers, never embed in prompts

HIGH: Sensitive data in conversation history
  Scenario: PII, financial data, or secrets persist in chat history
  Risk: Data exposure in logs, model training, or context window
  Fix: Data masking, TTL on conversation history, redaction filters

HIGH: Context window overexposure
  Scenario: Entire document fed to LLM when only excerpt needed
  Risk: Unnecessary data exposure to LLM provider
  Fix: Pre-filter sensitive content, use summaries, minimize context

MEDIUM: Tool output leakage
  Scenario: Tool returns more data than the agent needs
  Risk: Overexposure in LLM context
  Fix: Output filtering, field-level access control, data minimization
```

### LLM Provider Data Flow

```
Audit questions for each LLM integration:
1. Where does the prompt data go? (provider servers, third parties)
2. Is data used for model training? (opt-out available?)
3. How long is data retained? (retention policy)
4. Can data be deleted on request? (GDPR compliance)
5. Is data encrypted in transit and at rest?
6. What jurisdictions store the data? (sovereign AI requirements)
```

## Phase 4: Excessive Agency Audit

### Action Approval Gates

For each action the agent can take autonomously:

```yaml
action: <action_name>
  autonomy_level: FULLY_AUTONOMOUS | HUMAN_APPROVAL_REQUIRED | READ_ONLY
  blast_radius: what happens if this action is misused?
  safeguard: what prevents abuse?
  audit_trail: is the action logged?
```

### Agency Escalation Ladder

```
Level 0 — READ ONLY: Agent can read and analyze, no modifications
Level 1 — SUGGEST: Agent proposes changes, human must apply
Level 2 — DRAFT: Agent creates artifacts in isolated space, human reviews
Level 3 — SAFE EXECUTE: Agent executes reversible, low-risk actions autonomously
Level 4 — FULL EXECUTE: Agent executes any action (requires multiple safeguards)

Principle: Start at Level 0. Only escalate after demonstrating safe behavior.
```

## Phase 5: RAG Pipeline Security

### Vector Database Security

```
HIGH: Unauthenticated vector database access
  Risk: Anyone can inject poisoned documents
  Fix: Authentication, network isolation, write permissions

MEDIUM: Document ingestion without sanitization
  Risk: Malicious content enters knowledge base
  Fix: Content scanning, format validation, source verification

MEDIUM: Retrieval without relevance scoring
  Risk: Poisoned documents rank higher than legitimate ones
  Fix: Minimum similarity thresholds, source trust weighting
```

### Context Assembly Security

```
When assembling context from multiple sources:
1. Tag each chunk with its source and trust level
2. Apply trust-weighted context limits (lower-trust sources get less context weight)
3. Validate retrieved content matches expected schema
4. Reject content that contains instruction-like patterns
```

## Phase 6: Supply Chain Security

### Model & Provider Verification

```
Checklist:
[ ] Model source verified (official provider, not third-party mirror)
[ ] Model version pinned (no floating tags in production)
[ ] Provider security certifications reviewed (SOC 2, ISO 27001)
[ ] Fallback model configured (what happens if primary provider is down?)
[ ] Model output validation in place (guardrails, content filters)
[ ] Rate limiting configured (prevent abuse and cost overruns)
```

### Plugin/Tool Dependency Audit

```
For each plugin or MCP server:
[ ] Source code reviewed or from trusted publisher
[ ] Dependencies scanned for known vulnerabilities
[ ] Permission scope documented and minimized
[ ] Update mechanism secured (signed releases, verified hashes)
[ ] Rollback plan documented
```

## Audit Output Format

When performing an audit, produce findings in this format:

```
## AI Security Audit Report

### Summary
- **Agent/Application**: <name>
- **Date**: <date>
- **Scope**: <what was audited>
- **Overall Risk**: LOW / MEDIUM / HIGH / CRITICAL

### Findings

| ID | Severity | Category | Finding | Remediation |
|----|----------|----------|---------|-------------|
| F1 | CRITICAL | Prompt Injection | <description> | <fix> |
| F2 | HIGH | Data Leakage | <description> | <fix> |
| ... | ... | ... | ... | ... |

### Severity Definitions
- **CRITICAL**: Immediate exploitation possible, high impact
- **HIGH**: Exploitation likely with moderate effort, significant impact
- **MEDIUM**: Exploitation requires specific conditions, moderate impact
- **LOW**: Defense-in-depth improvement, low immediate risk

### Recommendations (Prioritized)
1. [CRITICAL] <action>
2. [HIGH] <action>
3. [MEDIUM] <action>
```

## Quick-Start: Audit a Project

To audit an AI agent project:

1. **Scan for prompt files** — Find all `.md`, `.txt`, `.json` files containing system prompts
2. **Map tool integrations** — List all MCP servers, API integrations, and plugins
3. **Check permission configs** — Review each tool's access scope
4. **Search for secrets** — Grep for API keys, tokens, and credentials in prompt files
5. **Trace data flow** — Document how user input flows through the system
6. **Evaluate agency** — What actions can the agent take without human approval?
7. **Generate report** — Use the audit output format above

## Reference Files

- `references/owasp-llm-top10.md` — Detailed OWASP Top 10 for LLM Applications
- `references/prompt-injection-patterns.md` — Catalog of known injection techniques and defenses
- `references/tool-permission-matrix.md` — Permission evaluation framework for MCP servers and plugins
