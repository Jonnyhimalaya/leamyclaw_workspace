# 🧠 Morning Action Brief — 2026-04-25

## 🔴 Fix Now

### 1. Upgrade Both Servers: v2026.4.14 → v2026.4.23 (9 releases behind)
- **Intel:** v2026.4.23 released April 24. No breaking changes reported. Community feedback positive. Includes gateway trust-escalation fix (PR #67303) we've been waiting for since April 16, plus security "fail-closed" defaults for agent config edits, WhatsApp onboarding fix, and duplicate reply suppression.
- **Our exposure:** Both main VPS and Kilmurry server are at v2026.4.14 — sitting on a known tool-name collision bypass vulnerability for 9 days. The WhatsApp fix matters for Kate's onboarding flows. The duplicate reply fix may be silently affecting user experience across all client instances. The new "fail-closed" security defaults for agent config edits could block custom configs — need to verify after upgrade.
- **Recommended action:** `openclaw update` on both servers. Test Kate's WhatsApp channel and Faye's instance post-upgrade. Check that agent config edits still work (new fail-closed default). Also upgrade Dano's server (172.237.126.222) — he's on an unknown version.
- **Effort:** Low (30 min total — 3 servers × 10 min each)

### 2. Skill Safety Scanner — 20+ Days Overdue Across All Instances
- **Intel:** ClawHub supply chain risk remains real (12%+ malicious plugins, 91% bundle malware per Snyk ToxicSkills). Three scanner tools now available: built-in `openclaw skill-scan`, Bitdefender AI Skills Checker (free, cloud-based), and clawvet (6-pass open-source scanner on GitHub). Bitdefender's tool specifically detects hidden backdoors, data exfiltration, prompt injection, and obfuscation.
- **Our exposure:** Four instances completely unscanned: main VPS, Nexus, Jack (Kilmurry), Kate. Faye's new instance (deployed April 22) also unscanned. Any ClawHub-sourced skill on any instance could be exfiltrating data, injecting prompts, or opening backdoors. This has been flagged since April 5 with zero progress.
- **Recommended action:** Run `openclaw skill-scan` on all 5 instances immediately. For ongoing protection, add Bitdefender AI Skills Checker to the consultancy pre-install checklist. Consider adding clawvet to CI/CD for any skill repos.
- **Effort:** Low-Medium (1 hour — scan all instances, review results, remove anything flagged)

## 🟡 Improve

### 3. Security Debt Is Compounding — Needs a Dedicated Cleanup Session
- **Intel:** Today's sweep surfaced no new security issues — but that's because the old ones are still festering.
- **Our exposure:** Three items have been open for weeks with no progress:
  - **GA4 service account key** — exposed in git since ~April 3 (22 days). Key unrotated in Google Cloud. Blocks Kate's GA4 dashboard. Every day this sits, a leaked credential is live in the wild.
  - **GitHub classic PATs** — main VPS + Dano using broad `repo` scope tokens. Kilmurry Jack's fine-grained PAT can unexpectedly read `leamyclaw_workspace`. Flagged April 22, no action.
  - **Meta token** — Kilmurry Facebook page managed by a different account than Jack's developer account. Unresolved since the Wednesday meeting discussion.
- **Recommended action:** Block 2 hours this weekend for a security sprint: (1) Rotate GA4 key in Google Cloud Console, update credentials file, (2) Replace classic PATs with per-server fine-grained PATs, (3) Get the correct Meta account from Jack/Kate. These are all Jonny-blocked — he needs to do them or delegate access.
- **Effort:** Medium (2 hours, but requires Jonny's direct involvement)

## 🟢 Opportunities

### 4. OpenRouter Image Gen Now Works — Simplify Client Deployments
- **Intel:** v2026.4.23 enables `image_generate` with just an `OPENROUTER_API_KEY`. No separate OpenAI key needed. Plus: agents can now pass quality, format, background, and compression hints.
- **Our exposure:** Current client deployments (Kilmurry, Dano) each need separate API keys for different capabilities. This creates credential sprawl and onboarding friction. For new consultancy clients, every additional API key is a setup step that can go wrong.
- **Recommended action:** Update the consultancy deployment playbook: for new clients, recommend OpenRouter as the single API key for both LLM and image generation. Test `image_generate` via OpenRouter on our main instance first. Document which models are available and quality settings. This is a real selling point: "One API key, full AI capabilities."
- **Effort:** Low (1 hour to test and update playbook)
- **Research:** OpenRouter already supports multiple image models. The key advantage is billing consolidation — clients get one invoice, one key, one rate limit to manage.

### 5. Bitdefender + clawvet — Add to Consultancy Security Checklist
- **Intel:** Two new skill security scanning tools have emerged: Bitdefender AI Skills Checker (free, cloud-based, AI-powered detection) and clawvet (open-source, 6-pass scanner with CI/CD integration). Both address the ClawHub supply chain risk that Snyk flagged.
- **Our exposure:** Our consultancy deployment checklist currently has 4 mandatory security checks (version, skill scan, gateway binding, exec security mode). The "skill scan" step has no defined tooling — it's just a line item. These tools make it concrete and repeatable.
- **Recommended action:** Add to consultancy security checklist: (1) Pre-install: run Bitdefender AI Skills Checker on any ClawHub skill before deploying to client, (2) Post-install: run `openclaw skill-scan` as part of deployment verification, (3) For clients with CI/CD: add clawvet to their pipeline. Write this up as a consultancy reference doc.
- **Effort:** Low (30 min to update checklist and write reference doc)

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~5 hours
- **Priority recommendation:** Do items 1 and 2 today — they're both low effort and close genuine security gaps. The server upgrade (item 1) takes 30 minutes and fixes a vulnerability that's been open for 9 days. The skill scan (item 2) takes an hour and addresses a risk that's been ignored for 20+ days. Item 3 needs Jonny's direct involvement — schedule it for this weekend. Items 4-5 can wait until Monday but are worth doing before the next client deployment.

**Nothing was manufactured here.** The version gap and unscanned skills are real, documented, overdue risks. The security debt is accumulating. The opportunities are genuine simplifications. Saturday morning is a good time to close these gaps before the work week.
