# 🧠 Morning Action Brief — 2026-04-07

## 🔴 Fix Now

### 1. Claim Anthropic Transition Credit Before April 17 (10 days left)
- **Intel:** Anthropic is giving Pro/Max subscribers a one-time credit equal to their monthly plan fee. Must be claimed via Settings → Usage → "Claim credit" by April 17. Credit is valid for 90 days across API usage.
- **Our exposure:** We have active Claude subscriptions (both `anthropic:claw` and `anthropic:work` profiles use OAuth tokens). Those tokens could die any day as rollout continues. If we don't claim the credit, we leave free money on the table — likely $20-$200 depending on plan tier.
- **Recommended action:** 
  1. Go to console.anthropic.com → Settings → Usage → Claim credit. Do this TODAY.
  2. While there, create an API key (Settings → API Keys → Create Key).
  3. Run: `openclaw models auth paste-token --provider anthropic --profile-id anthropic:api-key`
  4. Set priority: `openclaw models auth order set --provider anthropic anthropic:api-key`
  5. Restart gateway.
- **Effort:** Low (15 minutes)
- **Research:** Community confirms migration takes ~20 mins. No widespread issues. Opus 4.6 pricing is $5/$25 per MTok — 66% cheaper than Opus 4.0. With GPT-5.4 as primary (your April 6 decision), Anthropic API usage should be modest — mainly Sonnet for sitemgr/marketing agents and as a fallback. Estimated monthly: $50-100.

### 2. Upgrade All Instances to v2026.4.5 (Critical Bug Fixes)
- **Intel:** v2026.4.5 fixes three bugs that directly affect us: `pairing-required` errors (post-2026.3.31 regression), `sessions_spawn` dying on loopback scope-upgrade, and corrupted `exec-approvals.json`. Also removes legacy config aliases that will break on next restart if not migrated.
- **Our exposure:** Main VPS is on v2026.4.1. Kilmurry Kate is on v2026.4.2. Both are running configs with potentially deprecated aliases. The `pairing-required` fix and `sessions_spawn` fix are directly relevant — we use subagents heavily and the multi-agent team relies on spawn working.
- **Recommended action:**
  1. **Main VPS first:** Stop gateway → `openclaw doctor --fix` (run 2-3x, community reports sometimes needs multiple passes) → upgrade to v2026.4.5 → restart → verify agents spawn correctly.
  2. **Kilmurry (Kate's server):** Same process, but need SSH password from Kate. Wednesday meeting is the window.
  3. **Gotcha from community:** `doctor --fix` can sometimes introduce invalid keys like `dmPolicy`. Check `openclaw.json` manually after running if startup fails.
- **Effort:** Medium (30 mins per instance, but Kilmurry blocked on SSH access)

### 3. Main VPS RAM Is Critical — Fix Before It OOMs
- **Intel:** As of April 5, main VPS had only 259MB free with 46MB swap in use. Running: main gateway (~770MB), Nexus gateway (~597MB + 143MB Next.js), SearXNG, Docker, two PM2 dashboards.
- **Our exposure:** An OOM kill would take down the entire agent team, Nexus, and both mission control dashboards simultaneously. This is a single point of failure for the consultancy.
- **Recommended action (immediate, no cost):**
  1. Clear Nexus npm/node caches (~9.3GB disk, also reduces memory pressure from disk swap): `rm -rf /home/nexus/.npm/_cacache /home/nexus/node_modules/.cache`
  2. Stop Nexus gateway when not actively testing: `sudo systemctl stop openclaw-nexus`
  3. Set `--max-memory=4096` on main gateway to prevent runaway usage.
  4. Add swap file (2GB) as safety net: `sudo fallocate -l 2G /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile`
  - **Recommended action (this week):** Upgrade VPS to 16GB. At current density (3 gateways + dashboards + services), 8GB is structurally insufficient. Hetzner CPX31 is ~€15/mo for 16GB.
- **Effort:** Low (immediate fixes: 10 mins) / Medium (VPS upgrade: 1 hour with migration)

## 🟡 Improve

### 4. GA4 Key Rotation — Unresolved 4 Days, Blocks Kate's Dashboard
- **Intel:** GA4 service account key was exposed in git history. Git was scrubbed but key never rotated in Google Cloud. This also blocks Kate's GA4 dashboard page (needs permissions for property 4940940).
- **Our exposure:** Exposed credential in the wild. Low probability of exploit (it's a GA4 read key, not write), but it's unprofessional to leave it and it's blocking a client deliverable. Kate's Wednesday meeting is the natural deadline.
- **Recommended action:**
  1. Google Cloud Console → IAM → Service Accounts → rotate key.
  2. Download new JSON, replace `credentials/ga4-service-account.json`.
  3. Grant the new service account access to Kate's GA4 property (4940940).
  4. Test Kate's dashboard page.
- **Effort:** Low (20 minutes)

## 🟢 Opportunities

### 5. ClawHub Supply Chain Audit — Do Before Installing Any New Skills
- **Intel:** 12%+ of ClawHub plugins confirmed malicious (341-1,467 packages, 35k+ downloads). 91% bundle malware, 36% use prompt injection. v2026.4.5 now has ClawHub directly in the Skills panel UI, which makes it *easier* for users (and agents) to install untrusted skills.
- **Our exposure:** We haven't audited installed skills on either server. The new ClawHub UI in v2026.4.5 increases the attack surface — any agent with skill-install access could pull a malicious package. For client deployments (Kate, Nexus), a compromised skill could access their data.
- **Recommended action:**
  1. Before upgrading to v2026.4.5, audit all installed skills: `ls ~/.openclaw/skills/` on both servers.
  2. Cross-reference against known-malicious list (check GitHub issues on openclaw/openclaw for community reports).
  3. After upgrade, restrict ClawHub access in agent configs — agents should NOT be able to self-install skills without approval.
  4. Add to deployment playbook: "Skills audit" as a mandatory pre-upgrade step.
- **Effort:** Medium (1 hour across both servers)

## 📋 Summary
- 5 items flagged (3 critical, 1 improvement, 1 opportunity)
- Estimated total implementation effort: ~4 hours (excluding VPS migration)
- **Priority recommendation:** Claim the Anthropic credit first — it's 15 minutes, has a hard deadline (April 17), and is free money. Then tackle the RAM situation before it OOMs and takes everything down. Upgrade to v2026.4.5 can follow once the server is stable. GA4 rotation and ClawHub audit should happen at or before the Wednesday Kate meeting.
