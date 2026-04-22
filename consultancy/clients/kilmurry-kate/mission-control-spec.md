# Kate Mission Control - Product Spec

## Purpose
Kate's Mission Control is the operating system for Kilmurry Lodge marketing and commercial visibility.

It is not a generic reporting dashboard. It should help Kate:
- see what matters this morning
- produce and approve content faster
- respond to guest feedback faster
- improve discoverability across Google and AI surfaces
- connect marketing activity to revenue outcome
- retain human control over all AI-assisted work

## Product shape
Six modules:
1. Command centre
2. Content engine
3. Reputation & reviews
4. SEO & visibility
5. Revenue intelligence
6. AI task log

## Core product principles
- Homepage must stay compressed and scannable.
- Each module should correspond to a real operating workflow, not a vanity analytics category.
- AI must always be reviewable, attributable, and interruptible.
- Where direct integrations do not yet exist, v1 should accept manual or CSV-fed inputs instead of pretending automation exists.
- Every panel should lead naturally to an action, not just a metric.

---

## V1 / V2 / V3 roadmap

### V1 - Useful immediately
Build the shell, navigation, visual system, and a practical first version of each module using real data where available and manual ingestion where needed.

Deliver:
- Command centre homepage
- Content engine tracker
- Reviews inbox shell + manual review cases
- SEO visibility scorecard shell
- Revenue intelligence shell
- AI task log + approval queue
- Admin data files / lightweight local storage

### V2 - Automation and enrichment
Add ingestion, automation, and deeper comparisons.

Deliver:
- social post performance sync
- competitor review tracking
- schema checks
- OTA parity / rate comparisons
- richer search and AEO monitoring
- better event ingestion

### V3 - Predictive / assistant layer
Add suggestions, forecasting, and proactive recommendations.

Deliver:
- recommendation engine
- alert thresholds
- AI-assisted summaries per module
- prompt effectiveness ranking
- revenue / event opportunity alerts

---

## Module specs

## 1. Command centre
### Goal
Give Kate one morning screen that answers: what needs attention today?

### V1 panels
1. Occupancy snapshot
   - current occupancy / pickup vs same time last month and last year
   - source: manual CSV or local JSON feed until PMS hookup exists
2. Top 3 tasks due today
   - pulled from AI task log / task store
3. Reputation snapshot
   - review count, average score, latest 3 review cases
4. Revenue vs forecast
   - one red/green status chip with current number and delta
5. Social pulse
   - one metric only, default to reach or engagement
6. Upcoming local events
   - next 14 days shortlist with relevance tag

### UX rule
No deep charts on the homepage. This should feel like a cockpit strip, not a BI tool.

---

## 2. Content engine
### Goal
Turn content from a scattered task into one managed workflow.

### V1 panels
1. Rolling 4-week board
   - statuses: idea, draft, approved, scheduled, live, reviewed
2. Draft brief generator
   - structured form: topic, audience, offer, tone, CTA
   - output: caption draft + image prompt + channel notes
3. Brand voice checker
   - pass / flag against 5 brand pillars
4. Platform router
   - one draft, adapted variants for Instagram / Facebook / LinkedIn / TikTok
5. Asset library
   - tagged assets, filters, upload metadata
6. Post-performance logger
   - manual entry initially: post, date, platform, outcome, notes

### Data model
Primary object: `content_item`
- id
- title
- theme
- status
- target_platforms
- owner
- draft_text
- approved_text
- asset_refs
- publish_date
- performance_notes
- performance_metrics

---

## 3. Reputation & reviews
### Goal
Own guest feedback across platforms and respond faster.

### V1 panels
1. Unified review queue
   - manual ingest to start, grouped by source
2. AI response draft
   - generate response, human approve before send
3. Theme tagging
   - food, rooms, staff, location, events, value, other
4. Negative review escalation
   - auto-highlight under 3 stars
5. Monthly review digest
   - pattern summary and suggested focus area
6. Competitor tracker shell
   - Castletroy Park placeholder with manual comparison entries in v1

### Data model
Primary object: `review_case`
- id
- platform
- rating
- author
- date
- body
- tags
- urgency
- suggested_reply
- approval_status
- response_sent
- competitor_flag

---

## 4. SEO & visibility
### Goal
Make discoverability legible and actionable.

### V1 panels
1. Keyword cluster board
   - rooms, weddings, dining, events, Ryder Cup
2. AEO readiness scorecard
   - proxy score built from content coverage, schema coverage, GBP freshness, entity mention checks
3. Schema health card
   - manual or fetched validation results
4. Content gap list
   - topics / queries lacking dedicated pages
5. Backlink monitor shell
   - manual comparison log vs Castletroy Park initially
6. Google Business Profile pulse
   - photos, posts, Q&A, review recency

### Important note
AEO score must be explicitly presented as a proxy, not fake precision.

---

## 5. Revenue intelligence
### Goal
Show whether marketing and demand signals are improving commercial outcome.

### V1 panels
1. Rate comparison board
   - tonight + next 30 days, manual entries acceptable initially
2. Demand calendar
   - local events, conferences, graduations, sports, Ryder Cup milestones
3. OTA parity checker
   - manual parity log to start
4. Direct booking share tracker
   - monthly ratio trend
5. Campaign ROI logger
   - spend, channel, campaign, result, notes
6. Ryder Cup 2027 milestone panel
   - booking-window milestones and prep tasks

### Data model
Primary objects:
- `rate_snapshot`
- `demand_event`
- `campaign_entry`
- `booking_share_period`

---

## 6. AI task log
### Goal
Create trust, auditability, and learning around AI-assisted work.

### V1 panels
1. Output log
   - every AI-generated caption, response, brief, report
2. Approval queue
   - nothing publishes without human sign-off
3. Prompt library
   - saved reusable prompts
4. Feedback loop
   - mark good / bad / needs edit
5. Team activity feed
   - who approved what and when
6. Monthly AI summary
   - tasks completed, time saved estimate, error / rework rate

### Data model
Primary object: `ai_task`
- id
- type
- prompt
- output_summary
- linked_entity_type
- linked_entity_id
- created_by
- created_at
- approval_status
- approved_by
- feedback
- reusable_prompt_flag

---

## Technical recommendation
- Next.js 14 app router
- Tailwind
- TypeScript
- local JSON or SQLite-backed store for v1
- modular cards and detail drawers
- file-based seed data for fast iteration

## V1 build order
1. Shell, nav, module cards, overall theme
2. Command centre
3. AI task log
4. Content engine
5. Reputation & reviews
6. Revenue intelligence
7. SEO & visibility

Reason: command centre and AI task log define the product frame. Content + reviews are highest practical value. SEO/revenue are partly integration-constrained, so start with honest shells fed by local data.

## Honest integration posture
For Kate's MC, v1 should be explicit about data state:
- live
- manually updated
- placeholder / awaiting integration

That is better than fake automation.
