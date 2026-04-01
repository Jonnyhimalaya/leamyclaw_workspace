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

*This log is updated after every consultancy session. All changes are version-controlled on GitHub with full rollback capability.*
