---
name: creating-agent-skills
description: Creates Claude Code agent skill files following documented best practices, including proper structure, frontmatter, and content organization. Use when building new skill modules, packaging expertise into reusable Claude skills, or reviewing existing skills for compliance with best practices.
---

## Quick Start

Create a skill file with YAML frontmatter followed by structured markdown:

```yaml
---
name: analyzing-spreadsheets
description: Analyzes spreadsheet data to extract trends, anomalies, and summary statistics. Use when working with CSV/Excel files or when the user asks for data analysis.
---

## Quick Start
[immediate actionable example]

## Workflow
[step-by-step process]

## Examples
[input/output pairs]

## Best Practices
[guidelines]

## Common Pitfalls
[anti-patterns]
```

## Workflow

Progress:
- [ ] Step 1: Identify the domain expertise or task to package
- [ ] Step 2: Write gerund-form kebab-case name (max 64 chars)
- [ ] Step 3: Write third-person description with trigger phrases (max 1024 chars)
- [ ] Step 4: Draft Quick Start with zero preamble — code/steps only
- [ ] Step 5: Write Workflow as numbered/checklist steps
- [ ] Step 6: Add 2+ concrete Examples (real input → real output)
- [ ] Step 7: Add Best Practices (concise, non-obvious tips)
- [ ] Step 8: Add Common Pitfalls (things to avoid)
- [ ] Step 9: Trim to ~500 lines; split into reference files if longer
- [ ] Step 10: Validate frontmatter syntax and description phrasing

## Examples

**Example 1:**
Input: "Someone who reviews pull requests for security vulnerabilities in Node.js apps."
Output:
```yaml
---
name: reviewing-code-security
description: Reviews Node.js pull requests for security vulnerabilities such as injection, auth bypass, and unsafe dependencies. Use when reviewing PRs, auditing code, or the user asks for a security review.
---

## Quick Start
Run through the checklist against the diff: input validation, auth checks, dependency versions, secrets exposure.

## Workflow
Progress:
- [ ] Scan diff for new/changed endpoints
- [ ] Check input sanitization and parameterized queries
- [ ] Verify auth/authorization on new routes
- [ ] Check for hardcoded secrets or tokens
- [ ] Review new dependencies for known CVEs
...
```

**Example 2:**
Input: "asdkjhaksjdh"
Output:
```yaml
---
name: handling-placeholder-tasks
description: Provides a minimal placeholder workflow when input is unclear or insufficient. Use when the request lacks enough detail to define real expertise.
---

## Quick Start
Ask nothing — treat as a stub. Document assumptions and proceed with a generic best-practice checklist.

## Workflow
Progress:
- [ ] Note that input was insufficient
- [ ] Apply generic best practices for the closest inferable domain
- [ ] Flag for human review
```

## Best Practices

- Keep the **name** as a gerund verb phrase describing the action, not the domain noun (`writing-tests`, not `test-writer`).
- Front-load the **description** with the action, then append "Use when..." triggers — this is what Claude scans to decide relevance.
- Avoid teaching Claude things it already knows (e.g., "a CSV is comma-separated values"). Only include domain-specific judgment calls.
- Prefer **concrete numbers, thresholds, and defaults** over vague guidance ("use temperature 0.2" beats "tune the parameters").
- If a skill covers multiple large sub-domains, split into a main skill file plus linked reference docs rather than one giant file.

## Common Pitfalls

- Writing descriptions in first or second person ("I help you...", "You can use this to...").
- Omitting trigger conditions from the description, making it unclear when Claude should invoke the skill.
- Padding Quick Start with introductory prose instead of jumping straight to action.
- Making Examples abstract ("input: some data, output: some result") instead of realistic and specific.
- Letting the skill balloon past ~500 lines instead of modularizing into separate reference files.