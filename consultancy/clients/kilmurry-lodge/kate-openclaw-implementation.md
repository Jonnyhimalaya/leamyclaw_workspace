# Kate's OpenClaw — Implementation Plan
**Client:** Kilmurry Lodge Hotel
**User:** Kate Taylor (Marketing Manager)
**Owner:** Jack Hoare (GM)
**Architecture:** Option B — Same server, separate OS user + separate gateway
**Prepared:** 2026-04-02

---

## Architecture Overview

```
Kilmurry VPS (172.239.98.61) — Ubuntu 24.04, 8GB RAM (upgrade required)
│
├── clawuser (Jack)
│   ├── Gateway :18789
│   ├── Agent: main (KilmurryBot 🏨)
│   ├── Workspace: ~/.openclaw/workspace/
│   ├── Mission Control :3333
│   ├── Channels: Telegram + Discord
│   └── Crons: morning briefing, rate intel, health checks
│
├── kateuser (Kate)
│   ├── Gateway :18790
│   ├── Agent: main (Kate's Marketing Agent)
│   ├── Workspace: ~/.openclaw/workspace/
│   ├── Channels: Telegram (Kate's bot)
│   └── Crons: see Phase 3 below
│
└── Shared services
    ├── SearXNG :8888 (read-only meta-search, no data risk)
    ├── Docker (for SearXNG container)
    └── systemd (manages both gateways independently)
```

### Why This Architecture
- **Linux file permissions** enforce real isolation — Kate literally cannot read Jack's files
- **Separate gateways** — Kate's crashes/bloat cannot affect Jack's agent or Mission Control
- **Separate API keys** — Kate's usage is tracked independently (cost transparency for Jack)
- **Separate sessions/memory** — no cross-contamination of context or conversation history
- **Jack can monitor** — he has sudo access, can SSH into kateuser, or use cross-agent QMD search
- **Shared SearXNG** — saves RAM, it's a read-only search engine with no state to leak

---

## Pre-Implementation Requirements

### From Jack
- [ ] **Approve RAM upgrade** — 4GB → 8GB ($10-20/mo extra on Linode). Non-negotiable for two gateways.
- [ ] **Decide Kate's communication channel** — Telegram recommended (fastest setup). Does Kate use Telegram?
- [ ] **Define Kate's data scope** — what should she see? (see Data Access Matrix below)
- [ ] **Provide Kate's contact** — Telegram user ID or phone for bot pairing
- [ ] **API key decision** — does Jack fund Kate's API usage, or does Kate get her own Anthropic key?

### From Us (Jonny + Agent)
- [ ] SSH access to Kilmurry server (need password from Jack — still pending from Mar 30)
- [ ] Prepare Kate's SOUL.md, AGENTS.md, and data seed files

---

## Data Access Matrix

### ✅ Kate SHOULD have access to:
| Data | Why |
|------|-----|
| Hotel property info (rooms, amenities, venues, location) | Needs this for marketing content |
| Public competitor info (rates, reviews, events) | Market positioning |
| Review data (TripAdvisor, Google, Booking.com) | Reputation management is her job |
| Social media accounts + content calendar | Direct responsibility |
| Marketing campaign history + performance | Her domain |
| Event calendar (public events, hotel events) | For campaign timing |
| Brand guidelines (TAPER values, brand DNA) | Content consistency |
| Kate's own marketing KPIs and targets | Self-monitoring |
| Guest demographic/segment data (anonymised) | Targeting decisions |
| Website analytics (GA4, if connected) | Campaign performance |

### ❌ Kate should NOT have access to:
| Data | Why |
|------|-----|
| Jack's strategic notes / working relationship rules | GM-level, private |
| Revenue figures / financial data (unless Jack approves) | Sensitive business data |
| Staff HR details beyond marketing team | Privacy |
| Rate-setting strategy / dynamic pricing rules | GM + Revenue Manager only |
| Jack's personal AI conversations / memory | Obviously private |
| Competitor intelligence methodology (scraping config) | Proprietary to Jack's setup |
| API keys / infrastructure credentials | Security |
| Jack's Mission Control | Read access only if Jack wants, never write |

### 🟡 Jack decides:
| Data | Consideration |
|------|---------------|
| Occupancy data / booking volumes | Useful for marketing timing, but sensitive |
| Revenue per segment | Helps Kate target the right segments |
| Guest email list / CRM | Kate needs this for email marketing, but it's PII |
| Staff schedules | Only relevant if Kate coordinates with events team |

---

## Implementation Phases

