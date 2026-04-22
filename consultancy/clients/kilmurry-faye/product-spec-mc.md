# Faye Mission Control — Product Spec v1

**Owner:** Faye Fitzgerald (Revenue Manager, Kilmurry Lodge)
**Engineer:** Faye's OpenClaw agent (via Claude Code ACP harness once authed)
**Created:** 2026-04-22
**Status:** Draft — awaiting Jonny approval

## 1. Purpose

Faye's Mission Control is a **daily revenue decision cockpit**. It answers three questions every morning:

1. **Where are we vs budget?**
2. **What dates need attention?**
3. **Should I move any rates?**

It is NOT a replacement for Right Revenue or Avvio — it is an **intelligence layer on top** that reduces Faye's 4–8 hr/day rate workload by surfacing what matters, in one screen, with context.

## 2. Architecture Pattern

Mirror Kate's MC setup (proven pattern from 2026-04-22 rebuild):

- **Stack:** Next.js 14 + Tailwind + TypeScript
- **Server:** Kilmurry box (172.239.98.61) as `fayeuser`
- **App port:** 3338 (next free after Kate's 3336)
- **Nginx basic-auth port:** 3339 (next free after Kate's 3337)
- **systemd unit:** `faye-mc`
- **Repo:** `Jonnyhimalaya/kilmurry-faye-mission-control` (private)
- **URL:** http://172.239.98.61:3339 (Tailscale recommended for access)
- **Auth:** nginx basic-auth, login `faye` / generated password
- **Labelling discipline:** every panel tagged `LIVE`, `MANUAL`, or `DEMO` (Kate MC rule — no pretending)

## 3. Modules (matches Jonny's brief)

### 3.1 Business Overview *(top-of-page summary)*
**Purpose:** Glanceable "how are we doing" bar.
**KPIs (today / this week / this month):**
- Occupancy % (actual vs budget vs LY)
- ADR (€)
- RevPAR (€) — the headline metric
- Revenue pace (ahead/behind LY %)
- Pickup last 7 days (rooms)
- Cancellations last 24h (rooms + €)
**Source:** Right Revenue scrape (browser automation) → cache every 30 min
**Labels:** `LIVE` once scrape is stable; `MANUAL` until then (Faye pastes daily)

### 3.2 Competitor Pricing Model *(interactive graph)*
**Purpose:** See KLH vs comp set rates across next 14/30/90 days at a glance.
**Visual:** Line chart, one line per competitor, KLH bold.
**Hover:** tooltip shows date, competitor name, rate, rate delta vs KLH, sold-out flag.
**Comp set (known):** Castletroy Park, Radisson Blu Limerick, Strand Limerick, Savoy, Clayton, Woodlands, Limerick Strand — confirm with Faye.
**Source:** Right Revenue "Rate Shop" data (browser scrape) OR Avvio if it has a rate shop export.
**Alerts:** when KLH is >€25 below comp set average or >€25 above on high-demand dates.

### 3.3 Hot Dates Calendar + Availability Gaps + Kate's Content Calendar
**Purpose:** Unified 90-day forward calendar showing demand signals and marketing actions together.
**Layers (each togglable):**
- Hot Dates events (185 from existing `/home/clawuser/shared/hot-dates-2026.json`)
- Availability gaps (where current pickup is tracking behind pace)
- Kate's social content calendar — pulled via shared folder or API from Kate's MC
- Comp set sold-out dates (demand pressure flag)
**Interaction:** click a date → panel shows: current bookings, KLH rate, comp rates, events that day, Kate's planned posts, suggested action.
**Data sources:**
- Hot Dates JSON (shared folder — live now)
- Kate MC API (need endpoint from Kate's MC — `/api/content-calendar` to be added)
- Right Revenue pickup (scrape)

### 3.4 Month at a Glance *(rate grid + events overlay)*
**Purpose:** Faye's rate-movement workbench.
**Layout:** Calendar grid, one cell per day, 30–90 day view.
**Per cell shows:** KLH rate, occupancy %, pickup delta, event badges (local events, Hot Dates).
**Connect events to rate decisions:** toggle "show events" overlays local gig/match/holiday context on rate cells → Faye can see at a glance "Munster home game Friday + we're still €169 = push to €199".
**Action:** click cell → rate change proposal drafted (waits for Faye approval, doesn't push to Right Revenue unless/until automation is built).

### 3.5 Packages & Offers — Sell-Through + Competitor Gap Analysis
**Two sub-panels:**

**a) How are our current packages selling?**
- List of live packages (Spa, Dinner B&B, Golf, Weekend Break, etc.) — names confirmed with Faye
- Per package: units sold last 7/30 days, revenue contribution, lead time, cancellation rate
- Traffic light: selling well / underperforming / dead

**b) Competitor package gap analysis**
- Scrape top 5 comp set package pages (Castletroy, Radisson, etc.)
- Extract package names, pricing, inclusions
- Gap table: "Radisson sells a Proposal Package — we don't. Estimated €1,200 ADR boost per sale."
- Updated weekly (not real-time — package pages are slow-moving)

### 3.6 Upselling Prompt Engine
**Purpose:** Suggest upsell opportunities Faye can push to reception/sales.
**Triggers:**
- Corporate booking arriving this week → prompt suite upgrade offer
- Leisure booking on date with event nearby → prompt late checkout / breakfast add-on
- Cluster of single-night bookings → prompt stay-longer discount
**Output:** daily "upsell candidates" list with suggested script.
**Source:** RezLynx arrivals export (needs access — flag for Faye).

### 3.7 Avvio Reports Integration
**Two panels:**

**a) Avvio Daily Report**
- Direct website bookings yesterday, revenue, conversion rate, funnel drop-off
- Ingested either via Avvio API (if available) or email parse (if Avvio emails the report) or browser scrape
- Auto-refreshed at 09:00 each morning

**b) Avvio Weekly Report**
- Same metrics but aggregated + WoW / YoY trend
- Delivered Monday 09:00

