# Universal OpenClaw Implementation Playbook
**Purpose:** The standard implementation every client gets, regardless of sector. This is the foundation layer — sector-specific and business-specific modules stack on top.

---

## Playbook Structure

```
┌─────────────────────────────────────────────┐
│       BUSINESS-SPECIFIC CUSTOMISATION       │  ← Unique to each client
│    (custom skills, workflows, integrations) │
├─────────────────────────────────────────────┤
│          SECTOR MODULE (optional)           │  ← hotels.md, education.md, etc.
│     (industry patterns, common agents)      │
├─────────────────────────────────────────────┤
│       UNIVERSAL FOUNDATION (this file)      │  ← Every client gets this
│  (infrastructure, security, monitoring,     │
│   memory, identity, communication)          │
└─────────────────────────────────────────────┘
```

---

# PHASE 0 — Pre-Deployment (Before Touching a Server)

## 0.1 Discovery & Assessment
- Run the **New Company AI Assessment Protocol** (`protocols/new-company-ai-assessment-protocol.md`)
- Produce a **Business Snapshot** — sector, size, workflows, pain points, existing tools
- Identify the **first high-value pilot** — one clear win to prove value before scaling
- Map existing tech stack (use `templates/tech-stack-audit-worksheet.md`)
- Score AI opportunities (use `templates/ai-opportunity-scoring-sheet.md`)

## 0.2 Architecture Decision
- **Server:** Dedicated Linode VPS per client (data isolation — non-negotiable)
- **Sizing:** 4GB minimum (8GB recommended if browser automation needed)
- **Region:** Closest to client's geography
- **Domain/access:** Decide on SSH access model (our key + client key, or our key only)

## 0.3 Client Agreement
- Scope: what's included in the pilot
- Access: what systems/accounts we'll need
- Credentials: **NEVER in chat** — use a password manager or secure handoff
- Data boundaries: what data the agent can/cannot access
- Communication channel: how the client talks to their agent (Telegram, Discord, WhatsApp)

---

# PHASE 1 — Server Setup (Day 1)

## 1.1 Base Infrastructure
Every client server gets:

- [ ] Ubuntu LTS (latest stable)
- [ ] Dedicated non-root user (e.g. `clawuser`)
- [ ] SSH key-only authentication (disable password login)
- [ ] UFW firewall (allow SSH + any needed ports only)
- [ ] Fail2ban installed and active
- [ ] Automatic security updates enabled (`unattended-upgrades`)
- [ ] Node.js LTS (via nvm or nodesource)
- [ ] OpenClaw installed (`npm install -g openclaw`)
- [ ] Git configured

## 1.2 OpenClaw Core Setup
- [ ] `openclaw init` — initialise workspace
- [ ] Gateway configured on loopback (127.0.0.1) with auth token
- [ ] Primary model configured (recommend Opus or Sonnet depending on budget)
- [ ] Fallback model configured (cross-provider: if primary is Anthropic, fallback to OpenAI or vice versa)

### systemd Gateway Service (MANDATORY — not tmux, not screen, not nohup)

**Why not tmux?** tmux holds processes and environment variables in memory only. If the tmux session is killed, the server reboots, or you close your SSH terminal, the gateway dies and any env vars (including secrets) are lost forever. We learned this the hard way — twice — during the Kilmurry and Leamy migrations on 30 March 2026.

**systemd gives you:** auto-restart on crash, boot persistence, proper logging via journalctl, and a clean reproducible environment.

