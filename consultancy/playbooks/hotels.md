# Hotels & Hospitality Playbook
**Purpose:** Comprehensive playbook for designing and deploying agentic AI systems in hotels and hospitality businesses. Built from real-world deployments, not theory.

---

## Why Hotels Are a Strong Fit for Agentic AI

Hotels are operationally complex but highly repetitive. They typically have:
- Constant customer communication across multiple channels
- Many recurring workflows that follow predictable patterns
- Fragmented technology stacks with poor integration
- Review and reputation pressure requiring fast response
- Booking, occupancy, and revenue coordination across departments
- Event-driven demand changes requiring anticipation, not reaction
- Managers overloaded by exceptions and follow-up
- Deep institutional knowledge trapped in individual staff members' heads
- Multiple revenue streams (rooms, F&B, events, venues) needing different treatment

This makes them excellent candidates for agentic design — but the deployment must respect how hotels actually work: around people, not systems.

---

## The Golden Principle: Observe First, Automate Later

The most successful hotel AI deployments follow a strict progression:

**Phase 1 — Intelligence Layer** (Weeks 1-4)
- Monitor, scrape, aggregate, summarise
- No system writes, no guest-facing output
- Build trust through accurate observation

**Phase 2 — Draft & Recommend** (Weeks 4-8)
- AI drafts responses for human review
- Recommendations with reasoning
- Human approves everything before it goes live

**Phase 3 — Autonomous (Guardrailed)** (Month 3+)
- Auto-send within defined safe zones
- Escalation rules for edge cases
- Human oversight remains on high-stakes decisions

Skipping phases destroys trust. Hotels are reputation businesses — one bad automated guest response can undo months of goodwill.

---

## Typical Hotel Pain Points

### Front Desk & Guest Communication
- Repetitive FAQs consuming reception time
- Missed follow-up on enquiries
- Slow response times losing bookings
- Inconsistent guest communication tone
- Pre-arrival information sent too late or not at all
- Reception staff spending time on tasks that don't require human judgment

### Reviews & Reputation
- Reviews scattered across 4-6 platforms with no unified view
- Responses slow (>48 hours) or non-existent
- Patterns in complaints not surfaced to management
- No structured sentiment tracking over time
- F&B ratings often lower than accommodation — the weak spot many hotels ignore

### Revenue Management
- Pricing decisions reactive instead of proactive
- Revenue managers carrying dozens of unwritten rate rules in their heads
- Competitor monitoring inconsistent or manual
- Event-driven demand not anticipated early enough
- Rate inquiry responses taking 15-25 minutes each, consuming 4-8 hours daily
- Revenue management systems (RMS) often under-used or over-ridden
- No systematic tracking of why business is lost

### Sales & Corporate
- Pipeline lives in the sales manager's head and scattered emails
- No visibility into enquiry-to-booking conversion
- Lost business not tracked — no feedback loop on why deals went elsewhere
- Contact databases large but dirty (10K-30K contacts, mostly untouched)
- Proposal generation manual and time-consuming

### Operations
- Maintenance issues tracked informally (WhatsApp, memory, sticky notes)
- Housekeeping coordination friction during busy periods
- Handover notes inconsistent between shifts
- No single daily operations view for management
- Energy monitoring data available but not acted upon

### Management Visibility
- GM/proprietor spends time chasing updates from multiple people/systems
- Reports are manual and produced infrequently
- No single command centre view of the entire operation
- Financial data siloed in accounting software

### Multi-Venue Complexity
Many independent hotels aren't just hotels — they're ecosystems:
- Restaurants (potentially multiple, each with different identity)
- Bars and entertainment venues
- Event/wedding spaces at multiple capacity levels
- Self-catering or extended-stay apartments
- Conference and corporate facilities
- Each venue needs different content, different pricing, different operational attention

The playbook must treat multi-venue properties as multi-business operations, not monolithic "hotels."

---

## The Institutional Knowledge Problem

**This is the most underestimated challenge in hotel AI deployment.**

Hotels with long-tenure staff (10-30+ years) have enormous amounts of operational knowledge that exists nowhere except in people's heads:
- Unwritten rate rules and exceptions (dozens to hundreds)
- Supplier relationships and negotiation history
- Guest preferences and VIP handling protocols
- Seasonal patterns and local event impacts
- "How we actually do things" vs "how the manual says"

