# Kilmurry Lodge — Consultancy Work Log

**Consultant:** Stephen (Jonny) Himalaya
**Client:** Kilmurry Lodge Hotel, Limerick
**Contact:** Jack Cahill
**Start date:** March 2026
**OpenClaw server:** 172.239.98.61 (Tailscale: 100.111.174.13)

---

## Monday 30 March 2026

### Full Server Audit & Architecture Review
- SSHed into Kilmurry server (172.239.98.61)
- Complete infrastructure assessment: Ubuntu 24.04, 4GB RAM, 40GB disk
- Documented server state: OpenClaw 2026.3.28, single agent, Telegram + Discord channels
- Identified critical issues: running via tmux (fragile), no health monitoring, no auto-cleanup, Mission Control crash-looping (734 PM2 restarts), Chrome zombie processes consuming 1GB RAM
- Produced full architecture schematic documenting every component

### Process Manager Migration (tmux → systemd) ✅
- Created systemd service file for OpenClaw gateway
- Migrated gateway from tmux (dies on disconnect) to systemd (auto-restart, boot persistence)
- Enabled on boot: gateway now survives reboots and crashes automatically
- Killed old tmux session — no longer needed
- Verified: gateway healthy, all channels connected

### Mission Control Fix ✅
- Diagnosed crash-looping Mission Control dashboard (734 PM2 restarts)
- Root cause: corrupted Next.js build cache → "Failed to find Server Action" errors
- Fix: clean rebuild (`rm -rf .next && npm run build`)
- PM2 counter reset, process saved for boot persistence
- Verified: dashboard serving HTTP 200

### PM2 Boot Persistence ✅
- Created `pm2-clawuser.service` for systemd
- Mission Control (Next.js dashboard) now auto-starts on server boot
- Both OpenClaw gateway + Mission Control survive reboots

### Health Monitoring System — Deployed ✅
- Created custom `server-health.sh` script adapted for Kilmurry's environment
- Monitors: RAM, swap, disk, Chrome zombies (auto-kill), PM2 health, gateway liveness, system load, orphan processes
- Created alert wrapper: sends findings to Jack's Telegram (only when issues detected — no spam)
- Configured system crontab: runs every 4 hours
- Tested live: caught swap usage (270MB), Chrome zombies (1GB — auto-killed), PM2 crash count — all alerts delivered to Jack's Telegram successfully

### Chrome Zombie Cleanup ✅
- Found and killed orphan Chrome processes from March 24 consuming ~1GB RAM
- Health script now auto-kills Chrome zombies on every 4-hour check

### Server Cleanup ✅
- Removed old tmux sessions (no longer needed post-systemd migration)
- Verified: zero orphan processes, gateway running clean on systemd
- Memory usage reduced after Chrome cleanup

### QMD Memory Backend — Deployed ✅
- Installed QMD (semantic memory search) for the agent
- Configured BM25 search mode with vault paths
- Agent can now search its own memory and vault files semantically
- Enables faster, more accurate recall of past conversations and decisions

### Architecture Schematic — Written & Published ✅
- Full architecture schematic document covering all server components
- Published to Mission Control dashboard
- Updated post-remediation to reflect all fixes applied

### Discord Bot Investigation
- Jack reported Discord bot not responding
- Investigated and confirmed bot was actually working (misleading log message)
- Verified via channel status check

---

## Tuesday 31 March 2026

### Morning Briefing Investigation
- Identified why Jack's daily morning briefing stopped arriving on Telegram since March 25th
- Root cause found: delivery mode was set to "none" — briefings were generated and saved to server but never sent to Telegram
- Secondary issue: using expensive model (Opus) with no fallback — prone to API overload errors
- Fixes prepared for next session

---

## Wednesday 1 April 2026

### Security Hardening — Tailscale VPN ✅
- Installed Tailscale VPN on Kilmurry server
- Server assigned private IP: 100.111.174.13
- Jack created Tailscale account, connected his server, iPhone, and laptop
- Consultant access added via device sharing
- Result: server now accessible through private encrypted network
- Verified: Mission Control accessible via Tailscale from all authorised devices

### Security Hardening — Firewall (UFW) ✅
- Enabled UFW firewall (was completely inactive — server was wide open to the internet)
- Rules configured:
  - SSH (port 22): open for remote management
  - Mission Control (port 3333): restricted to Tailscale devices only — public internet blocked
  - All other incoming traffic: denied by default
- Verified: Mission Control loads via Tailscale, blocked from public IP

### Security Hardening — Telegram Bot Lockdown ✅
- Configured `allowFrom` whitelist with Jack's Telegram user ID
- Set DM policy to allowlist mode
- Result: only Jack can message the bot — all other users silently ignored
- Tested and confirmed: unauthorised Telegram accounts cannot interact with bot

