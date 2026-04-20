# Kilmurry Lodge Hotel — OpenClaw Architecture Schematic
**Audit Date:** 2026-03-30
**Last Updated:** 2026-04-20 (post-audit + Codex reroute)
**Audited by:** Orchestrator (from Leamy Maths server → SSH)

## 2026-04-20 Update Summary
- **OpenClaw upgraded:** v2026.4.12 → **v2026.4.15** (gateway trust-escalation fix applied, Opus 4.7 default, Gemini TTS available)
- **Primary model changed:** Anthropic Claude Opus 4.6 → **`openai-codex/gpt-5.4`** (free via Codex OAuth) to fix cron failures post-Anthropic subscription cutoff (Apr 4) and $200 credit expiry (Apr 17)
- **Fallbacks updated:** `anthropic/claude-opus-4-7` → `anthropic/claude-sonnet-4-6` → `anthropic/claude-opus-4-6`
- **Interactive Kilmurry bot unchanged** — still uses Claude Max via ACP → Claude Code harness (subscription covers this path)
- **Custom Dream Cycle cron removed** — superseded by native `memory-core` plugin dreaming
- **4 crons repointed** to new model: Advisor Check, session-health-check, kilmurry-morning-brief, weekly-rate-intelligence. Advisor Check test run on GPT-5.4 returned `ok`.
- **AGENTS.md:** Micro-Learning Loop section appended (same as our main workspace pattern). Previous `.learnings/` placeholders will now populate.
- **Memory hygiene:** 10 daily memory files from Apr 7-14 archived to `memory/archive/`.
- **Mission Control massively expanded** since March audit — see Section 7 below for current state.
- **Config backup kept:** `~/.openclaw/openclaw.json.pre-codex-primary-backup` before the change.

