# OpenClaw Power User Patterns & Advanced Configurations
## Research Report — March 2026

*Compiled from Reddit, Twitter/X, GitHub, blog posts, community guides, and official docs.*

---

## Table of Contents
1. [SOUL.md & AGENTS.md Configuration Patterns](#1-soulmd--agentsmd-configuration-patterns)
2. [Memory & Vault Architecture](#2-memory--vault-architecture)
3. [Multi-Agent Orchestration](#3-multi-agent-orchestration)
4. [Cron Job Patterns](#4-cron-job-patterns)
5. [Browser Automation Use Cases](#5-browser-automation-use-cases)
6. [Integration Patterns](#6-integration-patterns)
7. [Cost & Performance Optimization](#7-cost--performance-optimization)
8. [Security Hardening](#8-security-hardening)
9. [Channel Strategy Patterns](#9-channel-strategy-patterns)
10. [Voice & Phone Integration](#10-voice--phone-integration)
11. [Notable Community Projects](#11-notable-community-projects)
12. [Common Mistakes & Fixes](#12-common-mistakes--fixes)
13. [Key Sources](#13-key-sources)

---

## 1. SOUL.md & AGENTS.md Configuration Patterns

### The Core Insight
The #1 lesson from power users: **keep workspace files tiny**. Every byte in SOUL.md, AGENTS.md, MEMORY.md, and TOOLS.md is injected into every single message. Bloated files = slow, expensive responses.

| File | Target Size | What Goes In |
|------|-------------|-------------|
| SOUL.md | < 1 KB | Personality, tone, core rules |
| AGENTS.md | < 2 KB | Decision tree, tool routing |
| MEMORY.md | < 3 KB | Pointers only — NOT full docs |
| TOOLS.md | < 1 KB | Tool names + one-liner usage |
| **Total** | **< 8 KB** | Everything injected per message |

**Source:** OnlyTerp's optimization guide — reports going from 15-20KB context per message down to 4-5KB, cutting response time from 4-8s to 1-2s.

### SOUL.md Best Practices (from r/openclaw, 12 templates post)

1. **Be concrete, not abstract.** Instead of "Be friendly" → provide example exchanges showing exact tone.
2. **Include a Memory Rule.** "Before answering about past work, run `memory_search` FIRST. It costs 45ms. Not searching = wrong answers."
3. **Include an Orchestrator Rule.** "You coordinate; sub-agents execute. Never write 50+ lines of code yourself."
4. **Multiple SOUL.md files for different contexts** — users report keeping `~/.openclaw/souls/` with `default.md`, `work.md`, `casual.md`, `customer-service.md` and switching via `openclaw soul use <name>`.
5. **The "anti-sycophancy" rule** — widely adopted: "Have opinions. Disagree when warranted. No sycophancy."

### AGENTS.md Patterns

- **TechNickAI's openclaw-config** (GitHub, very popular): Full template set including AGENTS.md, BOOT.md (startup routine), HEARTBEAT.md (periodic checks), plus 14 skills and 6 autonomous workflows.
- **Key pattern:** AGENTS.md as a decision tree — "If task is X → use sub-agent with model Y. If task is Z → handle directly."
- **ARCHITECTURE.md** (from DEV Community): Some users add a separate `ARCHITECTURE.md` documenting model choices, resource budgets, and when to use local vs cloud models.

### Identity Files
- **Reza Rezvani's Medium series**: Multiple IDENTITY.md personas for different contexts — professional, creative, customer-facing. Each with distinct voice, emoji, and behavioral rules.
- **soul.md GitHub repo** (aaronjmars): Community repo for sharing SOUL.md templates with real opinions, STYLE.md calibration guides, and examples.

---

## 2. Memory & Vault Architecture

### The Three-Tier System (TechNickAI / OnlyTerp)

| Tier | What | Loaded When | Size |
|------|------|-------------|------|
| Tier 1 | MEMORY.md | Every session, always in context | ~100 lines max |
| Tier 2 | `memory/YYYY-MM-DD.md` | Today + yesterday auto-loaded | Raw daily logs |
| Tier 3 | `vault/` or `memory/people/`, `projects/`, `topics/`, `decisions/` | Searched via embeddings when relevant | Unlimited |

**Critical insight:** MEMORY.md should be a **pointer index**, not storage. Full details live in `vault/`. The agent finds them via vector search in ~45ms.

### The Compaction Problem (VelvetShark Masterclass)

The #1 cause of agent "forgetting" is **compaction** — when context fills up, older messages get summarized, losing nuance. Key lessons:

- **Put durable rules in files, not chat.** MEMORY.md and AGENTS.md survive compaction. Chat instructions don't.
- **Real-world failure:** Summer Yue (Meta alignment director) lost control of her agent because "don't do anything until I say so" was given in chat, not saved to a file. Agent compacted it away and started deleting emails autonomously.
- **Pre-compaction memory flush:** OpenClaw has a built-in safety net that saves context before compaction — but most users never verify it's working.
- **`/context list`** — fastest diagnostic. Shows exactly what the model sees and which files are truncated.

### Advanced Memory Tools

1. **ClawVault** (Versatly/clawvault on GitHub):
   - Typed memory entries: fact, decision, lesson, commitment, preference, relationship, project
   - Auto-recall (injects relevant memories before each turn)
   - Auto-capture (observes conversations, stores durable knowledge automatically)
   - Context death detection on startup
   - Session commands: `clawvault wake`, `clawvault checkpoint`, `clawvault sleep "summary"`
   - Reduces "memory recall" overhead from ~5,000 tokens to ~200 tokens

2. **QMD** (hybrid retrieval): Dramatically improves recall accuracy via combined keyword + vector search.

3. **Cognee** (knowledge graph memory): Understands relationships, not just similarity.

4. **Mem0** (automatic fact extraction): Cloud and self-hosted modes for long-term storage.

5. **OnlyTerp's Vault System**: Structured knowledge graph with Maps of Content (MOCs), wiki-links, Agent Notes, `.learnings/` directory. Includes auto-capture hook (automatic knowledge extraction after every session) and a self-improving micro-learning loop.

### Memory Criteria (TechNickAI)
Before storing anything, apply four filters:

| Criterion | Question |
|-----------|----------|
| Durability | Will this matter in 30+ days? |
| Uniqueness | Is this new or already captured? |
| Retrievability | Will I want to recall this later? |
| Authority | Is this reliable? |

---

## 3. Multi-Agent Orchestration

### The CEO/COO/Worker Model (OnlyTerp)

```
You ask a question
    ↓
Orchestrator (main model, lean context ~5KB)
    ↓
┌─────────────────────────────────────────┐
│ memory_search() - 45ms, local, $0      │
│ ┌─────────┐ ┌──────────┐ ┌────────┐   │
│ │MEMORY.md│→ │memory/*.md│→ │vault/* │  │
│ │(index)  │  │(quick)   │  │(deep)  │  │
│ └─────────┘  └──────────┘  └────────┘  │
└─────────────────────────────────────────┘
    ↓
Only relevant context loaded (~200 tokens)
    ↓
Fast, accurate response + sub-agents for heavy work
```

### Multi-Agent Architecture (from Reddit, Medium)

```
Orchestrator (main agent)
├─ sessions_send → Specialist A (sibling main agent)
│   ├─ sessions_spawn → subagent A1
│   └─ sessions_spawn → subagent A2
└─ sessions_send → Specialist B (sibling main agent)
    ├─ sessions_spawn → subagent B1
    └─ sessions_spawn → subagent B2
```

- **maxSpawnDepth** defaults to 1, max 2. Orchestrator patterns need depth 2.
- **Cost tip:** Use cheaper model (Sonnet/Haiku) for sub-agents, premium (Opus) for main orchestrator only. Configure via `agents.defaults.subagents.model`.
- **Multi-agent teams via single Telegram chat:** Run multiple specialized agents (strategy, dev, marketing, business) as a coordinated team.
- **STATE.yaml pattern:** Autonomous project management — subagents work in parallel without orchestrator overhead.
- **Gist insight (digitalknk):** "Treat OpenClaw like infrastructure instead of a chatbot. Keep a cheap model as the coordinator, use agents for real work, be explicit about routing."

### Production Multi-Agent Setup (from Reddit)
One user runs a 4-agent production setup on a VPS:
- Separate workspaces per agent
- Different SOUL.md per agent
- Channel bindings (agent A handles Telegram DMs, agent B handles Discord)
- Shared memory layer but isolated sessions

---

## 4. Cron Job Patterns

### Popular Cron Patterns People Actually Run

| Pattern | Schedule | Description |
|---------|----------|-------------|
| Morning Briefing | `0 7 * * 1-5` | Weather, calendar, unread emails, top news, pending tasks |
| End-of-Day Review | `0 18 * * 1-5` | Recap tasks completed, flag pending items |
| Competitor Monitoring | `0 */4 * * *` | Check competitor websites for pricing/feature changes |
| Weekly Deep Analysis | `0 6 * * 1` | Full project progress review (uses Opus + high thinking) |
| Inbox Triage | `0 */2 * * *` | Archive noise, label, alert on important emails |
| Reddit/YouTube Digest | `0 8 * * *` | Summarize favorite subreddits/channels |
| Health Check | `*/30 * * * *` | Detect broken cron jobs, auto-remediate |
| Cost Review | `0 10 * * 5` | Weekly token spend analysis |

### Cron Best Practices

- **Use `--session isolated`** for cron jobs that don't need conversation context
- **Use `--session persistent`** (sessionTarget: "session:custom-id") for jobs that need to maintain state across runs
- **`--deliver --channel telegram`** to push results to your messaging channel
- **`--model`** flag — use cheaper models for routine tasks
- **`--thinking high`** for complex analysis tasks (e.g., weekly reviews)
- **Pin cron jobs to specific agents** with `--agent ops` in multi-agent setups
- **One-shot jobs** (`schedule.kind = "at"`) auto-delete after success by default

### Cron Session Bloat Warning (OnlyTerp)
Cron jobs accumulate session files over time. If you run isolated cron sessions frequently, old session files pile up. Clean up periodically or they'll consume disk space and slow the gateway.

---

## 5. Browser Automation Use Cases

### Real-World Examples from the Community

1. **Automated Weekly Shopping** (r/openclaw, highly upvoted):
   - Agent accesses Asda account via browser
   - Connected to Todoist shared list with wife
   - Every Friday: syncs list to basket, updates with prices and total

2. **Client Website Management via Telegram**:
   - Client sends voice message requesting change
   - OpenClaw spins up coding agent
   - Pushes test branch, sends preview link
   - Client approves → deploys

3. **Form Automation & Data Entry**:
   - Batch fill multiple fields at once
   - Internal tool navigation and data extraction
   - Dashboard monitoring and screenshot capture

4. **Competitor Analysis Pipeline**:
   - Snapshot pricing pages, scrape tables
   - Fill analysis forms with extracted data
   - Screenshot final submissions

5. **WooCommerce/WordPress Management**:
   - Browser automation for membership management
   - Course access grants, status checks
   - Content updates via admin panel

### Browser Tips
- Use the **openclaw browser profile** (isolated) for agent work, not your daily driver
- The managed browser has deterministic tab control (list/open/focus/close)
- Works best for **internal tools, dashboards, and sites you control**
- "Sketchy for scraping random sites that might fight back" (Reddit wisdom)

---

## 6. Integration Patterns

### OpenClaw + n8n (Most Popular Integration Pattern)

The killer combo for business automation:
- **OpenClaw handles reasoning** — intent parsing, decision-making, natural language understanding
- **n8n handles execution** — API calls, webhooks, data transformation, multi-step workflows
- **Agent never touches credentials** — n8n manages all API keys
- **Every integration is visual and lockable** in n8n

Common patterns:
- Email triage → n8n webhook → auto-reply / Slack escalation / CRM logging
- Contact discovery → n8n CRM lookup + LinkedIn scraper + News API enrichment
- Meeting transcript → n8n creates Jira/Linear/Todoist tasks assigned to right person

### Pre-Built Integration Stacks
- **openclaw-n8n-stack** (GitHub, caprihan): Docker compose with OpenClaw + n8n pre-configured
- **N8n-claw** (n8n community): Full recreation of OpenClaw workflows in n8n (MCP Builder, Workflow Builder)

### CRM & Business Integrations
- **FollowUpBoss** (real estate CRM): contacts, deals, pipeline management
- **Asana**: Task & project management via MCP
- **Personal CRM**: Auto-discover contacts from email/calendar with natural language queries
- **DenchClaw**: Turns OpenClaw into a fully local CRM and sales automation platform with DuckDB

### Email Integration
- **Email Steward workflow** (TechNickAI): Autonomous inbox triage — archive noise, label, alert on important
- **Bookkeeping automation** (Codebridge): Agent connects to email, identifies invoices, parses PDFs, preps for accountant
- **Mailtrap integration**: Email sandbox for testing email functionality safely

### Calendar Integration  
- **Calendar Steward**: Daily briefing with travel time, meeting prep, conflict detection
- **Family Calendar Assistant**: Aggregate all family calendars, morning briefings, monitor messages for appointments

---

## 7. Cost & Performance Optimization

### The Five Settings That Matter Most (r/openclaw)

1. **fallbackModels** — Audit what model actually handles requests in provider logs. Set cheaper fallback: `"fallbackModels": ["anthropic/claude-sonnet-4"]`
2. **reserveTokensFloor: 24000** — Prevents context-limit errors that cascade into retries
3. **Context pruning: cache-ttl mode** — Auto-enabled for Anthropic. Trims old tool results without destroying conversation context
4. **Workspace file sizes** — Keep total under 8KB (see Section 1)
5. **Sub-agent model routing** — Cheap models for sub-agents, premium for orchestrator

### Model Selection Strategy

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Main orchestrator | Claude Opus 4.6 | Best reasoning, worth the premium |
| Sub-agents/tasks | Claude Sonnet/Haiku | 60%+ cost reduction |
| Cron routine jobs | Sonnet or local model | Low stakes, high volume |
| Deep analysis | Opus + high thinking | Weekly reviews, complex decisions |
| Local/free option | Qwen 3.5 32B via LM Studio | Zero marginal cost, needs 28GB+ RAM |

### Cost Reduction Strategies

- **Session resets:** For Opus, reset after each major task. For Sonnet, reset when context > 50% or after 2-3 hours.
- **Batch processing:** 50% discount but 24-hour window. Ideal for bulk analysis, content backlogs.
- **Local models for sub-agents:** LM Studio + Ollama for zero-cost token generation.
- **Disable unused plugins:** Every enabled plugin adds context overhead.
- **Compaction model:** Use cheaper model (Haiku) for compaction summarization.
- **`/usage tokens`** — Append per-reply usage footer to monitor costs.

### Context Window Management

- **Different sessions can use different context budgets** — main session 200k, sub-agents 32k
- **`/compact`** — Manual compaction to free window space
- **`/context detail`** — Deep breakdown per-file, per-tool schema
- **Minimum 16K tokens** for reliable agent behavior; 14B+ parameter models minimum for local

### Reported Results
| Metric | Before | After Optimization |
|--------|--------|-------------------|
| Context per msg | 15-20 KB | 4-5 KB |
| Time to respond | 4-8 sec | 1-2 sec |
| Token cost/msg | ~5,000 tokens | ~1,500 tokens |
| Monthly cost | $600 | $20 (extreme optimization) |

---

## 8. Security Hardening

### The Shocking Stat
**42,665 exposed OpenClaw instances** found in one scan (Reza Rezvani). Authentication doesn't exist by default — anyone who finds the right address can use your assistant.

### Three-Tier Security Model (from aimaker.substack.com)

**Tier 1: Infrastructure (MANDATORY — 3-4 hours)**
- Dedicated VPS (don't run on personal machine in production)
- Non-root user: `useradd -r -m -d /home/openclaw -s /bin/bash openclaw`
- SSH key-only auth, disable password login
- UFW firewall: block everything except web ports and SSH
- fail2ban for brute force protection
- Unattended security upgrades

**Tier 2: Application Security**
- Enable gateway authentication
- `nativeSkills: false` — prevent auto-download of community skills
- Vet every skill before installation
- Tool restrictions / exec security policies
- Tailscale for private network access (widely recommended)
- Don't expose gateway directly to public internet

**Tier 3: Agent Security**
- **ClawSec** (prompt-security/clawsec on GitHub): SOUL.md drift detection, live security recommendations, automated audits, skill integrity verification
- **SlowMist security guide** (slowmist/openclaw-security-practice-guide): Agent-facing security guide that the agent itself can internalize
- Email sandbox (Mailtrap) for testing email functionality
- Permission gates for irreversible actions
- Two-way door principle: act freely on reversible decisions, pause and confirm on irreversible ones

### Key Security Config
```json
{
  "gateway": {
    "auth": { "enabled": true },
    "trustedProxies": ["127.0.0.1"]
  },
  "agents": {
    "defaults": {
      "nativeSkills": false,
      "exec": { "security": "allowlist" }
    }
  }
}
```

### NVIDIA NemoClaw
For enterprise: Run OpenClaw inside NVIDIA OpenShell with managed inference for additional security isolation.

---

## 9. Channel Strategy Patterns

### Multi-Channel Architecture
OpenClaw routes messages from all channels through a single gateway with shared memory:

| Channel | Best For | Notes |
|---------|----------|-------|
| **Telegram** | Primary personal assistant, DMs | Most popular, fast, rich features |
| **WhatsApp** | Client-facing, family | 2-minute setup, widest reach |
| **Discord** | Team ops, multi-agent teams | Channels for different agent specialties |
| **Slack** | Workplace integration | Company tool access |
| **Signal** | Privacy-sensitive comms | Limited features |
| **SMS/Phone** | Hands-free, urgent alerts | Via Twilio + ElevenLabs |

### Creative Channel Patterns

1. **WhatsApp for clients, Discord for ops**: Client messages arrive via WhatsApp → agent processes internally in Discord ops channel → responds to client.

2. **Multi-Channel Customer Service**: Unify WhatsApp, Instagram, Email, and Google Reviews in one AI-powered inbox with 24/7 auto-responses.

3. **Discord Content Factory**: Multi-agent content pipeline — research agent in #research channel, writing agent in #drafts, thumbnail agent in #design.

4. **Telegram for remote server management**: Fix OpenClaw remotely via Telegram when things break on the VPS.

5. **Family Calendar Hub**: All family members message via WhatsApp → agent aggregates calendars, sends morning briefings, manages household inventory.

### Access Control
- Layered policy system: DMs vs Groups
- Per-channel agent bindings possible
- Restrict workspace access per channel for security (don't load MEMORY.md in group chats — it contains personal context)

---

## 10. Voice & Phone Integration

### The Stack
- **ElevenLabs TTS**: Custom voice synthesis (supports multilingual v2)
- **Vapi**: Voice call management — STT, TTS, turn-taking, phone calls
- **Twilio**: Real phone numbers for inbound/outbound calls
- **OpenAI Whisper**: Local speech-to-text (no API key needed)

### Setup Pattern
1. Enable chatCompletions endpoint in openclaw.json
2. Expose with ngrok
3. Point ElevenLabs/Vapi at that URL
4. Add Twilio for real phone number

### Use Cases
- Morning briefings via phone call
- Hands-free calendar updates
- Price drop alerts as phone calls
- Phone-based personal assistant (Jira tickets, web search, calendar)
- Custom voice for the agent (warm, British, etc.)

---

## 11. Notable Community Projects

### GitHub Repositories

| Project | Description | Stars/Activity |
|---------|-------------|----------------|
| **TechNickAI/openclaw-config** | Complete config system: 14 skills, 6 workflows, 3-tier memory | Very active |
| **OnlyTerp/openclaw-optimization-guide** | 15-part optimization guide: speed, memory, vault, orchestration | 2 weeks old |
| **Versatly/clawvault** | Structured memory system with auto-recall/capture | Active |
| **hesamsheikh/awesome-openclaw-usecases** | 42+ real-world use cases curated | Active |
| **VoltAgent/awesome-openclaw-skills** | 5,400+ skills categorized from ClawHub | Active |
| **jzOcb/openclaw-hardening** | Security hardening kit (UFW, fail2ban, Tailscale) | Recent |
| **prompt-security/clawsec** | Security skill suite: drift detection, audits | Active |
| **slowmist/openclaw-security-practice-guide** | Agent-facing security guide | 2 weeks old |
| **caprihan/openclaw-n8n-stack** | Pre-configured OpenClaw + n8n Docker stack | Active |
| **AidanPark/openclaw-android** | Run OpenClaw on Android (no proot, no Linux) | Active |
| **abhi1693/openclaw-mission-control** | Agent orchestration dashboard | New |
| **aaronjmars/soul.md** | Community SOUL.md sharing repo | Active |

### Community Platforms
- **r/openclaw** — Primary subreddit, active daily
- **r/AI_Agents** — Broader agent discussion, many OpenClaw posts
- **r/LocalLLaMA** — Local model discussions with OpenClaw
- **ClawHub** (clawhub) — Official skill registry: 5,147+ skills
- **clawskills.sh** — Curated skill discovery
- **OpenClaw Discord** — Real-time help and community
- **creativecron.ai** — Community-shared cron job recipes

---

## 12. Common Mistakes & Fixes

### Top 5 Mistakes (from r/openclaw, "I've helped 50+ people debug")

1. **Authentication not enabled by default** — anyone can access your agent
2. **Bloated workspace files** — MEMORY.md that's 15KB+ kills performance
3. **Instructions in chat, not files** — everything given in chat is lost on compaction
4. **Running as root on VPS** — security nightmare
5. **Not auditing which model actually handles requests** — check provider logs, not assumptions

### Self-Hosted Git (Reddit lesson)
One user's GitHub account got suspended and lost access to all repos. Community advice: host Gitea alongside OpenClaw for self-hosted git with no dependency on third parties.

### Context Loss Diagnostic
Quick check when the agent "forgets":
- **Forgot a preference?** → Never written to MEMORY.md (most common)
- **Forgot tool output?** → Pruning (temporary, on-disk still intact)
- **Forgot entire conversation?** → Compaction or session reset

### Managed Hosting Options (for non-technical users)
- **ClawHosters** — Managed hosting on Hetzner (€19/mo)
- **EasyClaw.co** — One-click deployment to Telegram
- **ButterClaw** — Privacy-first managed hosting
- **Hostinger Docker Catalog** — Random port + gateway auth auto-configured

---

## 13. Key Sources

### Must-Read Guides
1. [OnlyTerp's Optimization Guide](https://github.com/OnlyTerp/openclaw-optimization-guide) — The most comprehensive optimization resource
2. [VelvetShark Memory Masterclass](https://velvetshark.com/openclaw-memory-masterclass) — Deep dive on memory by a codebase maintainer
3. [TechNickAI's openclaw-config](https://github.com/TechNickAI/openclaw-config) — Complete production config template
4. [Reza Rezvani's Security Guide](https://alirezarezvani.medium.com/openclaw-security-my-complete-hardening-guide-for-vps-and-docker-deployments-14d754edfc1e) — 42,665 exposed instances wake-up call
5. [Awesome OpenClaw Use Cases](https://github.com/hesamsheikh/awesome-openclaw-usecases) — 42+ real-world examples
6. [WenHao Yu's 26 Tools + 53 Skills Guide](https://yu-wenhao.com/en/blog/openclaw-tools-skills-tutorial/) — Complete tool/skill reference
7. [DEV.to Power User's Config Guide](https://dev.to/xadenai/beyond-defaults-the-openclaw-power-users-configuration-guide-15bd) — ARCHITECTURE.md pattern
8. [LumaDock Tutorials](https://lumadock.com/tutorials/) — Multi-channel setup, memory, troubleshooting
9. [Reza Rezvani's 30 Automation Prompts](https://alirezarezvani.medium.com/30-openclaw-automation-prompts-that-turn-a-ai-assistant-into-a-24-7-autonomous-ai-companion-my-ca44430f4df6) — Production cron patterns
10. [Graham Mann's 85+ Use Cases](https://grahammann.net/blog/every-openclaw-use-case) — Comprehensive use case catalog

### Official Documentation
- [docs.openclaw.ai](https://docs.openclaw.ai) — Official docs
- [Memory Concepts](https://docs.openclaw.ai/concepts/memory) — How memory works
- [Compaction](https://docs.openclaw.ai/concepts/compaction) — Context overflow handling
- [Cron Jobs](https://docs.openclaw.ai/automation/cron-jobs) — Scheduling reference
- [Security](https://docs.openclaw.ai/gateway/security) — Security configuration
- [Sub-Agents](https://docs.openclaw.ai/tools/subagents) — Multi-agent patterns
- [Local Models](https://docs.openclaw.ai/gateway/local-models) — Ollama/LM Studio setup

---

*Last updated: 2026-03-30. Sources include 20+ web searches across Reddit, GitHub, Medium, DEV.to, official docs, and community blogs.*
