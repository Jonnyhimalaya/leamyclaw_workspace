# Hotels Playbook
**Purpose:** Reusable playbook for designing bespoke agentic systems for hotels and hospitality businesses.

---

## Why hotels are a strong fit for agentic systems
Hotels are operationally complex but highly repetitive.

They typically have:
- constant customer communication
- many recurring workflows
- fragmented systems
- review pressure
- booking / occupancy coordination
- event-driven demand changes
- managers overloaded by exceptions and follow-up

This makes them excellent candidates for agentic design.

---

## Typical Hotel Pain Points
### Front desk / guest communication
- repetitive FAQs
- missed follow-up
- slow response times
- inconsistent guest comms
- pre-arrival info sent too late or not at all

### Reviews / reputation
- reviews not answered quickly
- patterns in complaints not surfaced
- no structured sentiment reporting

### Operations
- maintenance issues tracked informally
- housekeeping coordination friction
- handover notes inconsistent
- no single daily operations view

### Revenue / sales
- pricing decisions reactive instead of proactive
- competitor monitoring inconsistent
- event-driven demand not anticipated well
- direct booking opportunities underused

### Management visibility
- GM spends time chasing updates from multiple people/systems
- reports are manual
- no single command center view

---

## Best Early Agentic Wins for Hotels

## 1. Review Monitor Agent
### What it does
- watches Google / TripAdvisor / Booking.com reviews
- classifies sentiment and urgency
- drafts personalised responses
- flags operational patterns (e.g. breakfast complaints, slow check-in)
- sends weekly reputation summary

### Why it’s a good pilot
- low risk
- visible value
- easy to understand
- directly tied to reputation and guest experience

---

## 2. Guest Comms Agent
### What it does
- drafts or sends pre-arrival information
- answers common guest questions
- handles routine enquiries
- sends post-stay follow-up / review prompts
- creates a consistent guest communication tone

### Risks
- should start in draft or approve-then-send mode
- complaints and unusual cases must escalate

---

## 3. Daily GM Briefing Agent
### What it does
Every morning produces one briefing with:
- arrivals / departures
- occupancy snapshot
- notable guest issues
- reviews received
- maintenance items
- events affecting demand
- outstanding escalations

### Why it’s powerful
This becomes the GM's command layer.
A very strong pilot or phase-2 feature.

---

## 4. Event / Demand Scout Agent
### What it does
- monitors local events, conferences, concerts, sports, university activity
- flags occupancy-impacting events
- helps anticipate pricing and staffing needs

### Especially relevant for
- city hotels
- university-adjacent hotels
- conference / wedding / event-driven properties

---

## 5. Maintenance / Ops Triage Agent
### What it does
- logs maintenance issues
- categorises urgency
- routes issues
- keeps a status board
- produces handover summaries

### Good for
Hotels that currently coordinate maintenance via WhatsApp, calls, or memory.

---

# Suggested Hotel Agent Team

## Orchestrator
**Role:** GM-facing command layer
**Main interface:** Telegram / WhatsApp / Mission Control
**Purpose:** central summary, delegation, escalation, reports

## Specialist Agents
### 1. Guest Comms Agent
- guest questions
- pre-arrival and post-stay messaging
- FAQ handling

### 2. Review Monitor Agent
- review intake
- response drafts
- sentiment / pattern reporting

### 3. Operations Coordinator Agent
- maintenance tracking
- shift / handover summaries
- housekeeping coordination support

### 4. Revenue / Pricing Intel Agent
- competitor monitoring
- event-based demand signals
- occupancy trend alerts

### 5. Marketing / Content Agent
- social content
- offers / campaigns
- local event tie-ins
- website copy suggestions

### 6. Scout Agent
- local intelligence
- competitor activity
- tourism / event monitoring

---

# Mission Control for Hotels
Recommended modules:
- Today’s briefing
- Reviews
- Guest communications queue
- Occupancy / demand indicators
- Maintenance / ops board
- Events calendar
- Agent reports / artifacts
- Memory / decisions

---

# Approval Model for Hotels
## Safe to automate early
- internal summaries
- monitoring
- report generation
- draft replies
- internal reminders

## Approve-then-act
- guest-facing replies
- offer/promotion changes
- outbound campaigns
- operational escalation messages

## Do not automate early
- refunds
- rate changes directly in PMS without approval
- compensation offers
- booking changes with financial implications
- anything legally or reputationally sensitive

---

# Hotel Discovery Questions
## Guest journey
- How do enquiries arrive?
- How do bookings arrive?
- What is the pre-arrival process?
- What are the most common guest questions?
- How are complaints handled?
- How is post-stay follow-up done?

## Operations
- How is housekeeping coordinated?
- How are maintenance issues tracked?
- How do shifts / handovers work?
- What gets dropped when the hotel is busy?

## Revenue
- Who manages pricing?
- Do they watch competitors?
- How do they react to events / demand spikes?
- How much reliance is there on OTAs vs direct bookings?

## Tech stack
- PMS?
- channel manager?
- booking engine?
- CRM?
- website platform?
- WhatsApp / email / phone process?
- analytics / reports?

---

# Common Hotel Workflow Opportunities
| Workflow | Agentic pattern | Value |
|---|---|---|
| Review response | monitor -> draft -> approve/send | reputation + time saved |
| Guest FAQs | intake -> classify -> answer/escalate | faster guest response |
| Daily operations summary | aggregate -> summarise -> deliver | GM leverage |
| Event impact monitoring | monitor -> flag -> recommend | occupancy / pricing intelligence |
| Maintenance triage | intake -> route -> track | fewer dropped issues |
| Post-stay follow-up | trigger -> personalise -> send | more reviews / repeat business |

---

# Pilot Recommendation Heuristic for Hotels
## Best first pilot if they are review-sensitive
Start with **Review Monitor Agent**

## Best first pilot if front desk is overloaded
Start with **Guest Comms Agent**

## Best first pilot if GM is overwhelmed
Start with **Daily GM Briefing Agent**

## Best first pilot if they are events-driven
Start with **Event / Demand Scout Agent**

---

# Risks Specific to Hotels
- guest-facing communication mistakes hurt trust fast
- bookings and room changes can have financial consequences
- hotel systems are often fragmented and messy
- operational knowledge often lives in staff heads, not systems
- ownership / GM / front desk may have different expectations

This means hotel systems should start with:
- observation
- drafting
- summaries
- recommendations
before moving into deeper automation.

---

# What a Strong Hotel Deployment Looks Like
A great hotel system should:
- reduce repetitive comms load
- help the GM see the whole operation clearly
- improve review responsiveness
- surface patterns in guest feedback
- anticipate demand from local context
- reduce dependence on memory and ad-hoc coordination
- create a visible audit trail of what AI is doing

---

# Reusable Deliverables for Hotel Clients
For each hotel client, create:
- business workflow map
- hotel-specific agent org chart
- approval matrix
- tech stack map
- 30-day pilot plan
- Mission Control module map
- SOPs for the first 3 core workflows
