# Resumption-Friendly Patterns

## Goal
Make it easy for a completely fresh agent (or new session) to become productive with minimal context loss.

## Key Techniques

1. **Clear "First Things to Read"**
   - Always designate 2–4 files as the resumption surface (e.g. README and other key documentation artifacts).

2. **Living Documents**
   - Maintain files that evolve with the project.
   - These are far more valuable than one-time explanations when resuming.

3. **Structured Result History**
   - Use consistent result formats (AGENT PUSH RESULT blocks, machine data) so an agent can quickly scan what was done and why.

4. **Resumption Notes in Explanations**
   - When documenting a system, include a short section: "What a new agent should read in the first 10 minutes."

## Observed Benefit
Projects that follow these patterns can be picked up by a new Grok session with very little human re-explanation, even after weeks of inactivity.

This was a major factor in the long-term success of the autonomy calibration work.