**Open question for Faye:** Does Avvio offer API access, or do reports come by email?
- If email: set up IMAP ingestion (pattern already in Kate's stack)
- If API: OAuth setup with Jack's account
- If neither: scheduled browser scrape

### 3.8 Room Sales Pickup Report *(automated, daily)*
**Purpose:** Replace whatever manual pickup Faye does now.
**Output:** daily PDF + in-MC view:
- Rooms picked up last 24h, broken down by: stay date, rate, source (direct / OTA / corporate), lead time
- Pickup trend vs pace (am I gaining or losing pace?)
- Dates with zero pickup flagged red
- Delivered to Faye's inbox/Telegram at 08:00
**Source:** RezLynx or Right Revenue booking export.

### 3.9 Real-Time Alerts (Flag cancellations / large bookings)
**Purpose:** Let Faye react fast to demand signals.
**Triggers:**
- Any cancellation >€500 → instant alert
- Any booking >€2,000 → instant alert (rate adjustment opportunity)
- Any date moving from amber→green or green→red in 24h
- Comp set sold-out detection → "Castletroy sold out Fri 15 May — room to lift KLH rate"
**Channel:** Telegram (once paired) + MC banner + email fallback.
**Source:** RezLynx webhook or short-interval poll.

## 4. Data Sources — Status Map

| Source | Status | Path |
|---|---|---|
| Hot Dates JSON (185 events) | ✅ LIVE | `/home/clawuser/shared/hot-dates-2026.json` |
| Right Revenue data | ❌ Blocked (API refused) | Browser automation required |
| RezLynx PMS | ❓ Unknown — need access | API or export TBC |
| Avvio reports | ❓ Unknown — email or API? | Ask Faye |
| Kate's content calendar | ⚠️ Not exposed yet | Kate MC needs `/api/content-calendar` endpoint |
| Comp set rates | ❌ Not built | Scrape via existing rate-scout pattern |
| Comp set package pages | ❌ Not built | New scraper (weekly) |

## 5. Phasing (MVP → Full)

### Phase 1 — MVP (1 build sprint)
Goal: something Faye can open Monday morning and get value from, even if data is partially manual.
- Shell app deployed (matches Kate MC pattern)
- Business Overview panel — `MANUAL` paste mode initially
- Hot Dates Calendar (already live data — easiest win)
- Month at a Glance grid — `MANUAL` rates for now
- Alert banner placeholder
- Nginx basic-auth + systemd

### Phase 2 — Data Plumbing (2–3 build sprints)
- Right Revenue browser scraper (the big unlock) — daily + on-demand
- Competitor Pricing graph with live comp set data
- Pickup Report automation
- Avvio report ingestion (once mechanism confirmed)
- Package sell-through panel (needs RezLynx access)

### Phase 3 — Intelligence Layer
- Upselling Prompt Engine
- Competitor package gap analysis
- Rate recommendation engine (suggestions, not auto-apply)
- Real-time alerts to Telegram

## 6. Open Questions for Faye (capture in first session)

1. Confirm comp set list (the 7 hotels listed right in section 3.2?)
2. Does Avvio deliver reports by API, email, or PDF download?
3. Does she have RezLynx report export access, or must it route through Jack?
4. Current package list — what's live, what's dead?
5. How does she want alerts delivered — Telegram (default), email, or both?
6. Preferred time for daily pickup + Avvio reports (suggest 08:00)?

## 7. Non-Goals (explicitly OUT of scope)

- Replacing Right Revenue
- Auto-publishing rate changes (Faye must approve)
- OTA rate management (separate concern)
- Guest PII handling (per PEB-001 constraint)
- Automated booking flows

## 8. Success Metrics

- Faye's daily rate-email hours: 4–8 → <2
- Time to spot a high-demand date and react: currently hours → target <15 min
- Rate exceptions codified: 0 → 47+
- Faye opens MC at least once per day within first 2 weeks
- Rate decisions referenced back to MC data within 4 weeks
