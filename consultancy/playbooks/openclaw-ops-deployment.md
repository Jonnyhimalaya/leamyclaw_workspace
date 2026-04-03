# OpenClaw-Ops Deployment Playbook
> Self-healing ops layer for any OpenClaw server
> Source: https://github.com/cathrynlavery/openclaw-ops
> Tested on: v2026.4.1+ · Linux (Ubuntu/Debian) + macOS

---

## What This Gives Your Client

1. **Self-healing gateway** — auto-restarts within 5 minutes of any crash, 24/7
2. **One-shot repair** — fixes the 6 most common post-update breakages in one command
3. **Update triage** — tells you exactly what broke after an OpenClaw update and auto-fixes it
4. **Security scoring** — 0-100 config hardening score with specific fixes
5. **Skill vetting** — static audit of any ClawHub skill before install (catches malware, prompt injection, leaked secrets)
6. **No maintenance required** — set it and forget it

## Prerequisites

- OpenClaw v2026.2.12+ (earlier versions have critical CVEs)
- `python3`, `curl`, `openssl` installed
- SSH access to the server

## Deployment Steps (5 minutes)

### Step 1: Install
```bash
git clone https://github.com/cathrynlavery/openclaw-ops.git ~/.openclaw/skills/openclaw-ops
```

### Step 2: Run heal.sh (one-shot fix)
```bash
bash ~/.openclaw/skills/openclaw-ops/scripts/heal.sh
```

**What it checks and fixes:**
| Check | What it does | Auto-fix? |
|-------|-------------|-----------|
| Version | Confirms ≥ v2026.2.12 (pre-CVE patch) | ❌ (flags only) |
| Gateway | Checks if gateway process is running | ✅ restarts |
| Auth | Validates API keys and auth mode | ✅ generates token |
| Exec approvals | Layer 1 (allowlists) + Layer 2 (exec-approvals.json) | ✅ fixes both |
| Cron jobs | Detects silently disabled crons | ✅ re-enables |
| Sessions | Finds stuck loops, bloated (>10MB), dead sessions | ✅ cleans up |

**Common fix:** `tools.exec.strictInlineEval` gets set to `true` by updates — blocks complex commands silently. heal.sh sets it to `false` and restarts gateway.

### Step 3: Set up watchdog (always-on monitoring)

**Linux (cron):**
```bash
mkdir -p ~/.openclaw/logs
(crontab -l 2>/dev/null | grep -v "openclaw-ops/scripts/watchdog.sh"; echo "*/5 * * * * bash \$HOME/.openclaw/skills/openclaw-ops/scripts/watchdog.sh >> \$HOME/.openclaw/logs/watchdog.log 2>&1") | crontab -
```

**macOS (LaunchAgent — survives reboots):**
```bash
bash ~/.openclaw/skills/openclaw-ops/scripts/watchdog-install.sh
```

**How it works:**
- Tier 1: HTTP ping every 5 min
- Tier 2: Gateway restart + heal.sh if simple restart fails
- Tier 3: After 3 failed attempts in 15 min → notification/escalation

### Step 4: Run security scan
```bash
bash ~/.openclaw/skills/openclaw-ops/scripts/security-scan.sh
```

**What it checks:**
| Check | Good | Bad |
|-------|------|-----|
| Gateway binding | loopback or Tailscale | 0.0.0.0 (open to internet) |
| Auth mode | token | none |
| Sandbox mode | explicitly set | not set |
| Version | ≥ v2026.2.12 | older (CVE-vulnerable) |
| File permissions | 600 on sensitive files | 664 (world-readable) |
| Credential leaks | none in workspace | API keys in git-tracked files |

**Fix file permissions if flagged:**
```bash
find ~/.openclaw -name "*.json" -path "*/agent/*" -exec chmod 600 {} \;
chmod 600 ~/.openclaw/.env
```

### Step 5: Verify watchdog is running
```bash
# Check cron is set
crontab -l | grep watchdog

# After 5 min, check log
tail -5 ~/.openclaw/logs/watchdog.log
```

## Ongoing Usage

### After every OpenClaw update:
```bash
# See what broke and why
bash ~/.openclaw/skills/openclaw-ops/scripts/check-update.sh

# Auto-fix what it found
bash ~/.openclaw/skills/openclaw-ops/scripts/check-update.sh --fix
```

### Before installing any ClawHub skill:
```bash
bash ~/.openclaw/skills/openclaw-ops/scripts/skill-audit.sh ~/.openclaw/skills/<skill-name>
```

### View incident history:
```bash
cat ~/.openclaw/logs/heal-incidents.jsonl
```

### View watchdog log:
```bash
tail -f ~/.openclaw/logs/watchdog.log
```

## Client Handoff Notes

When deploying for a client:
1. Run heal.sh FIRST — catches any existing issues
2. Set up watchdog cron — non-negotiable for any production server
3. Run security scan — document the score, fix anything below 100
4. Show the client the watchdog log after 24 hours — proves it's working
5. Add check-update.sh to post-update SOP
6. Run skill-audit.sh before ANY ClawHub install on their server

## What This Replaced For Us

| Before | After |
|--------|-------|
| Manual gateway restart diagnosis | heal.sh auto-fixes in seconds |
| 2-hour exec approval debugging (Apr 2) | heal.sh detects + fixes both layers |
| No idea what updates break | check-update.sh explains + auto-fixes |
| Basic server-health.sh (RAM/disk only) | Full ops monitoring + self-healing |
| No skill vetting before install | Static audit catches malware/injection |
| Gateway dies at 3am → down until morning | Watchdog restarts within 5 minutes |

---

*Deployed on our server: 2026-04-03. Deploy on Kilmurry: pending SSH access.*
