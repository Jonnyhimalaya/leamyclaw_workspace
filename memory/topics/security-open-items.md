# Security Open Items (as of 2026-04-05)

## 🔴 GA4 Service Account Key Rotation
- **Status:** UNRESOLVED since ~2026-04-03
- Key exposed in git history. Git was scrubbed but key NOT rotated in Google Cloud.
- Also blocks Kate's GA4 dashboard page (needs service account permissions for property 4940940).
- **Action:** Jonny needs to rotate in Google Cloud Console → IAM → Service Accounts.

## 🔴 Kilmurry Lodge Server — Unpatched (5+ days)
- CVE-2026-33579: Privilege escalation in OpenClaw `/pair approve` (CVSS 9.9). Active exploitation discussion on Reddit r/sysadmin.
- Server: 172.239.98.61 — running unknown OpenClaw version. Kate's agent deployed on 2026-04-04 at v2026.4.2 but the main clawuser instance status unknown.
- **Blocked on:** SSH password from Kate. No follow-up logged since original flag.
- **Action:** Jonny to get password from Kate at Wednesday meeting, or try alternative escalation.

## 🟡 ClawHub Supply Chain Risk
- Flagged 2026-04-05: 12%+ of ClawHub plugins malicious (341-1,467 confirmed, 35k+ downloads).
- Snyk ToxicSkills report (April 2026): 91% bundle malware, 36% prompt injection.
- ClawHub added VirusTotal scanning Feb 2026 but **only for new downloads** (existing installs unscanned).
- **Action:** Run built-in skill safety scanner (`openclaw skill-scan`) on all 4 instances: main, Nexus, Jack (Kilmurry), Kate. 17+ days overdue as of 2026-04-18. Not started.

## 🔴 Pending Server Security Upgrade
- Gateway trust-escalation fix (PR #67303) released ~April 16 in version after v2026.4.14.
- Current: both servers at v2026.4.14. Patch closes tool-name collision bypass path.
- **Action:** Check latest OpenClaw release, upgrade both VPS + Kilmurry servers.

## ✅ Resolved
- OpenClaw CVEs (our instance): Patched at v2026.4.1 (2026-04-02)
- xAI API credits: Topped up 2026-03-30
- HTTP 529 fallback: Fixed 2026-04-02 with profile rotation config
