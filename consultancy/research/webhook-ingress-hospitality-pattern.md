# Webhook Ingress → TaskFlow: Hospitality Automation Pattern

**Created:** 2026-04-08
**Source:** OpenClaw v2026.4.5 release + docs.openclaw.ai/plugins/webhooks + LumaDock hardening guide

## What It Is
OpenClaw v2026.4.5 ships a webhook ingress plugin that creates authenticated HTTP routes. External services POST to these routes, triggering OpenClaw TaskFlows automatically. No polling, no cron — event-driven.

## Architecture
```
Booking Platform (Freetobook/Beds24/etc.)
  ↓ POST /webhook/booking-created (shared-secret auth)
OpenClaw Gateway (webhook ingress plugin)
  ↓ payload transform → TaskFlow trigger
Agent Session
  ↓ executes workflow (draft email, update calendar, alert owner)
```

## Config Pattern (from docs)
```json
{
  "plugins": {
    "entries": {
      "webhooks": {
        "config": {
          "routes": {
            "booking-created": {
              "secret": "<shared-secret>",
              "taskflow": "<taskflow-id>",
              "transform": { "guest": "$.guest_name", "dates": "$.check_in" }
            }
          }
        }
      }
    }
  }
}
```

## Hardening (LumaDock guide, Feb 2026)
- Always use shared-secret auth (never expose unauthenticated routes)
- Rate limit to 10 req/min per route
- IP allowlist if the booking platform has static IPs
- Log all webhook payloads for audit trail
- Use HTTPS (Tailscale funnel or reverse proxy)

## Hospitality Use Cases
1. **Booking created** → draft pre-arrival email, add to events calendar
2. **Booking cancelled** → alert owner, update availability dashboard
3. **Check-in date approaching (T-3 days)** → send guest info pack, local recommendations
4. **Review received** → summarize, flag negative sentiment, draft response
5. **Occupancy threshold** → trigger dynamic pricing alert

## Pitch Value
- Saves 30-60 mins/day of manual booking management
- Zero missed guest communications
- Repeatable across hospitality clients (same pattern, different booking platforms)
- Low ongoing cost (runs on existing OpenClaw instance)

## Implementation Estimate
- First client (Kilmurry): 2-3 hours (includes booking platform API research)
- Subsequent clients: 1-2 hours (pattern is established)
- Requires: v2026.4.5+, booking platform webhook support, HTTPS endpoint

## Status
- Not yet implemented. Blocked on v2026.4.5 upgrade.
- Prototype target: Kilmurry Lodge (Kate's instance) after upgrade stabilizes.
