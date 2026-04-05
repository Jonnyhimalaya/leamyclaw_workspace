# 🧠 Morning Action Brief — 2026-04-05

## 🔴 Fix Now

### 1. Kilmurry Lodge Server Is a Sitting Duck — CVE-2026-33579 Is Being Actively Discussed
- **Intel:** CVE-2026-33579 (disclosed April 1) is a privilege escalation in the `/pair approve` path. A caller with pairing privileges but without admin can approve pending device requests for admin scope. 63% of exposed OpenClaw instances run without authentication. The r/sysadmin thread title is literally "If you're running OpenClaw, you probably got hacked in the last week."
- **Our exposure:** Kilmurry server (172.239.98.61) is **still running an unpatched version** with 33 known vulnerabilities flagged by Ant AI Security Lab. We've been blocked on Jonny getting the SSH password from Kate since late March. This is no longer a "when you get around to it" — this is a "someone could own that server today" situation. The pairing vuln alone lets an attacker escalate to admin on any instance that hasn't updated to v2026.3.28+.
- **Recommended action:** 
  1. **Today:** Message Kate directly for the SSH password. Frame it as urgent security — not optional maintenance.
  2. Once in: `openclaw --version` to confirm current version, then `npm install -g openclaw@latest`, run the full Post-Update Verification Checklist from the playbook.
  3. While waiting for access: verify our own server is on v2026.4.1+ (it should be from the Apr 2 update, but confirm).
- **Effort:** Low (30 min once we have access) — but blocked on credentials
- **Research:** NVD confirms CVSS high. Reddit thread has active discussion of exploitation in the wild. Snyk shows the 2026.3.31 package still has an arbitrary code injection vuln — need to be on 2026.3.28+ minimum, ideally latest.

### 2. GA4 Service Account Key Was Exposed in Git — Still Not Rotated
- **Intel:** This is from our own MEMORY.md, not today's sweep — but it's been flagged since at least late March and remains unresolved.
- **Our exposure:** The key was scrubbed from git history but the actual key hasn't been rotated in Google Cloud. If anyone cloned or forked the repo before the scrub, they have a valid service account key to our GA4 property (286245028) which covers all Leamy Maths analytics data.
- **Recommended action:** 
  1. Go to Google Cloud Console → IAM → Service Accounts → find the GA4 service account
  2. Delete the old key, generate a new one
  3. Update `credentials/ga4-service-account.json` with the new key
  4. Test GA4 access still works
- **Effort:** Low (15 minutes)

## 🟡 Improve

### 3. Anthropic Killed Subscription Auth for Third-Party Tools — Adjust Client Pitch & Our Playbook
- **Intel:** As of April 4 (yesterday), Anthropic no longer allows Claude Pro/Max subscriptions to cover usage in third-party tools like OpenClaw. Users must now use "extra usage bundles" (pay-as-you-go at full API rates: $3/$15 per million tokens for Sonnet, $15/$75 for Opus) or a separate API key. This is the third restriction in 3 weeks (after OAuth deprecation Mar 19, peak-hour caps Mar 28).
- **Our exposure:** We use API keys directly, so **our infrastructure is not broken**. But this matters for:
  - **Consultancy pitch:** We can no longer tell prospects "just use your existing Claude subscription." Every client now needs an API key or extra usage bundle, which is a harder sell and a higher perceived cost.
  - **Client cost modelling:** Our playbook's cost section needs updating. A client running Opus on API at $15/$75 per million tokens will spend significantly more than a flat $200/month Max subscription would have covered.
  - **Strategic signal:** Anthropic is clearly prioritising its own products (Claude Code, Cowork) over the ecosystem. More restrictions are likely. Our cross-provider fallback strategy (which we already have) becomes a stronger selling point.
- **Recommended action:**
  1. Update `consultancy/playbooks/universal-openclaw-implementation.md` Phase 0.3 (Client Agreement) to include explicit API key setup and cost estimation.
  2. Add a "Cost Modelling" section to the playbook with per-model API pricing and typical monthly estimates for different usage tiers.
  3. Strengthen the cross-provider fallback messaging in our pitch — position it as insurance against exactly this kind of platform risk.
  4. Consider adding Gemini 3.1 Pro as a cost-effective default for lighter client workloads. It's free-tier eligible and works well as an advisor/cron model.
- **Effort:** Medium (2 hours to update playbook + pitch materials)

### 4. ClawHub Plugin Supply Chain Is Compromised — Audit Our Skills
- **Intel:** Multiple security reports confirm 12%+ of ClawHub plugins are malicious (341–1,467 confirmed bad skills, 35k+ downloads). 91% of malicious plugins bundle malware, 36% use prompt injection. CertIK audit found API key theft targeting bank/corp/gov credentials.
- **Our exposure:** We primarily write custom skills (good), but we should audit:
  - Any community skills we've installed or referenced from `awesome-openclaw` or ClawHub
  - The `healthcheck` skill and any other bundled skills — are they from the official OpenClaw repo or third-party?
  - Kilmurry's deployment — did we install any community skills there?
- **Recommended action:**
  1. Run `ls ~/.openclaw/skills/` and `ls ~/.npm-global/lib/node_modules/openclaw/skills/` on both servers — catalogue every installed skill and its source.
  2. For any non-official skill: read the SKILL.md, check for suspicious exec calls, exfiltration patterns, or external URLs.
  3. Add a "Skill Vetting Checklist" to the playbook — mandatory before installing any community skill on a client server.
  4. Document this in `consultancy/research/` as a reusable guide.
- **Effort:** Low-Medium (1 hour for audit + 30 min for checklist doc)

## 🟢 Opportunities

### 5. "Deployment Auditing Skill" Pattern — Productise It Before Someone Else Does
- **Intel:** A highly upvoted Reddit post featured an AI skill specifically built to audit, fix, and improve OpenClaw setups (addressing common issues like agents forgetting tasks, memory drift, security misconfigs). The community is hungry for this.
- **Our exposure:** We already have the most comprehensive implementation playbook I've seen (the universal playbook is 500+ lines of battle-tested knowledge). We have incident reports, migration guides, security hardening steps. We have more operational experience than most of the community.
- **Recommended action:**
  1. Build an "OpenClaw Deployment Auditor" skill that runs the Post-Update Verification Checklist, checks memory architecture (is MEMORY.md < 3KB? is vault/ structured?), validates auth failover, tests exec approvals, and checks for known CVEs.
  2. Open-source it on GitHub — immediate credibility for the consultancy.
  3. Add a "premium audit" upsell: the free skill checks basics, but a paid consultancy engagement does the full Phase 0-7 review.
  4. Time this for the current "Apple II moment" hype wave — the community is actively looking for quality tooling.
- **Effort:** High (4-6 hours to build the skill, but high leverage)

## 📋 Summary
- 5 items flagged (2 critical, 2 improvements, 1 opportunity)
- Estimated total implementation effort: ~9 hours (but Kilmurry is blocked on SSH access)
- **Priority recommendation:** Get Kilmurry SSH access TODAY — that server is running known-exploitable vulnerabilities during a week when r/sysadmin is actively discussing OpenClaw compromises. Rotate the GA4 key while waiting. Everything else can wait until Monday.
