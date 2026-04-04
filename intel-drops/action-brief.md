# 🧠 Morning Action Brief — 2026-04-04

## 🔴 Fix Now

### 1. Anthropic Kills Subscription Access for OpenClaw — ENFORCED TODAY
- **Intel:** Anthropic announced that starting today (April 4, 3PM ET / 8PM Irish time), Claude Pro/Max subscriptions will no longer cover usage through third-party tools like OpenClaw. This is being enforced via OAuth token blocking.
- **Our exposure:** **Critical.** Our entire agent team runs on Claude models. The Orchestrator (Opus 4.6), Sitemgr (Sonnet 4.6), Marketing (Sonnet 4.6), and this Strategist (Opus 4.6) all route through OpenClaw. If we're authenticating via subscription OAuth rather than API keys, **the whole pipeline goes dark at 8PM tonight.**
- **Recommended action:**
  1. **Immediately verify** how our OpenClaw instance authenticates with Anthropic — check `openclaw.json` for whether we use API keys (`ANTHROPIC_API_KEY`) or subscription OAuth tokens.
  2. If using subscription OAuth: switch to API key auth before 8PM tonight. Generate keys at [console.anthropic.com](https://console.anthropic.com).
  3. **Claim the transition credit** — Anthropic is offering a one-time credit equal to your monthly subscription price (e.g., $200 for Max). Must redeem by April 17.
  4. Enable "extra usage" on your Anthropic account if you want to keep subscription + third-party as a fallback.
  5. **Budget impact:** Opus 4.6 API pricing is $5/MTok input, $25/MTok output (66% cheaper than Opus 4.0/4.1). Our multi-agent pipeline is token-heavy. Rough estimate: a busy day with 5 agents could run $5-15 in API costs vs $0 marginal on subscription. Monthly estimate: $100-300 depending on usage patterns. Monitor closely for the first week.
- **Effort:** Low (30 mins to switch auth method) but **time-critical** — must be done before 8PM tonight.
- **Research:** HN thread (47633396) confirms this is real and already being enforced. Community consensus: heavy agent users were consuming 6-8x what human subscribers use, making subscriptions unsustainable for Anthropic. The smart move is API keys with prompt caching (50% discount) and batch processing where possible.

### 2. Kilmurry Lodge: Likely Running Critically Vulnerable OpenClaw
- **Intel:** 9 CVEs disclosed in 4 days (March 18-21), including CVE-2026-22172 (CVSS 9.9 — any authenticated user becomes admin) and CVE-2026-32048 (sandbox escape). Ars Technica is now advising all OpenClaw users to "assume compromise" on unpatched instances. 40,000+ instances found exposed without auth.
- **Our exposure:** MEMORY.md confirms: *"Kilmurry server needs version check due to 33 OpenClaw vulnerabilities (sandbox escape); blocked on Jonny providing SSH password."* This has been blocked for weeks. Meanwhile, the CVE count has grown and the public exploit landscape has worsened.
- **Recommended action:**
  1. **Get Jonny to provide the Kilmurry SSH password today.** This can't wait. Frame it to Kate as an emergency security update.
  2. Once in: run `openclaw --version`. Anything below 2026.3.28 = emergency update needed.
  3. Run `openclaw doctor --fix` post-update to handle the 13 breaking config changes.
  4. Verify auth is enabled (not one of the 40K exposed instances).
  5. **Consultancy angle:** This is exactly the kind of "managed security update" service we should be selling. Document the process for the playbook.
- **Effort:** Medium (1-2 hours once SSH access is provided). The blocker is human, not technical.

## 🟡 Improve

### 3. GA4 Service Account Key Still Exposed — Rotate Now
- **Intel:** MEMORY.md records: *"GA4 service account key was exposed in git history. Scrubbed from git, but key needs rotation in Google Cloud."* This has been a known issue since it was discovered.
- **Our exposure:** The key gives read access to Leamy Maths analytics data. While scrubbed from current git, anyone who cloned the repo before the scrub has the key. Old keys in git history are a top-5 source of real-world breaches.
- **Recommended action:**
  1. Go to Google Cloud Console → IAM → Service Accounts
  2. Rotate the key for the GA4 service account
  3. Update `credentials/ga4-service-account.json` with the new key
  4. Test that the Marketing agent's analytics pipeline still works
  5. Add `.gitignore` rule for `credentials/` if not already present
- **Effort:** Low (15 minutes). No reason this should still be open.

## 🟢 Opportunities

### 4. "Managed OpenClaw" Consulting Package — The Market Is Screaming For It
- **Intel:** Multiple signals converging: (a) r/AiForSmallBusiness (28K subs) actively seeking OpenClaw guidance, (b) "50 Days with OpenClaw" blog reveals most users don't know what to do after installation, (c) community's #1 complaint is update fatigue ("every update I spend half my morning figuring out what broke"), (d) 13 breaking changes in v2026.3.28 alone with inadequate migration guides.
- **Our exposure:** This is pure opportunity. We're already living this pain and solving it for ourselves. We have the multi-agent architecture, the security posture, the update discipline.
- **Recommended action:**
  1. Package three consulting tiers: **Setup** (install + configure + first agent, €500), **Managed Updates** (monthly version management + security patches, €150/mo), **Full Stack** (custom agent design + ongoing management, €500/mo).
  2. Write a "What To Actually Do With OpenClaw" blog post targeting the exact gap velvetshark identified. Publish on leamymaths.ie/blog or a new consultancy domain. This is top-of-funnel content.
  3. Post a helpful comment in r/AiForSmallBusiness referencing our setup experience. Don't hard-sell — demonstrate expertise.
  4. Use the Kilmurry Lodge security update (item #2) as the first documented case study for the "Managed Updates" tier.
- **Effort:** Medium (content: 2-3 hours for blog post, pricing page: 1 hour, Reddit engagement: 30 mins). High ROI — this positions us before the market matures.

### 5. Task Flow Substrate — Upgrade Our Agent Pipeline
- **Intel:** v2026.3.31 introduced "Task Flow substrate" — durable background orchestration with managed child tasks. This is purpose-built for multi-agent pipelines like ours.
- **Our exposure:** Our current intel pipeline (Scout → Main → Strategist) works but is fragile — it's cron-scheduled with no error recovery, no retry logic, no visibility into failures. If Scout fails silently, the whole chain produces stale intel.
- **Recommended action:**
  1. Read the Task Flow docs and evaluate whether our 3-stage intel pipeline could be migrated to a single Task Flow with managed child tasks.
  2. Benefits would include: automatic retry on failure, progress visibility, proper error propagation, and the ability to add conditional branches (e.g., skip Strategist if Scout finds nothing noteworthy).
  3. This is a "when we have a spare afternoon" task, not urgent. But it would make the pipeline more resilient and would be a great feature to showcase in consulting demos.
- **Effort:** Medium-High (half day to prototype, full day to migrate). Not urgent but high strategic value.

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~6-8 hours (excluding Kilmurry SSH blocker)
- **Priority recommendation:** Item #1 (Anthropic billing) must happen before 8PM tonight — it's the only time-critical item. Item #2 (Kilmurry security) needs Jonny to unblock SSH access today. Everything else can be tackled over the weekend.
- **One-liner for Jonny:** Check your Anthropic auth setup RIGHT NOW — your agents may stop working at 8PM tonight. And give me that Kilmurry SSH password.