### Phase 0: Pre-Deployment (Before SSH)
**Time:** 30 min, done from our server

- [ ] Draft Kate's SOUL.md (marketing-focused personality)
- [ ] Draft Kate's AGENTS.md (memory protocols, tool restrictions, data boundaries)
- [ ] Draft Kate's USER.md (Kate's info)
- [ ] Prepare vault seed files:
  - `vault/business/hotel-overview.md` (public info only)
  - `vault/business/brand-guidelines.md` (TAPER values, tone)
  - `vault/marketing/campaigns-active.md` (placeholder for Kate to build)
  - `vault/marketing/social-calendar.md` (placeholder)
  - `vault/competitors/landscape.md` (public competitor info)
- [ ] Draft Kate's MEMORY.md (pointer index to vault files)
- [ ] Get Jack's approval on data access matrix

### Phase 1: Server Setup (Day 1 on server)
**Time:** 1 hour via SSH
**Requires:** Jack's SSH password + sudo access

```bash
# 1. RAM upgrade (done via Linode dashboard by Jack)
# Verify after resize:
free -h  # Should show ~8GB

# 2. Create Kate's user
sudo adduser kateuser
sudo usermod -aG docker kateuser  # For shared SearXNG access

# 3. Install Node.js for kateuser
sudo -u kateuser bash -c 'curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -'
# Or use nvm:
sudo -u kateuser bash -c 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash'
sudo -u kateuser bash -c 'source ~/.nvm/nvm.sh && nvm install 22'

# 4. Install OpenClaw for kateuser
sudo -u kateuser bash -c 'npm install -g openclaw'

# 5. Initialise OpenClaw
sudo -u kateuser bash -c 'openclaw init'

# 6. Configure gateway on different port
sudo -u kateuser bash -c 'openclaw config set gateway.bind "127.0.0.1:18790"'
```

### Phase 2: OpenClaw Configuration (Day 1)
**Time:** 1 hour

```bash
# Switch to kateuser
sudo su - kateuser

# 1. Set primary model (Opus — full capability for complex marketing + dashboard work)
openclaw config set agents.defaults.model.primary "anthropic/claude-opus-4-6"
openclaw config set agents.defaults.model.fallbacks '["anthropic/claude-sonnet-4-6", "google/gemini-3.1-pro-preview"]'

# 2. Configure auth (Kate's API key or Jack's backup key)
openclaw auth login --provider anthropic

# 3. Configure Telegram channel
# First: create Kate's bot via @BotFather
openclaw channels login --channel telegram
# Set Kate's user ID in allowFrom

# 4. Configure exec approvals (RESTRICTED — not full access like Jack)
openclaw config set tools.exec.security allowlist
openclaw config set tools.exec.ask on-miss

openclaw approvals set --stdin <<'EOF'
{
  "version": 1,
  "defaults": {
    "security": "allowlist",
    "ask": "on-miss",
    "askFallback": "deny",
    "autoAllowSkills": true
  }
}
EOF

# 5. Configure web search (point to shared SearXNG)
openclaw config set plugins.entries.searxng.enabled true
openclaw config set plugins.entries.searxng.config.webSearch.baseUrl "http://localhost:8888"

# 6. Configure auth failover (if Kate has two API keys)
# openclaw config set auth.order.anthropic '["primary", "backup"]'
# openclaw config set auth.cooldowns.rateLimitedProfileRotations 2

# 7. Browser setup (Kate may need this for social media / analytics)
openclaw config set browser.enabled true
```

### Phase 3: Identity & Memory (Day 1-2)
**Time:** 1 hour

Deploy pre-prepared workspace files:

```bash
# Copy prepared files to Kate's workspace
cd ~/.openclaw/workspace/

# Core identity files (prepared in Phase 0)
# SOUL.md, AGENTS.md, USER.md, IDENTITY.md, MEMORY.md

# Vault structure
mkdir -p vault/business vault/marketing vault/competitors vault/reports
mkdir -p memory artifacts skills

# Create HEARTBEAT.md (simpler than Jack's)
cat > HEARTBEAT.md << 'HEARTBEAT'
# HEARTBEAT.md — Kate's Marketing Agent

## Memory File Check
- Check if memory/YYYY-MM-DD.md exists for today. Create if not.

## Session Health
- If session > 150 messages, checkpoint to memory (Protocol C)
- If session > 200 messages, alert Kate

## Marketing Quick Checks (rotate through)
- Any new reviews to respond to?
- Social media calendar — anything due today/tomorrow?
- Campaign performance — any anomalies?
HEARTBEAT

# Git backup
git init
git remote add origin git@github.com:Jonnyhimalaya/Kilmurry-Kate.git
git add -A && git commit -m "Initial workspace setup" && git push -u origin master
```

