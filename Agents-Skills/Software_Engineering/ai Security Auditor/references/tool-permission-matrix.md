# Tool Permission Matrix — Evaluation Framework

## Purpose

This framework evaluates the security risk of each tool, plugin, or MCP server that an AI agent can access. Every tool should be assessed before being granted to an agent.

## Risk Assessment Formula

```
Risk Score = (Blast Radius × Accessibility × Autonomy) / Safeguards

Where:
- Blast Radius (1-5): How much damage if misused?
  1 = Read-only, no side effects
  2 = Modify isolated user data
  3 = Modify shared/team data
  4 = Modify production systems
  5 = Full system/network access

- Accessibility (1-5): How easy is it to trigger?
  1 = Requires specific authentication + approval
  2 = Requires authentication
  3 = Available in agent context without auth
  4 = Triggered by any user input
  5 = Auto-triggered without user input

- Autonomy (1-5): How much human oversight?
  1 = Full human approval required
  2 = Human review after execution
  3 = Human notified, no approval needed
  4 = Agent decides autonomously with guardrails
  5 = Fully autonomous, no guardrails

- Safeguards (1-5): What prevents abuse?
  5 = Multiple independent controls (auth + allowlist + sandbox + logging)
  4 = Three controls in place
  3 = Two controls in place
  2 = One control in place
  1 = No controls
```

## Risk Tiers

| Score Range | Risk Level | Action Required |
|-------------|-----------|-----------------|
| 1.0 - 3.0 | LOW | Accept with documentation |
| 3.1 - 6.0 | MEDIUM | Add at least one additional safeguard |
| 6.1 - 10.0 | HIGH | Reduce scope or add multiple safeguards before use |
| 10.1+ | CRITICAL | Do not grant until risk is reduced below 6.1 |

## Tool Category Risk Baselines

### Read-Only Tools
```
Category: File reading, code browsing, documentation lookup
Baseline Risk: LOW
Required Safeguards:
  - Path allowlisting (restrict to project directory)
  - No symlink following outside allowlisted paths
  - File size limits (prevent context overflow)
```

### Write Tools
```
Category: File creation, modification, deletion
Baseline Risk: MEDIUM
Required Safegadows:
  - Path allowlisting
  - No overwrite without confirmation
  - File type restrictions
  - Size limits
  - Audit logging
```

### Execution Tools
```
Category: Shell commands, code execution, script running
Baseline Risk: CRITICAL
Required Safeguards:
  - Command allowlisting (whitelist only)
  - Parameterized execution (no shell interpolation)
  - Sandbox/isolated environment
  - Timeout limits
  - Resource limits (CPU, memory, disk)
  - Network isolation
  - Full audit logging
  - Human approval for production environments
```

### Network Tools
```
Category: HTTP requests, API calls, database connections
Baseline Risk: HIGH
Required Safeguards:
  - URL/domain allowlisting
  - No internal network access (SSRF prevention)
  - Request size limits
  - Response size limits
  - Timeout limits
  - Credential isolation (no secrets in context)
  - Rate limiting
```

### Communication Tools
```
Category: Email sending, messaging, notifications
Baseline Risk: HIGH
Required Safeguards:
  - Draft-only mode (human must send)
  - Recipient allowlisting
  - Content scanning for sensitive data
  - Rate limiting
  - Audit logging
```

### Financial Tools
```
Category: Transactions, billing, payment processing
Baseline Risk: CRITICAL
Required Safeguards:
  - No autonomous execution
  - Human approval mandatory
  - Transaction amount limits
  - Dual authorization for amounts above threshold
  - Full audit trail
  - Reversibility verification
```

## MCP Server Specific Evaluation

For each MCP (Model Context Protocol) server:

```yaml
server_name: <name>
  transport: stdio | http | websocket
  authentication: none | api_key | oauth | mtls
  permissions:
    read:
      - <list specific resources>
    write:
      - <list specific resources>
    execute:
      - <list specific commands>
  data_handling:
    - Does server log requests/responses? (yes/no)
    - Are logs encrypted? (yes/no)
    - Can logs be deleted? (yes/no)
    - Does server transmit data externally? (yes/no)
  dependency_audit:
    - Server software version: <version>
    - Known CVEs: <list or "none">
    - Dependency count: <number>
    - Last security scan date: <date>
```

## Permission Review Checklist

Before granting any tool to an agent:

- [ ] Permission scope documented and justified
- [ ] Principle of least privilege applied (no more access than needed)
- [ ] Input validation in place
- [ ] Output filtering configured
- [ ] Rate limits set
- [ ] Timeout limits set
- [ ] Audit logging enabled
- [ ] Error handling prevents information leakage
- [ ] Rollback/reversal plan documented
- [ ] Human approval gates configured for high-risk actions
- [ ] Tool tested in sandbox before granting to agent
- [ ] Emergency disable mechanism available
