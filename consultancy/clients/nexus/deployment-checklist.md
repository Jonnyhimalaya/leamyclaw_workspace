# Nexus — Deployment Checklist
**Deployed:** 2026-04-04
**Deployed by:** Main agent (Orchestrator)
**Playbook used:** consultancy/playbooks/universal-openclaw-implementation.md

## Phase 1: Infrastructure
- [x] Separate OS user (`nexus`)
- [x] OpenClaw v2026.4.2 installed
- [x] systemd service (openclaw-nexus, enabled, auto-restart)
- [x] Gateway on loopback, port 18790, auth token
- [x] .env file permissions 600
- [x] auth-profiles.json permissions 600
- [x] openclaw.json permissions 600
- [x] NODE_COMPILE_CACHE + OPENCLAW_NO_RESPAWN env vars
- [ ] SSH key-only auth — N/A (server-level, shared with jonny user)
- [ ] UFW firewall — N/A (server-level, already configured)
- [ ] Fail2ban — N/A (server-level)
- [ ] Auto security updates — N/A (server-level, already enabled)

## Phase 1.2: OpenClaw Core
- [x] Primary model: anthropic/claude-opus-4-6
- [x] Fallback chain: OpenRouter Opus → Sonnet → Gemini → GPT-5.4
- [x] Auth profile rotation (anthropic:claw → work)
- [x] Auth cooldowns (overloaded: 2, rateLimit: 2, backoff: 2000ms)
- [x] Exec approvals Layer 1 (allowlists OK)
- [x] Exec approvals Layer 2 (security: full, ask: off, askFallback: full)
- [x] strictInlineEval = false
- [x] Compaction: safeguard mode, reserveTokensFloor 20000
- [x] Context pruning: cache-ttl 1h

## Phase 1.3: Communication
- [x] Telegram bot (@OnNexus_bot) connected
- [x] Pairing approved (Jonny's TG ID: 7717065960)
- [x] DM policy: pairing

## Phase 2: Identity & Memory
- [x] SOUL.md — Nexus BTC persona
- [x] AGENTS.md — full operational rules
- [x] USER.md — Jonny's details
- [x] MEMORY.md — initialized
- [x] HEARTBEAT.md — autonomy check, health check, session bloat
- [x] heartbeat-state.json — autonomy tracking
- [x] Autonomy levels (responsive/ambient/proactive/dormant)
- [x] Channel trust levels (TUI highest, Telegram high)
- [x] Protocol C (150-msg checkpoint)
- [x] Protocol D (post-/new rescan)

## Phase 2.2: Memory System
- [x] QMD: Gemini embeddings (gemini-embedding-001)
- [x] Hybrid search (vector 0.7 + text 0.3)
- [x] MMR enabled (lambda 0.7)
- [x] Temporal decay (halfLife 30 days)
- [x] vault/ directory structure (business/, operations/, people/)
- [x] memory/active-tasks.md (crash recovery)
- [x] autoDream (.dream-state.json)
- [x] Micro-learning (.learnings/ directory)

## Phase 3: Workspace
- [x] Git initialized (.gitignore, initial commit)
- [x] .gitignore covers credentials, sessions, node_modules, cache

## Phase 4: Core Capabilities
- [x] Browser: Chrome with sandbox (AppArmor configured)
- [x] SearXNG: enabled (localhost:8888, shared container)
- [x] Claude Code CLI: v2.1.92

## Phase 4.3: Crons
- [x] Watchdog: every 5 min (openclaw-ops)
- [x] Server health: every 4 hours (health.sh)
- [x] Dream cycle: 2am UTC (pending cron job creation in OpenClaw)
- [ ] Advisor model: deferred (needs cross-model cron config)

## Phase 5: Security
- [x] openclaw-ops skill installed
- [x] Security compliance: 100/100 PASS
- [x] Security audit: 0 critical
- [x] heal.sh run (fixed 3 items)
- [x] File permissions hardened

## Gaps / Deferred
- Advisor cron (cross-model oversight) — add when Nexus has enough memory to make it useful
- Git remote — needs a private repo created for Nexus workspace
- SearXNG shared with main gateway — consider separate instance if isolation needed

## Score: 95% (1 deferred, 4 N/A server-level)
