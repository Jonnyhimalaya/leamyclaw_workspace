# Open-Source Agentic AI in the Wild — Usage Patterns, Workflows, and Ideas for SME Solutions
**Date:** 2026-03-28
**Purpose:** Internal research bank for Jonny's SME AI consultancy

---

## Why this doc exists
We want to build **innovative bespoke agentic systems for SMEs**, not just copy flashy demos.

That means we need to learn from:
1. **How public builders are actually using open-source agentic AI**
2. **What repo / workflow patterns make agents effective long-term**
3. **Which ideas are relevant to SMEs vs hype**
4. **What reusable processes we can turn into consultancy playbooks**

This document turns a Paperclip ecosystem scan into a practical internal playbook.

---

## Source & Caveat
Primary source:
- Paperclip blog post: **"Who Is Actually Using Paperclip on GitHub?"**
  - https://paperclip.ing/blog/who-is-using-paperclip-on-github/

Important caveat:
- The post is **written by Paperclip**, so it is not neutral
- However, it is still useful because it looks at **public GitHub commit trails**, not just self-reported customer logos
- I also sampled linked repos directly to validate patterns independently

---

## High-Level Takeaway
The most important insight is **not** "Paperclip is popular."

The important insight is:

> The strongest public agentic projects are not structured like ordinary app repos. They are structured like **operating manuals for mixed human + agent teams**.

That means:
- durable documentation
- explicit roles
- product rules
- architecture docs
- gate criteria
- approval models
- agent instruction files
- repo structure that supports re-entry after context loss

This is directly relevant to our consultancy.

We are not just selling "AI agents."
We are selling:
- organisational design
- workflow architecture
- memory systems
- governance
- safe autonomy
- business-specific automation patterns

---

# Part 1 — What people are actually building

## 1. Founder-led product building is the biggest pattern
The clearest pattern is not industry — it's **operating style**.

The strongest repos appear to be built by:
- founders
- indie hackers
- tiny teams
- operators trying to move faster than headcount should allow

These are not mostly open-source prestige projects.
They feel like:
- real businesses
- real internal tools
- real operating systems for one-person or small teams

### Examples
- **Arca / propra-app** — commercial property intelligence
- **Olivia** — household command center
- **Quant Zero** — agentic quant trading system
- **Ghostwriters Inc** — ghostwriting/content business
- **SunoFlow** — AI music product

### Why this matters for us
This is exactly the SME use case:
- small teams
- too many moving parts
- lots of repetitive coordination
- need leverage, not more software clutter

---

## 2. Games and simulations are a serious segment
This was a surprise from the Paperclip analysis.

Examples:
- **asteroid-miner**
- **ai_village**
- **minetris**
- **influence-game**

These use agents for:
- role-play
- world simulation
- multi-agent interaction
- emergent behaviour
- strategic testing

### Why this matters for us
Not because SMEs want games.
Because simulation thinking can be useful for:
- testing workflows before deployment
- stress-testing agent policies
- modelling negotiation / escalation / approval systems
- training prompts and role boundaries safely

This is more relevant to **internal design/testing** than direct client delivery.

---

## 3. Creator businesses are using agents as production engines
Examples:
- **ghostwritersinc** — content / ghostwriting
- **superdots-blog** — AI content site
- **reelforge** — reels/video generation
- **autonomous fashion brand** projects

### Pattern
Agents are being used not just for back-office work, but for:
- content ideation
- draft creation
- editing workflows
- publishing operations
- media system maintenance
- distribution engine support

### SME relevance
Very high for:
- coaches
- personal brands
- service businesses
- e-commerce brands
- hotels / venues / restaurants
- local businesses trying to build audience presence

---

## 4. Some finance / crypto use, but not dominant
Examples:
- Quant Zero
- Wavedge
- convergence-mvp

### Pattern
In these cases, agentic AI is used where there are:
- measurable gates
- risk checks
- pipeline stages
- structured decision criteria

