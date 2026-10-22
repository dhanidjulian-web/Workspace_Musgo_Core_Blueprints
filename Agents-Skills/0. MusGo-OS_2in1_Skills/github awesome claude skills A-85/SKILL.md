---
name: building-claude-skills
description: Creates and manages Claude MCP skills following best practices from the awesome-claude-skills repository. Use when developing MCP tools, creating skill repositories, or contributing to Claude ecosystems.
---

# Building Claude Skills

## Quick Start

```bash
# Clone skill repository template
git clone https://github.com/your-username/claude-skills
cd claude-skills

# Create new skill file
touch skills/analyzing-data.md

# Add YAML frontmatter and content
echo '---
name: analyzing-data
description: Analyzes datasets and generates insights with visualizations. Use when exploring data patterns or creating reports.
---' > skills/analyzing-data.md
```

## Workflow

**Progress:**
- [ ] **Research existing skills** - Check awesome-claude-skills for similar tools
- [ ] **Define skill scope** - Single responsibility, clear trigger phrases
- [ ] **Create YAML frontmatter** - Gerund name, third-person description
- [ ] **Write quick start** - Immediate actionable example
- [ ] **Document workflow** - Step-by-step process with checkboxes
- [ ] **Add concrete examples** - Input/output pairs
- [ ] **List best practices** - Guidelines and tips
- [ ] **Note common pitfalls** - What to avoid
- [ ] **Test skill** - Verify with Claude MCP server
- [ ] **Submit to repository** - Create PR with proper documentation

## Examples

**Example 1: Data Analysis Skill**
```yaml
---
name: analyzing-sales-data
description: Processes sales datasets to identify trends, seasonal patterns, and revenue insights. Use when examining business performance or forecasting.
---
```

**Example 2: Code Review Skill**
```yaml
---
name: reviewing-python-code
description: Conducts thorough Python code reviews focusing on performance, security, and maintainability. Use when auditing codebases or mentoring developers.
---
```

**Example 3: Content Creation Skill**
```yaml
---
name: writing-technical-docs
description: Creates comprehensive technical documentation with proper structure and examples. Use when documenting APIs, software architecture, or user guides.
---
```

## Best Practices

**Naming Convention:**
- Use gerund form: `processing-images`, `managing-databases`
- Kebab-case only: lowercase, hyphens, no spaces
- Be specific: `analyzing-financial-data` vs `analyzing-data`

**Description Guidelines:**
- Start with action verb in third person
- Include specific use cases and trigger phrases
- Keep under 1024 characters
- Mention domain/context when relevant

**Content Structure:**
- Lead with executable code or immediate steps
- Use progress checklists for complex workflows
- Provide concrete input/output examples
- Include error handling and edge cases

**Repository Organization:**
```
skills/
├── data-analysis/
│   ├── analyzing-datasets.md
│   └── visualizing-metrics.md
├── development/
│   ├── reviewing-code.md
│   └── debugging-applications.md
└── content/
    ├── writing-documentation.md
    └── creating-presentations.md
```

## Common Pitfalls

**Avoid These Mistakes:**
- **Generic names:** `helper-tool` vs `parsing-json-apis`
- **First/second person:** "I analyze" or "You can" vs "Analyzes"
- **Missing triggers:** Description without use cases
- **Over-explanation:** Defining basic concepts Claude knows
- **Multiple responsibilities:** One skill = one clear purpose
- **Vague examples:** Abstract descriptions vs concrete input/output
- **No error handling:** Ignoring edge cases and failures

**Quality Checklist:**
- [ ] Name follows gerund kebab-case format
- [ ] Description is third-person with clear triggers
- [ ] Quick start provides immediate value
- [ ] Examples show concrete input/output
- [ ] Workflow has actionable steps
- [ ] Best practices are specific and useful
- [ ] Common pitfalls prevent real mistakes

**Integration Tips:**
- Test skills with Claude MCP server before submitting
- Follow repository contribution guidelines
- Include proper README and documentation
- Tag skills appropriately for discoverability
- Consider skill dependencies and prerequisites