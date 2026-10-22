---
_agensi: "da409d70-40be-49ad-a5f2-685620de3019"
---

```yaml
---
name: prompt-output-reverse-engineer
description: >
  Reverse-engineers an AI-generated output to identify its most probable original input intent,
  then constructs a fully structured, framework-driven prompt from that inferred intent.
  Use this skill when you have an AI output and want to recover or rebuild the prompt that
  produced it, or when you want to turn an informal prompt idea into a production-ready
  instruction set. Serves prompt engineers, AI power users, and anyone packaging reusable
  prompt assets.
  Trigger phrases: "reverse-engineer this output into a prompt",
  "I have an AI output, find the original prompt and write a new one",
  "turn this prompt into a skill", "convert this output into a SKILL.md",
  "package this as a SKILL.md", "make this prompt reusable",
  "build a SKILL.md from this prompt".
---
```

## Purpose

Given a raw AI-generated output (and optionally a subject label), this skill traces back to the original user intent that drove the output, ignores surface-level subject matter to isolate the functional goal, and then produces a complete, Role-Task-Steps-Examples-Format structured prompt reinforced with Chain-of-Thought and Tree-of-Thoughts reasoning patterns. The deliverable is a deployment-ready prompt the user can copy, save, or package.

---

## When to Use

1. You have an AI-generated output but have lost or never had the original prompt that produced it.
2. You want to infer the functional goal behind an output, stripping away its subject to find the reusable pattern.
3. You need to rebuild a prompt from a demo or example output shared by someone else.
4. You are packaging a one-off prompt into a reusable, well-structured instruction asset.
5. You want to audit an existing prompt by comparing its inferred intent against what it actually produces.
6. You are a prompt engineer stress-testing whether an output unambiguously maps back to a single clear input.
7. You received a PromptBase listing or template and want it converted into a structured SKILL.md-compatible format.
8. You want to upgrade an informal or poorly structured prompt into a production-grade instruction set with CoT and ToT embedded.

### SCOPE — This skill does NOT handle:
- Generating creative content (stories, articles, images, code) directly.
- Analysing outputs that are purely numerical or tabular data with no linguistic structure.
- Reverse-engineering prompts from outputs produced by image or audio models.
- Writing prompts that target a specific subject (the subject is always supplied by the user as a variable).
- Evaluating whether a reconstructed prompt is ethically safe or policy-compliant.
- Producing multiple competing prompt variants; it delivers one optimal structured prompt.

---

## Process

1. **Ingest the output**: Accept the raw AI-generated output from the user's message under `[prompt output]`; if a subject label `[subject of the output]` is provided, note it as context only — do not let it anchor the goal identification.

2. **Strip subject matter**: Identify and mentally set aside the surface topic (e.g. "wildlife", "crypto") so the analysis targets functional intent, not content domain.

3. **Decompose the output**: Break the output into its structural components — keywords, rhetorical mode (explanation, instruction, narrative, list), tone, level of detail, and implied audience — to map what kind of task the output was fulfilling.

4. **Identify the initial goal**: Using Chain-of-Thought reasoning, trace each structural component back one reasoning step at a time until you reach the single functional objective the user originally wanted accomplished (e.g. "script generation", "money-making strategy", "persuasive argument construction").

5. **Generate the inferred input statement**: Produce one clear, grammatically precise statement or question representing the most probable original prompt intent — this is the reconstructed input, not a guess about subject.

6. **Apply Tree-of-Thoughts evaluation**: Branch the inferred input into at least two alternative interpretations; evaluate each branch's fit against the output's structure and tone; select the highest-confidence path and discard weaker branches, documenting the selection rationale internally.

7. **Draft the Role block**: Write a detailed persona for the AI that would be optimal to fulfil the inferred goal — include domain expertise, behavioural traits, and quality standards relevant to the task type.

8. **Draft the Task block**: Write a precise task description focused on what the AI does (its functional action), not what it talks about; reference the user-supplied variable slots using brackets e.g. `[topic]`, `[context]`.

9. **Draft the Steps block**: Decompose the task into an ordered, imperative workflow using CoT structure — each step advances reasoning one increment, names a concrete output or decision, and sets up the next step.

10. **Draft the Examples block**: Construct one illustrative input/output pair that demonstrates the expected behaviour without revealing the actual subject the user will supply; use abstract placeholders.

11. **Draft the Format block**: Define the required output structure — length, delimiters (e.g. `###`), tone, markdown use, and any negative constraints (what the output must never do).

12. **Assemble and deliver the full prompt**: Render the complete prompt in a single fenced code block with `###Role###`, `###Task###`, `###Steps###`, `###Examples###`, `###Format###` sections separated by `---`; do not label or reference any prompting methodology by name inside the prompt itself.

13. **Save if requested**: If the user specifies a file path, write the assembled prompt to that path.

---

## Validation

- [ ] The inferred input targets the functional goal, not the surface subject of the output.
- [ ] The Role block contains a detailed persona with domain expertise and behavioural rules.
- [ ] The Task block describes what the AI does, not what it discusses.
- [ ] Every variable the user must supply is represented as a bracketed token (e.g. `[topic]`).
- [ ] The Steps block follows Chain-of-Thought incremental reasoning with no skipped logical jumps.
- [ ] A Tree-of-Thoughts branch evaluation was performed and the winning path is reflected in the prompt structure.
- [ ] No prompting methodology name (CoT, ToT, few-shot, etc.) appears inside the generated prompt text.
- [ ] The Examples block uses abstract placeholders, not the actual subject from the source output.
- [ ] Section separators (`###` or `---`) are present and consistent throughout the generated prompt.
- [ ] The full prompt is delivered inside a single fenced code block.
- [ ] The two variable slots from the source (`[subject of the output]`, `[prompt output]`) are folded into the Process narrative as free-form user inputs, not listed as a Variables section.
```

---

**End-of-Build Report**
- **Kebab-case skill name:** `prompt-output-reverse-engineer`
- **Estimated token count:** ~980 tokens
- **Suggested install path:** `skills/prompt-output-reverse-engineer.md`
- **Unresolved slots:** None — `[subject of the output]` and `[prompt output]` are both folded into Step 1 of the Process as free-form user inputs per skill instructions.