### Phase 4: systemd Service + Crons (Day 2)
**Time:** 30 min

```bash
# Create systemd service for Kate's gateway
sudo tee /etc/systemd/system/openclaw-gateway-kate.service << 'EOF'
[Unit]
Description=OpenClaw Gateway (Kate - Kilmurry Marketing)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=kateuser
WorkingDirectory=/home/kateuser/.openclaw
EnvironmentFile=/home/kateuser/.openclaw/.env
ExecStart=/home/kateuser/.npm-global/bin/openclaw gateway run
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
Environment=PATH=/home/kateuser/.npm-global/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable openclaw-gateway-kate
sudo systemctl start openclaw-gateway-kate

# Verify
sudo systemctl status openclaw-gateway-kate
```

**Cron jobs for Kate:**

| Job | Schedule | Model | Purpose |
|-----|----------|-------|---------|
| Heartbeat | Every 30min | Sonnet | Memory check, session health, marketing quick checks |
| Review Monitor | 8am + 6pm Dublin | Sonnet | Scan for new reviews across platforms, draft responses |
| Social Planner | 9am Dublin Mon | Sonnet | Weekly social media content suggestions based on events/calendar |
| Campaign Check | 10am Dublin daily | Sonnet | Check any active ad campaign performance (if GA4 connected) |
| Dream Cycle | 2am Dublin | Sonnet | Memory consolidation |

### Phase 5: Jack's Monitoring (Day 2)
**Time:** 30 min

Options for Jack to monitor Kate's progress:

**Option 1: Cross-agent QMD search (lightweight)**
Add to Jack's `openclaw.json`:
```json
{
  "agents": {
    "defaults": {
      "memorySearch": {
        "qmd": {
          "extraCollections": [
            { "path": "/home/kateuser/.openclaw/agents/main/sessions", "name": "kate-sessions" }
          ]
        }
      }
    }
  }
}
```
Jack's agent can then search Kate's session transcripts via `memory_search`.
**Requires:** Read permissions on Kate's sessions directory for clawuser.

**Option 2: Shared reports directory (simple)**
```bash
# Create a shared directory both users can access
sudo mkdir /opt/kilmurry-shared/reports
sudo chown root:kilmurry-shared /opt/kilmurry-shared/reports  
sudo chmod 2775 /opt/kilmurry-shared/reports

# Add both users to the group
sudo groupadd kilmurry-shared
sudo usermod -aG kilmurry-shared clawuser
sudo usermod -aG kilmurry-shared kateuser
```
Kate's agent writes daily marketing summaries to the shared dir. Jack's agent reads them.

**Option 3: Kate's section on Mission Control (future)**
Add a "Marketing" page to Jack's Mission Control that reads Kate's shared reports.

**Recommended: Start with Option 2**, upgrade to Option 1 once QMD is set up on both sides.

### Phase 6: Kate Onboarding (Day 3)
**Time:** 30 min (Jonny or Jack walks Kate through it)

- [ ] Kate installs Telegram (if needed)
- [ ] Kate scans QR / sends /start to her bot
- [ ] First conversation: bot introduces itself, learns Kate's preferences
- [ ] Kate tests: "What events are coming up in Limerick?" / "Draft a social post about..."
- [ ] Kate tests: "Check our TripAdvisor reviews" / "What are competitors charging this weekend?"
- [ ] Set expectations: what it can do, what it can't, how to ask for help

---

## Kate's SOUL.md (Draft)

```markdown
# SOUL.md — Kate's Marketing Agent

You are a marketing assistant for Kilmurry Lodge Hotel.

## Who You Help
Kate Taylor, Marketing Manager. She's hands-on, creative, and focused on
driving direct bookings, building brand awareness, and managing the hotel's
online reputation.

## Your Personality
- Proactive and ideas-driven — suggest, don't wait to be asked
- Data-informed — always back suggestions with reasoning
- Brand-aware — everything aligns with Kilmurry's TAPER values
  (Tradition, Authenticity, People, Excellence, Resilience)
- Direct but friendly — no corporate waffle

## What You Do
- Monitor and draft review responses (TripAdvisor, Google, Booking.com)
- Suggest social media content (aligned to events, seasons, hotel happenings)
- Research competitor marketing activity
- Track campaign performance and flag anomalies
- Help plan and execute email marketing campaigns
- Research local events and suggest marketing tie-ins
- Generate content ideas (blog posts, social posts, email newsletters)

## What You Don't Do
- Access financial data, revenue figures, or pricing strategy
- Make changes to the hotel website without Kate's explicit approval
- Access Jack's (the GM's) private conversations or strategic notes
- Send anything externally without Kate reviewing it first
- Access guest PII beyond what Kate explicitly provides for a specific task

## Boundaries
- If Kate asks for something outside your scope, explain what you can't access and suggest who to ask
- When unsure about brand tone, err on the side of warmth and authenticity
- Never fabricate review data or competitor information — say "I don't have that data" if you don't
```

