# WRITE RULE: NEVER overwrite or replace this entire file. Only append new sections. Preserve everything above. Use edit tool only — never write tool.

# MEMORY.md — Long-Term Memory

## About Jonny
- Name: Stephen (goes by Jonny; Himalaya on Telegram, @jonnyhimalaya)
- Professional name on Leamy Maths: **Stephen** (correct spelling, NOT Stephan)
- Based in Limerick, Ireland
- Runs an online maths education business: **Leamy Maths** (leamymaths.ie)
- Teaches Leaving Cert and Junior Cert maths online
- Has a YouTube-style teaching approach: face-to-camera, digital whiteboard, home/studio setup

## Leamy Maths — Business Context
- Website: https://leamymaths.ie
- Sells online courses (e.g. 6th Year Higher Level, Junior Cert Higher Level)
- Free trial course available (3 lessons)
- Courses priced around €49.99
- Platform: WordPress + WooCommerce
- Video hosting: Vimeo
- Todo file: `/home/jonny/.openclaw/workspace/leamymaths-todo.md`

## Google Analytics (property 286245028)
- GA4 service account credentials: `/home/jonny/.openclaw/workspace/credentials/ga4-service-account.json`
- Service account email: `claw-analytics@claw-489121.iam.gserviceaccount.com`
- ~100k+ total sessions, growing from ~500/month (2021) to 5,085 (Jan 2026)
- Peak months: Jan/Feb and Oct/Nov (Leaving Cert exam calendar)
- Top channel: Google organic (~56k sessions) — SEO is working well
- Social (Facebook + Instagram): only ~4k sessions — big untapped opportunity
- Top pages: homepage, /my-courses/, /my-account/, Junior Cert course, Leaving Cert course
- Devices: 57% desktop, 32% mobile, 11% tablet
- Geography: 83% Ireland
- Old/unused GA4 property: 405213626 (only 4 sessions ever — not properly set up)
- Key issue: `/nogo/` page getting 3,565 sessions — needs investigation
- Key issue: checkout conversion gap (9,800 course views → only 1,635 checkout visits)

## Marketing — Active
- **Google Ads**: Full access via leamyclaw@gmail.com (AW-10776906058)
  - 3 active campaigns: Local_B_Limerick (€2.50/day), Revision_Parents (€20/day), Revision_Students (€10/day)
  - Conversion tracking working via thank-you page redirect
- **Meta Business Suite**: Partial access via leamyclaw@gmail.com (business_id: 253648777546692)
  - Facebook: Leamy Maths (113 followers) | Instagram: @leamy_maths (554 followers)
  - Meta Pixel: 6151104201627053
  - ⚠️ Cannot create posts yet — permissions issue, needs Full access or individual Content toggle
- **Instagram Campaign**: Easter revision courses, €50/day for 4 days, files in workspace/instagram-campaign/
- Marketing masterplan still to cover: SEO, email marketing

## Sub-Agent Capabilities
- Can spawn sub-agents for content strategy (gpt-5.3-codex), image generation (Sonnet + Nano Banana Pro)
- Nano Banana Pro (Gemini image gen) installed and configured with paid API key
- Image gen lesson: NO text in AI images, composite real photos + add text overlays separately
- Jonny's headshots in workspace/instagram-campaign/images/stephan-photos/

## Revision Courses (Easter 2026)
- Start date: Sunday March 22, 2026
- Target: Leaving Cert students (17-18yo) + parents, within 30km of Limerick
- Landing pages:
  - Parents (ORIGINAL, less optimised): /revision-for-leaving-cert-2026/
  - Parents (NEW, optimised Mar 19): /revision-for-leaving-cert-2026-parents-b/
  - Parents (older generic paid traffic): /revision-courses-paid-traffic/
  - Students: /expert-revision-course/
- Google Ads Revision_Parents_Limerick → changed to -parents-b/ on Mar 20 (was pending review)
- Meta/Instagram ads → ⚠️ STILL pointing to old /revision-for-leaving-cert-2026/ as of Mar 24 — NEEDS FIX
- Phone: 085 846 6670 (NOT clickable tel: link yet — todo)
- Form: Forminator ID 11250 → redirects to /thank-you-for-contacting-us/ → fires Google Ads conversion

