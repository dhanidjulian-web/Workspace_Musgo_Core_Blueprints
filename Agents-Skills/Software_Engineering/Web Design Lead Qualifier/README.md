# Web Design Lead Qualifier

Research prospects, score them 1–10, and generate qualification reports with email drafts. Standalone tool for freelance web designers — no other skills required.

## What it does

- Crawls the prospect's website (Playwright + requests fallback)
- Discovers and audits key pages (about, services, contact, reviews)
- Scores fit on 5 signals: need, size, budget, accessibility, timing
- Writes a detailed qualification report
- Drafts personalised first-contact emails with talking points

## Setup

1. Install the skill via Agensi
2. On first use, the skill will guide you through Playwright setup (~150MB)
3. Point it at a website: *"qualify this lead: acmeplumbing.ie"*

## Requirements

- **Playwright** (recommended) — `pip3 install playwright==1.59.0 && python3 -m playwright install chromium`
- **requests + beautifulsoup4** (fallback) — `pip3 install requests beautifulsoup4`

## Part of WebClient Studio

This is the standalone lead qualifier. The full **WebClient Studio** bundle adds:

- **Pipeline Tracker** — local database, lead status management, follow-up reminders
- **Proposal Builder** — AI-generated proposals from your qualification research
- **Project Onboarder** — project briefs, onboarding checklists, sitemap drafts

Get the full bundle: [WebClient Studio on Agensi](https://agensi.io)

## License

MIT