## Outstanding / Not Touched (risk-managed)
- Jack's AGENTS.md is ~3,577 tokens with some duplicate sections (Search-First protocol superseded by Active Memory). **Deliberately NOT trimmed** — same type of cut that caused our previous regression. Review later with explicit approval.
- Large legacy workspace HTML files (prototype dashboards from Mar 17-28) still in root. Cosmetic clutter only, not in context.
- OPENCLAW_GATEWAY_TOKEN rotation pending (on Stephen's action list since Apr 13).

---

---

## 1. Infrastructure

| Component | Detail |
|-----------|--------|
| **Server** | Linode VPS, Ubuntu 24.04.4 LTS (kernel 6.8.0-71-generic, x86_64) |
| **IP** | 172.239.98.61 (public) |
| **RAM** | 4GB total (48% used at audit, 871MB free, 272MB swap used) |
| **Disk** | 40GB, 60% used (23GB), 16GB free |
| **Users** | `root` + `clawuser` (dedicated non-root user — good practice) |
| **Process manager** | systemd (openclaw-gateway.service) + PM2 (mission-control) |
| **Health monitoring** | Custom health script via cron (every 4h), alerts to Jack's Telegram |
| **OpenClaw version** | 2026.3.28 (behind our 2026.3.28 — same!) |
| **Node.js** | Present (exact version not captured, likely v22.x) |
| **Pending** | 11 apt updates, system restart required |

### ⚠️ Remaining Infrastructure Concerns
- **4GB RAM is tight** — Chrome alone uses significant RAM (multiple renderer processes visible). Same issue we had before upgrading Leamy to 8GB. Recommend upgrade path.
- **Swap usage** — confirms memory pressure (will improve once RAM upgraded)

### ✅ Resolved (2026-03-30)
- ✅ **systemd service installed** — OpenClaw now runs via `openclaw-gateway.service` with auto-restart and boot persistence. Replaces fragile tmux approach.
- ✅ **PM2 crash fixed** — Mission Control was at 734 restarts due to corrupted `.next` build. Rebuilt `.next`, reset restart count to 0. Now stable.
- ✅ **PM2 boot persistence added** — `pm2 startup` + `pm2 save` configured. Mission Control survives reboots.
- ✅ **Chrome orphans killed** — 10+ stale Chrome processes from Mar 24 terminated. Auto-cleanup now handled by health script.
- ✅ **Health monitoring deployed** — Custom health script runs every 4h via cron. Monitors RAM, swap, Chrome, disk, PM2, gateway, and orphan processes. Alerts Jack's Telegram on issues only.

---

## 2. OpenClaw Configuration

### Gateway
- Port: 18789 (loopback only)
- Auth: token-based (⚠️ OPENCLAW_GATEWAY_TOKEN rotation pending since Apr 13)
- Mode: local (no Tailscale)
- No remote access configured (no public URL, no Tailscale)
- Runs from `~/.npm-global/bin/openclaw gateway` — **not systemd** (despite earlier plan, service is currently disabled)

### Model (as of 2026-04-20)
- **Primary:** `openai-codex/gpt-5.4` (OAuth, free via Jack's Codex subscription)
- **Fallbacks:** `anthropic/claude-opus-4-7` → `anthropic/claude-sonnet-4-6` → `anthropic/claude-opus-4-6`
- **Compaction:** safeguard mode
- **Interactive bot:** routes via ACP → Claude Code harness, uses Claude Max subscription (unaffected by Apr 4 cutoff)

### Channels
| Channel | Status | Notes |
|---------|--------|-------|
| **Telegram** | ✅ Enabled | DM pairing policy, group allowlist, partial streaming |
| **Discord** | ✅ Enabled | Token via env var, group allowlist, partial streaming |

### Auth
- Anthropic: token-based
- OpenAI Codex: OAuth

### Browser
- Playwright Chromium (headless, no-sandbox)
- Persistent Chrome instance from Mar 24 (6 days old — memory leak risk)

### Tools
- Profile: full
- Web search: Brave (API key configured)

---

## 3. Agent Architecture

### Single Agent (Main Only)
Unlike our multi-agent setup (5 agents: main, sitemgr, marketing, scout, content), Kilmurry is running a **single main agent**. No sub-agents directory beyond the skeleton.

This is appropriate for the current stage — Jack is the primary user, and the bot focuses on intelligence gathering, not operational orchestration across departments.

---

## 4. Workspace — What's Been Built

### Core Identity Files ✅
- `SOUL.md` — Well-written. "KilmurryBot", hospitality-first, pilot→prove→rollout, GDPR-conscious, anti-echo-chamber mandate
- `USER.md` — Jack Hoare, third-gen owner, 108 rooms + 9 apts
- `IDENTITY.md` — KilmurryBot 🏨
- `AGENTS.md` — Standard template with memory protocols
- `HEARTBEAT.md` — Exists (minimal)
- `MEMORY.md` — **Extremely comprehensive** (~16KB). Covers:
  - Full property details (118 units, venues, history)
  - Complete leadership team (10+ named staff with roles)
  - Revenue streams, venues, events
  - Vision 2030, T.A.P.E.R. values, brand DNA
  - Technology stack (7 Access Group products, RezLynx PMS, Right Revenue, Alkimii)
  - AI strategy, Claude Teams relationship
  - Kate Taylor onboarding, Amy Russell timeline
  - Operating model (9 departments)
  - Revenue projections, Ryder Cup 2027
  - Competitor intelligence (booking engines, rate scraping methodology)
  - Working relationship rules ("challenge him, no echo chamber")

### Skills (2)
| Skill | Purpose |
|-------|---------|
| `kilmurry-intel` | **Unified 5-agent intelligence system** — Rate Scout, Event Scanner, Reviews, Social/Reddit, Competitor Deep-Dive, Local Pulse. 32 Brave searches + 8 RezLynx curls per run. Produces Telegram summary + HTML dashboard. |
| `reputation-intel` | Superseded by kilmurry-intel, kept for reference |

### Cron Jobs (3)
| Job | Schedule | What |
|-----|----------|------|
| `daily-morning-briefing` | 7am Dublin daily | Weather + tomorrow rates (4 hotels) + events. Saves to reports/, no Telegram delivery. |
| `weekly-rate-intelligence` | Mon 8am Dublin | Browser-based 14-day rate scraping across 4 competitors. Saves MD + JSON. |
| `session-health-check` | 10pm Dublin daily | Checks context usage, alerts Jack if >75%. NEW (just created). |
| `server-health-monitor` | Every 4 hours (`0 */4 * * *`) | System health (RAM, swap, Chrome, disk, PM2, gateway, orphans). Alerts Jack Telegram on issues only. |

### Reports & Deliverables
- **Daily briefings** — 5 reports (Mar 25-30)
- **Weekly rate intel** — 2 reports (Mar 24, Mar 30) with JSON data
- **Mission Control build guide** — documented for reproducibility

### HTML Dashboards/Visualisations (20+!)
Major outputs — all static HTML files in workspace:
- Revenue AI Agent Blueprint (79KB)
- Rate comparison dashboards (v1 + v2) with event overlays
- Demand heatmap 2026
- Agent ecosystem: evolution map, in-action walkthrough, directory (169KB)
- Marketing system: org chart, campaign orchestration, day-to-day, job spec
- Kate Taylor: onboarding vision (112KB), 90-day plan (111KB)
- Creative engine: soul-to-scale, complete edition
- Campaign assessments, product epic briefs
- Executive summary March 2026
- Guest experience reinvestment plan
- Christmas party campaign 2026, corporate BBQ landscape, UL/Limerick events
- AI marketing under-the-hood, daily briefing under-the-hood, orchestration live demo

### Data Files
- Rate comparison data (JSON)
- Intel data directory (rates, events, reviews, social, competitor JSONs)
- Rate data directory (historical)
- TripAdvisor audit, Reddit social audit, reputation data
- Travelodge rates, weekend events/rates/social posts
- Tasks.json (task management)
- Hot dates calendar 2026

### Memory Files (10)
Daily logs: Mar 17, 18, 20, 23, 26, 30
Special: Kate day 1 session, overnight tasks Mar 24, Tarmo Tulit notes, weekly recap Mar 29

---

## 5. Mission Control Dashboard

- **Location:** `~/mission-control/` (Next.js app)
- **URL:** `http://172.239.98.61:3333`
- **Managed by:** PM2 (stable after `.next` rebuild)
- **Pages:** 10 (Dashboard, Tasks, Agents & Team, Tools, Calendar, Memory, Intelligence, Kate's Week, Stephen's Queue, Connections)
- **State:** All data hardcoded/static — no live API connections yet
- **Status:** Stable after `.next` rebuild on 2026-03-30. Restart count reset to 0.

---

## 6. Security Observations

| Area | Status | Notes |
|------|--------|-------|
| Config permissions | `-rw-------` (600) | ✅ Good — matches our fix |
| Credentials dir | `drwx------` | ✅ Properly locked |
| Gateway auth | Token-based, loopback | ✅ Not exposed to internet |
| Bot tokens | In config file (Telegram) + env var (Discord) | Mixed approach |
| Brave API key | In plugins config | Standard |
| SSH | Root login with password | ⚠️ Should be key-only |
| System updates | 11 pending, restart required | ⚠️ Needs attention |

---

## 7. Comparison: Kilmurry vs Leamy Maths Setup

| Aspect | Kilmurry | Leamy Maths |
|--------|----------|-------------|
| **RAM** | 4GB (tight) | 8GB (upgraded from 4GB) |
| **Agents** | 1 (main only) | 5 (main, sitemgr, marketing, scout, content) |
| **Process management** | systemd (robust) | systemd (robust) |
| **Health monitoring** | Custom health script + cron (every 4h) | Custom health script + cron alerts |
| **Chrome cleanup** | Auto-kill in health script | Auto-kill in health script |
| **Memory backend** | Default (SQLite + embeddings?) | QMD (local BM25) |
| **Cron jobs** | 3 | 5+ |
| **Skills** | 2 | 2+ custom |
| **Channels** | Telegram + Discord | Telegram + Discord |
| **Model** | Opus 4.6 | Opus 4.6 |
| **OpenClaw version** | 2026.3.28 | 2026.3.28 |
| **Content volume** | Massive (20+ HTML dashboards) | Moderate |
| **Mission Control** | Next.js (stable via PM2) | Next.js (stable via PM2) |

---

## 8. Recommendations for Client Playbook

### Immediate (This Week)
1. **RAM upgrade** — 4GB → 8GB minimum. Chrome + Opus sessions will choke this.
2. ~~**systemd service** — Replace tmux with proper systemd unit (auto-restart, boot persistence)~~ ✅ DONE (2026-03-30)
3. ~~**Server health script** — Port our `scripts/server-health.sh` approach (Chrome cleanup, RAM monitoring)~~ ✅ DONE (2026-03-30)
4. **System updates** — Apply 11 pending updates + reboot
5. **SSH hardening** — Disable root password login, key-only

### Short Term
6. ~~**PM2 mission-control crash** — Investigate 734 restarts. Likely needs `next build` + `next start` (production mode)~~ ✅ DONE (2026-03-30) — `.next` rebuilt, restart count reset to 0
7. ~~**Chrome orphan cleanup** — 6-day-old Chrome processes eating RAM~~ ✅ DONE (2026-03-30) — killed + auto-cleanup in health script
8. **Backup strategy** — Only one backup visible (workspace-backup-2026-03-23.tar.gz)

### Medium Term
9. **Multi-agent architecture** — When ready, add specialist agents (Revenue, F&B, Marketing) matching the 9-department operating model
10. **QMD memory backend** — Switch from default to local BM25 (no embedding costs, no external dependency)
11. **Cron delivery** — Morning briefing currently saves to file only, no Telegram delivery. Jack probably wants it pushed.

---

## 9. What's Impressive

Genuinely good work here:
- **MEMORY.md is exceptional** — 16KB of deeply structured hotel knowledge, staff profiles, competitive intelligence, working relationship rules
- **SOUL.md anti-echo-chamber mandate** — Smart. Most bot setups miss this entirely.
- **kilmurry-intel skill** — Sophisticated 5-agent intelligence pipeline with search budget awareness
- **Rate scraping methodology** — RezLynx cookie + EUR currency fix is clever
- **Volume of HTML deliverables** — 20+ dashboards/visualisations delivered in 2 weeks
- **Operating model alignment** — "Amy's operating model IS the agent architecture" shows strategic thinking
- **"Golden Rule" for AI feedback** — "Always explain WHY when rejecting AI output" is gold

---

*This schematic serves as our reference for the Kilmurry Lodge client file and as a template for future consultancy client onboarding audits.*

---

## 7. Mission Control — Current State (updated 2026-04-20)

March audit captured MC as a basic 3-dashboard prototype. Significant build-out since then.

### Stack
- **Framework:** Next.js 14.2.35 (App Router), React 18, TypeScript, Tailwind v4
- **Port:** 3333
- **Runtime:** PM2 (`pm2 restart mission-control`)
- **Repo:** `github.com/Jonnyhimalaya/kilmurry-mission-control`
- **Branching:** `dev` active, `main` stable (locked 13 Apr)

### Route structure (src/app/)
| Route | Purpose |
|---|---|
| `/` | Main dashboard |
| `/agents` | Agent directory |
| `/calendar` | Calendar view |
| `/intel` | Intelligence hub |
| `/marketing` | Marketing department module |
| `/revenue` | Revenue department module |
| `/memory` | Memory browser |
| `/reports` | Reports viewer |
| `/tools` | Tools index |
| `/stephen` | Stephen-specific view |
| `/kate` | Kate-specific view |
| `/tasks` | Task list |
| `/connections` | Integration connections |

### API layer
- Gateway wrapper at `lib/gateway.ts`
- `useApi` hook at `lib/useApi.ts`
- intel endpoints, reports/download endpoints

### Notable features built since March
- **6 department modules:** Marketing, Revenue, Sales, Facilities, Guest Relations, F&B
- **Intelligence hub:** Hot Dates Intelligence (185 events, weighted index v2), World Scenarios (Iran 4-week dashboard), Forecasting Intelligence (Alkimii Bridge)
- **Marketing depth:** Campaign Detail with self-contained tabs, Agent Architecture diagrams, sequence drill-downs, 10 agent configurations, Kate's Actions strip, approval buttons
- **Morning Brief page** — renders cron output as reviewable dashboard
- **Prediction Challenge dashboard** — 14 predictions locked 11-19 April, scoring integrity maintained even when predictions revised internally
- **Hot Dates Review Queue** — human-in-the-loop event filtering with training notes (Faye feeds back)
- **Sales Kanban** — real pipeline integration

### Workflow rules (locked in)
- `dev` gets every commit; `main` only stable merges
- `.next/`, `node_modules/`, `.env*`, `credentials` never committed
- All features labelled explicitly: **Prototype** / **Candidate** / **Production**
- `git status` clean before + after every change
- Standard fix for MC breakage: `rm -rf .next && npm run build && pm2 restart mission-control`

---

## 8. Features Worth Porting to Other Clients

Jack's MC has matured faster than ours in several areas. Port candidates:

| Feature | Why |
|---|---|
| **Hot Dates Intelligence** | Event-weighted scoring with learning feedback loop. Direct analogue for any calendar-sensitive business (Leamy Maths exams, retail seasonal peaks, B2B trade shows). |
| **Prediction Challenge dashboard** | Quantifies forecast accuracy. Locked scoring + revised internal predictions. Great consultancy deliverable. |
| **Department module architecture** | Clean URL + route structure per team function. Replicable pattern. |
| **Morning Brief page** | Turns cron agent output into reviewable dashboard. Replaces passive Telegram message with active dashboard review. |
| **dev/main branching + explicit labels** | More mature than our current MC workflow. Adopt. |
| **Gateway wrapper + useApi hook** | Clean API abstraction pattern. |

---

## 9. Catalogue Ownership & Update Rules

This file is the **single source of truth** for Jack's OpenClaw + MC architecture.
- `consultancy/clients/kilmurry-lodge/` is where all client-specific detail lives
- `consultancy/catalogue/` is where cross-client patterns and optimisations aggregate
- Do not duplicate this content into `vault/` — vault is for internal ops, not client catalogues
- Update this file on any material change to Jack's stack
