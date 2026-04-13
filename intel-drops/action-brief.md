# 🧠 Morning Action Brief — 2026-04-12

## 🔴 Fix Now

### 1. OpenClaw Upgrade Overdue: v2026.4.1 → v2026.4.11 (Both Servers)
- **Intel:** v2026.4.11 released April 11 with stability, safer routing, reliable subagents, and messaging fixes. Separately, CVE-2026-32922 fix guide published — CVSS 9.9 privilege escalation via device token rotation (patched in v2026.3.11, so we're covered there). But GHSA-7437-7HG8-FRRW and SSRF bypass fixes are in v2026.4.10 and we're still on v2026.4.1/v2026.4.2.
- **Our exposure:** Main VPS (v2026.4.1) and Kilmurry (v2026.4.2) are both **10 versions behind**. We're missing the SSRF bypass fix, the GHSA security patch, Active Memory, Codex harness, and all the subagent reliability improvements that directly affect our multi-agent pipeline. This has been flagged since April 8 with zero progress.
- **Recommended action:** Upgrade main VPS today — `npm i -g openclaw@latest`, restart gateway. Kilmurry upgrade blocked on SSH access (see item 3). Main VPS upgrade is unblocked and should take 5 minutes.
- **Effort:** Low (15 min for main VPS)
- **Research:** CVE-2026-32922 affects all versions before v2026.3.11. We're past that. But the GHSA-7437-7HG8-FRRW fix in v2026.4.10 is confirmed security-relevant and we're exposed. 63% of public OpenClaw instances reportedly run without auth — we're not that bad, but being 10 versions behind is indefensible.

### 2. Main VPS Memory Crisis + OOM Bug in Ecosystem
- **Intel:** GitHub issue #41778 confirms `openclaw-message` OOM crashes on 4GB servers from v2026.3.7+. Separate issue #45440 shows rapid memory growth on constrained systems. Community fix guide recommends increasing Node.js heap limits and reducing concurrent context buffers.
- **Our exposure:** Our 8GB main VPS had only **259MB free RAM** as of April 5, with 46MB swap in use. We're running 3 gateways (main ~770MB, Nexus ~740MB, plus SearXNG/Docker/PM2). We're not a 4GB box, but we're operating like one. Any memory regression in the upgrade could tip us into OOM. The Nexus npm cache cleanup (~9.3GB) was flagged but never confirmed done.
- **Recommended action:** Before upgrading OpenClaw: (1) Confirm Nexus npm cache was cleared — `du -sh /home/nexus/.npm /home/nexus/node_modules/.cache`; (2) Set `NODE_OPTIONS="--max-old-space-size=2048"` in gateway systemd unit files; (3) Consider stopping Nexus gateway when not actively testing (frees ~740MB instantly); (4) After upgrade, monitor with `free -h` for 30 minutes.
- **Effort:** Medium (30 min setup + monitoring)
- **Research:** The OOM fix guide recommends: increase Node heap to 2GB (`--max-old-space-size=2048`), reduce `maxContextTokens` in openclaw.json, disable unused plugins to reduce baseline memory. On our 8GB box with 3 gateways, the real fix is either dropping to 2 gateways or upgrading to 16GB RAM.

## 🟡 Improve

### 3. Kilmurry Server: Still a Black Box After 7 Days
- **Intel:** N/A from today's scan — this is a persistent gap.
- **Our exposure:** We haven't been able to SSH into Kilmurry (172.239.98.61) since the original flag on April 5. We can't verify: (a) OpenClaw version or patch status, (b) RAM/disk usage with Kate's gateway + Jack's expanding Mission Control, (c) ClawHub plugin audit for supply chain risk (12%+ malicious rate). Kate's Wednesday meeting was supposed to resolve the SSH password — did it? No follow-up logged.
- **Recommended action:** Jonny to confirm: did Kate provide the SSH password at Wednesday's meeting? If yes, do the audit immediately (version check, `free -h`, disk check, installed plugins list). If no, escalate — we cannot responsibly run a client deployment we can't access.
- **Effort:** Low (once access is obtained — 20 min audit)

## 🟢 Opportunities

### 4. Lead Gen Automation: Ready-Made Consultancy Pitch Material
- **Intel:** X users reporting OpenClaw bots handling end-to-end lead generation in solar, roofing, and pool industries — closing deals from $50k to $2M. 183+ startups generating $271k+/month collectively. Garry Tan (YC) endorsing OpenClaw.
- **Our exposure:** This is pure opportunity. Our consultancy is launching, and we now have third-party proof that OpenClaw drives real revenue in high-ticket B2B/B2C. These aren't hobby projects — they're production sales pipelines.
- **Recommended action:** (1) Create a "Lead Gen Automation" one-pager for consultancy pitches — reference the solar/roofing case studies, frame our offering as "we build and maintain these systems for Irish SMEs"; (2) Target sectors: local trades (plumbers, electricians, builders), property, professional services. These are Limerick-area businesses Jonny can reach. (3) Price point: setup fee + monthly retainer for maintenance and optimisation.
- **Effort:** Medium (2-3 hours to draft pitch materials)
- **Research:** The YC endorsement and 183-startup ecosystem data give credibility. DigitalOcean also published an official 1-Click deploy tutorial — this simplifies our deployment story for clients who want to self-host. We could offer a "managed" tier (we host on our infra) and a "self-hosted" tier (we set up on their DigitalOcean, they pay hosting directly).

### 5. DigitalOcean 1-Click Deploy: Add to Consultancy Playbook
- **Intel:** DigitalOcean published an official community tutorial covering 1-Click Application Deploy and App Platform setup for OpenClaw.
- **Our exposure:** Our current deployment playbook recommends Docker via `ghcr.io/openclaw/openclaw`. DigitalOcean 1-Click is a simpler on-ramp for less technical clients and reduces our deployment time.
- **Recommended action:** Review the DigitalOcean tutorial. If solid, add it as an alternative deployment path in our consultancy playbooks — especially for the "self-hosted" tier where clients manage their own infra. Test a deployment to verify it works cleanly before recommending to clients.
- **Effort:** Low (1 hour to review + document)

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~5 hours
- **Priority recommendation:** Upgrade main VPS OpenClaw to v2026.4.11 today — it's unblocked, low effort, and closes known security gaps. Then resolve the RAM situation before it becomes an outage. The Kilmurry SSH access question needs a direct answer from Jonny — it's been a week.
