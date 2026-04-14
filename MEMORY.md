# MEMORY.md — Long-Term Memory (Pointer Index)
# Detail lives in vault/ and memory/topics/. memory_search finds it in <50ms.

## About Jonny
- Stephen (goes by Jonny; @jonnyhimalaya), Limerick, Ireland
- Runs **Leamy Maths** (leamymaths.ie) — online maths education
- Co-founder of a BTC company (Nexus)
- Launching **AI consultancy** — OpenClaw setups for SMEs
- Direct, no-fluff style. Wants me as his marketing guru.
- Professional name on site: **Stephen** (NOT Stephan)

## 🔴 Active Alerts (2026-04-08)
- Anthropic now on API billing (expensive path). Cost consciousness is critical.
- Anthropic harness blocking: OpenClaw prompt-level blocks observed. sitemgr and marketing agents at risk; consider migrating to Gemini 3.1 Pro or GPT-5.4.
- Telegram RAM alerts from cron context failing (chat ID unresolvable) → fix health scripts
- RAM elevated (~37-40%, improving since Nexus npm cache cleared) → [server resources](memory/topics/server-resources.md)
- GA4 key exposed, unrotated → [security items](memory/topics/security-open-items.md) — **BLOCKING Kate's dashboard**
- ClawHub supply chain risk (12%+ malicious plugins) → [security items](memory/topics/security-open-items.md)
- **Anthropic credits claimed** on 2026-04-11. Anthropic remains on API billing, so cost consciousness is still critical.

## Active Projects
- Leamy Maths → vault/business/leamy-maths.md
- Marketing campaigns → vault/marketing/campaigns-active.md
- Multi-agent team → vault/technical/multi-agent-team.md
- Infrastructure & tools → vault/technical/infrastructure.md
- AI Consultancy → vault/consultancy/overview.md
  - Recommended deployment pattern: Docker standardisation (`ghcr.io/openclaw/openclaw` via docker-compose) instead of manual npm installs.
  - Evaluate **Lobu.ai** (open-source multi-tenant OpenClaw fork) as a scaling architecture.
  - Evaluate Coolmanns memory architecture (v6) for multi-layer decay and GPU semantic search.
  - Pitch Gemma 4 (12B, ~7GB RAM) for compliance-heavy client deployments (e.g., Kilmurry hotel data).
- Kilmurry Lodge (Jack) → memory/topics/client-deployments-status.md | port 18789 (clawuser)
- Kilmurry Lodge (Kate Taylor, marketing) → memory/topics/client-deployments-status.md | port 18792 (kateuser), dashboard port 3334
  - TG bot: @Katetaylor123_bot | Kate's TG ID: 8778805348
  - Tailscale IP: 100.111.174.13 (Kate + Jack access MC via this)
  - GitHub push unresolved — kateuser + clawuser lack GitHub auth on Kilmurry server → HTTPS fine-grained token needed
  - Wednesday meeting: Kate needs to provide GA4 access, Meta token, email platform, Google Ads account ID
- Nexus (BTC company) → memory/topics/client-deployments-status.md | port 18790 (nexus user), dashboard port 3334
- Revision course tracking → revision-course-2026.json
- Todo list → tasks.md (active) / tasks-completed.md (archive)
- Competitive analysis → leamymaths-competitive-analysis.md

## Topic Files (Consolidated)
- [Security Open Items](memory/topics/security-open-items.md) — GA4 key, Kilmurry CVE, ClawHub supply chain
- [Anthropic Auth Migration](memory/topics/anthropic-auth-migration.md) — OAuth→API key transition
- [Client Deployments Status](memory/topics/client-deployments-status.md) — Nexus + Kilmurry Lodge
- [Server Resources](memory/topics/server-resources.md) — RAM/disk tracking, trends
- [Twitter Research 2026-04-05](memory/topics/twitter-research-2026-04-05.md) — ClawSuite, ClawChief, ByteRover, etc.

## Kilmurry GitHub + Mission Control (2026-04-08)
- Kilmurry repos now use HTTPS auth with a single fine-grained GitHub token covering:
  - `Jonnyhimalaya/Kilmurry`
  - `Jonnyhimalaya/kilmurry-kate`
- Kate repo/server mapping:
  - repo: `Jonnyhimalaya/kilmurry-kate`
  - user: `kateuser`
  - app path: `/home/kateuser/kilmurry-marketing-mc`
- Jack repo/server mapping:
  - repo: `Jonnyhimalaya/Kilmurry`
  - user: `clawuser`
  - Mission Control path: `/home/clawuser/mission-control`
  - workspace path: `/home/clawuser/.openclaw/workspace`
- Jack’s agent is now safe to edit Mission Control directly as long as it follows build → verify → commit → push discipline.
- If Kilmurry repo pushes fail in future, check HTTPS token auth and branch divergence before assuming missing repos or bad memory.

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
- Observations → always add to tasks.md (not leamymaths-todo.md — that's been split)
- Mission Control exists at localhost:3333 — ENHANCE, don't rebuild
  - "Blocked by Jonny" panel deployed 2026-04-07 (commit 5662555) — shows GA4 rotation, Kilmurry SSH pw, Meta re-login, credits top-up
- WooCommerce memberships: use the skill, verify wcm-active status
- Delegate repetitive browser work to sitemgr (Wrench/Sonnet) — Opus thinks, Wrench clicks (bulk membership adds on Opus cost €15)
- Memory Resilience: Always follow Protocol C (checkpoint every ~150 msgs) and D (rescan .reset transcripts on /new)
- **Primary model:** GPT-5.4 (decided 2026-04-06 by Jonny — Opus API billing too expensive)
- **Native dreaming** enabled in OpenClaw (memory-core, 3am daily, replaces old autoDream)
- **Local Model Fallback:** Gemma 4 viable via Ollama (Apache 2.0, good tool use) — recommended for consultancy budget tiers and API failovers.
- **CLI capabilities:** `openclaw infer` available in v2026.4.7+ for multimodal inference (images/audio/video) — good for marketing workflows.
- **ClawChief architecture** active: priority-map.md, auto-resolver.md, tasks.md
- Cross-agent shared memory: NOT wanted — isolation is a feature (Jonny's decision, 2026-04-06)
- **⚠️ `chattr +i` lesson:** Never immutable-lock files the gateway reads at runtime (exec-approvals.json, openclaw.json). Only lock static files (SOUL.md, AGENTS.md). Immutable flag blocks ALL access including reads.