### SME relevance
The lesson is not "build trading bots."
The lesson is:
- the best agentic systems have **gates**
- high-risk actions need **approval layers**
- research -> decision -> execution should be explicit

That applies directly to:
- ad budget changes
- pricing changes
- customer communication
- website edits
- inventory changes
- appointment / booking operations

---

# Part 2 — Repo patterns worth copying

## Pattern A — Repo as operating manual
### Strong examples
- Olivia
- Quant Zero
- Arca / propra-app

### Common traits
They include docs like:
- product vision
- ethos / principles
- architecture
- roadmap / milestones
- decision files
- criteria docs
- operational manuals
- agent role instructions

### Why it works
When an agent returns to the repo later, it can quickly answer:
- What is this system for?
- What matters most?
- What are the non-goals?
- What is allowed / not allowed?
- What is the current architecture?
- How do we decide if something is good enough?

### Relevance to us
Extremely high.
This should become standard for every consultancy deployment.

### What we should create for every client
- `MISSION.md` — why the system exists
- `OPERATING_MODEL.md` — human/agent workflow boundaries
- `AGENTS.md` — role definitions and escalation paths
- `DECISIONS.md` — business / product rules
- `SYSTEM_ARCHITECTURE.md` — stack, integrations, data flow
- `APPROVAL_GATES.md` — what can be automatic vs human-approved
- `RUNBOOKS/` — repeatable operations (weekly reports, onboarding, etc.)

---

## Pattern B — Human as CEO, agents as staff
### Strong example
- Quant Zero

### Structure
- Human sets direction
- Agents perform specialised work
- Promotion / execution is gated
- Criteria are explicit

### Why it matters
This is the right mental model for SMEs.
Not: "replace staff with AI"
But: "treat agents like staff with scopes, checklists, and approvals"

### Relevance to us
Very high. This should be how we sell and design systems.

### Our consulting framing
For clients, agents should map to business roles:
- Front desk assistant
- Review monitor
- Booking coordinator
- Revenue analyst
- Content assistant
- Maintenance triage
- Customer follow-up assistant

---

## Pattern C — Criteria-based progression
### Strong example
- Quant Zero thresholds / gate criteria

### Pattern
Before something moves forward, it must meet measurable criteria.

### SME adaptation examples
- Marketing agent may recommend ad changes, but only if:
  - CTR below threshold
  - CPC above threshold
  - conversion lag persists for X days
- Review agent may auto-draft responses, but only auto-send for 4-5 star reviews
- Booking agent may auto-answer FAQs, but escalate complaints / refunds / edge cases
- Ops agent may create task lists, but never change payroll or payment settings

### Why it matters
Agentic systems get much safer and more useful when criteria are explicit.

---

## Pattern D — Durable context for agent re-entry
### Strong example
- Olivia's documentation-first approach

### Pattern
Instead of relying on chat history, important context is written into files.

### Why it matters
This aligns exactly with our memory philosophy:
- chat is ephemeral
- files are durable
- durable files reduce rework, drift, and hallucinated continuity

### Consultancy implication
Every client deployment should have:
- daily log memory
- curated long-term memory
- SOPs / runbooks
- role docs
- notable decisions written down

---

## Pattern E — Runtime rules and secrets handling in-repo
### Strong example
- Influence Game

### Pattern
The repo encodes:
- rules of behaviour
- secrets handling
- environment constraints
- runtime assumptions

### Why it matters
This is critical for client work.
Agents should know:
- which tools are allowed
- which actions need approval
- where secrets live
- what channels they may write to
- what data is sensitive

### Consultancy implication
We need a standard **Security & Permissions Matrix** per client.

---

# Part 3 — What this means for SME solutions

## Core truth
SMEs do **not** primarily need "AI features."
They need:
- fewer dropped balls
- better follow-up
- less repetitive admin
- better visibility
- faster execution
- continuity when humans are busy

So the best bespoke systems will combine:
1. **orchestration**
2. **memory**
3. **artifacts / audit trail**
4. **approval gates**
5. **domain-specific workflows**

