Client: Aidan
Start date: 2026-04-08
Resume date: 2026-04-22 (after 9-day SSH lockout)
Primary contact: Aidan

PHASE 1 — Server Setup
[x] VPS provisioned (Linode, 172.237.101.137, Ubuntu 24.04.3 LTS, 2 vCPU, 4GB, 40GB)
[x] Non-root user created (clawuser)
[x] SSH hardened (key-only, verified 2026-04-22 16:56 UTC — password auth disabled via /etc/ssh/sshd_config.d/99-openclaw-hardening.conf)
[x] Firewall configured (UFW active, OpenSSH allowed)
[x] Fail2ban installed and active
[x] Unattended-upgrades installed
[x] Node.js LTS installed (v24.15.0 via nvm)
[x] OpenClaw installed (v2026.4.21 global npm)
[x] clawuser password rotated (saved to ~/.openclaw/workspace/credentials/aidan-server.md on main VPS)
[ ] systemd service running — BLOCKED (need credentials + gateway config)
[ ] API keys configured — BLOCKED (awaiting credential strategy decision)
[ ] Auth profile rotation configured (auth.order + auth.cooldowns)
[x] Exec approvals configured (exec-approvals.json — main=full, defaults=allowlist+ask)
[ ] Exec tested (agent can run 'echo test')
[ ] Channel connected (Telegram)
[ ] First message received

PHASE 2 — Identity & Memory
[x] SOUL.md written (2.6KB, BTM-tuned tone, anti-echo-chamber mandate)
[x] USER.md written (2.3KB, Aidan's business context + constraints + pilot)
[x] IDENTITY.md set (Atlas, 🎯)
[x] AGENTS.md configured (5.8KB, Protocols A-E, durable agent rule, boil-the-ocean)
[x] vault/ directory created (business/, offers/, content/, pipeline/, proof/, technical/)
[x] Business knowledge seeded (vault/business/btm-core.md, vault/business/pilot-30d.md)
[x] MEMORY.md written as pointer index (2.3KB)
[x] priority-map.md written (tiered Q1 priorities)
[x] Protocol C checkpoint tracking file (memory/heartbeat-state.json)
[x] .learnings/ seeded (corrections.md, ERRORS.md with SSH lockout lesson, LEARNINGS.md)
[ ] QMD installed (unzip → bun → @tobilu/qmd)
[ ] QMD configured (searchMode: "search", extraPaths: ["vault"])
[ ] Gateway restarted, memory_search tested

PHASE 3 — Monitoring
[x] Health script deployed (scripts/server-health.sh, fixed + tested 2026-04-22)
[x] HEARTBEAT.md configured
[ ] Health cron active
[ ] Backup script running
[ ] Session monitoring active

PHASE 4 — Core Capabilities
[ ] Browser automation (if needed)
[ ] SearXNG enabled and tested (or Brave as fallback)
[ ] Core cron jobs running (health, dream, advisor, costs)
[ ] Intel sweep cron (optional)
[ ] Mission Control (if applicable)

PHASE 5 — Sector Module
[ ] Sector playbook applied: service-businesses / high-ticket-advisory
[ ] Sector-specific skills installed
[ ] Sector cron jobs configured

PHASE 6 — Custom
[ ] Custom skills: authority content engine, advisory CRM follow-up, testimonial extraction
[ ] Custom integrations: ActiveCampaign, Circle, ClickFunnels, Calendly, Zoom, WhatsApp
[ ] Custom dashboards: pipeline, content engine, authority tracking

PHASE 7 — Handoff
[ ] Client trained
[ ] Support model agreed
[ ] First monthly review scheduled

---

## Deployment Log

### 2026-04-22 16:52 UTC — Resumed after 9-day SSH lockout
- Aidan opened Linode Lish console, reset root password, reset clawuser to `Secure2026`
- I re-entered via password, installed SSH key (ed25519, `jonny-main-vps-to-aidan`), verified key auth works
- Then hardened SSH PROPERLY (with pre-hardening triple-verify of key auth)
- Rotated clawuser password post-hardening (for sudo only — SSH is key-only)

### 2026-04-22 16:53 UTC — Node + OpenClaw install
- nvm → Node v24.15.0 → npm v11.12.1
- `npm install -g openclaw` → v2026.4.21 (bundled runtime deps for acpx, amazon-bedrock, browser, etc.)

### 2026-04-22 16:55 UTC — Identity + workspace scaffold
- Created ~/.openclaw/workspace/{memory,vault,scripts,credentials,.learnings}
- Seeded SOUL/USER/IDENTITY/AGENTS/MEMORY/TOOLS tuned to BTM (premium advisor voice)
- Atlas as the agent name (carries operational load so Aidan stays in highest-value mode)

### 2026-04-22 16:58 UTC — Monitoring primitives
- server-health.sh deployed + fixed (two bugs: gateway-not-installed false positive, chrome_count pipe)
- HEARTBEAT.md configured with autonomy tiers
- heartbeat-state.json seeded
- .learnings/ERRORS.md records the SSH lockout root cause for future deployments

### 2026-04-22 16:59 UTC — Exec approvals set
- `main` agent: security=full, ask=off
- Defaults: security=allowlist, ask=on-miss, askFallback=deny
- Sub-agents will need explicit approval — principle of least privilege

### BLOCKED on Jonny
- Credentials strategy (A: Jonny's keys, B: Aidan's own, C: OpenRouter single key)
- Monthly budget ceiling
- Telegram bot ownership (new via BotFather vs Aidan's own)

Once unblocked: auth profiles → models config → systemd gateway service → Telegram channel → first message → QMD → cron → handoff.
