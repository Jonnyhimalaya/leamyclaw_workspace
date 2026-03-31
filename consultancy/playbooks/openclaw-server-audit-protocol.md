# OpenClaw Server Audit Protocol

**Purpose:** Step-by-step checklist for auditing a client's OpenClaw deployment via SSH. Produces a standardised architecture schematic, prioritised recommendations, and optimisation roadmap.

**When to use:** Initial client onboarding, periodic health reviews (quarterly recommended), post-incident analysis, or pre-upgrade assessments.

**Time estimate:** 45-90 minutes for a full audit. Results feed directly into the client's architecture schematic and Mission Control page.

---

## Pre-Audit Checklist

Before SSHing in:

- [ ] Confirm SSH access (host, user, auth method)
- [ ] Get client's permission in writing (message/email)
- [ ] Know which channels they use (Telegram, Discord, WhatsApp, etc.)
- [ ] Check if they have a Mission Control instance
- [ ] Prepare a blank architecture schematic from template
- [ ] Note their subscription tier / billing arrangement with us

**⚠️ CRITICAL: Never accept credentials in chat. Use SSH keys or have the client set up access securely.**

---

## Phase 1: Infrastructure Baseline

**Goal:** Understand what we're working with before touching OpenClaw.

### 1.1 System Overview

```bash
# OS and kernel
cat /etc/os-release | head -5
uname -r

# Hardware
nproc
free -h
df -h /
lsblk | head -10

# Uptime and load
uptime
```

**What good looks like:**
- Ubuntu 22.04+ or Debian 12+
- ≥2 CPU cores (1 core is tight but workable)
- ≥2GB RAM (4GB+ preferred for multi-agent setups)
- ≥20% free disk
- Load average < number of cores

**Red flags:**
- 🔴 <1GB free RAM — browser automation will OOM
- 🔴 Swap >50% used — system is thrashing
- 🔴 Disk >80% — logs/sessions accumulating
- 🟡 Ubuntu 20.04 or older — security patches may lag

### 1.2 Memory Deep Dive

```bash
# Detailed memory breakdown
free -h
cat /proc/meminfo | grep -E "MemTotal|MemFree|MemAvailable|SwapTotal|SwapFree|Cached|Buffers"

# Top memory consumers
ps aux --sort=-%mem | head -15

# Check for Chrome/Chromium zombies
pgrep -a chrome | wc -l
pgrep -a chromium | wc -l
```

**Red flags:**
- 🔴 Chrome processes >500MB total — zombies from browser automation
- 🔴 Multiple gateway processes — duplicate instances
- 🟡 Node processes >400MB each — possible memory leak

### 1.3 Network & Ports

```bash
# Listening ports
ss -tlnp | grep -E "LISTEN"

# Firewall status
sudo ufw status 2>/dev/null || sudo iptables -L -n 2>/dev/null | head -20

# External exposure check
curl -s ifconfig.me
```

**What good looks like:**
- Gateway port (default 18789) bound to 127.0.0.1 (not 0.0.0.0)
- Mission Control (3333) bound to 127.0.0.1 or behind reverse proxy
- UFW enabled with minimal open ports (22, maybe 80/443)

**Red flags:**
- 🔴 Gateway bound to 0.0.0.0 — publicly accessible
- 🔴 No firewall active
- 🟡 SSH on default port 22 with password auth enabled

---

## Phase 2: OpenClaw Installation

### 2.1 Version & Installation Method

```bash
# Version
openclaw --version

# Installation method
which openclaw
npm list -g openclaw 2>/dev/null | head -3

# Node version
node --version
```

**What good looks like:**
- Latest stable version (check against GitHub releases)
- Node 20+ (22 preferred)
- Installed globally via npm

**Red flags:**
- 🔴 More than 2 minor versions behind — missing security patches and features
- 🟡 Node <20 — may miss performance improvements

### 2.2 Gateway Process Management

```bash
# Check for systemd service (preferred)
systemctl status openclaw-gateway 2>/dev/null

# Check for PM2
pm2 list 2>/dev/null

# Check for tmux (fragile)
tmux list-sessions 2>/dev/null

# Check for screen
screen -ls 2>/dev/null

# What's actually running?
pgrep -af "openclaw"
```

**What good looks like:**
- ✅ systemd service, enabled, active
- ✅ Auto-restart on failure configured
- ✅ Survives reboot (enabled)

**Red flags:**
- 🔴 Running in tmux/screen — will die on disconnect or reboot
- 🔴 Running as root — security risk
- 🟡 PM2 without boot persistence (`pm2 startup` not run)

### 2.3 Gateway Health