---

# Part 4 — Reusable agentic workflow patterns for SMEs

## 1. Intake -> classify -> route -> follow-up
Works for:
- hotel enquiries
- service business leads
- property management issues
- maintenance requests
- school admin
- support inboxes

### Pattern
1. collect incoming item
2. classify it
3. route to correct queue/agent/person
4. draft response or next action
5. follow up if unresolved

### Example agents
- Inbox agent
- Triage agent
- Follow-up agent
- Executive summary agent

---

## 2. Monitor -> flag -> recommend -> approve -> act
Works for:
- ads
- pricing
- bookings
- occupancy
- review monitoring
- stock / availability

### Pattern
1. monitor data source
2. detect change / issue
3. recommend action
4. human approves
5. action agent executes

This is probably the single most important safe-autonomy pattern for SMEs.

---

## 3. Weekly release / drip workflow
Works for:
- courses
- membership content
- coaching programmes
- member communities
- subscription content

### Pattern
1. content exists in advance
2. access is controlled centrally
3. each period adds next content slice
4. artifacts prove what changed

We literally just implemented this for Leamy Maths revision content.

This should become a reusable education/coaching playbook.

---

## 4. Review / reputation loop
Works for:
- hotels
- restaurants
- clinics
- salons
- local trades
- any service business

### Pattern
1. monitor reviews daily
2. classify sentiment + urgency
3. draft responses
4. escalate negatives
5. produce weekly reputation report

Very strong early win for hospitality clients.

---

## 5. Calendar / event / occupancy anticipation loop
Works for:
- hotels
- event spaces
- tourism businesses
- courses / workshops

### Pattern
1. monitor known future events
2. anticipate demand spikes / staffing needs
3. prompt pricing / communications / content changes
4. issue daily briefings

This is exactly the kind of high-value, non-obvious bespoke automation SMEs will pay for.

---

## 6. Content engine workflow
Works for:
- coaches
- agencies
- e-commerce
- education businesses
- hospitality

### Pattern
1. strategy agent proposes themes
2. content agent drafts assets
3. brand/owner approves
4. scheduler agent publishes or queues
5. analytics agent reports results

This is where creator-business patterns from the Paperclip ecosystem become directly useful.

---

## 7. Internal command center / daily briefing
Works for almost every SME.

### Pattern
Every morning:
- what needs attention today?
- what's overdue?
- urgent customer issues?
- appointments / bookings / events?
- important unread messages?
- anomalies?

This is a powerful, universal offering.

---

# Part 5 — A reusable consultancy process

## Phase 1 — Discovery
Goal: find the business bottlenecks, not the fanciest AI use case.

### Questions
- What are the repetitive tasks?
- Where are things dropped or forgotten?
- Which processes depend too much on one person?
- What decisions are frequent but structured?
- What data sources already exist?
- What actions are safe to automate? Which are risky?

### Deliverable
- current-state workflow map
- bottleneck list
- risk map
- shortlist of agent opportunities

---

## Phase 2 — Design
Goal: architect the agent team and approval model.

### Deliverable
- proposed agent org chart
- tool permissions matrix
- memory design
- daily/weekly workflows
- approval gates
- Mission Control layout

---

## Phase 3 — Pilot
Goal: deliver 1-2 high-value workflows fast.

Best pilot candidates:
- reviews
- inbox triage
- daily briefing
- content engine
- follow-up system

Avoid high-risk automation first.

---

## Phase 4 — Harden
Goal: make it reliable enough to trust.

### Add:
- artifacts
- audit trail
- rate limit / budget controls
- failure handling
- escalation rules
- monitoring

---

## Phase 5 — Expand
Goal: add deeper workflows after trust is earned.

This is when to add:
- pricing recommendations
- operational scheduling
- outbound communications
- direct system integrations

---

# Part 6 — Opportunity bank by SME vertical

