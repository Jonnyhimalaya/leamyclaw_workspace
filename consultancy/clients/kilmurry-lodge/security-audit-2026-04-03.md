# Kilmurry Lodge Server Security Audit
> Date: April 3, 2026 | Server: 172.239.98.61 | Auditor: Main Agent

## 🔴 CRITICAL

### 1. OpenClaw v2026.3.28 — 33 Known Vulnerabilities
- Current: **v2026.3.28** (installed Mar 30)
- Latest: **v2026.4.2**
- Ant AI Security Lab identified **33 vulnerabilities including sandbox escape**
- Patches available in latest release
- **Action:** Update to v2026.4.2 immediately

### 2. Root SSH Login Enabled with Password Auth
- `PermitRootLogin yes` in sshd_config
- Password authentication is enabled
- Root is accessible remotely with a password
- **Action:** Disable root login, use key-based auth only, create admin user

### 3. Chromium Running Without Sandbox
- `browser.noSandbox: true` in config
- Combined with the sandbox escape CVE, this is high-risk
- **Action:** Enable sandbox after OpenClaw update, or disable browser if not needed

## 🟡 WARNING

### 4. No Exec Security Restrictions
- `tools.profile: "full"` — agent has unrestricted command execution
- No exec-approvals.json or allowlist configured
- **Action:** At minimum set ask: "on-miss", ideally use allowlist

### 5. Disk Usage at 66%
- 25GB used of 40GB
- Getting full — workspace has many HTML files from demo generation
- **Action:** Clean up old demo files, monitor disk usage

### 6. Brave Search API Key Exposed
- Hardcoded in openclaw.json (not using env vars)
- **Action:** Move to .env or credentials directory

### 7. Gateway Bound to Loopback Only ✅
- `gateway.bind: "loopback"` — good, not exposed to internet
- Firewall only allows SSH (22) and port 3333 from Tailscale range
- **This is correctly configured**

## 📊 Server Overview

| Metric | Value |
|--------|-------|
| OS | Ubuntu 24.04.4 LTS |
| Kernel | 6.8.0-71-generic |
| OpenClaw | v2026.3.28 (needs v2026.4.2) |
| Node.js | v22.22.1 |
| RAM | 3.8GB total, 1.4GB used |
| Disk | 40GB total, 25GB used (66%) |
| Agents | 1 (main only) |
| Model | claude-opus-4-6 |
| Channels | Telegram + Discord |
| Firewall | UFW active (SSH + Tailscale) |
| Gateway | Running (PID 558167, since Apr 1) |

## Remediation Plan

### Phase 1 — Immediate (Tonight)
1. Update OpenClaw: `npm install -g openclaw@latest && openclaw gateway restart`
2. Disable root SSH: Set `PermitRootLogin no`, ensure clawuser has sudo
3. Clean up disk: Remove old HTML demo files from workspace

### Phase 2 — This Week
4. Enable browser sandbox (or disable browser entirely)
5. Configure exec security (allowlist or on-miss)
6. Move API keys to .env
7. Set up SSH key auth, disable password auth
8. Install openclaw-ops skill for self-healing + monitoring

### Phase 3 — Kate's Setup
9. Create kateuser OS account
10. Separate gateway on port 18790
11. Full security hardening per kate-openclaw-implementation.md
