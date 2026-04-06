# MEMORY.md — Long-Term Memory (Pointer Index)
# Detail lives in vault/ and memory/topics/. memory_search finds it in <50ms.

## About Jonny
- Stephen (goes by Jonny; @jonnyhimalaya), Limerick, Ireland
- Runs **Leamy Maths** (leamymaths.ie) — online maths education
- Co-founder of a BTC company (Nexus)
- Launching **AI consultancy** — OpenClaw setups for SMEs
- Direct, no-fluff style. Wants me as his marketing guru.
- Professional name on site: **Stephen** (NOT Stephan)

## 🔴 Active Alerts (2026-04-06)
- Anthropic now on API billing (expensive path). Cost consciousness is critical.
- Telegram RAM alerts from cron context failing (chat ID unresolvable) → fix health scripts
- RAM critical (259MB free, swap in use) → [server resources](memory/topics/server-resources.md)
- GA4 key exposed, unrotated → [security items](memory/topics/security-open-items.md)
- Kilmurry unpatched (CVE-2026-33579, CVSS 9.9) → [security items](memory/topics/security-open-items.md)
- ClawHub supply chain risk (12%+ malicious plugins) → [security items](memory/topics/security-open-items.md)

## Active Projects
- Leamy Maths → vault/business/leamy-maths.md
- Marketing campaigns → vault/marketing/campaigns-active.md
- Multi-agent team → vault/technical/multi-agent-team.md
- Infrastructure & tools → vault/technical/infrastructure.md
- AI Consultancy → vault/consultancy/overview.md
- Kilmurry Lodge (Kate Taylor) → memory/topics/client-deployments-status.md
- Nexus (BTC company) → memory/topics/client-deployments-status.md
- Revision course tracking → revision-course-2026.json
- Todo list → leamymaths-todo.md
- Competitive analysis → leamymaths-competitive-analysis.md

## Topic Files (Consolidated)
- [Security Open Items](memory/topics/security-open-items.md) — GA4 key, Kilmurry CVE, ClawHub supply chain
- [Anthropic Auth Migration](memory/topics/anthropic-auth-migration.md) — OAuth→API key transition
- [Client Deployments Status](memory/topics/client-deployments-status.md) — Nexus + Kilmurry Lodge
- [Server Resources](memory/topics/server-resources.md) — RAM/disk tracking, trends
- [Twitter Research 2026-04-05](memory/topics/twitter-research-2026-04-05.md) — ClawSuite, ClawChief, ByteRover, etc.

## Agent Team (Quick Ref)
| ID | Name | Model | Role |
|----|------|-------|------|
| main | 🧠 Orchestrator | opus-4-6 | Strategy, delegation |
| sitemgr | 🔧 Wrench | sonnet-4-6 | WordPress admin |
| marketing | 📊 Prism | sonnet-4-6 | Analytics, ads |
| scout | 🔍 Radar | grok-3-mini | Research |
| content | 🎨 Pixel | gpt-5.4 | Social, graphics |

## Key Credentials & Access
- WP admin: leamyclaw@gmail.com (browser login)
- GA4: service account in credentials/ga4-service-account.json (⚠️ needs rotation)
- Google Ads: AW-10776906058
- Meta: business_id 253648777546692 (session expired)
- Kilmurry server: 172.239.98.61 (clawuser, needs password from Jonny)

## Preferences
- "Use initiative. Don't ask for this and that. Research, document, strategise."
- Observations → always add to leamymaths-todo.md
- Mission Control exists at localhost:3333 — ENHANCE, don't rebuild
- WooCommerce memberships: use the skill, verify wcm-active status
- Delegate repetitive browser work to sitemgr (Wrench/Sonnet) — Opus thinks, Wrench clicks (bulk membership adds on Opus cost €15)
- Memory Resilience: Always follow Protocol C (checkpoint every ~150 msgs) and D (rescan .reset transcripts on /new)
