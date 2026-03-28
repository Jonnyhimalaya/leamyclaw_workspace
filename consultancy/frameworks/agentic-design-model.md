# Agentic Design Model for SMEs
**Purpose:** Define what a high-quality, innovative, bespoke agentic system should look like.

---

## Core Principle
A strong agentic system is **not** just "AI added to a business." 
It is a deliberately designed operating layer that:
- understands the business goal
- fits the real workflows already in place
- augments humans without creating chaos
- has memory, governance, and observability
- improves execution speed, consistency, and leverage

---

## The 10 Design Factors

## 1. Business Outcome Alignment
**Question:** What business outcome is this system actually improving?

Every agentic design must map to one or more of:
- revenue growth
- cost reduction
- time saved
- fewer dropped balls
- faster response times
- improved customer experience
- better visibility / reporting
- reduced dependence on one overloaded person

**Bad design:** "Let's add a chatbot."
**Good design:** "Let's reduce GM time spent on repetitive guest comms by 8 hours/week."

---

## 2. Workflow Fit
**Question:** Does the design fit how the business already works?

You are not designing in a vacuum. You are fitting AI into:
- existing steps
- existing staff roles
- existing bottlenecks
- existing tools
- existing habits

Good agentic design respects operational reality.

**Bad design:** Replace everything at once.
**Good design:** Insert AI at the highest-friction points first.

---

## 3. Role Clarity
**Question:** Who does what — human vs orchestrator vs specialist agents?

Every system should define:
- the orchestrator's role
- each specialist agent's scope
- what agents can recommend
- what agents can draft
- what agents can execute
- what must escalate to humans

If roles are fuzzy, the system becomes noisy and unsafe.

---

## 4. Approval Model / Autonomy Gradient
**Question:** What can be automatic, and what needs human approval?

A strong agentic design uses an **autonomy gradient**:
1. Observe only
2. Summarise only
3. Draft only
4. Recommend action
5. Approve-then-act
6. Limited auto-action in low-risk areas

**Examples:**
- Auto-draft review replies → good
- Auto-refund angry customers → bad
- Auto-send routine reminders → probably good
- Auto-edit pricing / payment settings → bad

---

## 5. Memory Design
**Question:** What must the system remember, and where?

Memory should be layered:
- **daily operational memory** — what happened today
- **long-term memory** — enduring client facts, business rules, preferences
- **runbooks / SOPs** — how workflows work
- **artifacts** — proof of work and task outputs

**Principle:** chat is transient, files are durable.

---

## 6. Observability / Artifacts
**Question:** How do humans verify what the system did?

A good agentic system should leave behind:
- reports
- screenshots
- summaries
- task logs
- before/after evidence
- audit trail for high-impact changes

If it acts invisibly, trust will collapse.

---

## 7. Tooling & Integration Fit
**Question:** Does the design match the real tech stack?

You must know:
- what system is source of truth
- what has an API
- what requires browser automation
- what is manual only
- where credentials live
- what is stable vs fragile

Sometimes the best design is not a deep integration. Sometimes it's:
- email parsing
- browser automation
- spreadsheet sync
- approval workflow around existing tools

---

## 8. Reliability & Failure Handling
**Question:** What happens when things go wrong?

Design for:
- API outages
- rate limits
- ambiguous inputs
- missing data
- failed writes
- duplicate actions
- stale memory
- agent drift

Every important workflow needs:
- fallback behaviour
- clear escalation path
- retries only where safe
- human visibility

---

## 9. Security & Data Boundaries
**Question:** What data is sensitive, and who gets access?

Must define:
- data boundaries
- client isolation
- channel permissions
- credential handling
- external write permissions
- PII exposure risks
- what never leaves the system

Security is not optional. It's part of the product.

---

## 10. Economic Viability
**Question:** Is the system worth its cost?

Every design should be tested against:
- setup cost
- infrastructure cost
- model/API cost
- maintenance overhead
- expected time savings
- revenue upside
- failure cost if wrong

Some workflows are clever but economically stupid.
We want high-leverage, high-repeat-value systems.

---

# The 5-Layer Agentic Architecture

## Layer 1 — Human Interface
How the owner/staff talk to the system:
- Telegram
- WhatsApp
- dashboard
- email digests
- Mission Control

## Layer 2 — Orchestration
The central coordinator that:
- maintains top-level context
- routes tasks
- decides whether to delegate
- determines if approval is needed
- composes summaries for humans

## Layer 3 — Specialist Agents
Narrow agents with clear scopes, for example:
- guest comms
- review monitor
- site manager
- revenue analyst
- content creator
- scout/intel

## Layer 4 — Memory & Artifacts
Where continuity and proof live:
- daily logs
- long-term memory
- artifacts folder
- reports
- decision files
- SOPs

## Layer 5 — Tools & Integrations
The operational layer:
- browser automation
- APIs
- spreadsheets
- CRM/PMS/POS integrations
- email
- analytics
- CMS/admin systems

---

# Innovative Agentic Design Checklist
Use this to judge whether a design is genuinely strong.

## A. Strategic
- [ ] Solves a real business problem
- [ ] Linked to measurable business outcomes
- [ ] Designed around bottlenecks, not novelty

## B. Operational
- [ ] Fits existing workflows
- [ ] Respects staff reality
- [ ] Does not require unrealistic behaviour change on day 1

## C. Organisational
- [ ] Roles are explicit
- [ ] Approval gates are explicit
- [ ] Escalation paths are explicit

## D. Technical
- [ ] Uses the real source-of-truth systems
- [ ] Knows what is API vs browser vs manual
- [ ] Has fallback behaviour

## E. Trust
- [ ] Leaves artifacts / proof
- [ ] Can be audited
- [ ] Humans stay in control of risky actions

## F. Economic
- [ ] Saves meaningful time or money
- [ ] Maintenance burden is justified
- [ ] Can scale beyond a single one-off task

---

# What makes a design feel innovative?
Innovation is **not** just more agents.

A design feels genuinely innovative when it combines:
- deep understanding of the business
- elegant workflow insertion
- safe autonomy
- memory and continuity
- proactive intelligence
- visibility and trust

### Examples of real innovation
- Daily AI briefing that anticipates demand from events, bookings, and reviews
- Review monitor that drafts replies and surfaces operational issues hidden inside feedback
- Course drip system tied to schedule and proof-of-release artifacts
- GM command center that turns 6 systems into one daily operational view
- Pricing recommendation loop that watches competitors, occupancy, and event calendar before suggesting changes

---

# Red Flags in Agentic Design
Avoid these.

- too many agents with overlapping roles
- AI bolted on without workflow mapping
- no approval model
- no memory discipline
- no artifacts or audit trail
- forcing full autonomy too early
- broad permissions with weak controls
- trying to replace core systems instead of augmenting them
- designing for demos rather than sustained use

---

# Default Design Heuristic
When in doubt:
1. start with one orchestrator
2. add 2-4 specialists max
3. focus on one daily workflow and one weekly workflow
4. keep high-risk actions human-approved
5. make the system observable
6. document everything that must survive context resets

---

# Summary
A strong bespoke SME agentic system should be:
- **aligned** with business outcomes
- **embedded** in real workflows
- **role-based**
- **memory-backed**
- **artifact-producing**
- **approval-aware**
- **secure**
- **economically justified**

That is the model.
