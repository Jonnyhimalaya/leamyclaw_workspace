# Kilmurry Lodge Mission Control — Feature Catalogue
_Last audited: 2026-04-13 from repo `Jonnyhimalaya/kilmurry-mission-control`_
_20 commits total. Port 3333, PM2, Next.js 14, TypeScript._

---

## Architecture Overview

Mission Control is a hybrid system:
- **Core shell:** Next.js 14 app (TypeScript, Tailwind, SSR-ready)
- **Intelligence layer:** Static HTML/JS pages in `/public/` for prototype modules
- **API layer:** Next.js route handlers (`/app/api/`) that proxy to the OpenClaw gateway + workspace files
- **Live connectivity:** Real-time data via `useApi` polling hook (60s refresh on most routes)
- **Sidebar:** Fixed 260px, gold accent colour scheme, dark theme

The system splits neatly into **3 tiers:**
1. **Core Next.js pages** — live API data, real OpenClaw integration
2. **Department Modules** — static HTML prototypes, demo data, vision-layer
3. **Intelligence Tools** — static HTML pages (some with real data from hot-dates JSON)

---

## Core Next.js Pages (Live, API-Backed)

### 🏠 Dashboard (`/`)
- Agent status via `session_status` + `sessions_list` gateway calls
- Session count, active sessions, total tokens + cost (USD)
- Doc count (HTML + JSON files in workspace)
- Memory file count
- Cron jobs: list with last run, status, next run, duration
- Intelligence feed preview (recent intel items)
- Auto-refresh every 60s

### 📋 Tasks & Projects (`/tasks`)
- Kanban board: Backlog / In-Progress / Blocked / Done
- Real data from `tasks.json` in workspace (falls back to hardcoded defaults)
- Add/move/delete tasks via PATCH/POST/DELETE API routes
- Priority labels (high/medium/low)

### 🤖 Agents & Team (`/agents`)
- Live session list via gateway `sessions_list`
- Shows model, status, message count, cost per session
- Session detail drill-down

### 🔧 Tools (`/tools`)
- Live tool/plugin status from gateway
- Categorised: Channel, Auth, Search, Model, Skill, System
- Green/muted/red status dots

### 📅 Calendar & Crons (`/calendar`)
- Cron job list with schedule, last run, next run, status
- Data from gateway `sessions_list` + OpenClaw cron API

### 📚 Memory & Docs (`/memory`)
- Lists workspace memory files (`.md`) with size + last modified
- Click to expand and read file content inline
- Read-only view

### 📊 Intelligence Feed (`/intel`)
- Aggregates intel items from multiple workspace JSON files:
  - `rate-comparison-data.json`
  - `weekend-rates.json`
  - Hot dates JSON
  - Any other data files in workspace
- Sorted by recency, type-tagged

### 📑 Reports (`/reports`)
- Report generation/download interface
- `/api/reports/download/ga4-guide` endpoint for downloadable docs

### 💰 Revenue Intelligence (`/revenue`)
- **Most mature Next.js page** — very rich UI
- Demo data only (revenue API returns hardcoded data with `demo: true` flag)
- Sections (tab-navigated):
  - Overview: occupancy, ADR, RevPAR, TRevPAR, arrivals/departures
  - Forecast: 7/14/30 day view with occupancy bars
  - Competitors: rate comparison table
  - Segments: booking segment breakdown
  - Channels: OTA vs direct vs corporate
  - Room Types: per-category performance
  - Events: upcoming events and impact
  - Rate Recommendations: AI-suggested rate actions
- Note on data: "Will eventually be replaced by RezLynx PMS direct feed"
- 117 keys total (108 rooms + 9 apartments)

### 📣 Marketing Hub (`/marketing`)
- GA4 integration (real data via service account, property `319963337`)
- Meta API integration (reads token from workspace `credentials/.env`)
- Shows: GA4 sessions, bounce rate, top pages
- Shows: Meta reach, impressions, engagement (when token valid)
- Error boundary wrapping — fails gracefully if GA4/Meta creds are absent

### 👤 Kate's Week View (`/kate`)
- Kate's onboarding documents listed with download links:
  - Vision v3, 90-Day Plan v3, 18-Month Roadmap v3
  - AI Marketing Org Chart, Campaign Orchestration Map, Campaign Flow
- Week 1 priorities hardcoded (brand audit, social audit, content calendar)
- Milestone timeline (Week 1-2 through Month 3)

