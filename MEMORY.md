# MEMORY.md — Long-Term Memory (Pointer Index)
# Detail lives in vault/. memory_search finds it in <50ms.

## About Jonny
- Stephen (goes by Jonny; @jonnyhimalaya), Limerick, Ireland
- Runs **Leamy Maths** (leamymaths.ie) — online maths education
- Co-founder of a BTC company
- Launching **AI consultancy** — OpenClaw setups for SMEs
- Direct, no-fluff style. Wants me as his marketing guru.
- Professional name on site: **Stephen** (NOT Stephan)

## Active Projects
- Leamy Maths → vault/business/leamy-maths.md
- Marketing campaigns → vault/marketing/campaigns-active.md
- Multi-agent team → vault/technical/multi-agent-team.md
- Infrastructure & tools → vault/technical/infrastructure.md
- AI Consultancy → vault/consultancy/overview.md
- Kilmurry Lodge (Kate Taylor) → consultancy/clients/kilmurry-lodge/kate-marketing-control-panel.md
- Revision course tracking → revision-course-2026.json
- Todo list → leamymaths-todo.md
- Competitive analysis → leamymaths-competitive-analysis.md

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
- GA4: service account in credentials/ga4-service-account.json
- Google Ads: AW-10776906058
- Meta: business_id 253648777546692 (session expired)
- Kilmurry server: 172.239.98.61 (clawuser, needs password from Jonny)

## ⚠️ Known Issues
- ~~xAI API credits exhausted~~ ✅ Topped up 2026-03-30 — Scout + x_search working
- ~~HTTP 529 doesn't trigger fallback chain~~ ✅ Fixed 2026-04-02: v2026.4.1 `auth.cooldowns.overloadedProfileRotations` + `rateLimitedProfileRotations` configured. Profile rotation: claw → work, then model fallback chain.
- OpenAI quota needs topping up (GPT-5.4 + GPT-4o failing)
- Meta session expired — needs Jonny to log in manually
- **Security:** GA4 service account key was exposed in git history. Scrubbed from git, but key needs rotation in Google Cloud.
- **Security:** Kilmurry server needs version check due to 33 OpenClaw vulnerabilities (sandbox escape); blocked on Jonny providing SSH password.

## Preferences
- "Use initiative. Don't ask for this and that. Research, document, strategise. We will be the most innovative, most informed agentic consultant."
- Observations → always add to leamymaths-todo.md
- Mission Control exists at localhost:3333 — ENHANCE, don't rebuild
- WooCommerce memberships: use the skill, verify wcm-active status
- Memory Resilience: Always follow Protocol C (checkpoint every ~150 msgs) and D (rescan .reset transcripts on /new) to prevent data loss.
