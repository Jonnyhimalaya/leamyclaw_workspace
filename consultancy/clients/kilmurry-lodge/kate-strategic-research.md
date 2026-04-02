# Kate Marketing Control Panel — Strategic Research
**Date:** 2026-04-02
**Purpose:** Community wisdom + industry best practices to make this a banger

---

## 🔑 Key Strategic Insights

### 1. Bidirectional Dashboard Pattern (Community Best Practice)
The top-performing Mission Control builds in the OpenClaw community are **bidirectional** — the agent writes data, the human reviews and approves/rejects through the dashboard, and the agent reads those decisions back.

**Apply to Kate's panel:**
- Review responses: agent drafts → Kate approves/edits in dashboard → agent posts
- Content briefs: agent generates → Kate approves → goes to content calendar
- Rate recommendations: agent suggests → Kate/Jack approves → logged as decision
- Campaign ideas: agent proposes → Kate accepts/modifies → becomes task

This turns the dashboard from a passive display into an **active workflow tool**. Kate doesn't just read — she acts.

### 2. File-Based Architecture (Proven Pattern)
TenacitOS (500+ stars) proves the pattern: **OpenClaw IS the backend.** No database needed.
- Agent writes structured JSON to `data/` directories
- Next.js API routes read those files
- Dashboard renders them with React components
- Zero extra infrastructure, zero sync issues

**Our architecture should follow this exactly:**
```
Kate's agent (cron jobs) → writes JSON to workspace/data/
Next.js API routes → read from workspace/data/
React pages → render with charts/tables/calendars
Kate's actions → write back to workspace/data/actions/
Kate's agent → reads actions, executes approved ones
```

### 3. AEO — The Killer Differentiator
Kate specifically asked for AEO (AI Engine Optimization) — tracking how Kilmurry appears in ChatGPT, Perplexity, Gemini recommendations. This is bleeding-edge stuff.

**hotelrank.ai** is the emerging SaaS for this (~$X/mo), but we can build it ourselves:
- Agent queries ChatGPT/Perplexity/Gemini: "best hotels in Limerick", "hotels near University of Limerick", "Limerick hotel for business travel"
- Logs whether Kilmurry appears, at what position, what was said about it
- Tracks competitor mentions in the same queries
- Plots visibility over time

**Why this is huge:** 44% of travelers now use AI for hotel discovery. 70% of AI recommendation links are direct (not OTA). If Kilmurry ranks well in AI recommendations, it bypasses Booking.com's commission entirely. This alone could justify the entire platform investment.

**Implementation:** Cron job using OpenClaw's own AI capabilities:
```
Daily at 6am → query 10-15 target prompts across 3 AI platforms
→ parse results for Kilmurry mentions, position, sentiment
→ write to data/aeo/YYYY-MM-DD.json
→ dashboard shows visibility trends over time
```

### 4. Review Management — Don't Reinvent, Augment
Industry tools (MARA, ReviewPro, GuestRevu, Birdeye) charge $50-200/mo for review aggregation + AI responses. We can replicate 80% of this:

**Phase 1 (free, scraping):**
- Google Business Profile reviews via GBP API (free, official)
- TripAdvisor: scrape public reviews (their API only returns 3 per location — useless)
- Booking.com: scrape from extranet or public page

**Agent workflow:**
1. Scrape new reviews (twice daily)
2. Categorise by theme (room, food, service, location, value, staff)
3. Score sentiment (positive/negative/neutral)
4. Draft response in brand voice
5. Write to dashboard for Kate's approval
6. Kate edits/approves → response ready to post

**The approve/post workflow in the dashboard is the key UX differentiator.** Kate opens the panel, sees 3 new reviews with draft responses, tweaks one, approves all three, done. 5 minutes instead of 45.

### 5. Event Calendar — Underrated Value
Kate's Module 8 (Local Events & Demand Calendar) sounds simple but is actually one of the highest-value modules for a hotel:

**Sources we can scrape:**
- Limerick.ie events
- Thomond Park (Munster Rugby fixtures, concerts)
- University Concert Hall schedule  
- UL academic calendar (graduations = hotel demand spike)
- TUS Gaelic Grounds
- Eventbrite Limerick region
- National Technology Park conferences
- Fáilte Ireland campaign periods

**The magic:** Overlay events against historical booking data (when PMS connected) to show which events actually drive bookings vs which don't. This turns a simple calendar into a **demand forecasting tool**.

**Phase 1:** Just the calendar with manual demand impact tags
**Phase 2:** Automated demand scoring when PMS data is available

### 6. Tech Stack Recommendations (from Community)

**Proven Mission Control stack:**
- Next.js 15 (App Router)
- Tailwind CSS v4
- shadcn/ui (component library — beautiful, consistent, fast to build)
- Recharts or Chart.js (data visualisation)
- date-fns (date handling for calendars)
- lucide-react (icons)