### ⚙️ Stephen's Queue (`/stephen`)
- Task queue for the AI agent ("Stephen" = KilmurryBot's working name)
- Hardcoded PEB (Project Excellence Backlog) items with week, priority, status
- Items include: RezLynx PMS API, Microsoft Clarity, GA4, HubSpot sales pipeline, GuestRevu, Alkimii HR browser automation, Meta Business Suite, CASK online presence, Energy (IMS) monitoring, EU AI Act compliance
- Status: done/backlog

### 🔗 Connections (`/connections`)
- Lists tools + docs from workspace
- Shows connection health

---

## Department Modules (Static HTML, Prototype/Vision Layer)

All live in `/public/` and served directly by Next.js static file serving.

| Module | File | Status | Notes |
|--------|------|--------|-------|
| 📣 Marketing | `/marketing-dept/index.html` + `marketing.js` | Prototype | Most developed; full campaign view, agent diagrams, sequence drill-downs, 10 agents |
| 💰 Revenue | `dept-revenue.html` | Prototype | Demo data |
| 🤝 Sales | `dept-sales.html` | Prototype | Real sales pipeline kanban integrated |
| 🔧 Facilities | `dept-facilities.html` | Prototype | Demo data |
| ⭐ Guest Relations | `dept-guest.html` | Prototype | Demo data |
| 🍽️ F&B Intelligence | `dept-fb.html` | Prototype | Demo data |

---

## Intelligence Tools (Static HTML)

| Tool | File | Data Source | Status |
|------|------|-------------|--------|
| ☀️ Morning Brief | `morning-brief.html` | Static/workspace | Live concept |
| 📊 Forecasting / Alkimii | `dept-forecasting.html` | Demo | Alkimii bridge concept |
| 📅 Hot Dates Review Queue | `hot-dates-review.html` | `data/hot-dates-2026.json` (185 real events) | Real data |
| 🎯 Prediction Challenge | `prediction-challenge.html` | Hardcoded 14 predictions (Apr 11-19) | Locked predictions |
| 🌍 World Scenarios | `world-scenarios.html` | Static | Macro risk scenarios |

---

## Data Architecture

### Live/Real Data Sources
- **OpenClaw gateway** (sessions, tools, status, crons, memory) — via `invokeGateway()` lib
- **GA4 service account** (`credentials/ga4-service-account.json`) → property 319963337
- **Meta API** (token from `workspace/credentials/.env`) → business 253648777546692
- **Hot Dates JSON** (`public/data/hot-dates-2026.json`) — 185 real events from Faye

### Demo/Hardcoded Data
- Revenue page (all KPIs — note says "will be replaced by RezLynx")
- Most department modules
- Stephen's Queue (task backlog)
- Kate's milestones

---

## Key Technical Decisions

| Decision | Detail |
|----------|--------|
| **Static + Next.js hybrid** | Static HTML for fast prototyping, Next.js for live-data pages |
| **Gateway as data backend** | All OpenClaw data proxied through `/app/api/` routes via `invokeGateway()` |
| **Error boundaries** | Revenue + Marketing pages have React error boundaries — fail gracefully |
| **Demo flag** | Revenue API explicitly sets `demo: true` — clear signal, not pretending |
| **WORKFLOW.md** | Repo discipline doc: label Prototype/Production Candidate/Production, never commit `.next/` or credentials |
| **Branching** | `main` + `dev` branches; feature branches encouraged for large changes |

---

## Open Items / What's Not Yet Done

| Item | Context |
|------|---------|
| **RezLynx PMS API** | Revenue data is all demo; real PMS feed is the #1 unlock |
| **Alkimii HR browser automation** | On Stephen's Queue Week 2 backlog |
| **Meta token refresh** | Token likely expired; marketing page will fail silently |
| **GA4 key rotation** | Exposed service account key (leamymaths context) — Kilmurry has its own |
| **Sales pipeline (HubSpot)** | PEB-005 on backlog |
| **GuestRevu** | PEB-004, review monitoring dashboard not yet built |
| **Microsoft Clarity** | PEB-011 — 30 min quick win, still on backlog |
| **Mission Control auth** | IP allowlist or basic auth not yet implemented (Tailscale is the current control) |
| **Kate MC vs Jack marketing module boundary** | Overlap between Kate's MC (port 3334) and Jack's Marketing Department prototype |

---

## What We Can Learn / Reuse for Consultancy

1. **Hybrid static+Next.js pattern** works well for fast client prototyping — ship vision as static HTML, promote to Next.js when it needs live data
2. **Gateway-as-API pattern** — all OpenClaw data proxied via `/api/` routes is clean and reusable
3. **`demo: true` flag on API responses** — honest, prevents client confusion
4. **WORKFLOW.md in the repo** — lightweight discipline doc every client deployment should have
5. **Department-module architecture** — easy to add new departments without touching core app
6. **Stephen's Queue page** — an agent-visible task backlog inside the MC itself is a great pattern
7. **Error boundaries** on data-heavy pages prevent one broken integration killing the whole dashboard
8. **Hot Dates JSON as shared data layer** — single source of truth feeding multiple department modules
9. The **prediction challenge** is an interesting accountability mechanism — worth productising
