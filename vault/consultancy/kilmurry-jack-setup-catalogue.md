# Kilmurry Jack — Full Setup & Changes Catalogue
_Updated: 2026-04-20_

Snapshot of Jack's KilmurryBot + Mission Control environment. Treat this as our reference for how Jack's side is configured so we maintain full understanding.

---

## 1. Server & OpenClaw Infrastructure

### Base
- **Server:** 172.239.98.61 (Linode, shared with Kate)
- **User:** `clawuser` (sudo) + `kateuser` (Kate's isolated instance)
- **OpenClaw version:** v2026.4.15 (as of 2026-04-20)
- **Workspace:** `/home/clawuser/.openclaw/workspace`
- **Agent data:** `/home/clawuser/.openclaw/agents/main/`
- **Gateway:** port 18789, runs from `~/.npm-global/bin/openclaw gateway` (not systemd)

### Auth (as of 20 Apr post-audit)
- Primary model: `openai-codex/gpt-5.4` (OAuth, free via Codex subscription)
- Fallbacks: `anthropic/claude-opus-4-7` → `anthropic/claude-sonnet-4-6` → `anthropic/claude-opus-4-6`
- Interactive bot (via ACP → Claude Code) still uses his Claude Max subscription

### Plugins enabled
`anthropic`, `google`, `openai-codex`, `acpx`, `memory-core` (dreaming on), `active-memory`, `browser`

### ACP config
- `acp.enabled = true`
- `acp.dispatch.enabled = true`
- Telegram thread bindings: `spawnAcpSessions = true` — every new chat thread spawns a fresh Claude Code session (zero API cost, uses Jack's Claude Max subscription)

### Cron jobs (post-audit, 4 total)
| Job | Schedule | Purpose | Status |
|---|---|---|---|
| Advisor Check | every 6h | Audits today's daily memory file | ✅ working |
| session-health-check | daily 22:00 | Checks session context bloat | ✅ working |
| kilmurry-morning-brief | daily 07:00 | Full morning exec brief | ✅ will self-heal next run |
| weekly-rate-intelligence | Mondays 08:00 | Weekly rate check | ✅ will self-heal next run |

### Removed
- Custom `Dream Cycle` cron — redundant, replaced by native Memory Dreaming Promotion

---

## 2. Workspace File Structure

### Root (bootstrap files)
- `SOUL.md` (1.8KB) — Jack's persona, tool-language framing
- `USER.md` (1.0KB) — About Jack
- `IDENTITY.md` (0.3KB)
- `TOOLS.md` (0.9KB)
- `HEARTBEAT.md` (0.9KB)
- `AGENTS.md` (14.3KB) — extensive operational rules, now with Micro-Learning Loop
- `MEMORY.md` (5.2KB) — pointer index, disciplined trim to <5KB via dreaming

### vault/ — structured topic detail
| Path | Content |
|---|---|
| `vault/property/overview.md` | 118 units, Residence extension Q1 2027, venues |
| `vault/people/team.md` | Eugene, Faye, Ciara, Kate, Amy, Robin, Stephen |
| `vault/business/strategy.md` | Vision 2030, Revenue AI phases, Ryder Cup 2027 |
| `vault/business/claude-teams-data-briefing-12-apr-2026.md` | RACI, budgets, pipeline |
| `vault/business/cask-intelligence.md` | Full CASK annual data |
| `vault/business/bigger-stage-intelligence.md` | €800-900K contract analysis |
| `vault/technology/stack.md` | RezLynx, Right Revenue, Alkimii, Claude Teams, Sage |
| `vault/technology/mission-control-workflow.md` | dev/main split, label discipline |
| `vault/technology/hot-dates-index-v2.md` | Weighted event scoring spec |
| `vault/technology/hot-dates-weighted-index-task.md` | Jonny's build task |
| `vault/forecasting/kpi-statistical-baseline-2024-2025.md` | RevPAR Normal(97.82, 23.47) |
| `vault/operations/academic-calendars-2025-2026.md` | UL official source |
| `vault/operations/structure.md` | Org structure |
| `vault/marketing/reputation.md` | TripAdvisor + Reddit audit |

### reports/ — daily briefings archive
- ~17 daily briefings from Mar 25 → Apr 19
- Recent ones are 10-12KB (full executive format)

### scripts/
- `health-cron.sh`, `server-health.sh` — Stephen-written monitoring
- `check-kilmurry-rates.md` — rate check SOP
- `health.log` — local log file

### credentials/
- Kept local, gitignored
- `.env.local`, `.env` for Mission Control Next.js

### Leftover HTML prototypes in root (22 files)
Mar 17-28 era vision prototypes — Kate's onboarding, campaign maps, rate dashboards, etc. These are static artefacts from pre-MC phase, now replaced by the live Mission Control. Cosmetic clutter only, not injected into context.

---

## 3. Mission Control — `~/mission-control`

### Stack
- **Framework:** Next.js 14.2.35 (App Router), React 18, TypeScript, Tailwind v4
- **Port:** 3333
- **Runtime:** PM2 (`pm2 restart mission-control`)
- **Repo:** `github.com/Jonnyhimalaya/kilmurry-mission-control`
- **Branching:** `dev` active, `main` stable

### Route structure (src/app/)
| Route | Purpose |
|---|---|
| `/` | Main dashboard |
| `/agents` | Agent directory |
| `/calendar` | Calendar view |
| `/intel` | Intelligence hub |
| `/marketing` | Marketing department module |
| `/revenue` | Revenue department module |
| `/memory` | Memory browser |
| `/reports` | Reports viewer |
| `/tools` | Tools index |
| `/stephen` | Stephen-specific view |
| `/kate` | Kate-specific view |
| `/tasks` | Task list |
| `/connections` | Integration connections |

### API routes (src/app/api/)
- Gateway wrapper (`lib/gateway.ts`)
- `useApi` hook (`lib/useApi.ts`)
- intel endpoints
- reports/download endpoints

### Notable features built
- **6 department modules:** Marketing, Revenue, Sales, Facilities, Guest Relations, F&B
- **Intelligence hub:** Hot Dates Intelligence (185 events, weighted v2), World Scenarios (Iran 4-week dashboard), Forecasting Intelligence (Alkimii Bridge)
- **Marketing depth:** Campaign Detail with self-contained tabs, Agent Architecture diagrams, sequence drill-downs, 10 agent configurations, Kate's Actions strip, approval buttons
- **Morning Brief page** — render of cron output
- **Prediction Challenge dashboard** — 14 predictions locked 11-19 April, scoring integrity maintained even when predictions revised internally
- **Hot Dates Review Queue** — human-in-the-loop event filtering with training notes (Faye feeds back)
- **Sales Kanban** — real pipeline integration

### Workflow rules (locked in)
- `dev` gets every commit; `main` only stable merges
- `.next/`, `node_modules/`, `.env*`, `credentials` never committed
- All labels explicit: **Prototype** / **Candidate** / **Production**
- `git status` clean before + after every change
- Fix for MC breaking: `rm -rf .next && npm run build && pm2 restart mission-control`

---

## 4. Strategic Context Jack Operates In

### Core identity
- Jack Hoare, Managing Proprietor, 3rd generation
- **Endgame:** step back from day-to-day ops. Every system measured against: does this get Jack closer to "the mower"?
- Standing instruction: **CHALLENGE HIM.** Be real, not agreeable. No echo chamber.

### Role split (locked 13 Apr)
- **Claude Teams** = strategic (M365, sensitive, personnel, financials)
- **KilmurryBot** = operational (MC, dashboards, cron)

### Cost discipline (standing rule)
- **Research/analysis:** inline Opus (Jack pays tokens)
- **Building (code, files, dashboards):** spawn Claude Code (free on subscription)
- Reconfirmed 13 Apr

### Business numbers (current, per MEMORY.md)
- Revenue budget 2026: Total €7,766K | Rooms €4,229K | F&B ~€2,966K
- Jan-Feb 2026: €160K behind budget
- YoY: €789K (2013) → €4.0M (2024) → €3.85M (2025) → €4.23M target (2026)
- Ryder Cup 2027: 605 room-nights, €385K+. 144 inquiries in pipeline.
- Sales pipeline: BiggerStage €800-900K (contracted), Fiserv €350-450K (high priority)
- RACI: 9 departments, 564 activities

### Known tensions / ongoing threads
- **CASK live music:** Darren Kiely + Kingfishr started here, Dolan's monopoly blocks artist access, Jack wants re-entry strategy
- **Residence-CASK coexistence:** physical adjacency of €175+/night studio guests and 600-cap student nights — subject of MiroFish Sim 1 (the current experiment)
- **Limerick City College partnership:** Brazilian students, 12+ weeks, Residence angle
- **Race Day rule (13 Apr):** Thursday race day = Wednesday dampens. 2026 = Thu 16 Apr. Operate light.

### MiroFish decision (13 Apr)
- **WAIT** on MiroFish as prior-feeder. Build Monte Carlo Track A first (€10-20K/mo value).
- Re-evaluate Q3 2026.
- If adopted later: offline fork only (local Neo4j + Ollama), use as scenario-generator only.
- Current MiroFish run is a learning/proof-of-concept exercise, not production strategy.

---

## 5. Standing Rules & Operational Norms

### Memory hygiene (Jack's side)
- MEMORY.md trimmed to <5KB via dreaming
- Daily logs archived ~weekly
- vault/ holds detail; MEMORY.md just pointers
- Dream cycle now native via `memory-core` plugin

### Git discipline (Mission Control)
- Every cycle: `git status` clean before + after
- Push dev every session
- Promote dev→main only for stable candidates
- Never commit build artefacts or credentials
- Labels on everything: Prototype/Candidate/Production

### Cron reliability lessons
- Anthropic subscription cutoff (Apr 4) broke all crons. $200 credit masked it until Apr 17. Now using Codex OAuth.
- **Lesson:** For any client install, crons need a provider path that doesn't depend on Claude Max / ChatGPT subscription OAuth — API keys or Codex OAuth both work.

### Golden rule
- When rejecting AI output, ALWAYS explain WHY.
- "No" = nothing. "No, because..." = training data.

---

## 6. Outstanding Items on Jack's Watchlist (from his MEMORY.md)

| Item | Owner | Status |
|---|---|---|
| OPENAI_API_KEY fallback for crons | Stephen | ✅ solved via Codex OAuth reroute (20 Apr) |
| OPENCLAW_GATEWAY_TOKEN rotation | Stephen | 🔴 pending |
| Hot Dates weighted index build | Stephen | 🔴 pending |
| Real-time ops intel spec | Stephen | 🔴 pending |
| 20 Apr: Prediction dashboard rebuild | Jack | 🔴 scheduled today |
| CASK sentiment monitoring | Jack | 🟡 design phase |
| Weather/F&B correlation model | Jack | 🟡 design phase |
| Dynamic staffing model | Jack | 🟡 design phase |
| SOUL.md recalibration (tool vs partner framing) | Jack | 🟡 minor |

---

## 7. Features Worth Porting to Leamy / Our MC

- **Hot Dates Intelligence** — event-weighted scoring with learning feedback loop. Direct analogue for maths exams/Leaving Cert calendar.
- **Prediction Challenge dashboard** — quantifies forecast accuracy, scoring integrity locked. Great consultancy deliverable.
- **Department module architecture** — clean URL structure per team function.
- **Morning Brief page rendering cron output** — turns agent text into reviewable dashboard.
- **dev/main branching with explicit labels** — more mature than our current workflow.
- **Gateway wrapper + useApi hook** — clean API abstraction we could adopt.
