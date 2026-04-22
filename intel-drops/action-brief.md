# 🧠 Morning Action Brief — 2026-04-21

## 🔴 Fix Now

### 1. Both Servers Still on v2026.4.14 — Gateway Trust-Escalation Vuln Unpatched
- **Intel:** v2026.4.15 stable (April 16) includes the gateway trust-escalation fix (PR #67303) that closes tool-name collision bypass. v2026.4.19-beta.2 (April 19) fixes nested agent cross-session blocking and Telegram stale callback wedging.
- **Our exposure:** Main VPS (172.239.114.188) and Kilmurry server (172.239.98.61) are both still on v2026.4.14. The tool-name collision bypass is a privilege escalation path — anyone with agent access could potentially bypass gateway approval. The nested agent blocking bug means our multi-agent team (6 agents on main VPS) can starve each other's sessions. Kate's Telegram bot (@Katetaylor123_bot) is exposed to the stale callback pagination wedge.
- **Recommended action:** Upgrade main VPS to v2026.4.15 stable today. This is a `npm update` — low risk, it's been stable for 5 days. For Kilmurry, this is blocked on SSH password from Kate (flagged since early April). Escalate at next Wednesday meeting — this is now the third week waiting. Consider: can Jack provide the password instead?
- **Effort:** Low (main VPS: 15 min). Medium for Kilmurry (blocked on access).
- **Research:** Community on X confirms the nested agent fix in 4.19-beta.2 is solid for 24/7 multi-session setups. The beta is 2 days old — recommend staying on 4.15 stable for now, move to 4.19 once it graduates.

### 2. Skill Safety Scanner — 20 Days Overdue Across All 4 Instances
- **Intel:** Snyk ToxicSkills report: 91% of malicious ClawHub skills bundle malware, 36% use prompt injection. 12%+ of ClawHub plugins confirmed malicious. OpenClaw has a built-in scanner (`openclaw skill-scan`) but it's never been run on our instances.
- **Our exposure:** Four instances (main, Nexus, Jack/Kilmurry, Kate/Kilmurry) have never been scanned. If any skill was installed from ClawHub without manual vetting, we could be running compromised code on infrastructure that handles Nexus BTC operations, Kilmurry hotel data (guest info, financials), and Leamy Maths student data. This is the kind of thing that ends a consultancy's reputation.
- **Recommended action:** Run `openclaw skill-scan` on main VPS today (main + Nexus instances). For Kilmurry, bundle this with the upgrade once SSH access is resolved. Add `openclaw skill-scan` to the consultancy deployment checklist as a mandatory post-install step.
- **Effort:** Low (10 min per instance). Zero downtime.

## 🟡 Improve

### 3. Anthropic Cost Trap on v2026.4.15 Upgrade — Opus 4.7 Default Will Spike Bills
- **Intel:** v2026.4.15 changed the default model to Claude Opus 4.7 across all Anthropic selections. Separately, Anthropic now blocks Pro/Max subscription usage in third-party tools — all API calls are pay-as-you-go only.
- **Our exposure:** We're already on API billing (good — the subscription ban doesn't bite us directly). But Jack's Kilmurry instance currently uses Opus 4.6 deliberately. When we upgrade Kilmurry to v2026.4.15+, the default shift to Opus 4.7 could silently increase costs if his config uses alias references rather than explicit model pinning. Kate uses Sonnet primary with Gemini fallback (safe). Our own main agent uses GPT-5.4 (safe). But any consultancy client we upgrade is at risk.
- **Recommended action:** Before upgrading any instance to 4.15+, verify model is pinned explicitly (not using aliases like "opus" or "claude"). Add "pin model version explicitly" to the consultancy upgrade checklist. For Jack specifically: confirm his openclaw.json pins `claude-opus-4-6` not an alias.
- **Effort:** Low (5 min audit per instance). High impact if missed.
- **Research:** The OpenRouter migration guide on charlesjones.dev is directly relevant — OpenRouter lets you lock specific model versions and adds automatic failover. Worth including in the consultancy onboarding playbook as the standard API gateway recommendation.

## 🟢 Opportunities

### 4. X API Price Cut — Scout Costs Drop, Kilmurry Social Monitoring Unlocked
- **Intel:** As of April 20, X API owned reads dropped to $0.001/request (1,000 reads for $1). Write costs went up slightly ($0.015/post, $0.20 for posts with URLs). Follow/unfollow/like removed from self-serve tiers.
- **Our exposure/opportunity:** Scout (Radar/Grok) runs daily X scans for our intel pipeline. At $0.001/read, the cost of monitoring becomes negligible — we could increase scan frequency or depth for near-zero marginal cost. More interesting: Kilmurry has no social media monitoring. At these prices, we could build a social listening pipeline for the hotel (mentions, competitor tracking, review sentiment) for under $5/month. That's a real consultancy deliverable.
- **Recommended action:** (1) Audit Scout's current X API spend and see if we can increase scan depth. (2) Spec out a Kilmurry social monitoring cron — daily scan for "@KilmurryLodge" mentions, competitor hotels, Limerick tourism keywords. This is a pitch-ready feature for the Wednesday meeting. (3) Note the write cost increase — any automated posting workflows should be reviewed.
- **Effort:** Low for Scout adjustment (config change). Medium for Kilmurry social monitoring (new cron + skill, ~2 hours to build).

### 5. Hermes Agent Is a Real Competitor — Consultancy Needs a Positioning Answer
- **Intel:** Hermes Agent (Nous Research) just dropped a resilience-focused update with pluggable memory, credential rotation, and anti-detection browsing. Decrypt, KuCoin, and multiple comparison sites published "Hermes vs OpenClaw" pieces this week. Their killer feature: automatic skill generation from experience (after 5+ tool calls, it creates reusable skills). 8,700 GitHub stars, 142+ contributors, growing fast.
- **Our exposure:** We're building a consultancy on OpenClaw. If a prospect asks "why not Hermes?", we need a crisp answer today, not next month. The comparison articles position it as: OpenClaw = breadth (50+ channels, massive ecosystem), Hermes = depth (self-improving, learning loop). Hermes is Python-based, MIT licensed, supports OpenClaw config migration (!) — meaning clients could switch with minimal friction.
- **Recommended action:** Write a one-page consultancy positioning doc: "Why OpenClaw over Hermes" — focus on channel coverage (WhatsApp, Telegram, Discord integration that Hermes lacks), production maturity (195K stars vs 8.7K), multi-agent team architecture, and the skill ecosystem size. Acknowledge Hermes's learning loop as genuinely interesting and note it as a feature to watch. Add to `consultancy/research/`.
- **Effort:** Medium (1 hour to write). Important for sales conversations.
- **Research:** Per the comparison article (essamamdani.com), Hermes is sequential/synchronous, Python-only, and lacks OpenClaw's channel breadth. Its strength is genuine — auto-generated skills from complex tasks — but it's not production-ready at OpenClaw's scale. OpenClaw's native dreaming + QMD memory is our counter-narrative. There's also a third player, Spacebot (Rust, true concurrency, team-scale) — worth a mention in the doc.

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~4 hours (excluding Kilmurry SSH blocker)
- **Priority recommendation:** Upgrade main VPS to v2026.4.15 and run `openclaw skill-scan` today. Both are low-effort, high-impact security items that have been open too long. The Kilmurry SSH password is the single biggest blocker across multiple workstreams — make it the first agenda item Wednesday.
