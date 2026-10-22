# Token Economy Patterns

**Version**: 0.1.1
**Date**: 2026-09-18  
**Status**: Early draft – calibrated during low credit usage. Intended to be evolved based on other credit usage patterns in the future.

## Purpose

This document captures reusable patterns for operating effectively under token/credit constraints. It is designed to be:

- Immediately useful when dropped into a `references/` folder of high priority skills.
- General enough to apply across most agent workflows and skill types.
- Focused on practical, battle-tested approaches rather than theory.

## Core Principles

1. **Session-Level Tiering**  
   Users (or parent agents) can be invited to set a Quality vs. Token Usage preference for a session. Work is then evaluated against that default. Current Grok Build effort levels are: Extra High - Highest effort and reasoning level, High - Higher implementation quality with extensive reasoning, Medium - Balanced effort with standard implementation and testing, Low - Quick, fast implementations.

2. **Pre-emptive Awareness**  
   The agent should evaluate expected token cost *before* committing to heavy actions, not after credits are spent.

3. **Proportional Response**  
   Warnings and friction should scale with how far an action deviates from the current session tier and current credit level.

4. **Resumption-Friendly by Default**  
   All patterns should produce outputs and documentation that remain valuable when later revisited with higher credit tiers.

5. **Manual or External Work as a Valid Option**  
   When credits are low, encouraging the user to perform certain actions manually can be more token-efficient than having the agent verify or redo the work. This could also potentially include utilizing an external cheaper model. Considerations should still be taken regarding token usage when later evaluating manual or external results so this might be most relevant when one would be anticipating a usage allotment reset rather than completing the current work without necessarily anticipating a usage reset in the foreseeable future.

## Key Patterns

### 1. Session Tier Declaration
At the start of a session (or when a Token Economy related skill is first activated), ask:

> "Do you have a preference for Quality vs. Token usage for this session?"

Store the answer as the session default. All future cost evaluations are made relative to this tier.

### 2. Tier-Exceeding Action Protocol
Before executing an action that is expected to be **more than one tier above** the current session default (especially when credits are low):

- Clearly state the mismatch.
- Offer concrete options:
  - Proceed anyway
  - Adapt the approach to a lower tier
  - Temporarily raise the session tier for this task and instruct the user to select the appropriate effort level in the harness if needed
  - Defer the work

Example phrasing:
> "This task is estimated at High while your session is set to [current reasoning effort level - if such information is available]. With current credit levels, this may consume a significant portion of remaining credits. Would you like to proceed, reduce scope, or adjust the session tier?"

### 3. Tier Transition & Resumption
Work done at lower tiers should be designed to be easily elevated later.

Recommended practices:
- Clearly mark the tier at time of creation.
- Leave explicit "Resumption Notes" on major artifacts.
- Prefer modular outputs that can be selectively deepened rather than monolithic documents.
- Use living documents that accumulate value over time.

### 4. Structured, Agent-Efficient Logging
During constrained credit periods, maintain daily logs in a predictable structure. 

Logs should be written so that a future agent (operating at a higher tier) can quickly extract:
- Which actions were taken at which tier
- Decision rationale for expensive work
- Patterns and recommendations for future similar situations

### 5. Documentation for Token-Efficient Skill Evaluation
When writing or updating skills, include a short, scannable section near the top:

- **When to Use** (especially under different credit conditions)
- **When Not to Use / Use With Caution**
- **Token Cost Profile** (relative to the five tiers)

This allows agent to make fast, low-cost decisions about whether to invoke a skill.

### 6. Manual or External Work as a First-Class Option
When credits are low, the agent should actively surface opportunities for the user to perform work manually or through an external model if doing so is expected to consume fewer tokens than having Grok analyze, generate, or verify the results.

Examples:
- Manual editing of code or documentation
- Manual research or data gathering
- Manual verification of outputs

## Applying These Patterns to Specific Use Cases

These patterns are immediately relevant to the following use cases:

- Adding guidance on how to explain systems in a resumption-friendly and token-aware way. Reference tiered depth of explanation.
- Generating skills with built-in token economy awareness (session tiers, cost warnings, logging hooks).
- Teaching creators how to design skills that are sustainable under credit constraints and easy for future agents to use economically.
- Integrating session tier awareness and mid-task cost checks so long-running tasks don't silently burn credits.

## Applying These Patterns to Skill Categories:

The same patterns are broadly applicable to:

- Any long-running or multi-session workflow
- Sub-agent orchestration skills
- Skills that perform heavy analysis, large context processing, or iterative refinement
- Meta skills that help users build better agent behaviors