### Morning Briefing Fix ✅
- Changed delivery mode from "none" to "announce" with Jack's Telegram chat ID
- Switched model from Opus (expensive, unreliable) to Sonnet (cheaper, faster, more reliable)
- Triggered test run — briefing delivered successfully to Jack's Telegram
- Will run automatically at 7am Dublin time daily going forward

### GitHub Backup System — Deployed ✅
- Jack's entire OpenClaw workspace backed up to private GitHub repository (334 files)
- Config backup folder added: openclaw.json, cron jobs, skill definitions
- Credentials excluded via .gitignore (API keys, bot tokens never stored in git)
- Git backup protocol embedded in agent's instructions — agent will self-backup after meaningful changes
- Full version history and rollback capability now available for Jack's entire system

### Operational Intelligence Patterns — Deployed ✅
- **Autonomy levels** — agent adjusts proactivity based on Jack's activity (responsive/ambient/proactive/dormant). Saves API costs during quiet periods.
- **Structured logging (NDD format)** — all agent actions now logged as Noticed/Decision/Did for a clean audit trail
- **Advisor model** — quality control cron runs every 6 hours, reviews agent's recent work for mistakes or missed tasks
- **Dream cycle** — nightly memory consolidation at 2am: distils daily logs into long-term memory, archives old logs, trims bloat
- **Append-only audit logs** — daily log entries can never be edited or deleted, creating a tamper-proof record
- **HEARTBEAT.md upgraded** — sleep-when-idle protocol prevents token waste overnight
- All changes backed up to GitHub

