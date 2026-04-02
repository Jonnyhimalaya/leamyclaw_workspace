# Infrastructure & Technical Notes

## Mission Control Dashboard
- Location: `/home/jonny/mission-control/` (Next.js app)
- Running on **http://localhost:3333** (production via PM2, auto-starts on reboot)
- Gateway token in `.env.local`
- 15+ pages including consultancy section
- Branded Leamy Maths teal (#4A8C8C), dark theme
- **THIS EXISTS. DO NOT REBUILD IT. ENHANCE IT.**

## QMD Memory Backend (Installed Mar 27, 2026)
- Replaced default SQLite + OpenAI embeddings
- Config: hybrid search mode, temporal decay enabled, maxResults: 8, reindex every 10min
- Installed via Bun (v1.3.11) + @tobilu/qmd (v2.0.1)
- Vault architecture: MEMORY.md = slim pointers, detail in vault/ files

## Server Health
- Health script: `scripts/server-health.sh`
- Cron job: every 4 hours, Telegram alerts only if issues found
- HEARTBEAT.md monitors session sizes (>100 warn, >200 critical)
- Long sessions cause Anthropic 529 overloaded errors — /new to reset
- **Auth failover (v2026.4.1):** Profile rotation configured: `auth.order.anthropic: [claw, work]`, `rateLimitedProfileRotations: 2`, `overloadedProfileRotations: 2`. Full chain: claw → work → openrouter/opus → sonnet → gemini → gpt-5.4 → gpt-4o

## Artifacts System (Mar 27, 2026)
- Agents produce screenshots, reports, task plans
- Central protocol: `artifacts/PROTOCOL.md`
- Saved to `artifacts/YYYY-MM-DD/{agent}-{task-slug}.md` + PNGs
- Key rule: artifacts go to disk, never loaded into context

## Research Workflow
- Grok (via X/Twitter) = go-to for OpenClaw ecosystem queries
- Scout agent with xAI API key automates this (when credits available)
- Brave Search for web research
