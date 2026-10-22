# Health Gating Patterns

## Core Principle
Every significant autonomous action should be preceded and followed by a structured, machine-readable health check.

## Recommended Output
Always include a `## Machine Data` block with at minimum:
- COMPOSITE (GREEN / YELLOW / RED)
- Key dimensions (Recency, Stability, Drift, Change Safety, Sync Risk)
- Timestamp
- Branch and cleanliness status

## Usage in Prompts / Personas
When delegating to the HealthGatedOperator (or any autonomous sub-agent), include language such as:

"Before any write operation, run a machine health check. Only proceed with autonomous changes if the composite is GREEN or you have a strong justification for YELLOW. Always report pre- and post-health."

## Benefits
- Creates observable audit trail
- Enables streak tracking and autonomy escalation
- Makes resumption much easier for new sessions
- Provides natural "pause" signals when health degrades

This pattern was central to achieving multiple successful autonomous pushes under terminal restrictions.