```bash
# Liveness check
curl -s http://127.0.0.1:18789/healthz | python3 -m json.tool 2>/dev/null || curl -s http://127.0.0.1:18789/healthz

# Channel status
openclaw channels status 2>/dev/null

# Recent logs (if systemd)
journalctl -u openclaw-gateway --no-pager -n 50 2>/dev/null

# Config validation
openclaw doctor 2>/dev/null
```

**What good looks like:**
- `{"ok":true,"status":"live"}` from health endpoint
- All configured channels showing "connected"
- No recurring errors in recent logs

**Red flags:**
- 🔴 Health endpoint not responding — gateway down
- 🔴 Channel stuck on "awaiting gateway readiness" — auth/token issue
- 🟡 Repeated 529/rate-limit errors in logs — model overloaded, needs fallback chain

---

## Phase 3: Configuration Audit

### 3.1 Core Config

```bash
# Read main config (redact secrets before recording)
cat ~/.openclaw/openclaw.json | python3 -m json.tool 2>/dev/null

# Check for .env file
cat ~/.openclaw/.env 2>/dev/null | sed 's/=.*/=<REDACTED>/'

# Auth profiles (DO NOT copy — just check structure)
ls -la ~/.openclaw/auth-profiles.json 2>/dev/null
```

**Check for:**
- [ ] Primary model set and appropriate for budget
- [ ] Fallback chain configured (≥2 models)
- [ ] Channel tokens present (not empty strings)
- [ ] No credentials in openclaw.json (should be in .env or auth-profiles)

**Red flags:**
- 🔴 No fallback models — single point of failure
- 🔴 API keys hardcoded in openclaw.json — should be in .env
- 🔴 Using Opus as primary with no budget awareness — expensive
- 🟡 Only one AI provider configured — provider outage = total outage

### 3.2 Agent Architecture

```bash
# List agents
cat ~/.openclaw/openclaw.json | python3 -c "
import json, sys
cfg = json.load(sys.stdin)
agents = cfg.get('agents', {}).get('list', [])
for a in agents:
    print(f\"  {a.get('id','?'):12} model={a.get('model','default'):30} channels={a.get('channelBindings',{})}\")
print(f'\nTotal agents: {len(agents)}')
" 2>/dev/null
```