## Hospitality / Hotels
High-value workflows:
- review monitoring and response drafts
- pre-arrival / post-stay comms
- daily occupancy briefings
- event / conference demand monitoring
- housekeeping coordination summaries
- maintenance issue triage
- local recommendation assistant

## Education / Courses / Coaches
High-value workflows:
- content drip control
- student onboarding
- attendance / no-show follow-up
- membership access management
- weekly resource release
- social content engine
- parent/student enquiry handling

## Service Businesses (trades, clinics, salons, agencies)
High-value workflows:
- lead triage
- quote follow-up
- appointment reminders
- missed-call capture
- review solicitation
- SOP / knowledge assistant
- daily owner briefing

## E-commerce
High-value workflows:
- product content updates
- review / sentiment analysis
- customer service draft replies
- inventory anomaly alerts
- abandoned cart follow-up
- promo calendar planning

## Property / Real Estate / Management
High-value workflows:
- enquiry classification
- maintenance ticket routing
- document extraction and summarisation
- owner / tenant communication support
- local market monitoring
- portfolio briefings

---

# Part 7 — Design principles for our own systems

## Principle 1 — Separate orchestration from execution
The orchestrator should:
- maintain broad context
- delegate
- decide what needs approval
- protect against context bloat in specialists

Specialists should stay narrow.

---

## Principle 2 — Files > chat memory
Anything important should live in files:
- memory
- decisions
- workflows
- runbooks
- artifacts
- reports

---

## Principle 3 — One job, one artifact
No microtasking.
Artifacts should track the job, not every step.

---

## Principle 4 — Start with assistance, then graduate to autonomy
Typical path:
1. observe only
2. draft only
3. recommend
4. approve-then-act
5. limited autonomy in low-risk areas

---

## Principle 5 — Vertical customisation beats generic agents
A hotel system should not look like a course business system.
A property management system should not look like an e-commerce system.

The value is in the bespoke workflow design.

---

## Principle 6 — Governance is a feature
For clients, governance is not bureaucracy.
It is what makes AI usable in real operations.

Governance includes:
- permissions
- approval gates
- audit trails
- artifacts
- escalation paths
- secrets handling
- data separation

---

# Part 8 — What we should build internally next

## 1. Consultancy pattern library
Create a folder of reusable patterns:
- review-monitoring.md
- inbox-triage.md
- daily-briefing.md
- content-engine.md
- drip-release-system.md
- approval-gates.md
- agent-org-chart-template.md

## 2. Vertical playbooks
Create per-vertical playbooks:
- hotels.md
- education.md
- service-businesses.md
- e-commerce.md
- property.md

## 3. Client deployment template
Each new client should get a standard structure:
- MISSION.md
- AGENTS.md
- DECISIONS.md
- APPROVAL_GATES.md
- MEMORY.md
- daily memory logs
- Mission Control dashboard template

## 4. Security checklist
Need a reusable checklist for:
- credentials
- permissions
- external writes
- messaging policies
- backups
- logs
- client isolation

## 5. Budget / cost controls
This is one genuinely good Paperclip-style idea worth copying.
We should add:
- per-agent budget awareness
- warnings
- optional hard caps
- model fallback strategy

---

# Final synthesis
The best public open-source agentic AI projects are not winning because they have the fanciest model.

They are winning because they combine:
- **clear purpose**
- **well-defined roles**
- **durable memory**
- **good documentation**
- **approval logic**
- **re-entry-friendly repo structure**
- **tight workflows tied to real business outcomes**

That is the real benchmark for us.

If we want to build the best bespoke agentic SME systems, we should think less like prompt engineers and more like:
- operations architects
- product managers
- workflow designers
- safety engineers
- organisational designers

That is where the edge is.

---

## Immediate next step suggestions
1. Turn this into a **pattern library folder** with one file per workflow
2. Write the **Hotels playbook** next (useful immediately for Kilmurry Lodge)
3. Write a **Client Deployment Template** next
4. Ask Radar to keep tracking public examples of agentic repos and append findings weekly
