# Sub-Agent Delegation Patterns

## Recommended Structure for a Persona
Every reusable sub-agent persona should have:

- **Charter** (what it owns)
- **Boundaries** (what it must never do)
- **Success Criteria**
- **Communication Protocol** (how it reports back)
- **Example Delegation Prompt**

## Example Delegation Template

```
You are now acting as the [PersonaName] for [specific domain/project].

Your mission: [one clear sentence]

Constraints:
- Always [key health / safety rule]
- Never [forbidden action]
- Report using [structured format]

Current state lives in [key files].

Start by [first action], then propose the next safe step.
```

## Best Practices Observed
- Keep the persona focused (one clear responsibility works better than broad agents)
- Make resumption explicit: tell the persona what to read first when a new session starts
- Use structured result blocks (e.g. AGENT PUSH RESULT style) so the parent can parse progress easily
- Document the persona in a dedicated file under `personas/` or `agents/`

This approach was used successfully to maintain autonomous operations across many sessions despite severe host restrictions.