**Check for:**
- [ ] Each agent has a clear role (not duplicating work)
- [ ] Models appropriate for role (don't use Opus for simple tasks)
- [ ] Channel bindings make sense (right agent handles right channels)
- [ ] No orphaned agents (configured but never used)

**Optimisation opportunities:**
- Scout/research agents → use cheaper models (Grok, Gemini Flash)
- Site management → Sonnet is usually sufficient
- Only orchestrator/strategy needs Opus-tier

### 3.3 Skills Audit

```bash
# List installed skills
ls -la ~/.openclaw/skills/ 2>/dev/null

# Check skill sizes (bloat detection)
du -sh ~/.openclaw/skills/*/ 2>/dev/null

# Count total skill files
find ~/.openclaw/skills/ -name "*.md" 2>/dev/null | wc -l
```

**Red flags:**
- 🟡 >10 skills — potential context bloat (community finding: "strip skills, use Sonnet" improves performance)
- 🟡 Skills >50KB — oversized, may burn tokens on every request
- 🔴 Skills with embedded credentials or API keys

### 3.4 Cron Jobs

```bash
# OpenClaw cron jobs
openclaw cron list 2>/dev/null

# System cron
crontab -l 2>/dev/null
sudo crontab -l 2>/dev/null
```

**Check for:**
- [ ] Cron frequency makes sense (not running expensive models every 5 min)
- [ ] Cron outputs delivered to appropriate channels
- [ ] No duplicate/overlapping schedules
- [ ] Health monitoring cron exists

**Cost flag:** Each cron run = API call. A cron running Opus every 30 minutes = ~$50-100/month just in cron costs.

---

## Phase 4: Memory & Identity

### 4.1 Workspace Structure

```bash
# Workspace overview
ls -la ~/.openclaw/workspace/

# Key files existence check
for f in SOUL.md AGENTS.md USER.md MEMORY.md TOOLS.md IDENTITY.md; do
    [ -f ~/.openclaw/workspace/$f ] && echo "✅ $f ($(wc -c < ~/.openclaw/workspace/$f) bytes)" || echo "❌ $f MISSING"
done

# Memory directory
ls -la ~/.openclaw/workspace/memory/ 2>/dev/null | tail -10
```

**What good looks like:**
- ✅ SOUL.md exists and is customised (not default template)
- ✅ MEMORY.md exists and <20KB (lean, curated)
- ✅ Daily memory files being created
- ✅ AGENTS.md has client-specific rules

**Red flags:**
- 🔴 No SOUL.md — agent has no personality or guidelines
- 🔴 MEMORY.md >50KB — bloated, burning tokens every session
- 🟡 No daily memory files — no session continuity
- 🟡 Default/template files unchanged — setup was never personalised

### 4.2 Memory Health

```bash
# MEMORY.md size
wc -c ~/.openclaw/workspace/MEMORY.md 2>/dev/null

# Recent memory activity
ls -lt ~/.openclaw/workspace/memory/*.md 2>/dev/null | head -10

# Session sizes (token burn indicator)
for f in $(ls -t ~/.openclaw/agents/*/sessions/*.jsonl 2>/dev/null | head -5); do
    msgs=$(grep -c '"role"' "$f" 2>/dev/null || echo 0)
    size=$(du -h "$f" 2>/dev/null | cut -f1)
    echo "$msgs msgs / $size — $f"
done
```

**Red flags:**
- 🔴 Sessions >200 messages — will cause API errors (529/overloaded)
- 🟡 Sessions >100 messages — approaching danger zone
- 🟡 No memory files in last 7 days — agent not logging

---

## Phase 5: Health & Monitoring

### 5.1 Automated Health Checks

```bash
# Check for health script
ls -la ~/.openclaw/workspace/scripts/server-health.sh 2>/dev/null || \
ls -la ~/scripts/server-health.sh 2>/dev/null || \
echo "❌ No health script found"

# Check if health monitoring is in cron
crontab -l 2>/dev/null | grep -i health
openclaw cron list 2>/dev/null | grep -i health
```

**What good looks like:**
- ✅ Health script exists and runs every 4h
- ✅ Alerts delivered to client's channel (Telegram/Discord)
- ✅ Auto-kills Chrome zombies
- ✅ Monitors RAM, disk, swap, gateway liveness

**Red flags:**
- 🔴 No health monitoring at all — problems go unnoticed
- 🟡 Health script exists but no alerting — checks run silently

### 5.2 Log Management

```bash
# Journal size
journalctl --disk-usage 2>/dev/null

# OpenClaw log sizes
du -sh ~/.openclaw/agents/*/sessions/ 2>/dev/null
du -sh ~/.openclaw/logs/ 2>/dev/null

# Old session cleanup
find ~/.openclaw/agents/*/sessions/ -name "*.jsonl" -mtime +30 2>/dev/null | wc -l
```

**Red flags:**
- 🔴 >1GB of old session files — needs cleanup
- 🟡 No log rotation configured

---

## Phase 6: Security

### 6.1 SSH Hardening

```bash
# SSH config
grep -E "^(PasswordAuthentication|PermitRootLogin|Port|AllowUsers)" /etc/ssh/sshd_config 2>/dev/null
```

**What good looks like:**
- ✅ `PasswordAuthentication no` (key-only)
- ✅ `PermitRootLogin no` (or `prohibit-password`)
- ✅ Non-default SSH port (optional but good)

### 6.2 File Permissions

```bash
# Config file permissions (should not be world-readable)
ls -la ~/.openclaw/openclaw.json
ls -la ~/.openclaw/auth-profiles.json 2>/dev/null
ls -la ~/.openclaw/.env 2>/dev/null

# Check for world-readable secrets
find ~/.openclaw -name "*.json" -perm /o+r 2>/dev/null
```

**Red flags:**
- 🔴 auth-profiles.json readable by others (should be 600)
- 🔴 .env readable by others
- 🟡 Running as root user

### 6.3 Credential Storage

```bash
# Check for credentials in workspace files (NEVER should contain API keys)
grep -rn "sk-\|ghp_\|xai-\|AIza" ~/.openclaw/workspace/ 2>/dev/null | head -5
```

**Red flags:**
- 🔴 API keys in workspace files — will be included in agent context
- 🔴 Credentials in MEMORY.md or daily logs

---

## Phase 7: Cost Optimisation

### 7.1 Model Cost Assessment

```bash
# Extract all model references
grep -r "model" ~/.openclaw/openclaw.json 2>/dev/null | grep -v "//"
```

**Cost tiers (approximate monthly, moderate usage):**

| Model | Cost/month (est.) | Best for |
|-------|-------------------|----------|
| Opus 4 | $80-200 | Strategy, orchestration, complex reasoning |
| Sonnet 4 | $15-40 | Site management, routine tasks, customer-facing |
| Grok 3 Mini | $5-15 | Research, web search, monitoring |
| Gemini Flash | $3-10 | Simple classification, routing |
| GPT-4o Mini | $3-8 | Light tasks, formatting |

**Optimisation checklist:**
- [ ] Is the primary model appropriate for the workload?
- [ ] Are sub-agents using cheaper models where possible?
- [ ] Is thinking/reasoning enabled only where needed?
- [ ] Are cron jobs using appropriate models (not Opus for health checks)?
- [ ] Is the fallback chain ordered by cost (cheap fallbacks first, or quality first)?

### 7.2 Token Burn Indicators

```bash
# Skill bloat (loaded every session)
total_skill_size=0
for f in ~/.openclaw/skills/*/SKILL.md; do
    size=$(wc -c < "$f" 2>/dev/null || echo 0)
    total_skill_size=$((total_skill_size + size))
done
echo "Total skill context: ${total_skill_size} bytes"

# MEMORY.md size (loaded every session)
wc -c ~/.openclaw/workspace/MEMORY.md 2>/dev/null

# AGENTS.md size
wc -c ~/.openclaw/workspace/AGENTS.md 2>/dev/null
```

**Rule of thumb:** Every 1KB of always-loaded context ≈ 250 tokens per request. At 100 requests/day with Opus, that's ~$0.75/day per KB of bloat.

---

## Phase 8: Output & Deliverables

After completing the audit, produce:

### 8.1 Architecture Schematic
Use the standard template at `consultancy/clients/<client>/architecture-schematic.md`:
- Server specs & health
- OpenClaw version & process management
- Agent architecture diagram
- Channel configuration
- Cron jobs & automation
- Security posture
- Recommendations (prioritised: critical → nice-to-have)

### 8.2 Recommendations Report
Categorise findings:

| Priority | Category | Description | Effort |
|----------|----------|-------------|--------|
| 🔴 Critical | Fix immediately — data loss, security, or outage risk | |
| 🟠 High | Fix this week — performance, reliability | |
| 🟡 Medium | Fix this month — optimisation, cost savings | |
| 🟢 Low | Nice to have — polish, future-proofing | |

### 8.3 Mission Control Page
- Create/update the client's page in Mission Control
- Rebuild and verify it reflects current state
- Share URL with client

### 8.4 Quick Wins List
Identify 3-5 things you can fix during the audit itself:
- Kill Chrome zombies
- Set up systemd (if tmux)
- Deploy health script
- Fix file permissions
- Add fallback models

**Always ask permission before making changes.** Document everything you do.

---

## Post-Audit

- [ ] Architecture schematic written and synced to workspace-consultancy
- [ ] Mission Control page updated and rebuilt
- [ ] Recommendations shared with client (prioritised)
- [ ] Quick wins completed and documented
- [ ] Changes committed to git
- [ ] Daily memory file updated with audit summary
- [ ] Follow-up date scheduled for unresolved items

---

## Appendix: One-Liner Audit Summary

Run this for a quick health snapshot:

```bash
echo "=== OpenClaw Server Audit Quick Check ==="
echo "OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
echo "OpenClaw: $(openclaw --version 2>/dev/null || echo 'NOT FOUND')"
echo "Node: $(node --version 2>/dev/null || echo 'NOT FOUND')"
echo "RAM: $(free -h | awk '/Mem:/{print $3"/"$2" used"}')"
echo "Swap: $(free -h | awk '/Swap:/{print $3"/"$2" used"}')"
echo "Disk: $(df -h / | awk 'NR==2{print $3"/"$2" ("$5" used)"}')"
echo "Gateway: $(curl -s http://127.0.0.1:18789/healthz 2>/dev/null || echo 'NOT RESPONDING')"
echo "Process: $(systemctl is-active openclaw-gateway 2>/dev/null || echo 'no systemd')"
echo "Chrome: $(pgrep -a chrome 2>/dev/null | wc -l) processes"
echo "Agents: $(cat ~/.openclaw/openclaw.json 2>/dev/null | python3 -c 'import json,sys; print(len(json.load(sys.stdin).get("agents",{}).get("list",[])))' 2>/dev/null || echo '?')"
echo "SOUL.md: $([ -f ~/.openclaw/workspace/SOUL.md ] && echo '✅' || echo '❌')"
echo "MEMORY.md: $([ -f ~/.openclaw/workspace/MEMORY.md ] && echo "✅ $(wc -c < ~/.openclaw/workspace/MEMORY.md) bytes" || echo '❌')"
echo "Health script: $([ -f ~/scripts/server-health.sh ] || [ -f ~/.openclaw/workspace/scripts/server-health.sh ] && echo '✅' || echo '❌')"
```

---

*Last updated: 2026-03-31*
*Based on: Kilmurry Lodge audit (2026-03-30), Leamy Maths infrastructure (2026-03-30)*
