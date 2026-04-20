# MEMORY.md - Long-Term Memory (Pointer Index)
# Detail lives in vault/ and memory/topics/. memory_search finds it in <50ms.

## About Jonny
- Stephen (goes by Jonny; @jonnyhimalaya), Limerick, Ireland
- Runs **Leamy Maths** (leamymaths.ie) - online maths education
- Co-founder of a BTC company (Nexus)
- Launching **AI consultancy** - OpenClaw setups for SMEs
- Direct, no-fluff style. Wants me as his marketing guru.
- Professional name on site: **Stephen** (NOT Stephan)

## 🔴 Active Alerts
- GA4 key exposed in git, unrotated → [security items](memory/topics/security-open-items.md)
- ClawHub supply chain risk (12%+ malicious plugins) → [security items](memory/topics/security-open-items.md)
- **OpenClaw v2026.4.14** — both servers upgraded (main VPS + Kilmurry). Fixes Kate's Telegram alerts and CDP issues.
  - ⚠️ Gateway trust-escalation fix (PR #67303) is in a later release (~April 16). Both servers need upgrading past v2026.4.14.
  - Skill safety scanner (`openclaw skill-scan`) still unrun across all 4 instances (main, Nexus, Jack, Kate) — 17+ days overdue as of 2026-04-18.
- Meta token for KilmurryLodge Facebook page unresolved - real page managed by a different account (not Jack's developer account)
- Jack's Google Search Console access pending - needs his Google login (same account as GA4)

## Active Projects
- Leamy Maths → vault/business/leamy-maths.md
- Marketing campaigns → vault/marketing/campaigns-active.md
- Multi-agent team → vault/technical/multi-agent-team.md
- Infrastructure & tools → vault/technical/infrastructure.md
- AI Consultancy → vault/consultancy/overview.md
  - Recommended deployment pattern: Docker standardisation (`ghcr.io/openclaw/openclaw` via docker-compose) instead of manual npm installs.
  - Evaluate **Lobu.ai** (open-source multi-tenant OpenClaw fork) as a scaling architecture.
  - Consultancy deployment checklist should include 4 mandatory security checks: version, skill scan, gateway binding, exec security mode.
  - Semgrep published OpenClaw Security Engineer's Cheat Sheet — good consultancy reference.
  - `localModelLean: true` config option: drops heavyweight tools for budget-tier models (Gemma 4 etc.).
  - Google TTS now bundled natively in Google plugin — opportunity for Kilmurry voice briefings, Leamy audio supplements.
  - Evaluate Coolmanns memory architecture (v6) for multi-layer decay and GPU semantic search.
  - Pitch Gemma 4 (12B, ~7GB RAM) for compliance-heavy client deployments (e.g., Kilmurry hotel data).
  - ACP Harness: Claude Code deployed via ACP harness for Kilmurry (Jack) - routes build work off API billing (uses Claude Max team subscription).
  - MiroFish (swarm prediction engine): moved from main VPS to dedicated Linode London server (172.236.25.67, 16GB RAM, 315GB disk). Docker deployed, gpt-4o model, ports 3000+5001. Auto-restart enabled. Main VPS copy removed (disk freed).
  - MiroFish operational notes: Atlas graph visualisation non-functional on self-hosted (ignore); specify round duration explicitly in prompt; Zep free tier ~300 req/window (enough for sim, tight for report); long-term → upgrade Zep ($25/mo) or switch to MiroFish-Offline (Neo4j local).
- Kilmurry Lodge (Jack) → memory/topics/client-deployments-status.md | port 18789 (clawuser)
- Kilmurry Lodge (Kate Taylor, marketing) → memory/topics/client-deployments-status.md | port 18792 (kateuser), dashboard port 3334
  - TG bot: @Katetaylor123_bot | Kate's TG ID: 8778805348
  - Tailscale IP: 100.111.174.13 (Kate + Jack access MC via this)
  - GitHub push unresolved - kateuser + clawuser lack GitHub auth on Kilmurry server → HTTPS fine-grained token needed
  - Kate MC live data (as of 2026-04-15): GA4 → 5,001 sessions, 3,414 users, 13,869 page views, 34% bounce, 3m 29s avg session; Campaigns → €1,005 ad spend, 2,214 paid sessions, CPC €0.31
- Wednesday meeting items still open: Meta token (different FB account), Jack's Search Console access, email platform
- Nexus (BTC company) → memory/topics/client-deployments-status.md | port 18790 (nexus user), dashboard port 3334
- Revision course tracking → revision-course-2026.json
- Todo list → tasks.md (active) / tasks-completed.md (archive)
- Competitive analysis → leamymaths-competitive-analysis.md

## Topic Files
- [Security Open Items](memory/topics/security-open-items.md)
- [Client Deployments Status](memory/topics/client-deployments-status.md)
- [Server Resources](memory/topics/server-resources.md)
- [Kilmurry MC Catalogue](memory/topics/kilmurry-mc-catalogue.md)
- [MiroFish Research](memory/topics/mirofish-research.md)

## Kilmurry GitHub + Mission Control
- HTTPS auth via single fine-grained token covering: `Kilmurry`, `kilmurry-kate`, `kilmurry-mission-control`
- Kate: repo `kilmurry-kate`, user `kateuser`, path `/home/kateuser/kilmurry-marketing-mc`
- Jack: repo `Kilmurry`, user `clawuser`, MC `/home/clawuser/mission-control`, ws `/home/clawuser/.openclaw/workspace`
- Jack's agent edits MC directly: build → verify → commit → push
- Push failures: check HTTPS token auth + branch divergence first

## Agent Team (Quick Ref)
| ID | Name | Model | Role |
|----|------|-------|------|
| main | 🧠 Orchestrator | gpt-5.4 | Strategy, delegation |
| sitemgr | 🔧 Wrench | sonnet-4-6 | WordPress admin |
| marketing | 📊 Prism | sonnet-4-6 | Analytics, ads |
| scout | 🔍 Radar | grok-3-mini | Research |
| content | 🎨 Pixel | gpt-5.4 | Social, graphics |
| strategist | 🎯 Strategist | gemini-3.1-pro | Morning briefs |

## Key Credentials & Access
- WP admin: leamyclaw@gmail.com (browser login)
- GA4: service account in credentials/ga4-service-account.json (⚠️ needs rotation)
- Google Ads: AW-10776906058
- Meta: business_id 253648777546692 (session expired)
- Kilmurry server: 172.239.98.61 (clawuser, needs password from Jonny)

## Preferences
- "Use initiative. Don't ask for this and that. Research, document, strategise."
- Observations → always add to tasks.md (not leamymaths-todo.md - that's been split)
- Mission Control exists at localhost:3333 - ENHANCE, don't rebuild. "Blocked by Jonny" panel active (shows GA4 rotation, Kilmurry SSH pw, Meta re-login, credits top-up)
- WooCommerce memberships: use the skill, verify wcm-active status
- Delegate repetitive browser work to sitemgr (Wrench/Sonnet) - Opus thinks, Wrench clicks (bulk membership adds on Opus cost €15)
- Memory Resilience: Always follow Protocol C (checkpoint every ~150 msgs) and D (rescan .reset transcripts on /new)
- **Primary model:** GPT-5.4 (decided 2026-04-06 by Jonny - Opus API billing too expensive)
- **Native dreaming** enabled in OpenClaw (memory-core, 3am daily, replaces old autoDream)
- **Active Memory plugin:** Enabled natively as of v2026.4.12 (replaces manual Search-First rule).
- **Anthropic credits:** Claimed 2026-04-11. Still on API billing — Anthropic cost caution remains active.
- **v2026.4.16 model default:** Shifted to Claude Opus 4.7 — verify client Anthropic deployments aren't hitting unexpected cost spikes.
- **Hermes Agent:** Competitor to OpenClaw with built-in learning loop — monitor for feature parity.
- **Codex CLI review pattern:** Community best practice before upgrading OpenClaw — adopt for consultancy.
- **X API price cut (2026-04-20):** Owned reads drop to $0.001/req — opportunity for Scout cost reduction and Kilmurry social monitoring.
- **Main VPS swap:** Persistent ~335MB swap across all health checks 2026-04-19 (16hrs, flatlined) — undiagnosed. Possible slow memory leak or oversized process. Run `smem` or `ps aux --sort=-%mem` to investigate.
- **Local Model Fallback:** Gemma 4 viable via Ollama (Apache 2.0, good tool use) - recommended for consultancy budget tiers and API failovers.
- **Browser automation:** Do NOT use `noSandbox=true` (security risk). CDP issues fixed in v2026.4.14. Watch sessions — Chrome procs accumulate (12 killed 2026-04-18). Disk holding ~60%.
- **CLI capabilities:** `openclaw infer` available (v2026.4.7+) for multimodal inference
- **ClawChief architecture** active: priority-map.md, auto-resolver.md, tasks.md
- Cross-agent shared memory: NOT wanted - isolation is a feature (Jonny's decision, 2026-04-06)
- **⚠️ `chattr +i` lesson:** Never immutable-lock files gateway reads at runtime. Only lock static files (SOUL.md, AGENTS.md).
