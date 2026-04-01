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

### Architecture Schematic — Written & Published ✅
- Full architecture schematic document covering:
  - Server infrastructure & specs
  - OpenClaw configuration & agent setup
  - Channel configuration (Telegram + Discord)
  - Cron jobs & automation
  - Health monitoring
  - Security posture
  - Prioritised recommendations
- Published to Mission Control dashboard — viewable at `/consultancy/clients/kilmurry-lodge`
- Updated post-remediation to reflect all fixes applied

### Discord Bot Investigation
- Jack reported Discord bot not responding
- Investigated: found misleading log message ("awaiting gateway readiness") — bot was actually working
- Confirmed via `openclaw channels status` showing "connected"
- Lesson learned: always test by messaging the bot before deep debugging

---

## Tuesday 31 March 2026

### Consultancy Playbook: Server Audit Protocol — Written ✅
- Created standardised 8-phase SSH audit checklist for client deployments
- Phases: Infrastructure → OpenClaw Install → Config → Memory → Health → Security → Cost → Deliverables
- Includes exact commands to run, "what good looks like" vs red flags
- One-liner quick-check script for 10-second server snapshots
- Based directly on lessons from Kilmurry audit

### Consultancy Playbook: Security Hardening — Written ✅
- Created comprehensive 6-layer security model for client deployments:
  - Layer 1: Network perimeter (Tailscale VPN, UFW firewall, SSH hardening)
  - Layer 2: Channel lockdown (allowFrom whitelists, DM policies)
  - Layer 3: Data segregation (vault structure, access control per agent)
  - Layer 4: Agent sandboxing (exec deny/allowlist, workspaceOnly filesystem)
  - Layer 5: Credential management (secure storage, rotation schedules)
  - Layer 6: Monitoring & audit (daily security scans, anomaly detection)
- 28-item implementation checklist
- Client communication template (plain English explanation of changes)
- Directly applicable to Kilmurry's upcoming security hardening

### Operational Intelligence Patterns — Implemented ✅
- Implemented 6 advanced operational patterns (inspired by industry best practices):
  1. Autonomy levels — agent adjusts proactivity based on human activity
  2. Structured logging (Noticed/Decision/Did format) — auditable action trail
  3. Advisor model — cheap AI reviews main agent's work every 6 hours
  4. Sleep-when-idle — zero token waste during quiet periods
  5. Automated nightly memory consolidation
  6. Append-only audit logs for tamper-proof records
- All patterns documented in universal implementation playbook for future client deployments

### Morning Briefing Investigation
- Identified why Jack's daily morning briefing stopped arriving on Telegram
- Root cause: delivery mode was set to "none" — briefings were generated and saved to server but never sent
- Secondary issue: using expensive model (Opus) with no fallback — prone to API overload errors
- Fixes applied (see April 1 below)

---

## Wednesday 1 April 2026

### Security Hardening — Tailscale VPN ✅
- Installed Tailscale on Kilmurry server
- Server assigned private IP: 100.111.174.13
- Jack created Tailscale account, connected:
  - Server (localhost-0)
  - iPhone
  - Laptop
- Consultant (Jonny) added via device sharing — can access server through VPN
- Verified: Mission Control accessible via Tailscale IP from all authorised devices

### Security Hardening — Firewall (UFW) ✅
- Enabled UFW firewall (was completely inactive — server wide open)
- Rules configured:
  - SSH (port 22): open (for remote management)
  - Mission Control (port 3333): **Tailscale devices only** — public internet blocked
  - All other incoming traffic: denied
- Verified: Mission Control loads via Tailscale IP, blocked from public IP

### Security Hardening — Telegram Bot Lockdown ✅
- Configured `allowFrom` with Jack's Telegram user ID
- Set `dmPolicy` to `allowlist`
- Result: only Jack can message the bot — all other users silently ignored
- Tested: consultant's Telegram correctly blocked from accessing bot

### Morning Briefing Fix ✅
- Changed delivery mode from `"none"` to `"announce"` with Jack's Telegram chat ID
- Switched model from Opus (expensive, unreliable) to Sonnet (cheaper, faster)
- Triggered test run — briefing delivered successfully to Jack's Telegram
- Will run automatically at 7am Dublin time daily going forward

### GitHub Backup — Deployed ✅
- Jack's entire OpenClaw workspace backed up to private GitHub repository
- 334 files committed: workspace files, vault, reports, rate data, scripts, skills, dashboards
- Config backup folder added: openclaw.json, cron jobs, skill definitions
- Credentials excluded via .gitignore (API keys, bot tokens, .env)
- Git backup protocol embedded in agent's AGENTS.md — agent will self-backup after meaningful changes
- Full version history and rollback capability now available

### Remaining Items (Scheduled)
- [ ] Discord bot lockdown (need Jack's Discord user ID)
- [ ] SSH hardening (key-only authentication, disable passwords)
- [ ] Jack's server password change (exposed in chat during session)
- [ ] Fallback model chain configuration (protect against API outages)
- [ ] Agent sandboxing (restrict tools per agent role)

---

*This log is updated after every consultancy session. All changes are version-controlled on GitHub with full rollback capability.*