#### Step 1: Verify the correct gateway command
**ALWAYS run this first.** Do not guess flags.
```bash
openclaw gateway --help
```
As of v2026.3.28, the correct foreground command is `openclaw gateway run` (NOT `start --foreground` — that flag doesn't exist and will crash-loop).

#### Step 2: Create the environment file for secrets
Any channel that stores its token as `"source": "env"` (e.g. Discord) needs the actual value in a persistent file. Check the config first:
```bash
grep -E '"source":\s*"env"' ~/.openclaw/openclaw.json
```
If any env var references exist, create the `.env` file:
```bash
nano ~/.openclaw/.env
# Add each referenced variable, e.g.:
# DISCORD_BOT_TOKEN=MTQ4Nzgz...full-token-here
chmod 600 ~/.openclaw/.env
```
**CRITICAL:** Do this BEFORE starting the systemd service. A missing env var will crash the gateway, and rapid crash-loops can trigger Discord gateway rate limits that take hours to clear.

#### Step 3: Create the systemd service file
```bash
sudo tee /etc/systemd/system/openclaw-gateway.service << 'EOF'
[Unit]
Description=OpenClaw Gateway (<CLIENT_NAME>)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=<SERVICE_USER>
WorkingDirectory=/home/<SERVICE_USER>/.openclaw
EnvironmentFile=/home/<SERVICE_USER>/.openclaw/.env
ExecStart=/home/<SERVICE_USER>/.npm-global/bin/openclaw gateway run
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
Environment=PATH=/home/<SERVICE_USER>/.npm-global/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target
EOF
```
Replace `<CLIENT_NAME>` and `<SERVICE_USER>` with actual values.

#### Step 4: Test the command manually BEFORE enabling the service
```bash
# As the service user, run the gateway command directly to verify it starts:
su - <SERVICE_USER> -c "source ~/.openclaw/.env && openclaw gateway run"
# Wait for "listening on ws://..." message, then Ctrl+C
# If it crashes here, fix it before proceeding
```

#### Step 5: Enable and start
```bash
sudo systemctl daemon-reload
sudo systemctl enable openclaw-gateway
sudo systemctl start openclaw-gateway
```

#### Step 6: Verify
```bash
sudo systemctl status openclaw-gateway   # Should show "active (running)"
journalctl -u openclaw-gateway -n 20     # Check for errors
curl http://127.0.0.1:<PORT>/health      # Should return {"ok":true}
```

#### Checklist
- [ ] `openclaw gateway --help` run to verify correct command
- [ ] `.env` file created with all env var secrets (chmod 600)
- [ ] Service file created with correct ExecStart and EnvironmentFile
- [ ] Command tested manually before enabling service
- [ ] `systemctl enable` for boot persistence
- [ ] `systemctl start` and verified healthy
- [ ] journalctl checked for errors (especially channel connection)

## 1.3 Communication Channel
- [ ] At least one channel configured (Telegram is fastest to set up)
- [ ] Bot created and token secured
- [ ] Client's user ID whitelisted
- [ ] Test message sent and received

---

# PHASE 2 — Identity & Memory (Day 1-2)

## 2.1 Agent Identity
Every agent needs proper identity files:

- [ ] **SOUL.md** — personality, tone, boundaries, working relationship rules
  - Include anti-echo-chamber mandate (learned from Kilmurry — this is gold)
  - Define what the agent should challenge vs defer on
  - Set communication style to match the client's preference
- [ ] **USER.md** — the primary human's name, role, preferences, timezone
- [ ] **IDENTITY.md** — agent name, emoji, creature type
- [ ] **AGENTS.md** — operational rules, memory protocols, safety rules

## 2.2 Memory System — Vault Architecture
The #1 optimisation: MEMORY.md should be a **slim pointer index**, NOT a knowledge dump.

### Why this matters
Every workspace file (MEMORY.md, SOUL.md, AGENTS.md, TOOLS.md) is injected into EVERY message the agent processes. A bloated MEMORY.md (10-15KB) means:
- Slower responses (more tokens to process)
- Higher costs (paying for irrelevant context every message)
- Less room in the context window before compaction hits
- Compaction destroys chat-only context — the bigger your files, the less room for conversation

### Target file sizes (community best practice)
| File | Target | What goes in it |
|------|--------|----------------|
| SOUL.md | < 1 KB | Personality, tone, core rules |
| AGENTS.md | < 3 KB | Decision tree, memory protocols, safety |
| MEMORY.md | < 3 KB | **Pointers only** — NOT full docs |
| TOOLS.md | < 1 KB | Tool names + one-liner usage |
| **Total** | **< 8 KB** | Everything injected per message |

### Setup steps
- [ ] `memory/` directory created
- [ ] `vault/` directory created with subdirectories by domain (e.g. `vault/business/`, `vault/operations/`, `vault/people/`)
- [ ] Daily logging protocol in AGENTS.md (mandatory — we lost 6 days of context once)
- [ ] MEMORY.md initialised as a **pointer index**:
  - Key facts about the person (2-3 lines)
  - Active projects as pointers → `vault/projects/project-name.md`
  - Key people as pointers → `vault/people/person-name.md`
  - Known issues (brief)
  - Preferences (brief)
- [ ] Detailed knowledge goes in vault files, NOT in MEMORY.md:
  - Business context → `vault/business/overview.md`
  - Staff profiles → `vault/people/`
  - Tools and systems → `vault/technical/`
  - Competitors → `vault/business/competitors.md`

### Memory protocols in AGENTS.md
Add these protocols to every client's AGENTS.md:

```markdown
### Protocol A: Search-First, Write-Last
BEFORE answering any question about past facts, decisions, or preferences:
1. Call `memory_search` — never rely solely on conversation history
2. Only skip if the answer is obviously in the current session

AFTER every meaningful exchange:
3. Ask: "Does this need to survive the next session?" → If yes, write to the correct file immediately.

### Protocol B: File Routing
| What it is | Where it goes |
|---|---|
| Raw events, task logs | `memory/YYYY-MM-DD.md` (daily log) |
| Distilled lessons, persistent facts | `MEMORY.md` (pointers) or `vault/` (detail) |
| Operational rules | `AGENTS.md` |
| Persona, voice, style | `SOUL.md` |
```

### QMD Memory Backend (recommended)
- [ ] Install prerequisites: `apt install -y unzip` (as root)
- [ ] Install Bun: `curl -fsSL https://bun.sh/install | bash` (as service user)
- [ ] Install QMD: `bun install -g @tobilu/qmd`
- [ ] Configure in openclaw.json:
  ```json
  "memory": {
    "backend": "qmd",
    "qmd": {
      "searchMode": "search",
      "includeDefaultMemory": true,
      "update": { "interval": "10m", "onBoot": true },
      "limits": { "maxResults": 8, "maxSnippetChars": 700, "timeoutMs": 4000 }
    }
  }
  ```
- [ ] Add vault as extra search path in `agents.defaults.memorySearch.extraPaths: ["vault"]`
- [ ] Restart gateway to apply
- [ ] Test with `memory_search` — verify vault files are found

### QMD Search Modes
| Mode | What it does | Requirements | Cost |
|------|-------------|--------------|------|
| `search` | BM25 keyword matching | Nothing extra | Free |
| `query` | Hybrid BM25 + vector + reranking | Embedding API (OpenAI/Gemini) | ~$0.01/day |
| `vsearch` | Vector-only semantic search | Embedding API | ~$0.01/day |

**Start with `search` (BM25).** It's free, fast, and works well for small-to-medium vault sizes. Upgrade to `query` (hybrid) when the client has 50+ vault/memory files or needs semantic matching.

### Hybrid search config (when ready to upgrade)
```json
"agents": {
  "defaults": {
    "memorySearch": {
      "extraPaths": ["vault"],
      "query": {
        "hybrid": {
          "enabled": true,
          "vectorWeight": 0.7,
          "textWeight": 0.3,
          "mmr": { "enabled": true, "lambda": 0.7 },
          "temporalDecay": { "enabled": true, "halfLifeDays": 30 }
        }
      }
    }
  }
}
```

## 2.3 Business Knowledge
Transfer discovery knowledge into **vault files** (not MEMORY.md):
- [ ] Company overview → `vault/business/overview.md`
- [ ] Key staff names and roles → `vault/people/` (one file per key person, or combined)
- [ ] Important dates, cycles, seasonality → `vault/business/calendar.md`
- [ ] Competitor landscape → `vault/business/competitors.md`
- [ ] Client's goals for the AI system → `vault/business/goals.md`
- [ ] MEMORY.md updated with pointers to all vault files

---

# PHASE 3 — Health & Monitoring (Day 2)

## 3.1 Server Health Script
Every client gets a health monitoring script. Standard checks:

- [ ] RAM usage (alert if >80%, critical if >90%)
- [ ] Swap usage (alert if >50%)
- [ ] Disk usage (alert if >75%)
- [ ] Chrome/Chromium orphan processes (auto-kill if found)
- [ ] PM2 health (if Mission Control running)
- [ ] Gateway liveness (`curl http://127.0.0.1:<port>/health`)
- [ ] System load
- [ ] Orphan node processes

Script template: adapt from `scripts/server-health.sh` (Leamy) or Kilmurry version.

## 3.2 Health Cron
- [ ] Health script runs every 4 hours via system crontab
- [ ] Alerts delivered to client's Telegram (only when issues found — no spam)
- [ ] Alert wrapper script with bot token and chat ID

## 3.3 Session Monitoring
- [ ] HEARTBEAT.md configured with session size checks
- [ ] Alert thresholds: >100 messages warning, >200 critical
- [ ] Heartbeat interval: 30 minutes (default)

## 3.4 Backup
- [ ] Workspace backup script (tar the workspace directory)
- [ ] Schedule: daily or weekly depending on activity level
- [ ] Retention: keep last 7 backups minimum
- [ ] Test restore procedure at least once

---

# PHASE 3.5 — Operational Intelligence Patterns (Day 2-3)

**These patterns are standard for every deployment. They make the agent smarter, cheaper, and more trustworthy over time. Inspired by analysis of best-in-class agentic architectures.**

## 3.5.1 Autonomy Levels

Every agent should adjust its proactivity based on whether the human is actively engaged or away. Track in `memory/heartbeat-state.json`:

```json
{
  "autonomy": {
    "lastHumanMessage": null,
    "level": "responsive"
  }
}
```

| Level | Condition | Behaviour |
|-------|-----------|-----------|
| **Responsive** | <30 min since last message | Answer questions, execute tasks. Don't initiate. |
| **Ambient** | 30 min – 2 hours | Light proactive work: memory maintenance, git commits, doc cleanup. |
| **Proactive** | 2 – 8 hours | Run analyses, background research, send summary if significant. |
| **Dormant** | 8+ hours or 23:00–08:00 | Only critical alerts. Otherwise sleep (HEARTBEAT_OK). |

Add to client's AGENTS.md and HEARTBEAT.md. The dormant level prevents token waste overnight.

**Checklist:**
- [ ] heartbeat-state.json created with autonomy tracking
- [ ] Autonomy level rules added to AGENTS.md
- [ ] HEARTBEAT.md Step 0 checks autonomy level before doing anything

## 3.5.2 Structured Logging (NDD Format)

All meaningful actions logged as **Noticed / Decision / Did**:

```markdown
### [Task Title] — HH:MM UTC
- **Noticed:** What triggered this (user request, anomaly, scheduled check)
- **Decision:** What I chose to do and why
- **Did:** What actually happened (with IDs, paths, outcomes)
```

This format is:
- **Auditable** — client can review what the agent did and why
- **Scannable** — future sessions understand context instantly
- **Compliance-friendly** — structured trail for financial/legal clients

**Checklist:**
- [ ] NDD format documented in client's AGENTS.md under memory logging protocol
- [ ] Append-only principle stated: never edit existing log entries, only add corrections below

## 3.5.3 Advisor Model (Meta-Oversight)

A cheap model reviews the main agent's work on a schedule. Catches mistakes before they compound.

```bash
openclaw cron add \
  --name "Advisor Check" \
  --cron "0 */6 * * *" \
  --tz "<CLIENT_TZ>" \
  --agent main \
  --model "google/gemini-3.1-pro-preview" \
  --session isolated \
  --timeout-seconds 60 \
  --message "You are the ADVISOR. Read today's memory file. Check for: mistakes, unverified tasks, security concerns, unfulfilled promises. If issues found, append an Advisor Notes section. If clean, do nothing."
```

**Key design choices:**
- Uses a **cheap model** (Gemini) — this is a quality gate, not heavy reasoning
- **Only writes when problems found** — no "all clear" noise
- **Read-only except for advisory notes** — can't take actions, only flag
- Runs every 6 hours — frequent enough to catch issues same-day

**Checklist:**
- [ ] Advisor cron job created
- [ ] Using cheap cross-provider model (Gemini or GPT-4o-mini)
- [ ] Verified: only writes notes, doesn't take actions

## 3.5.4 autoDream (Nightly Memory Consolidation)

Every deployment gets a nightly cron that consolidates daily logs into long-term memory:

```bash
openclaw cron add \
  --name "Dream Cycle" \
  --cron "0 2 * * *" \
  --tz "<CLIENT_TZ>" \
  --agent main \
  --model "anthropic/claude-sonnet-4-6" \
  --session isolated \
  --timeout-seconds 300 \
  --message "DREAM CYCLE: Phase 1 — read today's daily log + MEMORY.md, distil key decisions/lessons/facts into MEMORY.md. Phase 2 — archive daily logs older than 7 days to memory/archive/. Phase 3 — if MEMORY.md exceeds target size, trim stale info. If nothing to do, stop silently."
```

**What it does:**
1. Reads today's raw daily log
2. Extracts anything worth remembering long-term (decisions, lessons, milestones)
3. Appends distilled content to MEMORY.md
4. Archives old daily logs (>7 days) to `memory/archive/`
5. Trims MEMORY.md if it's getting bloated

**Why this matters:**
- MEMORY.md stays lean (cheaper context per message)
- Important context survives beyond daily logs
- Old logs don't clutter the memory directory
- Self-healing memory — agent gets smarter over time without manual curation

**Checklist:**
- [ ] Dream cycle cron created (2am local time)
- [ ] `memory/archive/` directory exists
- [ ] MEMORY.md size target set in the cron prompt (<3KB for pointer index, <5KB for inline)

## 3.5.5 Append-Only Audit Logs

For clients handling sensitive data (financials, customer PII), daily logs should be tamper-proof:

```bash
# Add to health script — lock yesterday's log at midnight
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
LOG="$HOME/.openclaw/workspace/memory/${YESTERDAY}.md"
[ -f "$LOG" ] && chattr +a "$LOG" 2>/dev/null
```

**AGENTS.md rules:**
- Never edit or delete existing daily log entries — append only
- If a log entry has an error, add a correction below it
- Every financial data access must be logged with: who requested, what was accessed, timestamp

**See also:** Security Hardening Playbook → Layer 7 (Append-Only Audit Logs) for full implementation.

**Checklist:**
- [ ] Append-only principle in AGENTS.md
- [ ] Health script locks previous day's log (if client needs audit trail)
- [ ] Log retention policy set (90-day archive, compress older)

## Standard Cron Suite (All Clients)

After implementing Phase 3 + 3.5, every client should have:

| Job | Schedule | Model | Purpose |
|-----|----------|-------|---------|
| Server Health | Every 4h | system cron | RAM, disk, Chrome cleanup, alerts |
| Dream Cycle | 2am | Sonnet | Memory consolidation |
| Advisor Check | Every 6h | Gemini | Quality control / meta-oversight |
| Session Costs | Every 4-8h | Sonnet | Track API spend |

Sector-specific cron jobs (e.g., rate scraping, review monitoring) are added in Phase 5.

---

# PHASE 4 — Core Capabilities (Day 2-3)

## 4.1 Browser Automation
If the client needs web-based tasks:

- [ ] Playwright/Chromium installed and working
- [ ] Persistent browser profile configured (if needed for logins)
- [ ] Chrome auto-cleanup in health script (critical — Chrome leaks memory)

## 4.2 Web Search
- [ ] Brave Search API key configured (or alternative)
- [ ] Test search working

## 4.3 Cron Jobs — Universal Set
Every client should have at minimum:

| Job | Schedule | Purpose |
|-----|----------|---------|
| Health check | Every 4h | Server monitoring + alerts |
| Session costs | Every 4-8h | Track API spend |
| Memory maintenance | Weekly | Review daily logs, update MEMORY.md |

Additional cron jobs are sector/business-specific.

## 4.4 Mission Control (Optional but Recommended)
- [ ] Next.js dashboard deployed
- [ ] PM2 managed with boot persistence
- [ ] Client-specific pages configured
- [ ] Accessible on localhost (or behind auth if exposed)

---

# PHASE 5 — Sector Module (Day 3-5)

Apply the relevant sector playbook:
- Hotels → `playbooks/hotels.md`
- Education → `playbooks/education.md`
- Service businesses → `playbooks/service-businesses.md`
- *(New sectors get new playbooks as we learn)*

Sector modules typically add:
- Industry-specific skills
- Specialised cron jobs (e.g. rate scraping for hotels, enrollment tracking for education)
- Domain knowledge in MEMORY.md
- Suggested agent team structure for multi-agent evolution

---

# PHASE 6 — Business-Specific Customisation (Day 5+)

This is where every client diverges:
- Custom skills for their specific workflows
- Integrations with their existing tools (PMS, CRM, booking engines, etc.)
- Custom dashboards in Mission Control
- Specialised agents (when the single-agent model outgrows its remit)
- Automated reporting tailored to their KPIs

---

# PHASE 7 — Handoff & Ongoing (Week 2+)

## 7.1 Client Training
- [ ] Show the client how to talk to their agent
- [ ] Explain what the agent can/can't do
- [ ] Set expectations on response time and accuracy
- [ ] Demonstrate how to ask for reports, tasks, information

## 7.2 Ongoing Support Model
- Monthly health review (server, costs, agent performance)
- Quarterly capability review (what to add next)
- Incident response (if agent breaks or server issues)
- Version upgrades (OpenClaw updates, model upgrades)

## 7.3 Growth Path
```
Single Agent → Multi-Agent → Department-Aligned Team → Autonomous Operations
```
Most clients start at single agent. Expansion is driven by:
- Volume of work exceeding one agent's context window
- Need for specialisation (different models for different tasks)
- Multiple humans needing different interaction styles
- Desire for 24/7 autonomous operations

---

# Implementation Checklist (Copy per Client)

```
Client: _______________
Start date: ___________
Primary contact: ______

PHASE 1 — Server Setup
[ ] VPS provisioned (size: ___)
[ ] Non-root user created
[ ] SSH hardened
[ ] Firewall configured
[ ] OpenClaw installed
[ ] systemd service running
[ ] API keys configured
[ ] Channel connected
[ ] First message received

PHASE 2 — Identity & Memory
[ ] SOUL.md written (<1KB, includes anti-echo-chamber)
[ ] USER.md written
[ ] IDENTITY.md set
[ ] AGENTS.md configured (<3KB, includes Search-First protocol)
[ ] vault/ directory created with domain subdirectories
[ ] Business knowledge seeded into vault/ files (NOT MEMORY.md)
[ ] MEMORY.md written as pointer index (<3KB, links to vault/)
[ ] QMD installed (unzip → bun → @tobilu/qmd)
[ ] QMD configured (searchMode: "search", extraPaths: ["vault"])
[ ] Gateway restarted, memory_search tested

PHASE 3 — Monitoring
[ ] Health script deployed
[ ] Health cron active
[ ] HEARTBEAT.md configured
[ ] Backup script running
[ ] Session monitoring active

PHASE 4 — Core Capabilities
[ ] Browser automation (if needed)
[ ] Web search configured
[ ] Core cron jobs running
[ ] Mission Control (if applicable)

PHASE 5 — Sector Module
[ ] Sector playbook applied: ___________
[ ] Sector-specific skills installed
[ ] Sector cron jobs configured

PHASE 6 — Custom
[ ] Custom skills: ___________
[ ] Custom integrations: ___________
[ ] Custom dashboards: ___________

PHASE 7 — Handoff
[ ] Client trained
[ ] Support model agreed
[ ] First monthly review scheduled
```

---

# Lessons Learned (Update This as We Go)

## From Kilmurry Lodge (Client #1, Mar 2026)
- **4GB RAM is not enough** if browser automation is active. Budget 8GB minimum.
- **tmux is not a process manager.** systemd from day 1, no exceptions.
- **Chrome orphan processes WILL eat all your RAM.** Health script with auto-kill is essential.
- **PM2 crash loops** are usually stale `.next` builds. Clean rebuild fixes it.
- **MEMORY.md quality matters hugely.** Kilmurry's was 16KB of structured gold — but that's too big to inject every message. Seed well, then restructure to vault pointers.
- **Anti-echo-chamber in SOUL.md** is a differentiator. Clients love an agent that pushes back thoughtfully.
- **Never accept credentials in chat.** Not even from the client. Establish secure handoff from day 1.
- **The agent produces value fast** when discovery is thorough. Kilmurry got 20+ deliverables in 2 weeks.
- **QMD install needs unzip + bun first.** Neither are on a fresh Ubuntu. Install unzip as root, bun as service user, then QMD via `bun install -g @tobilu/qmd`.

### INCIDENT: tmux → systemd Migration Failure (30 Mar 2026)
Both Kilmurry and Leamy servers were migrated from tmux to systemd on the same day. Both had issues:

**Leamy (our server):**
1. ExecStart used `openclaw gateway start --foreground` — the `--foreground` flag doesn't exist. Gateway crash-looped for 30 minutes. **Root cause:** Agent wrote the service file without running `openclaw gateway --help` first.
2. Discord token was stored only as an env var in the tmux session (`export DISCORD_BOT_TOKEN=...`). When tmux was killed, the token was lost permanently. Had to regenerate from Discord Developer Portal and create a `.env` file.

**Kilmurry:**
1. Initial config validation errors (`memory.qmd.searchMode` invalid, unrecognized `extraPaths` key) caused **9 crash-loops in 60 seconds** before someone ran `openclaw doctor --fix`.
2. Each crash-loop sent a fresh IDENTIFY to Discord's WebSocket gateway. Likely triggered Discord rate limiting — the bot never reached READY state afterwards despite the token being valid and Discord REST API working fine.

**Standing rules derived from this incident:**
1. Always run `<command> --help` before writing any ExecStart or automation script
2. Audit all `"source": "env"` references in config BEFORE killing the old process
3. Never store secrets only as in-memory env vars — persist to `.env` file
4. Create the `.env` file BEFORE starting systemd — crash-loops from missing secrets can trigger downstream rate limits (Discord, etc.)
5. Test the ExecStart command manually before enabling the service
6. If a working service file already exists on another server, use it as reference — don't hand-write a new one from scratch

## From Leamy Maths (Our Own Deployment)
- **Multi-agent is powerful but complex.** Don't rush clients into it. Single agent first, prove value.
- **Cross-provider fallbacks are essential.** Same-provider rate limits compound.
- **QMD memory backend** eliminates external API dependency — recommend for all clients.
- **Vault architecture is a game-changer.** MEMORY.md went from 13KB → 2KB (86% reduction) with zero information loss. Detail moves to vault/ files, `memory_search` finds it in <50ms. Every client should have this from day 1.
- **Start QMD with BM25 (`search` mode).** Free, no API needed, works great for small-medium vaults. Only upgrade to hybrid (`query` mode) when vault grows large or client needs semantic matching — and it requires an embedding API key (OpenAI or Gemini).
- **Search-First protocol in AGENTS.md is mandatory.** Without it, the agent guesses instead of checking its notes. Add "call memory_search before answering past-context questions."
- **WooCommerce membership quirk:** post_status must be "wcm-active" not "publish." Document platform quirks per client.
- **Session bloat causes API 529 errors.** Monitor session sizes, alert early.
- **Target <8KB total workspace files** injected per message (SOUL <1KB, AGENTS <3KB, MEMORY <3KB, TOOLS <1KB). Anything bigger belongs in vault/.

---

*This playbook is the foundation. Every sector module and client customisation builds on top of it. Update the lessons learned section after every client engagement.*
