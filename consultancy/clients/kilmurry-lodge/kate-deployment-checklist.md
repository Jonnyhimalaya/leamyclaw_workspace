# Kate Marketing Agent — Deployment Checklist
**Client:** Kilmurry Lodge Hotel (Kate Taylor instance)
**Start date:** 2026-04-04
**Primary contact:** Kate Taylor (via Jonny/Jack)
**Server:** 172.239.98.61 (shared with Jack's instance)

## PHASE 1 — Server Setup
- [x] OS user created: `kateuser` (password: KilmurryKate2026!)
- [x] SSH access via clawuser sudo
- [x] OpenClaw 2026.4.2 installed
- [x] Gateway on port 18792 (systemd: openclaw-kate.service)
- [x] Boot persistence enabled
- [x] Auth: Anthropic token (shared key with Jack) — fixed v1 format
- [x] Model: Sonnet 4-6 primary, Gemini fallback
- [x] Auth cooldowns configured (rotation: 3)
- [x] Exec approvals: full/off
- [x] Exec tested (health script runs)
- [x] TUI tested — working ✅ (Jonny verified 18:11 UTC)
- [x] Telegram bot — Kate created via BotFather (token: 8601857637:AAF...)
- [x] Kate's Telegram user ID: 8778805348 (@katetaylor123)

## PHASE 2 — Identity & Memory
- [x] SOUL.md — marketing persona, brand voice, T.A.P.E.R. values (<1KB)
- [x] USER.md — Kate Taylor profile + authorised admins (Jack, Jonny)
- [x] IDENTITY.md — KilmurryBot Marketing
- [x] AGENTS.md — ops rules, NDD logging, channel trust (<1KB)
- [x] vault/ structure: business/, people/, marketing/
- [x] vault/business/overview.md — full hotel context (2.2KB)
- [x] vault/people/team.md — all key staff with context (1.2KB)
- [x] vault/business/competitors.md — comp set analysis (1.5KB)
- [x] vault/marketing/control-panel-spec.md — dashboard docs (2.5KB)
- [x] vault/marketing/geo-seo-findings.md — SEO audit results (1.5KB)
- [x] MEMORY.md — pointer index (<1.5KB)
- [x] heartbeat-state.json created
- [x] .dream-state.json created
- [x] QMD installed (bun + @tobilu/qmd)
- [x] QMD configured (BM25 search, vault extraPaths)
- [x] Gateway restarted with QMD

## PHASE 3 — Monitoring
- [x] Health script: scripts/server-health.sh (port 18792)
- [x] Health cron: every 4h (kateuser crontab)
- [x] Watchdog cron: every 5min (root crontab, systemctl restart)
- [x] openclaw-ops skill installed
- [x] Doctor run: clean, no issues

## PHASE 3.5 — Operational Intelligence
- [x] Autonomy levels in heartbeat-state.json
- [x] NDD format in AGENTS.md
- [x] Advisor cron: every 6h (Gemini, isolated)
- [x] Dream cycle cron: 2am Dublin (Sonnet, isolated)
- [x] Append-only audit logs — not needed for marketing agent (documented decision)

## PHASE 4 — Core Capabilities
- [x] Browser automation: available via shared Chromium install
- [ ] SearXNG: not installed on Kilmurry server (using Brave — low priority)
- [x] Core crons: health (4h), dream (2am), advisor (6h), events (weekly)
- [x] Mission Control: 10-page marketing dashboard on port 3334
  - [x] Dashboard home
  - [x] Competitors — LIVE data (14 dates, 4 hotels, raise opportunities)
  - [x] Reviews — LIVE data (4.3/5, sentiment + theme analysis, 20 reviews)
  - [x] Events — LIVE data (34 events, 6 sources, demand scoring)
  - [x] SEO & AEO — LIVE data (55/100 GEO score, priority fixes)
  - [x] Content Calendar (placeholder)
  - [x] Campaigns (placeholder)
  - [x] Analytics (placeholder — GA4 script ready, needs property access)
  - [x] Email & CRM (placeholder)
  - [x] AI Log (sample entries)
- [x] PM2 managed: kilmurry-kate-mc (boot persistent)

## Infrastructure & Security
- [x] Shared data directory: /opt/kilmurry-shared/
- [x] kateuser in clawuser group (shared dir read only)
- [x] Isolation verified: kateuser CANNOT read Jack's workspace, auth, config, sessions, vault, credentials
- [x] kateuser has NO sudo access
- [x] Git init + GitHub remote (Jonnyhimalaya/kilmurry-kate)
- [x] Config backup in workspace (config-backup/)
- [x] GA4 service account copied to Kate's credentials dir

## Data Pipelines
- [x] events-scrape.py — 34 events from 6 sources (weekly cron Monday 6am)
- [x] ga4-fetch.py — ready, blocked on GA4 property access
- [x] reviews-scrape.py — written, needs browser for JS sites
- [x] Rate data flowing from Jack via /opt/kilmurry-shared/

## Deferred to Wednesday (Kate Meeting)
- [x] Telegram bot (BotFather) — DONE 2026-04-07
- [x] Kate's Telegram user ID whitelisted — DONE 2026-04-07
- [ ] GA4 property access (Kate adds service account as viewer)
- [ ] Google Ads account details
- [ ] Email platform decision
- [ ] Brand voice / campaign pillars document from Kate
- [ ] HEARTBEAT.md for Kate's agent

## Score: 93% (Phases 1-4 complete. Deferred items all require Kate/Wednesday.)
