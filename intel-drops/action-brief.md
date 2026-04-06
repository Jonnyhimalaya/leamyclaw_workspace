# 🧠 Morning Action Brief — 2026-04-06

## 🔴 Fix Now

### 1. Our OpenClaw Instance Is Behind the Security Overhaul (v2026.4.1 → v2026.4.5+)
- **Intel:** OpenClaw shipped v2026.4.5 with a major security overhaul: SSRF blocks, auth proxy, fail-closed hooks. 9 CVEs disclosed in the past week, including CVSS 9.9 criticals. 135,000+ exposed instances found online, 63% without authentication. A CEO's instance was sold on BreachForums for $25k.
- **Our exposure:** We're running v2026.4.1 — patched for the original CVEs but **missing the broader security overhaul** in v2026.4.5 (SSRF blocks, auth proxy, fail-closed hooks). Our multi-agent team has 5 agents with shell access, subagent spawning, and file operations. The new sandbox boundary bypass CVE (CVE-2026-32915) specifically targets leaf subagents resolving against parent scope — exactly the kind of architecture we run.
- **Recommended action:** Update to v2026.4.5+ today. Run `openclaw update` or `npm update -g openclaw`. Verify all agents restart cleanly. Check exec-approvals.json isn't malformed (v2026.4.5 now auto-sanitises it).
- **Effort:** Low (30 min including testing)

### 2. Kilmurry Lodge Is Now a Liability, Not Just a Risk
- **Intel:** CVE-2026-33579 (CVSS 9.9) — privilege escalation from pairing to admin — is now **confirmed actively exploited** in the wild. Pre-patch exploitation is documented. Their instance has been unpatched for 7+ days. Additionally, the new "email-based prompt injection" vector means any agent with email access can be hijacked to exfiltrate data, send phishing, or run up API bills ($2.4k reported in 48h by one user).
- **Our exposure:** Kilmurry is a client deployment on 172.239.98.61. If compromised, it's our reputation. We don't know what version clawuser is running, what skills are installed, or whether the instance is exposed to the internet. Kate has the SSH password. We've been waiting 5+ days for it.
- **Recommended action:** This can't wait for Wednesday's meeting. **Jonny should message Kate today** and ask her to either: (a) give us the SSH password immediately, or (b) run `openclaw --version` and `openclaw update` herself. If neither happens by Tuesday, recommend temporarily shutting down the instance remotely if possible, or formally advising Kate in writing that the system is at critical risk. Document the advisory — this protects us professionally.
- **Effort:** Low (the conversation), Medium (the actual patching once we have access)

## 🟡 Improve

### 3. Smart LLM Routing Could Cut Our API Costs 40-80%
- **Intel:** Three tools gaining traction: **ClawRouter** (open-source, analyses requests across 15 dimensions, claims up to 92% cost reduction, released 2 days ago), **claw-llm-router** (local classification, 40-80% savings, no third-party data sharing), and **Clawzempic** (community favourite, simpler approach). Meanwhile, Anthropic confirmed on April 4 that OpenClaw Claude-login is now "third-party harness usage" requiring separate Extra Usage billing.
- **Our exposure:** We're running Opus for strategy (this agent), Sonnet for site management and marketing, Grok for scouting, and GPT-5.4 for content. The cron pipeline alone runs 3 agents every morning. With Anthropic's billing change, our costs are going up. We also have no routing intelligence — every request goes to the assigned model regardless of complexity.
- **Recommended action:** Evaluate **claw-llm-router** first (local classification, privacy-preserving, proven). The concept: simple queries (file reads, status checks) route to cheaper models; complex reasoning stays on Opus/Sonnet. Could save €200-400/month once the consultancy scales. Start with a test on the marketing agent (highest volume, most variable complexity). Full research doc written to `consultancy/research/llm-cost-routing-2026-04.md`.
- **Effort:** Medium (2-3 hours to evaluate and configure)

### 4. ClawHub Supply Chain Audit — Still Not Done
- **Intel:** 12%+ of ClawHub plugins confirmed malicious (341-1,467 packages, 35k+ downloads). 91% bundle malware, 36% prompt injection. OWASP now lists this in their Top 10 for AI agents. Community reporting 800+ malicious packages in the marketplace.
- **Our exposure:** We haven't audited our installed skills on either server. We have custom skills (WooCommerce memberships, healthcheck, etc.) which are fine — but any ClawHub-sourced skills could be compromised. Kilmurry's skill inventory is completely unknown.
- **Recommended action:** On our VPS: `ls ~/.openclaw/skills/` and cross-reference each against the known-malicious lists on GitHub. For Kilmurry: add to the list of things to check once we get SSH access. For the consultancy: build a "client onboarding security checklist" that includes skill auditing — this is a sellable service.
- **Effort:** Low for our VPS (30 min), blocked for Kilmurry

## 🟢 Opportunities

### 5. Voice Agent + Video Generation = New Consultancy Offerings
- **Intel:** OpenClaw now has native video generation across multiple AI providers. Separately, users are successfully building two-way voice agents using ElevenLabs + Twilio integration. Both trending heavily on X.
- **Our exposure:** These are pure opportunity. For Leamy Maths: automated video explanations for maths concepts could differentiate from competitors (nobody else is doing AI-generated maths videos in Ireland). For the consultancy: voice agents are the #1 thing SMEs will want — "an AI that answers my phone." Kilmurry Lodge would be a natural pilot (hotel booking enquiries via voice agent).
- **Recommended action:** Don't build anything yet. But: (1) add "voice agent for hotel enquiries" to the Kilmurry proposal as a Phase 2 upsell, (2) test the video generation capability with one sample maths explainer this week, (3) add both to the consultancy service menu. First-mover advantage in the Irish SME market is real.
- **Effort:** Low to scope, Medium to prototype

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 1 overdue audit, 1 opportunity)
- Estimated total implementation effort: ~5 hours (excluding Kilmurry, which is blocked on access)
- **Priority recommendation:** Update our OpenClaw to v2026.4.5 RIGHT NOW (item 1, 30 min). Then message Kate about Kilmurry (item 2, 5 min to send). The security landscape has shifted from "some CVEs" to "active exploitation at scale" in the past 48 hours. Everything else can wait until those two are handled.
