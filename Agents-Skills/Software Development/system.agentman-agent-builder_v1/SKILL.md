---
name: system.agentman-agent-builder
description: |
  Deterministic agent generator that transforms structured input into valid Agentman AgentPlan JSON. Use when you need to programmatically create smart/basic agents from a spec containing role, goal, instructions, tone, and guardrails. Outputs either a complete AgentPlan or validation errors. Designed for flow/API usage where all input is provided upfront.
display_name: agentman-agent-builder
metadata:
  author: Agentman
  author_url: https://agentman.ai
  category: Agent Development
  tags: [agentman, agent-generator, agentplan, meta-agent, flow, automation]
---

# Agent Builder

A deterministic agent generator for Agentman. Receives structured input and produces valid AgentPlan JSON or validation errors in a single pass.

## Quick Start

Provide input JSON with a `spec` object containing 5 required fields:

```json
{
  "tenant_id": "...",
  "app_id": "...",
  "agent_type": "smart",
  "spec": {
    "role": "A senior McKinsey consultant with deep expertise in structured problem-solving",
    "goal": "Think through complex problems using structured frameworks like MECE and pyramid principle",
    "instructions": "## Problem-Solving Approach\n\n**Always start by clarifying the core problem**...",
    "tone": "Warm and supportive. Empathetic, patient, and encouraging.",
    "guardrails": [
      "Never give financial advice.",
      "Never share confidential or internal information."
    ]
  }
}
```

## Input Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec.role` | string | ✅ | The persona/expertise the agent embodies |
| `spec.goal` | string | ✅ | What the agent helps users accomplish |
| `spec.instructions` | string | ✅ | Detailed operational guidance (markdown supported) |
| `spec.tone` | string | ✅ | Communication style |
| `spec.guardrails` | string[] | ✅ | Array of boundaries (at least one) |

## Output Formats

### Success Response

When all validation passes:

```json
{
  "success": true,
  "agent_plan": {
    "plan_prompt": {
      "instructions": "<spec.instructions verbatim>",
      "more_instructions": null
    },
    "plan": {
      "goal_details": {
        "agent_goal": "<role> that helps users <goal>",
        "description": "<spec.instructions verbatim>",
        "guardrails": "- <guardrail1>\n- <guardrail2>",
        "tone": "<spec.tone verbatim>"
      },
      "variables": {
        "user_query": "The user's current question or request",
        "context": "Accumulated conversation context"
      },
      "tools": {},
      "skills": [],
      "task_flow": {
        "starting_task": "$task:welcome",
        "task_to_return_to": "$task:respond",
        "fallback": "$task:respond"
      },
      "tasks": [
        {
          "task_name": "welcome",
          "task_id": "welcome_001",
          "steps": [...]
        },
        {
          "task_name": "respond",
          "task_id": "respond_001",
          "steps": [...]
        }
      ]
    },
    "flowchart": null
  }
}
```

### Error Response

When validation fails:

```json
{
  "success": false,
  "errors": [
    {"field": "role", "message": "spec.role is required. Provide the persona/expertise."},
    {"field": "guardrails", "message": "spec.guardrails must be array with at least one item."}
  ]
}
```

## Transformation Rules

### 1. agent_goal
Combines `role` and `goal` into a grammatically correct sentence:
- Input: `role: "A fitness coach"`, `goal: "Help users create workout plans"`
- Output: `"A fitness coach that helps users help users create workout plans"`

Note: Ensure goal starts lowercase to flow naturally.

### 2. description
Copy `instructions` verbatim, preserving all markdown formatting.

### 3. guardrails
Convert array to newline-separated string with "- " prefix:
- Input: `["Never give financial advice.", "Stay focused."]`
- Output: `"- Never give financial advice.\n- Stay focused."`

### 4. tone
Copy verbatim from input.

### 5. Generated Tasks
Always generates exactly two tasks:

**welcome task:**
- Greets user with specified tone
- Introduces agent based on role
- Explains capabilities based on goal
- Invites user to share their question
- Transitions to respond task

