# Nexus — Client Discovery Notes

## Overview
- **Company:** Nexus (BTC company)
- **Co-founder:** Jonny (Stephen)
- **Agent deployed:** 2026-04-04
- **Bot:** @OnNexus_bot (Telegram)
- **Server:** Same VPS as Leamy Maths, isolated OS user `nexus`

## Architecture
- **OS user:** `nexus` (separate from `jonny`)
- **Gateway:** port 18790 (Jonny's on 18789)
- **Model:** Opus (shared API keys via auth-profiles.json)
- **Fallbacks:** OpenRouter Opus → Sonnet → Gemini → GPT-5.4
- **Systemd:** `openclaw-nexus.service` (enabled, auto-restart)
- **Browser:** Port 18792

## Data Isolation
- Separate home directory: `/home/nexus/`
- Separate workspace: `/home/nexus/.openclaw/workspace/`
- Separate sessions, memory, logs
- Shared only: LLM API keys (Anthropic, OpenAI, Google, OpenRouter, xAI)
- No access to `/home/jonny/` data

## SSH Access
- Via `nexus` user or `sudo su - nexus` from jonny

## Status
- [x] OS user created
- [x] OpenClaw 2026.4.2 installed
- [x] Gateway running (systemd)
- [x] Telegram bot connected (@OnNexus_bot)
- [x] Pairing approved (Jonny's TG ID)
- [x] SOUL.md / AGENTS.md / USER.md bootstrapped
- [x] Auth failover configured
- [x] Exec security: ask: on-miss
- [ ] Knowledge base loaded (Jonny uploading from Claude Project)
- [ ] openclaw-ops skill installed
- [ ] Watchdog cron
- [ ] Security audit
- [ ] SOUL.md refined with Jonny

## Pending
- Jonny uploading dataroom docs from Claude Project
- Security hardening pass (openclaw-ops, watchdog)
- Agent identity/persona refinement
- Mission Control page (if needed)
