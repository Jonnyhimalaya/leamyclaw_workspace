# Kate's Marketing Control Panel — Build Spec
**Client:** Kilmurry Lodge Hotel
**User:** Kate Taylor (Marketing Manager)
**Platform:** Next.js (Mission Control pattern) + OpenClaw agent backend
**Prepared:** 2026-04-02

---

## Concept

This is a **Mission Control for Kate** — same architecture pattern we built for Jack, tailored to marketing. The OpenClaw agent gathers intelligence, processes data, and writes structured JSON/MD files. The Next.js dashboard reads those files and renders them as interactive pages.

```
Data Sources → OpenClaw Agent (gather + process) → Structured Files → Next.js Dashboard
                                                                           ↓
                                                                    Kate's Browser
```

**What makes this buildable fast:**
- We've already built Mission Control for Jack (15+ pages, branded, PM2-managed)
- Claude Code can scaffold Next.js pages rapidly
- Most data sources start with web scraping (which OpenClaw already does)
- API integrations layer on incrementally — pages work before APIs are connected
- Kate's agent populates data files on cron schedules

---

## Kate's 10 Modules → Mission Control Pages

### Module 1: Competitive Intelligence Hub
**Page:** `/competitors`
**Data sources (Phase 1 — scraping):**
- Competitor rates from OTA listings (RezLynx scraping — already built for Jack)
- Google Alerts / web search for competitor mentions
- Competitor social media activity (scrape public pages)

**Data sources (Phase 2 — APIs):**
- Semrush API: organic rankings, backlink profiles, traffic estimates, ad copy
- ReviewPro or similar: competitor sentiment scores

**Agent cron:** Daily rate scrape + weekly competitor deep-dive (extend `kilmurry-intel` skill)
**Output files:** `data/competitors/rates-YYYY-MM-DD.json`, `data/competitors/seo-snapshot.json`
**Dashboard:** Rate comparison charts, SEO position table, mention timeline, social activity feed

---

### Module 2: SEO & AEO Performance Dashboard
**Page:** `/seo`
**Data sources (Phase 1 — free APIs):**
- Google Search Console API: impressions, clicks, CTR, position by query
- Google Rich Results Test: schema validation
- Agent-run AEO checks: query ChatGPT/Perplexity/Google for "hotels in Limerick" and log if Kilmurry appears

**Data sources (Phase 2 — paid):**
- Semrush API: site audit score, keyword position tracking, backlink health
- GA4: landing page performance, organic traffic trends

**Agent cron:** Weekly SEO health check + daily AEO spot checks
**Output files:** `data/seo/search-console-YYYY-MM-DD.json`, `data/seo/aeo-visibility.json`, `data/seo/audit.json`
**Dashboard:** Keyword ranking table, CTR trends, AEO visibility tracker, site health score

---

### Module 3: Content Planning & Calendar Engine
**Page:** `/content`
**Data sources:**
- Brand voice guide + campaign pillars (static docs in workspace)
- Event calendar data (from Module 8)
- Social post performance (from scheduling platform API or manual entry)
- Google Trends: seasonal interest data
- Semrush topic research: content gap analysis

**Agent capability:** Generate content briefs, draft social captions, suggest hashtag sets, recommend posting schedule based on past engagement
**Output files:** `data/content/calendar.json`, `data/content/briefs/`, `data/content/performance.json`
**Dashboard:** Visual content calendar (month/week view), brief generator, performance heatmap by content type

---

