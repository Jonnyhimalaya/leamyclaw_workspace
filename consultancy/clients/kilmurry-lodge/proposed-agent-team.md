# Kilmurry Lodge — Proposed Agent Team

## Phase 1: Quick Wins (Week 1-2)
*Prove value fast, low risk, visible results*

### 1. Guest Comms Agent 💬
**Model:** GPT-5.4 (fast, cheap, great at natural language)
**Handles:**
- Pre-arrival emails (personalised based on booking type — business, family, event)
- Post-stay thank you + review request emails
- FAQ responses (check-in times, parking, directions, WiFi, restaurant hours)
- WhatsApp/chat responses for common queries

**Why first:** Immediate time saving for front desk. Every hotel is drowning in repetitive guest questions. This alone could save 2-3 hours/day.

### 2. Review Monitor Agent ⭐
**Model:** Claude Sonnet 4.6 (better at nuance and tone)
**Handles:**
- Monitor new reviews across TripAdvisor, Google, Booking.com
- Draft personalised responses (positive and negative)
- Flag urgent negative reviews for immediate GM attention
- Weekly sentiment summary

**Why second:** Review response is something every hotel knows they should do but never has time for. Instant credibility boost online.

---

## Phase 2: Operations (Week 3-6)
*Deeper integration, more automation*

### 3. Revenue/Pricing Agent 📊
**Model:** Claude Sonnet 4.6
**Handles:**
- Monitor competitor rates (local hotels, OTA pricing)
- Suggest dynamic pricing adjustments based on occupancy, events, season
- Weekly revenue report
- Flag unusual booking patterns

**Depends on:** Understanding their PMS and whether it has an API for rate updates

### 4. Operations Coordinator Agent 🔧
**Model:** GPT-5.4
**Handles:**
- Housekeeping task lists generated from check-in/check-out schedule
- Maintenance request logging and tracking
- Shift handover summaries
- Daily ops briefing for GM (what's happening today — arrivals, departures, events, maintenance)

**Depends on:** Their willingness to adopt a digital workflow (vs paper)

---

## Phase 3: Marketing & Intelligence (Month 2+)
*Growth and competitive edge*

### 5. Marketing Agent 📈
**Model:** Claude Sonnet 4.6
**Handles:**
- Google Ads management for direct bookings
- Social media content calendar
- Email campaigns to past guests (seasonal offers, events)
- OTA commission analysis (which channels are most/least profitable)

### 6. Scout/Intel Agent 🔍
**Model:** xAI Grok or Sonnet
**Handles:**
- Local event monitoring (UL events, sports, conferences = demand spikes)
- Competitor tracking (new hotels, renovations, special offers)
- Tourism trend monitoring (Fáilte Ireland data, Shannon Airport traffic)

---

## Orchestrator
**Model:** Claude Opus 4.6 or Sonnet 4.6 (depending on budget)
- Coordinates all agents
- GM's primary interface (via Telegram or WhatsApp)
- Escalates issues that need human decision
- Produces daily/weekly executive summaries

## Infrastructure
- Dedicated Linode VPS (8GB RAM, ~€20/month)
- Separate OpenClaw gateway (fully isolated from all other clients)
- Mission Control dashboard (customised for hotel KPIs)
- All data on their server, no sharing with other clients

## Estimated Monthly Running Costs
| Item | Cost |
|------|------|
| Linode VPS (8GB) | ~€20/month |
| API costs (Anthropic + OpenAI + xAI) | ~€50-150/month depending on volume |
| Domain/SSL for Mission Control | ~€1/month |
| **Total infrastructure** | **~€70-170/month** |

*Your fee for setup, agent design, and ongoing management is on top of this.*