### Remaining Items (Scheduled)
- [ ] Discord bot lockdown (need Jack's Discord user ID)
- [ ] SSH hardening (key-only authentication, disable password login)
- [ ] Jack's server password change (security hygiene)
- [ ] Fallback model chain configuration (needs Jack's additional API keys)
- [ ] Agent sandboxing (restrict tool access per agent role)

---

---

## Thursday 3 April 2026

### Server Security Remediation ✅
- Jonny provided SSH password — first access since security was flagged on Apr 2
- **Version check:** OpenClaw v2026.3.28 — missing patches for 33 known vulnerabilities
- **Updated to v2026.4.2** — all CVEs patched
- **Root SSH disabled** — PermitRootLogin set to no, clawuser added to sudo
- **.env permissions fixed** (664 → 600)
- **Auth failover configured** — Opus → Sonnet → GPT-5.4 → GPT-4o, cooldowns set
- **Exec security hardened** — `ask: on-miss` (was unrestricted)
- **autoDream + micro-learning deployed** on Jack's instance
- **openclaw-ops skill installed** — self-healing gateway
- **Watchdog cron** — every 5 min, auto-restarts gateway if down
- **27 OS updates applied** (13 security), kernel upgraded to 6.8.0-106
- **Server rebooted** — came back cleanly
- **Browser sandbox enabled** — fixed AppArmor Chrome restriction
- **Full audit written:** `security-audit-2026-04-03.md`

### Agent Trust Level Fix ✅
- Kilmurry agent refused TUI commands ("can't verify identity")
- Root cause: agent invented own security policy — TUI = unverified
- Fix: Added Channel Trust Levels to AGENTS.md (TUI = highest, SSH = authenticated)
- Added Stephen King (Jonny) as authorised admin

### GEO-SEO Audit ✅
- Ran citability audit on kilmurrylodge.com: **55/100 (C grade)**
- Site is image-heavy with near-zero crawlable text
- llms.txt exists (auto-generated by AIOSEO) but has zero descriptions
- Full report: `vault/research/geo-seo-audit-2026-04-03.md`

---

## Saturday 4 April 2026

### Kate Taylor Marketing Agent — Full Deployment ✅
**Objective:** Deploy a separate OpenClaw instance for Kate Taylor (Digital Marketing & Brand Consultant) on the same server, with full data isolation from Jack's instance.

**Following:** Universal OpenClaw Implementation Playbook (consultancy/playbooks/universal-openclaw-implementation.md)

#### Phase 1 — Server Setup ✅
- Created `kateuser` OS user (separate from clawuser)
- Installed OpenClaw 2026.4.2
- Gateway on port 18792 (systemd: openclaw-kate.service, boot-persistent)
- Auth: Anthropic Sonnet 4-6 primary, Gemini fallback (shared API key)
- Auth cooldowns configured (profile rotation: 3)
- Exec approvals configured
- TUI tested and working

#### Phase 2 — Identity & Memory ✅
- SOUL.md — marketing persona, Kilmurry brand voice, T.A.P.E.R. values
- USER.md — Kate Taylor profile + authorised admins (Kate, Jack, Jonny)
- AGENTS.md — operational rules, NDD logging, channel trust levels
- Vault structure with 5 knowledge files:
  - vault/business/overview.md (hotel, venues, rooms, vision 2030, weddings)
  - vault/people/team.md (all key staff with context)
  - vault/business/competitors.md (4-hotel comp set, rate intel)
  - vault/marketing/control-panel-spec.md (dashboard documentation)
  - vault/marketing/geo-seo-findings.md (55/100 audit, priority fixes)
- MEMORY.md as pointer index (<1.5KB)
- QMD memory backend (BM25 search + vault extraPaths)

#### Phase 3 — Monitoring ✅
- Health script (scripts/server-health.sh, checks port 18792)
- Health cron every 4h
- Watchdog cron every 5min (root, systemctl restart)
- openclaw-ops skill installed
- Doctor run: clean

#### Phase 3.5 — Operational Intelligence ✅
- Autonomy levels in heartbeat-state.json
- NDD format logging
- Advisor cron every 6h (Gemini, isolated)
- Dream cycle cron 2am Dublin (Sonnet, isolated)

#### Phase 4 — Core Capabilities ✅
- **Marketing Control Panel** — 10-page Next.js dashboard on port 3334
  - 4 pages with LIVE data:
    - `/competitors` — 14-date rate comparison across 4 hotels, raise opportunities
    - `/reviews` — 4.3/5 average, 20 reviews, sentiment + theme analysis
    - `/events` — 34 events from 6 Limerick sources, demand scoring 1-5
    - `/seo` — GEO score 55/100, priority fix list
  - 6 pages with professional placeholder states (ready for data)
- PM2 managed (kilmurry-kate-mc), boot persistent
- Data pipelines:
  - events-scrape.py (weekly cron, 6 sources)
  - ga4-fetch.py (ready, blocked on property access)
  - reviews-scrape.py (needs browser for JS sites)
  - Rate data shared from Jack's agent via /opt/kilmurry-shared/

#### Security & Isolation ✅
- **Data isolation verified:** kateuser CANNOT read Jack's workspace, auth, config, sessions, vault, or credentials (all "Permission denied")
- **No sudo:** kateuser has no elevated privileges
- **Shared data:** Only /opt/kilmurry-shared/ (rates-latest.json) is accessible
- **Agent guardrails locked:**
  - SOUL.md + AGENTS.md made immutable (`chattr +i`) — only root can edit
  - Exec switched to allowlist mode — read commands, python3, curl, git, her scripts, openclaw cron/doctor/status only
  - Blocked: `openclaw config set`, rm, chmod, chattr, arbitrary shell
  - exec-approvals.json itself made immutable
- GitHub backup: Jonnyhimalaya/kilmurry-kate (workspace + config-backup)

#### Deployment Score: 93%
Remaining 7% requires Kate (Wednesday meeting):
- Telegram bot setup
- GA4 property access
- Google Ads account details
- Email platform choice
- Brand voice / campaign pillars document

#### Cost Structure
- Kate's gateway: ~317MB RAM
- Kate's dashboard: ~70MB RAM
- Model: Sonnet (~$3/$15 per MTok — much cheaper than Jack's Opus)
- Crons: 4 jobs using Sonnet + Gemini
- Estimated monthly API cost for Kate: ~$20-40/mo

---

### Consultancy Deliverables Tracker

| Deliverable | Status | Date |
|---|---|---|
| Server audit & remediation | ✅ Complete | 30 Mar |
| systemd migration | ✅ Complete | 30 Mar |
| Health monitoring | ✅ Complete | 30 Mar |
| Mission Control fix | ✅ Complete | 30 Mar |
| Tailscale VPN | ✅ Complete | 1 Apr |
| Firewall (UFW) | ✅ Complete | 1 Apr |
| Telegram lockdown | ✅ Complete | 1 Apr |
| Morning briefing fix | ✅ Complete | 1 Apr |
| GitHub backup | ✅ Complete | 1 Apr |
| Operational intelligence | ✅ Complete | 1 Apr |
| Security remediation (v2026.4.2) | ✅ Complete | 3 Apr |
| GEO-SEO audit | ✅ Complete | 3 Apr |
| Kate marketing agent | ✅ Complete | 4 Apr |
| Kate Marketing Control Panel | ✅ Complete | 4 Apr |
| Kate data pipelines (events, rates) | ✅ Complete | 4 Apr |
| Kate agent hardening | ✅ Complete | 4 Apr |
| Kate Telegram bot | ⏳ Wednesday | — |
| Kate GA4 + Google Ads | ⏳ Wednesday | — |

---

*This log is updated after every consultancy session. All changes are version-controlled on GitHub with full rollback capability.*
