# 🧠 Morning Action Brief — 2026-04-02

> **Note:** This is an afternoon brief — the scheduled morning run at 06:15 didn't fire (likely Opus timeout). Running now at 15:17 UTC.

---

## 🔴 Fix Now

### 1. Update Server from v2026.3.28 → v2026.4.1
- **Intel:** v2026.4.1 released April 1st. We're 4 days behind on a release containing 4 separate fixes that directly affect us.
- **Our exposure:**
  - **Raw errors leaking to Telegram chats** (#58831) — Jonny's students or the Kilmurry bot could be seeing ugly provider stack traces instead of friendly messages. This is live right now.
  - **HTTP 529 failover broken** (#58707) — Our known issue since March. The new `auth.cooldowns.rateLimitedProfileRotations` knob caps same-provider retries before cross-provider fallback. This is specifically the fix we've been waiting for.
  - **Gateway restart loops** (#58678) — Generated auth tokens triggering config reloader. If Jonny's seen unexplained restarts, this is why.
  - **Plugin install failures** (#53157) — Stale version constant blocking ClawHub installs.
- **Recommended action:** `npm update -g openclaw && openclaw gateway restart`. Brief downtime (~10 seconds). Needs Jonny's go-ahead since it touches production.
- **Effort:** Low (5 minutes). Risk: Low — CalVer minor, mostly fixes.

### 2. Switch from Brave Search to SearXNG — Immediately
- **Intel:** SearXNG bundled as web_search provider in v2026.4.1 (#57317). Self-hosted, no API key, no rate limits.
- **Our exposure:** **This is actively broken right now.** During this very briefing session, 2 of 3 web_search calls returned HTTP 429 (Brave rate limit exceeded on Free plan). Our daily intel pipeline, research tasks, and any agent doing web lookups are degraded. The Strategist, Main, and any agent using web_search are affected. We're paying for an AI consultancy that can't reliably search the web.
- **Recommended action:** After updating to v2026.4.1:
  1. Deploy SearXNG via Docker: `docker run -d --name searxng -p 8888:8080 searxng/searxng`
  2. Add to openclaw.json: `"plugins": { "web_search": { "provider": "searxng", "host": "http://localhost:8888" } }`
  3. Test with a simple search, then remove Brave API key dependency
- **Effort:** Low (15 minutes). Eliminates a recurring daily pain point.
- **Research:** SearXNG is a meta-search engine aggregating Google, Bing, DuckDuckGo etc. No API keys, no rate limits, fully self-hosted. The OpenClaw community has been asking for this since January — it's now first-party supported.

---

## 🟡 Improve

### 3. Lock Down Cron Jobs with `--tools` Allowlists
- **Intel:** New `openclaw cron --tools` flag in v2026.4.1 (#58504) allows per-job tool restrictions.
- **Our exposure:** We run 10+ cron jobs (heartbeat, intel sweep, scout, strategist, etc.). Currently every cron job has access to every tool. The heartbeat job has access to `exec` and `web_search` when it only needs `read` and `session_status`. The scout job has `exec` access when it only needs `x_search` and `write`. This violates least-privilege — if a prompt injection hit a cron job, it could run arbitrary commands.
- **Recommended action:** Audit each cron job and add `--tools` restrictions:
  - Heartbeat: `--tools read,exec,session_status,sessions_list`
  - Scout: `--tools x_search,read,write`
  - Main (intel sweep): `--tools web_search,web_fetch,x_search,read,write`
  - Strategist: `--tools web_search,web_fetch,x_search,read,write,memory_search,memory_get`
- **Effort:** Medium (30 minutes to audit and update all cron entries).
- **Consultancy value:** This becomes a standard hardening step in our security playbook for every client deployment.

### 4. Kill Bloated Session 3ff45b96
- **Intel:** Heartbeat has flagged session 3ff45b96 at 313+ messages **five times today** (08:42, 12:19, 12:49, 13:19, 13:49 UTC). Nobody has acted on it.
- **Our exposure:** Sessions over 200 messages cause exponentially growing token costs and increase the probability of hitting 529 rate limits — which is exactly the error we've been battling. This single session is likely contributing to our Anthropic rate-limit problems. It's also a compounding cost: every new message in a 313-message session sends the full context, burning through API credits faster.
- **Recommended action:** Jonny should `/new` on whatever chat this session belongs to. If it's a Telegram conversation, just start fresh — the agent will pick up context from MEMORY.md and vault files anyway.
- **Effort:** Low (10 seconds).

---

## 🟢 Opportunities

### 5. Consultancy Positioning: "Managed > DIY" Narrative
- **Intel:** 10+ new OpenClaw tutorials published in the past 2 weeks. $5 VPS guides, 3-hour beginner courses, one-click deployment services (myclaw.ai). The DIY market is exploding.
- **Our exposure:** This is actually good news. The tutorial flood means more people are aware of OpenClaw, but it also means more people will try DIY setups and hit the problems we solve: security hardening, multi-agent coordination, failover configuration, plugin management, error handling, session lifecycle management. Every one of today's "Fix Now" items is something a DIY deployer would miss.
- **Recommended action:** Create a "Why Managed?" one-pager for the consultancy pitch deck. Structure it around today's findings:
  - "A $5 VPS tutorial won't tell you about raw error leaks to your customers"
  - "YouTube guides don't cover failover chains for when Anthropic goes down at 2am"
  - "One-click installs don't lock down cron tools or handle 300-message session bloat"
  - Frame our service as the gap between "it works" and "it works reliably in production"
- **Effort:** Medium (1-2 hours to draft). High consultancy ROI.

---

## 📋 Summary
- **5 items flagged:** 2 critical, 2 improvements, 1 opportunity
- **Estimated total implementation effort:** ~3 hours (mostly the cron audit and consultancy doc)
- **Priority recommendation:** Items 1 and 2 together — update to v2026.4.1 and deploy SearXNG. Takes 20 minutes total and fixes three active production issues (error leaks, failover, web search). The SearXNG fix is the most impactful per minute spent — we literally cannot do our job reliably without it.
- **Blocked:** Kilmurry Lodge server version check still needs SSH password from Jonny.