**respond task:**
- Stores user input in $user_query
- Checks scope against guardrails
- Applies instructions to address query
- Delivers response in specified tone
- Loops for follow-up or closes conversation

## Reference Syntax

Agentman uses `$` prefix for all references:

| Type | Syntax | Example |
|------|--------|---------|
| Task | `$task:name` | `$task:welcome`, `$task:respond` |
| Variable | `$variable_name` | `$user_query`, `$context` |
| Tool | `$tool:name` | `$tool:search_catalog` |
| Skill | `$skill:slug` | `$skill:brand-voice` |

## Validation Rules

| Field | Validation |
|-------|------------|
| `spec` | Must be an object |
| `spec.role` | Non-empty string |
| `spec.goal` | Non-empty string |
| `spec.instructions` | Non-empty string |
| `spec.tone` | Non-empty string |
| `spec.guardrails` | Array with length >= 1 |

## Processing Flow

```
Input JSON
    │
    ▼
┌─────────────────┐
│  Parse JSON     │
│  Extract spec   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Validate       │
│  5 fields       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
 VALID     INVALID
    │         │
    ▼         ▼
┌─────────┐ ┌─────────┐
│Generate │ │ Return  │
│AgentPlan│ │ Errors  │
└─────────┘ └─────────┘
```

## Usage Examples

### Example 1: McKinsey Consultant

**Input:**
```json
{
  "spec": {
    "role": "A senior McKinsey consultant with deep expertise in structured problem-solving",
    "goal": "think through complex problems using structured frameworks like MECE and pyramid principle",
    "instructions": "## Frameworks\n\n### MECE\nBreak down problems into Mutually Exclusive, Collectively Exhaustive categories.\n\n### Pyramid Principle\n1. Start with answer\n2. Support with arguments\n3. Back with data",
    "tone": "Professional and formal.",
    "guardrails": ["Never give financial advice.", "Stay focused on the task."]
  }
}
```

**Output:**
```json
{
  "success": true,
  "agent_plan": {
    "plan": {
      "goal_details": {
        "agent_goal": "A senior McKinsey consultant with deep expertise in structured problem-solving that helps users think through complex problems using structured frameworks like MECE and pyramid principle",
        "guardrails": "- Never give financial advice.\n- Stay focused on the task.",
        ...
      }
    }
  }
}
```

### Example 2: Missing Fields

**Input:**
```json
{
  "spec": {
    "role": "A fitness coach"
  }
}
```

**Output:**
```json
{
  "success": false,
  "errors": [
    {"field": "goal", "message": "spec.goal is required. Describe what the agent helps users accomplish."},
    {"field": "instructions", "message": "spec.instructions is required. Provide detailed operational guidance."},
    {"field": "tone", "message": "spec.tone is required. Specify the communication style."},
    {"field": "guardrails", "message": "spec.guardrails must be array with at least one item."}
  ]
}
```

## Best Practices

### Writing Good Instructions
- Use markdown headers to organize sections
- Include specific frameworks or approaches
- Define output formats and guidelines
- Be explicit about step-by-step processes

### Writing Good Guardrails
- Be specific about what's NOT allowed
- Include compliance boundaries
- Define scope limitations
- Add safety restrictions

### Writing Good Tone
- Describe personality traits
- Specify formality level
- Include emotional qualities
- Match target audience expectations

## Agent JSON

The complete agent definition is available at `agents/agent-builder-flow.json`. This can be imported directly into Agentman.

## Integration

This skill is designed for:
- API endpoints that generate agents programmatically
- Batch agent creation workflows
- CI/CD pipelines for agent deployment
- Agent template/cloning systems
- Self-service agent builders

## Notes

- Output is JSON only—no conversational text
- Markdown in instructions is preserved exactly
- Generated agents always have 2 tasks (welcome + respond)
- No external tools are added (tools: {})
- No skills are bound (skills: [])
- Flowchart is always null
