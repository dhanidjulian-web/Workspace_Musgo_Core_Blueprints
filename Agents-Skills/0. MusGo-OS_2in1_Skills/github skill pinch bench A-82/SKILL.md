---
name: building-claude-skills
description: Creates structured Claude Code agent skills from professional expertise. Use when converting methodologies, workflows, or domain knowledge into reusable agent capabilities.
---

# Building Claude Skills

Create professional Claude Code agent skills that capture real expertise in a structured, reusable format.

## Quick Start

```yaml
---
name: analyzing-sales-data
description: Analyzes sales performance metrics and identifies trends. Use when reviewing quarterly reports or investigating revenue patterns.
---

# Sales Data Analysis

Extract insights from sales data using statistical analysis and visualization.

## Workflow

1. **Data Import** - Load CSV/Excel files with pandas
2. **Clean & Validate** - Handle missing values, outliers
3. **Calculate KPIs** - Revenue, conversion rates, growth metrics
4. **Trend Analysis** - Time series patterns, seasonality
5. **Visualization** - Charts showing key insights
6. **Report Generation** - Summary with actionable recommendations

## Examples

**Example 1:**
Input: Monthly sales data with columns: date, product, revenue, units
Output: Growth rate analysis, top performers, seasonal trends chart

## Best Practices

- Always validate data quality first
- Focus on actionable insights
- Use clear visualizations

## Common Pitfalls

- Don't ignore data quality issues
- Avoid correlation/causation confusion
```

## Workflow

Progress:
- [ ] Extract core methodology from source material
- [ ] Identify trigger scenarios for skill usage
- [ ] Structure into standardized sections
- [ ] Create concrete examples
- [ ] Add practical guidelines

**Step 1: Analyze Source Material**
- Identify the professional domain and specific expertise
- Extract key processes, tools, and methodologies
- Note common use cases and trigger scenarios

**Step 2: Structure the Skill**
- Write YAML frontmatter with gerund name and trigger-based description
- Lead with Quick Start showing immediate value
- Break methodology into clear workflow steps
- Provide concrete input/output examples

**Step 3: Add Practical Value**
- Include best practices from the expertise
- Highlight common mistakes to avoid
- Focus on actionable guidance over theory

## Examples

**Example 1:**
Input: "I'm a financial analyst who specializes in DCF modeling"
Output: Skill for `building-dcf-models` with valuation workflow, Excel templates, and sensitivity analysis

**Example 2:**
Input: "I help companies implement agile methodologies"
Output: Skill for `implementing-agile-practices` with sprint planning, retrospective formats, and team coaching techniques

**Example 3:**
Input: GitHub repository with data science utilities
Output: Skill for `processing-research-data` with analysis pipeline, visualization templates, and statistical methods

## Best Practices

- **Extract the "how"** - Focus on methodology, not just what someone does
- **Make it actionable** - Each section should enable immediate use
- **Use domain language** - Include terminology and concepts experts use
- **Show real examples** - Concrete inputs and outputs beat abstract descriptions
- **Keep focused** - One skill = one core capability
- **Test trigger phrases** - Description should match when someone would use this

## Common Pitfalls

- Don't create skills for basic tasks everyone knows
- Avoid overly broad skills that try to do everything
- Don't include personal opinions without professional backing
- Skip theoretical background - focus on practical application
- Don't make skills that require extensive setup or rare tools