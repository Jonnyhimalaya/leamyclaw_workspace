# Deployment Checklist — Accountant Client
**Start date:** 2026-04-20
**Primary contact:** TBD (Jonny's friend)
**Server:** 172.237.126.222 (Ubuntu 24.04 LTS, 4GB RAM, 40GB disk)
**Deployed by:** Jonny / main agent

---

## PHASE 1 — Server Setup

### Infrastructure
- [ ] Non-root user created (clawuser)
- [x] SSH accessible (password auth, root)
- [ ] Recovery-safe access path verified before SSH hardening
- [ ] SSH hardened (disable root login + password auth)
- [ ] UFW firewall configured
- [ ] Fail2ban installed
- [ ] Automatic security updates enabled
- [ ] Node.js LTS installed (via nodesource or nvm)
- [ ] OpenClaw installed (`npm install -g openclaw`)
- [ ] Git configured

### OpenClaw Core
- [ ] `openclaw init` run
- [ ] Gateway configured on loopback
- [ ] Primary model configured
- [ ] Fallback model configured
- [ ] Auth profile rotation configured
- [ ] Exec approvals configured (exec-approvals.json)
- [ ] Exec tested (echo test passes)
- [ ] systemd service created and running
- [ ] Channel (Telegram) connected
- [ ] First message received

---

## PHASE 2 — Identity & Memory

- [ ] SOUL.md written
- [ ] USER.md written
- [ ] IDENTITY.md set
- [ ] AGENTS.md configured
- [ ] vault/ directory created
- [ ] Business knowledge seeded into vault/
- [ ] MEMORY.md written as pointer index
- [ ] QMD installed and configured
- [ ] memory_search tested

---

## PHASE 3 — Monitoring

- [ ] Health script deployed
- [ ] Health cron active
- [ ] HEARTBEAT.md configured
- [ ] Git backup repo created
- [ ] Session monitoring active

---

## PHASE 4 — Core Capabilities

- [ ] SearXNG enabled and tested
- [ ] Core cron jobs running (health, dream, advisor)

---

## PHASE 5+ — Sector/Custom

- [ ] Sector: Accounting — specific workflows TBD
- [ ] Custom skills TBD

---

## Notes

- Server password in Telegram chat — ask client to change after setup
- 4GB RAM: browser automation NOT recommended unless absolutely needed (add swap buffer at minimum)
- Client name / Telegram ID: TBD