**Before you can automate anything, you must codify this knowledge.**

### The Knowledge Capture Framework
1. **Identify the carriers** — who holds institutional knowledge in each department
2. **Conduct structured discovery conversations** (30-40 min each, relaxed, not interrogative)
3. **Document the unwritten rules** — especially rate exceptions, supplier knowledge, guest handling
4. **Validate with the knowledge carrier** — "Is this what you actually do?"
5. **Store in searchable format** — the AI needs this as its reference material

Key discovery questions for knowledge carriers:
- "Walk me through a typical Tuesday from arrival to leaving"
- "What's the single task that eats the most time?"
- "If you were training your replacement, what are the top 10 things they'd need to know that aren't written anywhere?"
- "How often do you override the system's recommendations? When and why?"
- "If AI freed up 3-4 hours of routine work, what would you do with that time?"

The last question is critical — it reveals what the person actually values and where they'd reinvest freed capacity.

---

## Time Redeployment: Design WITH People, Not FOR Them

A common mistake: designing AI workflows based on management's vision of how staff should work, without asking staff what they actually need.

**The Time Redeployment Process:**
1. Survey each key role: how they spend time today (percentages across screen work, calls, face-to-face, thinking time)
2. Identify the "time sinks" — tasks they'd happily never do again
3. Identify the "value work" — tasks they'd do more of if they could
4. Map AI capabilities to time sinks, freeing capacity for value work
5. Let the person define what "better" looks like for their role

**Department-specific questions matter.** A revenue manager's frustrations are completely different from a financial controller's. Generic surveys produce generic results.

**The principle:** Don't design people's futures for them. Design WITH them. The first version is your vision. The second is theirs. The third — the blend — is what actually works.

---

## Revenue Management: The Highest-Value Agent Domain

Revenue management is consistently the highest-impact area for hotel AI deployment. It's also the most complex.

### Why Revenue Management Is Special
- A single skilled revenue manager may handle 15-30 rate enquiries per day
- Each enquiry follows a pattern: check RMS → check PMS → apply unwritten rules → draft response → send
- The "unwritten rules" are the real rate engine — often 30-50+ exceptions the RM carries in memory
- Revenue management systems frequently have their recommendations overridden
- API access to RMS platforms is often refused — browser automation may be the only path
- The revenue impact of getting pricing right is enormous (€100K+ annual swing for mid-size properties)

### Revenue Agent Architecture
**Phase 1: Intelligence Layer**
- Competitor rate monitoring (many booking engines are scrapeable)
- Event calendar with demand impact scoring
- Occupancy trend analysis
- Rate enquiry pattern recognition

**Phase 2: Draft & Recommend**
- AI-drafted rate responses for RM review
- Rate recommendations with reasoning
- Exception flagging ("this enquiry matches corporate rate pattern X")
- Time saved: 15-25 min per enquiry → 3-5 min (review and send)

**Phase 3: Autonomous (Guardrailed)**
- Auto-draft standard enquiries
- Escalate non-standard to human
- RM still approves all guest-facing responses

### Competitor Rate Scraping
Many hotel markets share common booking engine platforms. In some markets, 4-6 competitors use the same underlying system, making standardised rate scraping straightforward.

Common patterns:
- Booking engines often geo-default currency based on server location — always force the local currency parameter
- Cookie sessions may be required for fetching data
- Rate data should feed into event calendar context for correlation
- Build a competitive rate dashboard showing your property vs competitors across date ranges

### The Rate Knowledge Codification Project
Before building a rate agent:
1. Document every unwritten rate rule the RM carries
2. Catalogue corporate rate agreements
3. Map seasonal adjustments and their triggers
4. Record override patterns (when does the RM ignore the RMS?)
5. This becomes the AI's "rate brain" — without it, the agent is useless

---

## Sales Pipeline & Lost Business Analysis

These two systems work as a pair and create a powerful feedback loop.

### Sales Pipeline
Most independent hotels manage corporate sales through memory, email, and intuition. Building a structured pipeline changes this:

**Pipeline stages:** Enquiry → Proposal → Negotiation → Won/Lost
**Track:** stage, value, owner, age, stall points
**Surface:** conversion rate, average deal size, time-to-close, stalled deals

Use the CRM the hotel already has (many have dormant HubSpot or similar free accounts with thousands of contacts). Clean the data before building the pipeline.

