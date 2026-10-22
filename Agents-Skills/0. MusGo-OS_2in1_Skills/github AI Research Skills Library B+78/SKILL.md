```yaml
---
name: conducting-ai-research
description: Conducts systematic AI research using structured methodologies for literature review, experimentation, and analysis. Use when researching AI topics, analyzing papers, or designing experiments.
---

# AI Research Methodology

## Quick Start

```python
# Research pipeline template
research_pipeline = {
    "topic": "transformer attention mechanisms",
    "search_terms": ["transformer", "attention", "self-attention", "multi-head"],
    "databases": ["arxiv", "google_scholar", "semantic_scholar"],
    "timeframe": "2020-2024",
    "inclusion_criteria": ["peer_reviewed", "english", "empirical_results"]
}

# Execute systematic search
papers = search_literature(research_pipeline)
analysis = analyze_papers(papers)
synthesis = synthesize_findings(analysis)
```

## Workflow

### Phase 1: Research Planning
Progress:
- [ ] Define research question using PICO framework
- [ ] Establish inclusion/exclusion criteria
- [ ] Design search strategy with key terms
- [ ] Select relevant databases and sources

### Phase 2: Literature Search
Progress:
- [ ] Execute systematic search across databases
- [ ] Screen titles and abstracts
- [ ] Apply inclusion criteria
- [ ] Extract full-text papers

### Phase 3: Analysis & Synthesis
Progress:
- [ ] Extract key data points and findings
- [ ] Identify methodological patterns
- [ ] Map relationships between studies
- [ ] Synthesize insights and gaps

### Phase 4: Documentation
Progress:
- [ ] Create structured research notes
- [ ] Generate citation database
- [ ] Write synthesis report
- [ ] Document methodology for replication

## Examples

**Example 1: Literature Review**
Input: "Research transformer efficiency improvements"
Output:
```
Search Strategy:
- Primary terms: "transformer efficiency", "model optimization"
- Secondary terms: "parameter reduction", "inference speed"
- Databases: arXiv (2020-2024), ACL Anthology
- Filters: empirical studies, benchmarked results

Key Findings:
1. Pruning techniques: 20-40% parameter reduction
2. Knowledge distillation: 3-5x speed improvement
3. Quantization: Minimal accuracy loss (<2%)
```

**Example 2: Experimental Design**
Input: "Compare attention mechanisms"
Output:
```
Experiment Design:
- Models: Standard attention vs. linear attention vs. sparse attention
- Datasets: GLUE benchmark, WMT translation
- Metrics: Accuracy, inference time, memory usage
- Controls: Same architecture, training procedure
- Sample size: 5 runs per configuration
```

## Best Practices

**Search Strategy:**
- Use Boolean operators (AND, OR, NOT) effectively
- Include synonyms and related terms
- Set appropriate date ranges for relevance
- Cross-reference multiple databases

**Paper Analysis:**
- Extract methodology details systematically
- Note dataset sizes and evaluation metrics
- Track computational requirements
- Identify reproducibility information

**Documentation:**
- Maintain detailed search logs
- Use consistent citation format
- Create visual summaries (charts, diagrams)
- Version control research notes

**Quality Assessment:**
- Evaluate experimental rigor
- Check for potential biases
- Assess statistical significance
- Consider practical applicability

## Common Pitfalls

- **Confirmation bias:** Don't cherry-pick supporting evidence
- **Scope creep:** Keep research questions focused and answerable
- **Insufficient depth:** Read full papers, not just abstracts
- **Missing grey literature:** Include preprints and technical reports
- **Poor documentation:** Always record search parameters and dates
- **Isolation:** Collaborate and seek peer review of methodology
- **Static approach:** Update searches as new papers emerge
- **Methodology blindness:** Question and validate experimental designs

**Red Flags:**
- Studies without proper baselines
- Missing statistical analysis
- Unclear dataset descriptions
- Non-reproducible results
- Conflicting findings without explanation
```