**Don't need:**
- Convex or any real-time DB — file-based is sufficient for our update frequency
- WebSockets — cron-based data refresh is fine (Kate doesn't need second-by-second updates)
- Complex auth — simple password protection with rate limiting (TenacitOS pattern)

**Consider:**
- React Big Calendar for the events/content calendar view
- DnD Kit for drag-and-drop content calendar management
- Framer Motion for smooth transitions (makes it feel premium)

### 7. Google API Integration Pattern
We already have GA4 service account working for Leamy Maths. Same pattern for Kilmurry:

**APIs to connect (all free tier):**
| API | What it gives us | Quota |
|-----|-----------------|-------|
| GA4 Data API | Sessions, users, conversions, traffic sources | 10K requests/day |
| Search Console API | Impressions, clicks, CTR, position by query | 6K rows/request |
| Google Ads API | Impressions, clicks, CPC, conversions | 15K requests/day |
| GBP API | Reviews, ratings, business info | Generous |

**All use the same service account pattern** — one credentials file, multiple API scopes.

### 8. Semrush — Worth It But Phase 4
Semrush API starts at ~$120/mo (Guru plan). It's powerful but expensive for a Phase 1 launch. 

**What we can do WITHOUT Semrush:**
- Keyword position tracking → Google Search Console (free, actual data)
- Site audit → Google Lighthouse CLI (free, run via cron)
- Competitor traffic estimates → SimilarWeb free tier or scrape
- Backlink monitoring → Google Search Console shows linking domains

**What we genuinely NEED Semrush for:**
- Competitor keyword rankings (what terms competitors rank for that Kilmurry doesn't)
- Competitor ad copy analysis
- Content gap analysis
- Comprehensive backlink profiles

**Recommendation:** Launch without Semrush, add it in Phase 4 when Kate has proven the dashboard's value to Jack. The free tools cover 70% of the SEO module.

---

## 🏗️ Revised Build Strategy

### Architecture Upgrades Based on Research

1. **Bidirectional workflow** — every module that generates drafts gets an approve/edit/reject cycle
2. **AEO monitoring built-in from Day 1** — this is our competitive moat vs off-the-shelf tools
3. **File-based backend** — proven at scale by TenacitOS and others, no extra DB
4. **shadcn/ui + Recharts** — beautiful, fast to build, consistent design language
5. **Simple auth** — password + rate limiting, not OAuth/SSO complexity

### Priority Reorder (Based on Research)

**Week 1 — Highest Impact:**
1. `/reviews` — Review management with approve workflow (biggest immediate time saver)
2. `/events` — Local events calendar (demand context for everything else)
3. `/competitors` — Rate comparison (extends Jack's existing scraping)
4. `/aeo` — AI visibility monitoring (differentiator, no one else has this)

**Week 2:**
5. `/analytics` — GA4 dashboard (once service account is set up)
6. `/seo` — Search Console + AEO combined view
7. `/content` — Content calendar with AI brief generation

**Week 3-4:**
8. `/campaigns` — Paid media tracker (CSV upload initially, APIs later)
9. `/revenue` — Demand intelligence overlay
10. `/ai-log` — Agent activity and cost tracking

### New Module: `/aeo` (Not in Kate's Original 10 — We Add It)
Kate mentioned AEO inside Module 2 (SEO), but it deserves its own page. This is the module that will blow her mind — no hotel in Limerick is tracking this yet. We're ahead of the curve.

---

## 💰 Competitive Positioning

What Kate described is essentially what these SaaS tools charge:
| Tool | What it does | Monthly cost |
|------|-------------|-------------|
| ReviewPro | Review aggregation + sentiment | $100-200/mo |
| OTA Insight/Lighthouse | Rate shopping | $200-500/mo |
| Semrush | SEO + competitive intel | $120-230/mo |
| Hotelrank.ai | AEO visibility | ~$50-100/mo |
| Birdeye/MARA | Review management + AI responses | $100-300/mo |
| Looker Studio (custom) | Analytics dashboards | Free but needs dev |
| **Total SaaS equivalent** | | **$570-1,330/mo** |

**Our build:** ~$30-50/mo (API costs + server resources) + our consultancy time
**Kate gets:** 80-90% of the functionality at 5% of the SaaS cost, fully customised to Kilmurry, and an AI assistant that actually does the work (not just displays data)

This is the consultancy value proposition in action.

---

## 🎯 What Makes This a "Banger"

1. **AEO monitoring** — nobody in Limerick hospitality is doing this. First-mover advantage.
2. **Bidirectional review workflow** — approve responses in 2 clicks, not 20 minutes
3. **Event-driven demand forecasting** — "Munster play Saturday → rooms should be +15%"
4. **AI that writes, not just displays** — content briefs, review responses, rate suggestions, social copy
5. **Beautiful UI** — shadcn/ui + Recharts looks premium, feels like a $1000/mo SaaS
6. **Kate's personal AI on Telegram** — ask questions, get instant answers from the data
7. **Jack's oversight** — summary view on his Mission Control, full transparency
8. **Built on our proven stack** — not a prototype, same architecture that runs Jack's dashboard

This isn't just a dashboard. It's a **marketing operations platform** that happens to have an AI brain behind it.