### Lost Business Analysis
**This is the system most hotels don't have and desperately need.**

When a deal goes to a competitor, capture:
- Who was it?
- What was the value?
- Why did we lose? (Rate / Availability / Competitor / Timing / Quality / Slow Response)
- Who won?

Monthly pattern report: "We lost €47K this month. 40% rate-driven, 30% went to Competitor X, 20% availability, 10% slow response."

**Implementation rules:**
- Logging a lost deal must take under 60 seconds or adoption fails
- Pre-define reason categories (don't make the sales person write an essay)
- Build into the CRM pipeline as a "Lost" stage with custom fields
- Agent analyses patterns and produces monthly trend reports

---

## Customer Data Platform on a Budget

Enterprise CDPs (Sitecore, etc.) cost €50-200K/year. Independent hotels can build 80% of the capability from free tools:

### The Free-Tier Stack
1. **CRM** (HubSpot Free) — contact profiles, pipeline, email
2. **Session Replay + Heatmaps** (Microsoft Clarity) — free, unlimited traffic, frustration detection
3. **Web Analytics** (GA4) — traffic, sources, behaviour
4. **Data Pipeline** (Segment Free / RudderStack self-hosted) — connect website behaviour to CRM
5. **Booking Funnel Tracker** — custom JS snippet tracking the path from website to booking engine handoff

### Propensity Scoring
Once data flows into the CRM:
- Score contacts based on signals: website visits (+20), email opens (+10), past booking (+30), no engagement for 90 days (-15)
- Start rule-based, evolve to ML when enough data exists
- Surface "hottest leads" weekly to the sales team
- Validate scores against the sales person's instinct in Month 1

---

## Digital Experience Analytics

Most hotels have no visibility into how website visitors behave. The booking funnel — from browsing to the booking engine handoff — is a black box.

### The Budget Analytics Stack
1. **Microsoft Clarity** (free) — install in 30 minutes, immediate session replay and heatmaps
2. **Custom Booking Journey Tracker** — JS snippet tracking key funnel events
3. **Funnel Dashboard** — visualise drop-offs with estimated revenue impact
4. **Frustration Detection** — rage clicks, dead clicks, rapid back-navigation
5. **AI Interpretation** — weekly agent analysis: "Mobile checkout abandonment is 60%. The booking engine handoff is losing an estimated €X/week"

The critical insight: the booking engine is usually a third-party system (hosted externally). Tracking the handoff from the hotel website to the booking engine is the hardest part — and the most valuable.

### Quantify Everything in Revenue Impact
Don't say "the mobile experience is bad." Say "mobile booking abandonment at the checkout step costs an estimated €3,200/month based on traffic volume and average booking value." Hotels respond to revenue language.

---

## The Operating Model Drives Agent Architecture

**Critical lesson: the hotel's own organisational structure should define agent boundaries.**

Don't impose a generic agent team. Map the hotel's departments and let those become the agent domains:

Typical hotel department structure:
1. Sales & Revenue
2. Brand & Marketing
3. F&B and Events
4. Kitchen
5. People, Culture & Compliance
6. Facilities & Maintenance
7. Rooms Division
8. Technology
9. Finance & Accounts

Each department = a potential agent boundary. Each RACI line in the org chart = an orchestration rule.

**If the hotel has a formal operating model, don't build agent boundaries that contradict it.** The AI system should mirror how the humans actually work.

---

## The Human Orchestrator Model

A common assumption: the AI orchestrator sits at the centre, delegating to agents and reporting to management.

**Better model: specific humans own specific domains.** The AI serves each human within their domain:

- The **Marketing Consultant** is the marketing orchestrator — the AI feeds intelligence, drafts content, monitors competitors. The human makes creative decisions.
- The **Revenue Manager** owns pricing — the AI monitors rates, drafts responses, flags anomalies. The human sets strategy and approves.
- The **Sales Manager** owns relationships — the AI tracks pipeline, researches prospects, prepares briefings. The human builds trust.
- The **GM** gets the unified view — the AI aggregates across all domains into a daily briefing.

The AI isn't replacing the orchestration layer — it's providing each human orchestrator with superpowers.

### The Golden Rule for AI-Human Collaboration
**When rejecting AI output, ALWAYS explain WHY.**

"No" means nothing to a model. "No, because..." is training data.
- ❌ "I don't like this" → ✅ "The tone is too formal for our bar venue. Rewrite with playful energy."
- ❌ "Doesn't look right" → ✅ "This describes white tablecloths but our space is wooden benches and fairy lights."
- ❌ "Too corporate" → ✅ "This feels like a chain hotel ad. We need warmth — think Sunday with friends."

Train every team member who reviews AI output on this principle. Every explained rejection improves the next output.

---

## Suggested Hotel Agent Team

### Orchestrator
**Role:** Management-facing command layer
**Main interface:** Telegram / WhatsApp / Mission Control
**Purpose:** Unified summary, delegation, escalation, reports

### Specialist Agents

#### 1. Revenue Intelligence Agent
- Competitor rate monitoring and scraping
- Event-driven demand signals
- Rate enquiry draft responses
- Occupancy trend analysis
- Lost business pattern reporting
- Weekly/monthly revenue intelligence briefing

#### 2. Guest Communications Agent
- Pre-arrival information and confirmations
- FAQ handling and routine enquiries
- Post-stay follow-up and review prompts
- Communication tone consistency
- Escalation of complaints and unusual requests

#### 3. Reputation & Review Agent
- Multi-platform review monitoring (TripAdvisor, Google, Booking.com, Facebook)
- Sentiment classification and urgency scoring
- Response drafts for human approval
- Operational pattern detection (recurring complaints by category)
- Weekly reputation summary with trend tracking

#### 4. Sales Pipeline Agent
- Enquiry-to-booking tracking
- Pipeline health monitoring
- Prospect research and briefing preparation
- Proposal draft generation
- Lost business capture and analysis
- CRM data quality monitoring

#### 5. Operations & Maintenance Agent
- Issue logging and categorisation
- Urgency routing
- Status board maintenance
- Shift handover summaries
- Housekeeping coordination support
- Energy/utility monitoring integration

#### 6. Marketing & Content Agent
- Social media content generation
- Campaign performance tracking
- SEO monitoring and recommendations
- Website content suggestions
- Event and promotion tie-ins
- Brand voice consistency across venues

#### 7. Intelligence Scout Agent
- Local event monitoring
- Competitor activity tracking
- Tourism and travel trend research
- Market intelligence aggregation
- Media mention tracking

---

## Mission Control: The Hotel Command Centre

A web-based dashboard that gives management a single view of the entire operation.

### Recommended Modules
- **Daily Briefing** — arrivals, departures, occupancy, issues, events
- **Revenue Dashboard** — rates, competitor comparison, demand signals, pipeline value
- **Reputation Monitor** — recent reviews, sentiment trends, response queue
- **Guest Communications Queue** — pending, sent, escalated
- **Operations Board** — maintenance issues, housekeeping status, handover notes
- **Events Calendar** — local events with demand impact scoring, colour-coded by type
- **Sales Pipeline** — stages, values, stalled deals, lost business trends
- **Agent Activity Feed** — what each agent has done, reports produced
- **Analytics** — website traffic, booking funnel, session replay insights
- **Team Directory** — human team + AI agents with roles and status

### Build Approach
- Start with static/hardcoded data to prove the concept (Week 1)
- Connect live data sources progressively (Weeks 2-8)
- Use the dashboard as the proof-of-value artifact for the client

---

## The Intelligence Skill Pattern

The most reusable agent pattern for hotels: a unified intelligence sweep that combines multiple data sources into a single briefing.

### Architecture
Run 4-6 parallel sub-agents, each targeting a different intelligence domain:
1. **Rate Scout** — competitor booking engine prices for upcoming dates
2. **Event Scanner** — local events, conferences, sports, university activity
3. **Review Platforms** — new reviews across all platforms
4. **Social & Forums** — Reddit, Twitter/X, local community mentions
5. **Competitor Activity** — competitor website changes, new promotions, social posts

### Output
- Telegram/WhatsApp summary for the proprietor (concise, actionable)
- HTML dashboard with full detail (browseable, visual)
- Structured JSON data for other agents to consume

### Scheduling
- Daily morning briefing (arrival-focused) — 7am
- Weekly deep intelligence report (strategic) — Monday morning
- Rate intelligence refresh — weekly or bi-weekly
- Server health monitoring — every 4 hours

---

## Technology Stack Patterns

### Common Hotel Tech Stacks
- **PMS:** RezLynx, Opera, Mews, Guestline, Cloudbeds
- **RMS:** Right Revenue, Duetto, IDeaS, Atomize
- **HR:** Alkimii, Deputy, Rotacloud
- **Accounting:** Sage, Xero, MYOB
- **CRM:** HubSpot (often dormant), Salesforce (rare for independents)
- **Booking Engine:** Usually provided by PMS vendor or Net Affinity
- **Channel Manager:** SiteMinder, D-EDGE
- **Review Management:** GuestRevu, ReviewPro, TrustYou
- **Meeting/Transcription:** Fireflies.AI, Otter.ai

### Integration Reality
- **API access is often refused** by hotel-tech vendors, especially RMS platforms
- **Browser automation** (Playwright/Puppeteer) is frequently the only integration path
- Plan for this from the start — don't assume APIs will be available
- Cookie sessions, geo-currency defaults, and anti-scraping measures are common hurdles

### AI Tools Already in Use
Many hotels are already using:
- Claude/ChatGPT Teams for document work and strategy
- Fireflies.AI for meeting transcription
- AI image/video tools for marketing content
- SharePoint or Google Workspace for knowledge management

**Don't compete with these.** The agentic system complements existing AI usage:
- **Teams/ChatGPT:** Strategy documents, financial workbooks, one-off analysis
- **Agentic system:** Autonomous monitoring, scheduled tasks, 24/7 intelligence, dashboards, multi-agent coordination

Position them as complementary, not competing. The agentic system handles what can't be done in a chat window.

---

## Compliance & Change Management

### EU AI Act (Article 50 — Transparency)
- Required by August 2026
- Hotels using AI must disclose to guests and staff
- Define: when is a guest interacting with AI vs a human?
- Review all AI-generated guest communications for transparency requirements

### GDPR Considerations
- Identify the Data Protection Officer (DPO) early
- No guest PII in AI training data
- Review data processed by each agent
- Session replay tools (Clarity) anonymise by default — but add to privacy policy
- Staff consent required for any data used in AI workflows
- Regular audits of AI system outputs

### Staff Buy-In
The human side of deployment matters as much as the technical side:

1. **Frame it right:** "We're building tools to make your work better" — not "we're automating your job"
2. **Ask before building:** Time redeployment questionnaires before designing workflows
3. **Start with internal wins:** Summaries, monitoring, reports — things that help staff before touching guest-facing work
4. **Validate with instinct:** Let experienced staff validate AI recommendations against their judgment in Month 1
5. **Celebrate the human:** The AI makes them more effective, not less important

### Key Risk: The "Diminished Role" Perception
If AI frees up 3-4 hours daily for key staff, there's a real risk people feel their roles are diminished rather than elevated. Counter this by:
- Having each person define what they'd do with freed time
- Framing freed time as investment in higher-value work
- Ensuring the AI makes them look good, not replaceable

---

## Approval Model

### Safe to Automate Early
- Internal summaries and briefings
- Monitoring and intelligence gathering
- Report generation and dashboards
- Draft replies and proposals (for human review)
- Internal reminders and handover notes
- Data aggregation and pattern detection

### Approve-Then-Act
- Guest-facing replies and communications
- Rate recommendations and pricing changes
- Outbound marketing campaigns
- Operational escalation messages
- Social media posts
- Review responses

### Do Not Automate Early
- Refunds or compensation offers
- Rate changes directly in PMS without approval
- Booking modifications with financial implications
- Anything legally or reputationally sensitive
- Guest complaint responses (always human-reviewed)
- Anything involving guest PII

---

## Hotel Discovery Process

### Phase 0: Pre-Engagement Research
Before the first meeting:
- Audit their website (score /10, identify broken pages, schema errors)
- Check AI visibility (how do they appear in ChatGPT/Claude/Perplexity searches?)
- Scan review platforms (TripAdvisor, Google — overall score, F&B score, recent trends)
- Check social presence (content frequency, engagement, platform coverage)
- Identify competitors and their digital presence
- Map the tech stack from visible clues (booking engine, website platform)

### Phase 1: Discovery Conversations
- **With the proprietor/GM:** Vision, strategy, pain points, budget, timeline
- **With department heads:** How they actually work, what frustrates them, where knowledge lives
- **With the tech person (if any):** Current stack, integration possibilities, constraints

### Phase 2: Architecture Design
- Map departments to agent boundaries
- Identify which workflows to target first (use the pilot heuristic below)
- Design the approval model
- Plan Mission Control modules
- Estimate server requirements

### Phase 3: Deployment
- Server setup and hardening
- Agent identity and memory configuration
- Intelligence layer first (observation only)
- Dashboard proof of concept
- Progressive capability rollout

---

## Discovery Questions by Domain

### Guest Journey
- How do enquiries arrive? (email, phone, web form, WhatsApp, walk-in)
- How do bookings arrive? (direct, OTA, corporate, events)
- What is the pre-arrival process?
- What are the most common guest questions?
- How are complaints handled and escalated?
- How is post-stay follow-up done?
- Is there a guest preference or loyalty tracking system?

### Revenue
- Who manages pricing? How many rate enquiries per day?
- How many "unwritten rules" exist for pricing? Who carries them?
- Which revenue management system is used? Is it under-utilised or over-ridden?
- Can the RMS be accessed via API? (Usually no — plan for browser automation)
- How is competitor pricing monitored?
- How do local events impact demand? Is there an event calendar?
- What percentage of bookings are direct vs OTA?

### Sales
- How is the corporate pipeline managed? (CRM? Memory? Email?)
- What happens when a deal is lost? Is the reason captured?
- How many active corporate relationships exist?
- What does the contact database look like? (Size, quality, consent status)
- Who handles proposals? How long do they take?

### Operations
- How is housekeeping coordinated?
- How are maintenance issues tracked and routed?
- How do shifts/handovers work?
- What gets dropped when the hotel is busy?
- Is there energy monitoring? Is the data being used?

### Technology
- PMS? RMS? Channel manager? Booking engine?
- CRM? (Often dormant — check for existing HubSpot/Salesforce)
- Website platform? (WordPress, Squarespace, custom)
- Analytics? (GA4 often exists but is unconfigured/ignored)
- Collaboration tools? (SharePoint, Google Workspace, Slack)
- Existing AI tools? (Claude Teams, ChatGPT, Fireflies, etc.)

### People & Culture
- Who has been here longest? Where does institutional knowledge live?
- How does the team feel about AI? (Excited, cautious, nervous, disengaged)
- Is there a DPO or compliance officer?
- What training or change management has been done?
- Are there long-tenure staff whose knowledge needs capturing urgently?

---

## Pilot Recommendation Heuristic

### Best first pilot if the revenue manager is overloaded
Start with **Revenue Intelligence Agent** — competitor monitoring, event calendar, rate enquiry drafting. Highest time savings, highest revenue impact.

### Best first pilot if review scores are declining
Start with **Reputation & Review Agent** — unified monitoring, response drafting, sentiment tracking. Visible improvement, low risk.

### Best first pilot if the GM is overwhelmed
Start with **Daily Briefing + Mission Control** — aggregate everything into one view. Transforms management leverage.

### Best first pilot if the hotel is events-driven
Start with **Intelligence Scout** — event monitoring, demand signals, competitor activity. Directly impacts revenue decisions.

### Best first pilot if the front desk is drowning
Start with **Guest Communications Agent** — FAQ handling, pre-arrival comms, routine enquiry responses. Immediate time savings.

### Best first pilot if sales pipeline is invisible
Start with **Sales Pipeline Agent** — CRM setup, pipeline tracking, lost business capture. Creates visibility that didn't exist.

### Quick Wins (Do These Regardless)
1. **Microsoft Clarity installation** — 30 minutes, free, immediate session replay (do this on Day 1)
2. **GA4 connection** — surface website metrics in dashboards
3. **Daily morning briefing** — even a basic one immediately proves value
4. **Review monitoring** — aggregate reviews from all platforms into one feed

---

## Common Workflow Automation Patterns

| Workflow | Agentic Pattern | Value |
|---|---|---|
| Rate enquiry response | Monitor inbox → draft response → human review → send | 70-80% time reduction per enquiry |
| Review response | Monitor platforms → classify → draft → approve → post | Faster response, consistent tone |
| Daily operations briefing | Aggregate data → summarise → deliver to GM | Management leverage |
| Event demand monitoring | Scan sources → flag → score impact → recommend | Proactive pricing |
| Competitor rate tracking | Scrape booking engines → compare → alert on changes | Revenue intelligence |
| Sales pipeline management | Log enquiry → track stages → surface stalled deals → report | Pipeline visibility |
| Lost business tracking | Capture reason → categorise → pattern analysis → monthly report | Strategic feedback loop |
| Guest FAQ handling | Classify enquiry → answer/escalate → log | Front desk time savings |
| Post-stay follow-up | Trigger on checkout → personalise message → send | More reviews, repeat business |
| Maintenance triage | Log issue → categorise urgency → route → track status | Fewer dropped issues |
| Marketing content | Brief → generate drafts → human review → publish | Content velocity |
| Booking funnel analysis | Track visitor path → identify drop-offs → quantify revenue impact → recommend | Conversion optimisation |

---

## Server & Infrastructure Requirements

### Minimum Spec (Single Property, <200 rooms)
- 4GB RAM (8GB recommended — browser automation is memory-hungry)
- 2 vCPU
- 40GB storage
- Linux (Ubuntu 24.04 recommended)

### Essential Infrastructure
- **systemd service** for the gateway (not tmux — must survive reboots)
- **PM2** for any web dashboards (with boot persistence)
- **Health monitoring script** running every 4 hours:
  - RAM and swap usage
  - Chrome/browser zombie process detection and auto-kill
  - Disk usage
  - Dashboard process health (PM2 restart count)
  - Gateway liveness check
  - Alerts to proprietor only when issues found (don't spam with "all OK")

### Memory Architecture
- Use vault-style memory: thin pointer index + detailed files by domain
- Keep the main memory file under 3KB (pointer index only)
- Use BM25 text search (no external API costs) for retrieval
- Separate daily logs from permanent reference material
- Search-first protocol: agent searches before answering factual questions

---

## Risks Specific to Hotels

1. **Guest-facing mistakes hurt trust fast** — always start in draft mode
2. **Bookings and rate changes have financial consequences** — never automate PMS writes without approval
3. **Hotel systems are fragmented and messy** — expect integration friction
4. **Operational knowledge lives in staff heads** — budget time for knowledge capture
5. **Ownership/GM/front desk have different expectations** — align all stakeholders early
6. **Long-tenure staff may resist change** — involve them in design, don't impose
7. **Multi-venue properties need multi-context treatment** — the bar isn't the hotel isn't the events space
8. **API access is frequently denied** — plan for browser automation from Day 1
9. **Budget sensitivity** — independent hotels aren't enterprise buyers. Use free-tier tools wherever possible
10. **Seasonal staffing** — key people may not be available year-round. Don't build dependencies on individuals with uncertain tenure

---

## What a Strong Hotel Deployment Looks Like

After 90 days, a well-deployed hotel AI system should:
- ✅ Reduce repetitive communication workload by 50%+
- ✅ Give management a single daily view of the entire operation
- ✅ Respond to reviews within 24 hours (from 48-72+)
- ✅ Surface patterns in guest feedback that weren't visible before
- ✅ Anticipate demand from local events before they impact pricing
- ✅ Track sales pipeline from enquiry to conversion (or loss)
- ✅ Capture lost business reasons and report patterns monthly
- ✅ Reduce rate enquiry handling time by 70-80%
- ✅ Provide competitive rate intelligence weekly
- ✅ Create a visible audit trail of what AI is doing and recommending
- ✅ Make staff feel more effective, not less important

---

## Reusable Deliverables for Each Hotel Client

For every hotel engagement, produce:
1. **Pre-engagement audit** — website score, review scores, AI visibility, social presence, competitor map
2. **Business workflow map** — how the hotel actually operates (not the org chart version)
3. **Institutional knowledge register** — who carries what unwritten knowledge
4. **Agent architecture diagram** — mapped to the hotel's own department structure
5. **Approval matrix** — what's automated, what needs approval, what's human-only
6. **Tech stack integration map** — what connects, what needs browser automation, what's impossible
7. **30-day pilot plan** — first agent, success metrics, timeline
8. **90-day roadmap** — phased capability rollout
9. **Mission Control module map** — which dashboard modules, in what order
10. **Time redeployment plan** — per role, with staff input
11. **Architecture schematic** — server setup, services, monitoring, infrastructure
12. **Playbook customisation** — sector playbook adapted to this specific property