### Module 4: Revenue & Yield Intelligence
**Page:** `/revenue`
**Data sources (Phase 1 — manual + scraping):**
- Competitor rates (from Module 1)
- Event demand signals (from Module 8)
- Google Trends: "Limerick hotels" search interest
- Historical rate data (JSON files already being collected by Jack's agent)

**Data sources (Phase 2 — PMS integration):**
- RezLynx PMS API: occupancy, ADR, RevPAR, booking lead times, channel mix
- STR reports (if subscribed): market benchmarking

**⚠️ Data access note:** This module touches financial data. Jack decides what Kate can see.
**Agent cron:** Daily demand signal check, weekly revenue context report
**Output files:** `data/revenue/demand-signals.json`, `data/revenue/rate-context.json`
**Dashboard:** Demand calendar overlay, competitor rate comparison, occupancy trends (when PMS connected)

---

### Module 5: Reputation & Review Management
**Page:** `/reviews`
**Data sources (Phase 1 — scraping):**
- TripAdvisor reviews (web scrape)
- Google Business Profile reviews (GBP API or scrape)
- Booking.com reviews (scrape)

**Data sources (Phase 2 — aggregation tool):**
- ReviewPro, GuestRevu, or TrustYou API: unified feed + sentiment scoring
- Competitor review benchmarking

**Agent capability:** Auto-categorise reviews by theme (room, food, service, location, value), draft responses in brand voice, flag urgent negatives
**Agent cron:** Twice daily review scan (8am + 6pm)
**Output files:** `data/reviews/latest.json`, `data/reviews/sentiment-trends.json`, `data/reviews/drafts/`
**Dashboard:** Review feed with sentiment badges, theme breakdown chart, response drafts with approve/edit, competitor review comparison

---

### Module 6: Paid Media & Campaign Tracker
**Page:** `/campaigns`
**Data sources (Phase 1 — manual CSV upload):**
- Google Ads export (CSV → JSON)
- Meta Ads export (CSV → JSON)
- Booking engine conversion data (manual)

**Data sources (Phase 2 — APIs):**
- Google Ads API: impressions, clicks, CPC, conversions, ROAS
- Meta Marketing API: equivalent social campaign data
- GA4 API: on-site behaviour post-click
- Booking engine API: revenue attribution

**Agent capability:** Flag anomalies (spend spike, CTR drop, cost-per-conversion increase), weekly performance summary, competitor ad copy analysis (via Semrush)
**Output files:** `data/campaigns/google-ads.json`, `data/campaigns/meta-ads.json`, `data/campaigns/summary.json`
**Dashboard:** Campaign cards with KPIs, spend vs conversion charts, anomaly alerts, competitor ad comparison

---

### Module 7: Analytics & Attribution Overview
**Page:** `/analytics`
**Data sources (Phase 1 — GA4 API):**
- GA4: sessions, users, engagement rate, conversions, traffic sources
- Google Search Console: organic performance

**Data sources (Phase 2):**
- Booking engine: reservation + revenue data
- Hotjar/Clarity: heatmaps, session recordings (embed or link)
- UTM attribution modelling via GA4

**Agent cron:** Daily GA4 pull (we have the service account pattern from Leamy)
**Output files:** `data/analytics/ga4-daily.json`, `data/analytics/traffic-sources.json`
**Dashboard:** Traffic overview, source breakdown, conversion funnel, landing page performance table

---

### Module 8: Local Events & Demand Calendar
**Page:** `/events`
**Data sources (all scrapeable):**
- Limerick.ie event listings
- Thomond Park fixtures
- University Concert Hall schedule
- UL academic calendar (term dates, exams, open days, graduations)
- TUS Gaelic Grounds events
- National Technology Park conferences
- Eventbrite / Tickets.ie (Limerick region)
- Fáilte Ireland tourism calendar

**Agent cron:** Weekly event scan + daily checks for new additions
**Output files:** `data/events/calendar.json`, `data/events/demand-impact.json`
**Dashboard:** Interactive calendar view, events colour-coded by expected demand impact, historical overlay showing which events actually drove bookings

**Note:** Jack's agent already scrapes some of this via `kilmurry-intel`. We can share the data via the shared reports directory.

---

### Module 9: Email & CRM Performance
**Page:** `/email`
**Data sources (Phase 1 — manual/CSV):**
- Email platform exports (opens, clicks, unsubscribes, revenue per campaign)
- Guest segment definitions (manual)

**Data sources (Phase 2 — API):**
- Mailchimp/ActiveCampaign/Klaviyo API: live campaign data
- PMS guest database: segmentation source
- CRM (if exists): lead tracking, pipeline

**Agent capability:** Recommend send times, subject line A/B suggestions, segment-specific content ideas
**Output files:** `data/email/campaigns.json`, `data/email/segments.json`
**Dashboard:** Campaign performance table, segment breakdown, send time heatmap, AI recommendations panel

---

### Module 10: AI Task Automation Log
**Page:** `/ai-log`
**Data sources (automatic — OpenClaw native):**
- Agent session logs (what was generated, when, by which cron)
- API token usage + cost tracking (we have scripts for this)
- Time-saved estimates (manual benchmarks initially)
- Module usage analytics (which pages Kate visits most)

**Output files:** `data/ai-log/tasks.json`, `data/ai-log/costs.json`
**Dashboard:** Task timeline, cost tracker, usage by module, time-saved calculator

---

## Build Phases

### Phase 1: Foundation + Quick Wins (Week 1)
**Build time:** ~2-3 days with Claude Code
**Delivers:** 4 working pages + agent backend

| Page | Data Source | Method |
|------|-----------|--------|
| `/competitors` | OTA rates, web mentions | Extend existing `kilmurry-intel` skill |
| `/reviews` | TripAdvisor, Google, Booking.com | Web scraping + AI categorisation |
| `/events` | Local event sources | Web scraping (8+ sources) |
| `/ai-log` | OpenClaw native logs | Read agent session/cost files |

**Why these first:** No API keys needed. All powered by web scraping + the agent's existing capabilities. Immediately useful to Kate. Proves value fast.

**Also in Phase 1:**
- Kate's OpenClaw agent set up (separate OS user, Telegram bot)
- Base Next.js app scaffolded (clone Jack's Mission Control pattern)
- Branded with Kilmurry colours
- Responsive (Kate may use phone/tablet)
- Auth: simple password or IP-restricted (localhost + Tailscale if needed)

### Phase 2: Google Integrations (Week 2-3)
**Build time:** ~2-3 days
**Delivers:** 3 more pages with live API data

| Page | Data Source | Method |
|------|-----------|--------|
| `/analytics` | GA4 | Service account (same pattern as Leamy) |
| `/seo` | Search Console + AEO checks | Google API + agent-run AI queries |
| `/content` | Google Trends + event data + brand docs | API + workspace files |

**Requires from Kilmurry:**
- GA4 property ID + service account access
- Google Search Console verification
- Brand voice guide document from Kate

### Phase 3: Paid Media + Revenue (Week 3-4)
**Build time:** ~2-3 days
**Delivers:** 2 pages, deeper data

| Page | Data Source | Method |
|------|-----------|--------|
| `/campaigns` | Google Ads + Meta Ads | API or CSV upload initially |
| `/revenue` | Demand signals + competitor rates | Agent cron + manual PMS data |

**Requires from Kilmurry:**
- Google Ads account access (API key or OAuth)
- Meta Business Manager access
- Decision on PMS data sharing (Jack)

### Phase 4: CRM + Advanced (Month 2+)
**Build time:** ~1 week
**Delivers:** Remaining pages + polish

| Page | Data Source | Method |
|------|-----------|--------|
| `/email` | Email platform API | Depends on which tool they choose |
| Semrush integrations across all pages | Semrush API | ~$120/mo plan needed |
| PMS integration for `/revenue` | RezLynx API | Needs Access Group cooperation |

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Kate's Marketing Control Panel            │
│                    (Next.js on PM2, port :3334)              │
│                                                             │
│  /competitors  /seo  /content  /revenue  /reviews           │
│  /campaigns  /analytics  /events  /email  /ai-log          │
│                                                             │
│  Reads from: /home/kateuser/.openclaw/workspace/data/       │
│  (JSON files populated by Kate's agent crons)               │
└─────────────────────────────────────────────────────────────┘
         ↑                                    ↑
    Kate's Agent                        Shared Data
    (Sonnet, crons)                     (/opt/kilmurry-shared/)
         ↑                                    ↑
    Data Sources                        Jack's Agent
    (web scraping,                      (rate data, events
     Google APIs,                        already being collected)
     review platforms)
```

### Shared vs Isolated Data
- **Kate's agent writes** to `/home/kateuser/.openclaw/workspace/data/`
- **Jack's agent writes** shared data to `/opt/kilmurry-shared/` (competitor rates, events)
- **Kate's dashboard reads** from both (kateuser owns her data, shared dir is group-readable)
- **Jack's Mission Control** remains completely separate on `:3333`

### Jack's Monitoring View
Option: Add a "Marketing Overview" page to Jack's Mission Control that reads Kate's shared output files. Jack gets a summary view without accessing Kate's full dashboard or conversations.

---

## Cost Estimate (Revised)

| Item | Monthly | Notes |
|------|---------|-------|
| RAM upgrade 4GB → 8GB | +$12/mo | Required for two gateways + two dashboards |
| Kate's API usage (Sonnet) | ~$20-40/mo | Higher than initial estimate — more crons |
| Semrush API (Phase 4) | ~$120/mo | Kate/Jack decision — significant but powerful |
| Google APIs | $0 | Free tier covers hotel-scale usage |
| Meta Marketing API | $0 | Free |
| ReviewPro/similar (Phase 4) | ~$50-100/mo | Optional — scraping works for Phase 1-3 |
| **Phase 1-3 total** | **~$32-52/mo** | Before Semrush/ReviewPro |
| **Full platform** | **~$200-290/mo** | With all paid tools |

---

## What to Tell Kate

**Positioning:** Everything on her list is buildable. We deliver it in phases so she gets value immediately (Week 1) while deeper integrations layer on. Each module starts working with freely available data (web scraping, Google APIs) and gets richer as we connect paid tools (Semrush, ReviewPro, PMS).

**Timeline:**
- **Week 1:** 4 pages live (competitors, reviews, events, AI log) + her personal AI assistant on Telegram
- **Week 2-3:** Google integrations (analytics, SEO, content calendar)
- **Week 3-4:** Paid media tracking, revenue intelligence
- **Month 2+:** CRM, Semrush deep integration, PMS connection

**What she needs to provide:**
- Which email/CRM platform they use (or want to use)
- GA4 property access
- Google Ads + Meta account access
- Brand voice guide / campaign pillars document
- Decision on Semrush subscription
- Her preferred communication channel (Telegram recommended)

---

## Reply Draft for Kate

> Hi Kate,
>
> Great to get this — really thorough wishlist! Claude's been earning its keep.
>
> Good news: everything you've outlined is buildable. We'll deliver it as a **Marketing Control Panel** — a web dashboard you can access from any browser, backed by an AI assistant that gathers intelligence and generates insights for you automatically.
>
> Here's the approach:
>
> **Phase 1 (Week 1):** You'll get 4 live pages — Competitive Intelligence, Reviews & Reputation, Local Events Calendar, and an AI Activity Log — plus your own AI marketing assistant on Telegram that you can ask questions and get reports from anytime.
>
> **Phase 2 (Weeks 2-3):** Google integrations go live — Analytics, SEO dashboard, and Content Calendar with Google Trends data.
>
> **Phase 3 (Weeks 3-4):** Paid media tracking and revenue intelligence modules.
>
> **Phase 4 (Month 2+):** Email/CRM performance, and deeper integrations (Semrush, PMS) depending on which tools you decide on.
>
> Each module starts working immediately with freely available data and gets richer as we connect your paid tools.
>
> **What I need from you to get started:**
> 1. Which email marketing platform do you use (or plan to)?
> 2. Do you have GA4 set up on the Kilmurry website?
> 3. Who manages your Google Ads and Meta Ads accounts?
> 4. Can you share your brand voice guide / campaign pillars doc?
> 5. Are you on Telegram? (Fastest way to connect your AI assistant)
>
> Happy to jump on a call Thursday if that suits your offsite day, or I can get started with Phase 1 this week and we iterate from there.
>
> Stephen

---

*This document is the internal build spec. The email to Kate is the client-facing version.*