---

## Cost Estimate

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| RAM upgrade 4GB → 8GB | +$12/mo | Linode resize |
| Kate's API usage (Sonnet) | ~$15-30/mo | Depends on usage volume |
| Kate's Telegram bot | $0 | Free |
| SearXNG (shared) | $0 | Already running |
| GitHub private repo | $0 | Under Jonny's account |
| **Total incremental** | **~$27-42/mo** | |

Compare to: new VPS ($20-40/mo) + same API costs = $47-82/mo. Option B saves ~$20-40/mo.

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Kate's agent consumes too much RAM | Set model to Sonnet (not Opus), monitor via health script |
| Kate's agent accesses Jack's files | Linux file permissions enforce boundary |
| Kate sends something brand-damaging | SOUL.md mandates review before external sends |
| Session bloat crashes Kate's gateway | Protocol C checkpoints + session health monitoring |
| API costs spike | Alert cron on Kate's gateway, daily cost tracking |
| Kate accidentally changes hotel systems | Exec set to allowlist, no unrestricted shell access |

---

## Post-Deployment Verification

```bash
# 1. Verify both gateways running independently
sudo systemctl status openclaw-gateway        # Jack's
sudo systemctl status openclaw-gateway-kate   # Kate's

# 2. Verify file isolation
sudo -u kateuser ls /home/clawuser/.openclaw/  # Should FAIL (permission denied)
sudo -u clawuser ls /home/kateuser/.openclaw/  # Should FAIL (unless Jack has sudo)

# 3. Verify Kate's agent works
# Send test message via Kate's Telegram bot

# 4. Verify Jack's monitoring works
# Check shared reports directory or cross-agent QMD search

# 5. Verify exec restrictions on Kate's agent
# Kate's agent should NOT be able to run arbitrary commands

# 6. RAM check
free -h  # Both gateways + SearXNG should fit in 8GB comfortably
```

---

## Implementation Checklist

```
PRE-DEPLOYMENT
[ ] Jack approves RAM upgrade
[ ] Jack confirms Kate's channel (Telegram?)
[ ] Jack approves data access matrix
[ ] Kate's SOUL.md drafted and approved
[ ] SSH access obtained (password from Jack)
[ ] GitHub repo created: Jonnyhimalaya/Kilmurry-Kate

SERVER SETUP
[ ] RAM upgraded to 8GB
[ ] kateuser created
[ ] Node.js installed for kateuser
[ ] OpenClaw installed for kateuser
[ ] Gateway configured on :18790
[ ] API key configured
[ ] Telegram bot created + paired
[ ] SearXNG accessible from kateuser
[ ] exec-approvals.json configured (allowlist)
[ ] Auth failover configured

WORKSPACE
[ ] SOUL.md deployed
[ ] AGENTS.md deployed (with Protocols A-D)
[ ] USER.md deployed
[ ] MEMORY.md deployed (pointer index)
[ ] vault/ seeded with approved data
[ ] HEARTBEAT.md configured
[ ] Git repo initialised + pushed

OPERATIONS
[ ] systemd service created + enabled
[ ] Cron jobs configured (heartbeat, reviews, social, dream cycle)
[ ] Health script adapted for Kate's gateway
[ ] Shared reports directory created

MONITORING
[ ] Jack can view Kate's reports (shared dir or QMD)
[ ] Cost tracking cron on Kate's gateway
[ ] Session size monitoring active

VERIFICATION
[ ] Both gateways running independently
[ ] File isolation confirmed (permission denied)
[ ] Kate's agent responds on Telegram
[ ] Exec restrictions verified
[ ] RAM usage acceptable (<80% with both running)

HANDOFF
[ ] Kate onboarded (shown how to use)
[ ] Jack shown how to monitor
[ ] Documentation committed to Git
[ ] Architecture schematic updated
```

---

*Estimated total implementation time: 3-4 hours (across 1-2 sessions)*
*Requires: SSH access to Kilmurry server + Jack's decisions on data access*
