# 🧠 Morning Action Brief — 2026-04-20

## 🔴 Fix Now

### 1. Upgrade Both Servers to v2026.4.15 — Security Fix Is 4 Days Overdue
- **Intel:** v2026.4.15 released April 16. Contains the gateway trust-escalation fix (PR #67303) plus a new tool execution trust anchoring feature that prevents client tools from overriding built-in tool names to steal media permissions.
- **Our exposure:** Both our main VPS and Kilmurry server are stuck on v2026.4.14. The trust-escalation bypass (originally flagged as CVSS 9.9 — CVE-2026-33579) is unpatched on both. That's 4 client-facing agents (main, Nexus, Jack, Kate) running with a known privilege escalation path. The Kilmurry server is internet-exposed with Tailscale + port forwarding — this is real attack surface.
- **Recommended action:** Upgrade main VPS today. For Kilmurry, this is still blocked on SSH password from Kate/Jack — escalate at Wednesday meeting if not resolved sooner. Pre-upgrade: set `dreaming.storage.mode: "inline"` in openclaw.json to prevent the new dreaming storage default from breaking daily memory file parsing (see item #2).
- **Effort:** Low (20 mins per server, plus 5 mins config tweak)

### 2. Pin Dreaming Storage Mode Before Upgrade
- **Intel:** v2026.4.15 silently changed the default `dreaming.storage.mode` from `inline` to `separate`. Dream phases now write to `memory/dreaming/{phase}/YYYY-MM-DD.md` instead of the daily memory file. No automatic migration path.
- **Our exposure:** We have native dreaming enabled (memory-core, 3am daily). Our agents and morning intel pipeline read daily memory files. If dreaming output vanishes from those files after upgrade, the Strategist and Main agents lose dream-consolidated context — the exact thing that makes memory useful overnight. The intel pipeline could silently degrade without anyone noticing.
- **Recommended action:** Before upgrading, explicitly add `"dreaming": { "storage": { "mode": "inline" } }` to openclaw.json on both servers. This preserves current behaviour. Later, evaluate `separate` mode deliberately — it's arguably cleaner but requires updating any tooling that reads daily memory files.
- **Effort:** Low (2 mins config change per server, must be done pre-upgrade)

### 3. Run Skill Safety Scanner — Now 19 Days Overdue
- **Intel:** ClawHub supply chain risk remains active: 12%+ malicious plugins, 91% of flagged skills bundle malware (Snyk ToxicSkills report). `openclaw skill-scan` has been flagged as overdue since April 1st.
- **Our exposure:** 4 instances (main, Nexus, Jack, Kate) have never been scanned. Kate's instance was deployed from ClawHub skills on April 4th with no vetting. If any installed skill contains prompt injection or data exfiltration, it has had 19 days to operate. Kate's agent handles Kilmurry marketing data including GA4 analytics and ad spend figures.
- **Recommended action:** Run `openclaw skill-scan` on main VPS today. Run on Kilmurry when SSH access is resolved. Add skill scan to the consultancy deployment checklist as a mandatory step (it already should be there per MEMORY.md but clearly isn't being enforced).
- **Effort:** Low (5 mins per instance)

---

## 🟡 Improve

### 4. X API Price Cut Goes Live Today — Reconfigure Scout Economics
- **Intel:** Effective today (April 20), X API "Owned Reads" drop from current pricing to $0.001/request (1,000 reads for $1). Writes increase to $0.015/post. Posts with URLs jump to $0.20/post.
- **Our exposure:** Scout (Grok) runs daily X scans via x_search. This is pure read traffic — we benefit directly from the price cut. More importantly, the write price increase and $0.20/URL-post cost affect any future social automation we build for Kilmurry or Leamy Maths. If we were planning automated X posting with links (e.g., Kate's marketing agent posting hotel deals), the cost model just changed dramatically — a single URL post costs 200x a plain post.
- **Recommended action:** (a) Calculate Scout's current monthly X API spend and project savings under new pricing. (b) Flag the $0.20/URL-post cost to Jonny before building any X social posting automation for clients — it makes link-sharing bots economically questionable. (c) Consider increasing Scout's scan frequency or depth now that reads are cheaper. (d) Note: xAI credits were topped up but MEMORY.md says xAI credits are down — verify current balance.
- **Effort:** Low (30 mins analysis + config review)

---

## 🟢 Opportunities

### 5. Google Gemini TTS — Voice Briefings for Kilmurry & Leamy Maths
- **Intel:** v2026.4.15 bundles Google Gemini TTS natively in the Google plugin — WAV + PCM phone formats, full voice selection, no extra API keys needed beyond existing Gemini access.
- **Our exposure/opportunity:** Two immediate use cases: (a) **Kilmurry morning briefings** — Jack could get a spoken summary of yesterday's bookings/marketing metrics via Telegram voice note instead of reading a wall of text at 7am. Hotel managers live on their feet — audio is the right medium. (b) **Leamy Maths audio supplements** — Jonny's course content is video-heavy but there's no audio-only option. A "listen to the key formulas" feature for students commuting to school would differentiate from every other maths grinds site. (c) **Consultancy pitch material** — "Your AI agent can talk to you" is a visceral demo for SME prospects.
- **Recommended action:** After the v2026.4.15 upgrade, prototype a Kilmurry voice briefing as a proof of concept. It's the simplest win (Jack already gets a text brief → just add TTS). Use this as a case study for consultancy pitches.
- **Effort:** Medium (2-3 hours for prototype, leveraging existing briefing content)

---

## 📋 Summary
- 5 items flagged (3 critical security/ops, 1 improvement, 1 opportunity)
- Estimated total implementation effort: ~4-5 hours
- **Priority recommendation:** Items 1+2 together first (upgrade + dreaming pin) — they're a single 25-minute job on the main VPS that closes a CVSS 9.9 vulnerability. Item 3 (skill scan) immediately after. Items 4 and 5 are this-week-when-convenient.
- **Not flagged today:** The Anthropic OAuth token change, competitive positioning (Hermes/Spacebot comparison), LanceDB S3, local model lean mode, and phone call integration pattern are all noted in the intel but have no immediate action for us — either we're already compliant, or they're future-state consultancy features with no urgency.