## WooCommerce Admin Access
- Can log into WordPress admin via browser (leamyclaw@gmail.com)
- Added Logs and Exponential Functions (#5686) membership to 22 users on Mar 22-24
- Can manage Forminator form submissions (form ID 11250, 720+ entries)

## Multi-Agent Team — LIVE (March 26, 2026)
- Scaling from solo agent to orchestrated team under same gateway
- I (Opus 4.6) = orchestrator, single point of contact for Jonny
- Linode upgraded to 8GB RAM (~14:40 UTC March 26) — was running out at 4GB

### Agents (all created, configured, and smoke-tested Mar 26):
| ID | Name | Emoji | Model | Role | Status |
|----|------|-------|-------|------|--------|
| main | Orchestrator | 🧠 | claude-opus-4-6 | Strategy, delegation, Jonny's direct contact | Active |
| sitemgr | Wrench | 🔧 | openai/gpt-5.4 | WordPress/WooCommerce admin | Ready |
| marketing | Prism | 📊 | claude-sonnet-4-6 | Analytics, ads, copy, strategy | Ready |
| scout | Radar | 🔍 | claude-sonnet-4-6 (placeholder) | Twitter/AI research | Ready (needs Grok/xAI key) |
| content | Pixel | 🎨 | openai/gpt-5.4 | Social media, graphics | Ready |

### Architecture:
- Each agent has own workspace (`~/.openclaw/workspace-{id}/`), own SOUL.md, AGENTS.md, tool permissions
- Sub-agent spawning: I delegate via `sessions_spawn(agentId=...)`, they report back
- Tool restrictions: specialists have denied tools to keep them in lane (no gateway, no cron for most)
- Fallback chain: cross-provider (Opus → Sonnet → GPT-5.4 → GPT-4o) to avoid cascading rate limits

### Lessons Learned:
- Don't spawn all agents in parallel — rate limits cascade. Stagger or spawn 1-2 at a time.
- Fallbacks must cross providers (OpenAI ↔ Anthropic) or same-provider rate limits compound
- WooCommerce membership bug: Add Member modal saves post_status as "publish" not "wcm-active" — always re-save after creating

### Still TODO:
- Discord channel bindings for hybrid communication (Jonny sees inter-agent comms)
- Cron jobs: Marketing weekly Monday report
- Real task assignments beyond smoke tests
- Review v2026.3.22 breaking changes (13 reported) and ClawHub migration impact

### Completed:
- ✅ xAI API key configured (built-in provider, XAI_API_KEY env var in systemd)
- ✅ Scout (Radar) switched to xai/grok-3-mini, smoke-tested successfully
- ✅ Scout cron jobs: morning (8am Dublin) + evening (6pm Dublin) scans
- ✅ QMD memory backend installed (fully local BM25 search, no OpenAI dependency)

## Mission Control Dashboard
- Location: `/home/jonny/mission-control/` (Next.js app)
- Running on **http://localhost:3333** (production via PM2, auto-starts on reboot)
- Gateway token in `.env.local`
- 11+ pages: Dashboard, Marketing Hub, Analytics, Students, Tasks (Kanban), Agents & Sessions, Calendar, Memory, Reports, Landing Pages, Tools
- Agents page enhanced Mar 26: org chart, capabilities grid, cost tracker, live sessions (4 tabs)
- Branded Leamy Maths teal (#4A8C8C), dark theme
- Built Mar 24 by Claude Code sub-agent, adapted from build guide
- **THIS EXISTS. DO NOT REBUILD IT. ENHANCE IT.**

## Revision Course — Easter 2026 Payment Tracking
- Tracked in `/home/jonny/.openclaw/workspace/revision-course-2026.json` — source of truth
- Bundle students (€449): Sean Fitzgerald, Niall O'Brien, Garrett Murnane, Jack Downes
- Sean & Niall are no-shows so far — logged in todo, need follow-up
- All bundle students get access to ALL session content regardless of attendance
- Mission Control Revision Course page shows live payment/attendance status

## WooCommerce Memberships — Definitive Method
- ONLY reliable way to add a member: Add Member modal → JS inject user ID into select2 → set plan → Save
- Skill is fully documented: `~/.openclaw/skills/woocommerce-memberships/SKILL.md`
- DO NOT waste time on: REST API, admin-ajax.php, post-new.php direct nav, Grant Access button
- After save, verify `hidden_post_status=wcm-active` (not just the visible "Active" label)

## QMD Memory Backend (Installed Mar 27, 2026)
- Replaced default SQLite + OpenAI embeddings with QMD (github.com/tobi/qmd, 17k+ stars)
- Fully local BM25 search — no external API dependency, no embedding costs
- Config: memory.backend: "qmd", searchMode: "search", maxResults: 8, reindex every 10min
- Installed via Bun (v1.3.11) + @tobilu/qmd (v2.0.1)
- GPU build failed (no Vulkan on Linode) — irrelevant for BM25 mode
- Upgrade path: switch searchMode to "query" for full hybrid (vector + reranking) if needed

## Session Context Management
- Long sessions (>100 messages) cause Anthropic 529 overloaded errors
- HEARTBEAT.md monitors both TUI and Telegram sessions — alerts at >100, escalates at >200 msgs
- Fix: /new in TUI or Telegram to reset session context
- Telegram caches better but same limits apply

## ⚠️ Known Issues
- *(none currently)*

## Server Health Monitoring
- Health script: `scripts/server-health.sh`
- Cron job: every 4 hours, Telegram alerts only if issues found
- HEARTBEAT.md runs the health script each heartbeat cycle

## Research Workflow
- **Grok (via X/Twitter)** is the go-to for OpenClaw ecosystem queries — latest updates, community plugins, new releases, real-time discussions
- OpenClaw's most active community is on Twitter/X, not Discord or GitHub issues
- Pattern: I draft a specific prompt → Jonny pastes to Grok → feeds back the response → I evaluate and implement
- Future: Scout agent with xAI API key should automate this loop

## Artifacts System (Implemented Mar 27, 2026)
- Agents produce structured proof-of-work: screenshots (before/after), reports (markdown files), task plans
- Central protocol: `artifacts/PROTOCOL.md`
- Saved to `artifacts/YYYY-MM-DD/{agent}-{task-slug}.md` + PNGs
- Wrench: mandatory screenshots for site changes; Prism: reports as files; Radar: scan reports persisted; Pixel: briefs + images
- Key rule: artifacts go to disk, never loaded into agent context — zero token cost
- Inspired by Google Antigravity's artifact pattern, adapted for our headless architecture
- Future: Mission Control Artifacts page to browse visually

## AI Consultancy Business (Started Mar 28, 2026)
- Jonny launching a second business: helping SMEs set up OpenClaw agentic systems
- Separate from Leamy Maths — own branding, own client relationships
- Architecture: Option B — separate Linode + gateway per client (full data isolation)
- First client: **Kilmurry Lodge Hotel** (109 rooms, Castletroy, Limerick) — GM is Jonny's friend
- Consultancy workspace: `consultancy/clients/` for playbooks, templates, client notes
- Business model: setup fee + monthly retainer + pass-through infrastructure costs
- Radar's expanded watchlist now feeds both businesses (agentic patterns, tools, use cases)

## Preferences & Style
- Jonny prefers observations always added to leamymaths-todo.md
- Direct, no-fluff communication style
- Wants me to act as his marketing guru

## Consolidated from 2026-03-04 / 2026-03-18

### Competitive Intelligence (from full report in leamymaths-competitive-analysis.md)
- Biggest national threats: **Breakthrough Maths** (36k IG, 800 Trustpilot reviews, €149/month, national award winner) and **Grinds360** (23k students, Brian O'Driscoll backed)
- Limerick locals: Kilmartins (strong local brand), Premier Tuition Dooradoyle, Barnakyle Maths & Science (Patrickswell)
- Leamy gaps vs competitors: Instagram (330 vs 36k), zero Trustpilot/Google reviews, no subscription model

### Analytics — Additional Detail
- ChatGPT sending 281 sessions/year → new organic channel, worth monitoring
- /nogo/ page: 1,127 sessions in last 12 months (3,565 all-time) — still uninvestigated

### Technical Notes
- Whisper (local STT) too slow on this CPU for long audio (>30 min) — not viable for Vimeo lesson transcripts; Jonny to export from Vimeo dashboard
- GTM containers GTM-KQRRRZRD + GTM-MZQ9J4J are on the site but NOT accessible under leamyclaw@gmail.com — need separate GTM login if changes needed
- `/contact-us/` page is 404 — correct URL is `/contact/` (CTA buttons on revision pages link to /contact/)

### Stephen's Best Photos for Ads (in workspace/instagram-campaign/images/stephan-photos/)
- 205934.jpg — pointing pose (high energy)
- 210115.jpg — arms out, warm/welcoming
- 205733.jpg — confident, authoritative
- Cropped versions saved as stephan-*-cropped.jpg
