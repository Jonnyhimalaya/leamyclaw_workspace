# 🧠 Morning Action Brief — 2026-04-26

## 🔴 Fix Now

### 1. All Client Servers Are 10+ Versions Behind — OOM Bug, Security Patches Missing
- **Intel:** v2026.4.20 fixed a critical session-stacking → OOM crash bug. v2026.4.16+ patched the gateway trust-escalation vulnerability (PR #67303, tool-name collision bypass). Current stable is 4.20, bleeding edge is 4.24-beta.
- **Our exposure:** Both our main VPS and Kilmurry server were last confirmed at **v2026.4.14** (per security-open-items.md). That means:
  - Kilmurry (running 3 instances: Jack, Kate, Faye) is vulnerable to session stacking → OOM. With multiple agents on one box, this is a **when-not-if** crash scenario.
  - Gateway trust-escalation vulnerability is **unpatched** on both servers. An attacker with tool access could bypass trust boundaries.
  - Dano server (172.237.126.222) version unknown — may also be behind.
- **Recommended action:** Upgrade all 4 servers to v2026.4.20 (stable) this week. Use the community's pre-upgrade pattern: have each agent read the release notes, run impact analysis, backup config, then upgrade. A Reddit user built this into a reusable skill — we should do the same for consultancy.
- **Effort:** Medium (1-2 hours per server, 4 servers = half day). Kilmurry is the priority — most instances, most risk.

### 2. Skill Safety Scanner — Now 25+ Days Overdue Across All Instances
- **Intel:** Snyk ToxicSkills report: 91% of malicious ClawHub plugins bundle malware, 36% contain prompt injection. ClawHub's VirusTotal scanning only covers new downloads, not existing installs.
- **Our exposure:** `openclaw skill-scan` has never been run on any of our 4 instances (main, Nexus, Jack, Kate). Faye's instance was added since the original flag. That's 5 unscanned instances now. We've been installing skills from ClawHub without verification.
- **Recommended action:** Run `openclaw skill-scan` on all 5 instances. Block: this requires SSH access to Kilmurry (password still pending from Kate/Jack). For main VPS and Dano, can be done immediately.
- **Effort:** Low per instance (5 min each), but **blocked on Kilmurry SSH access** which has been unresolved since early April.

## 🟡 Improve

### 3. Token Cost Audit — Faye and Jack Burning Opus Tokens at Premium Rates
- **Intel:** Each OpenClaw session loads ~15k tokens of tool schemas into context. Community reports 50k+ tokens within 3 messages. Users auditing with `/context detail` are cutting costs 2-3x. DeepSeek V4 Pro launched this week at **1/6th the cost of Opus 4.7** with near-equivalent benchmark performance (VentureBeat confirmed). V4 Flash is even cheaper and is now OpenClaw's onboarding default.
- **Our exposure:** 
  - **Faye** runs Claude Opus 4.7 via API — the most expensive model available. Her revenue cockpit generates regular agent interactions. At 15k overhead per session + Opus pricing, this is likely our highest cost centre per query.
  - **Jack** runs Claude Opus 4.6 — same tier.
  - **Kate** runs Sonnet with Gemini fallback — more reasonable but still worth auditing.
  - Jonny already flagged Opus API billing as a concern (switched Main to GPT-5.4 to save money).
- **Recommended action:**
  1. Run `/context detail` on each client instance to get actual token breakdowns.
  2. Evaluate DeepSeek V4 Pro ($1.74/M tokens) as a drop-in for Faye and Jack's routine work. Keep Opus for complex reasoning tasks only via model routing.
  3. Trim workspace files — remove unused tool schemas, consolidate skills, use `localModelLean: true` where applicable.
  4. For consultancy: build a "cost tier" recommendation (V4 Flash for budget, V4 Pro for mid-tier, Opus/GPT-5.4 for premium).
- **Effort:** Low-Medium. Audit is 30 min per instance. Model switch is a config change but needs testing per agent.
- **Research:** DeepSeek V4 Pro benchmarks within 88 Elo of top-tier on standard reasoning tasks. For hotel operations and revenue analysis (Faye/Jack's use cases), it should be more than sufficient. The MIT licence means no vendor lock-in risk.

## 🟢 Opportunities

### 4. Google Meet AI Plugin — Immediate Kilmurry Application
- **Intel:** v2026.4.24-beta ships native Google Meet participation. The agent joins as a full participant using personal Google auth, can take notes, extract action items, export transcripts, and use tools mid-meeting. Community excitement is high — this is being called the standout feature of 2026.
- **Our exposure/opportunity:** Kilmurry Lodge runs regular operational meetings (vendors, staff, revenue reviews). Jack's agent could attend and produce structured meeting notes → action items → feed into Mission Control. This is also a **killer consultancy demo** — "your AI attends your meetings and updates your dashboard."
- **Recommended action:** 
  1. Once Kilmurry is upgraded to 4.24-stable, pilot Google Meet attendance for one of Jack's regular meetings.
  2. Document the workflow as a consultancy case study: "AI Meeting Assistant for Hospitality."
  3. For Leamy Maths: less applicable (Jonny works solo), but could be useful for parent consultation calls if those ever scale.
- **Effort:** Low to pilot (config + Google auth). Medium to productionise (prompt tuning, MC integration for meeting notes).

### 5. NVIDIA Enterprise Credibility + Consultancy Pricing Lever
- **Intel:** NVIDIA Developer Blog published an official guide for OpenClaw + NemoClaw on DGX Spark. This is a Fortune 500 company endorsing the platform for enterprise/regulated use. Separately, DeepSeek V4's MIT licence + near-SOTA benchmarks means we can now offer a credible "no API cost" tier using local deployment.
- **Our exposure/opportunity:** Our consultancy pitch currently lacks enterprise-grade references. The NVIDIA blog post is free credibility. Combined with DeepSeek V4 (open-source, local-deployable), we can now offer three distinct pricing tiers:
  - **Budget:** DeepSeek V4 Flash local / Qwen3.5 local (€0/month API cost)
  - **Standard:** DeepSeek V4 Pro API ($1.74/M tokens) or Kimi K2.6 ($0.60/M)
  - **Premium:** Claude Opus / GPT-5.4 (for clients who need best-in-class reasoning)
- **Recommended action:** 
  1. Add the NVIDIA blog link to consultancy pitch materials.
  2. Build a one-page "Deployment Tiers" sheet with the three-tier pricing model.
  3. Reference in any proposal for regulated/compliance-heavy clients (Dano's ION Group work is a natural fit).
- **Effort:** Low (2-3 hours to update pitch materials).

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~8-10 hours
- **Priority recommendation:** Server upgrades first (item #1). Every day on v2026.4.14 is a day with a known OOM vulnerability running on a server with 3 client instances. The skill scan (#2) rides the same SSH access blocker — solving Kilmurry access unlocks both. The cost audit (#3) is quick wins that could save significant money given Opus pricing. Google Meet (#4) and consultancy materials (#5) are Sunday-pace work.
- **Recurring blocker:** Kilmurry SSH access has been unresolved for 3+ weeks. This blocks upgrades, skill scans, and feature rollouts for 3 client instances. Escalate at next Jack/Kate meeting.
