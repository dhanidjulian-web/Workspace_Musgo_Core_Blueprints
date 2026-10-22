---
name: forge-toolbox
version: 1.0.0
description: Free agent toolkit — quick-reference guide to all Forge Executive monitoring tools. Get price alerts, cost tracking, repo scans, uptime checks, and more.
author: forge-mastermind
tags:
  - monitoring
  - automation
  - developer-tools
  - free
  - productivity
compatible:
  - openclaw
  - claude-code
  - codex-cli
  - cursor
  - gemini-cli
pricing: 0
license: MIT
_agensi: "3c26e34b-9482-487f-a1e1-4851b9479be9"
---

# Forge Agent Toolbox

A free collection of agent-ready monitoring tools. Each tool is a standalone CLI that installs in seconds and sends Telegram alerts.

## Tools

### 🔍 ScrapeWatch ($19)
Monitor any web page for price drops, stock changes, and content updates. Smart change detection via MD5 checksums.
→ https://agensi.io/skills/scrapewatch-auto-detect-price-drops-page-changes

### 💰 TokenTracker ($9)
Track AI token spend across providers. Set budgets. Get Telegram alerts on cost spikes.
→ https://agensi.io/skills/tokentracker-ai-agent-cost-usage-monitor

### 📡 GitHub Sentinel ($14)
Daily GitHub trending scan across 20 topics. Curated Telegram digest of the best new repos.
→ https://agensi.io/skills/github-sentinel-daily-trending-monitor-telegram-digest

### 🔔 Webhook Dispatcher ($12)
Receive POST webhooks and forward them as Telegram alerts. Dedup, batching, health checks.
→ https://agensi.io/skills/webhook-dispatcher-forward-webhooks-as-telegram-alerts

### 📊 Uptime Monitor ($8)
HTTP health checker. Telegram alerts when endpoints go down or recover. Latency tracking.
→ https://agensi.io/skills/uptime-monitor-http-health-checker-telegram-alerts

### 🔐 Cert Watch ($6)
SSL certificate expiry monitor. Get alerts before certs expire. Critical at <7 days.
→ https://agensi.io/skills/cert-watch-ssl-certificate-expiry-monitor-telegram-alerts

### 📋 LogWatch ($7)
Tail log files and get Telegram alerts when errors or warnings appear. Custom regex patterns.
→ https://agensi.io/skills/logwatch-log-file-monitor-telegram-alerts

## Quick Install (any tool)
```bash
# Download from Agensi, then:
unzip tool-name.zip && npm install --production && node src/index.js --auto-configure
```

All tools require Node.js v18+ and a Telegram account. MIT licensed.
