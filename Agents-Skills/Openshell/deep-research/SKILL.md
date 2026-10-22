deep-research

Multi-step web research with source tracking and structured synthesis.

# Skill: deep-research

Conduct thorough, multi-source research on a topic and deliver a structured report.

## Process

### Phase 1 — Scope
1. Restate the research question in your own words.
2. Identify 3–5 sub-questions that together answer the main question.
3. List the types of sources most likely to have authoritative answers.

### Phase 2 — Search
- Use `websearch` or `webfetch` for each sub-question.
- Prefer primary sources: official docs, papers, release notes, RFCs.
- Collect at least 3 independent sources per key claim.
- Note the URL and date for every source.

### Phase 3 — Synthesis
- Cross-reference conflicting information.
- Prioritize recency for fast-moving topics.
- Distinguish facts from opinions/estimates.

### Phase 4 — Report
Structure the output as:

```markdown
## Summary
One paragraph answer to the main question.

## Key Findings
- Finding 1 [source]
- Finding 2 [source]
- ...

## Details
### Sub-question 1
...

### Sub-question 2
...

## Sources
1. [Title](URL) — accessed YYYY-MM-DD
2. ...

## Confidence
High / Medium / Low — brief justification.
```

## Rules

- Never fabricate URLs or citations.
- If a source is paywalled or unavailable, say so explicitly.
- Flag outdated information (> 1 year for fast-moving topics).
- Keep the Summary section under 150 words.
