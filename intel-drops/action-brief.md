# 🧠 Morning Action Brief — 2026-04-14

## 🔴 Fix Now

### 1. Upgrade OpenClaw to v2026.4.10 — Both Servers
- **Intel:** v2026.4.10 dropped ~3 days ago with SSRF hardening (patches GHSA-7437-7HG8-FRRW) and the new Active Memory plugin. Our main VPS is on v2026.4.1, Kilmurry on v2026.4.2. Both are 9 versions behind.
- **Our exposure:** The SSRF bypass is a known security advisory we flagged weeks ago and haven't patched. Kilmurry is a client-facing server with Kate's marketing data flowing through it. CVE-2026-33579 (privilege escalation via `/pair approve`, CVSS 9.9) is also still unpatched on Kilmurry — active exploitation was discussed on r/sysadmin.
- **Recommended action:** 
  1. Main VPS: `npm update -g openclaw` → restart gateway. Test all agents post-upgrade.
  2. Kilmurry: Still blocked on SSH password from Kate — escalate at Wednesday meeting, or try Tailscale SSH (`ssh clawuser@100.111.174.13`) if configured.
  3. Post-upgrade: Enable the Active Memory plugin on main — it's exactly what we need for the "stateless agent" context problem across our multi-agent team.
- **Effort:** Low (main VPS: 15 min). Medium (Kilmurry: blocked on access).

### 2. GA4 Key Rotation — Still Unresolved Since April 3rd
- **Intel:** No new intel on this — that's the problem. It's been 11 days since we flagged the exposed GA4 service account key. It's still in git history, still unrotated, and still blocking Kate's dashboard.
- **Our exposure:** Kate's marketing dashboard (the one we built for her) can't show GA4 data until this key is rotated and permissions granted for property 4940940. We have a Wednesday meeting coming up — this needs to be on the agenda.
- **Recommended action:** Add to Wednesday meeting agenda: (1) Jonny rotates key in Google Cloud Console → IAM → Service Accounts, (2) grant new key read access to GA4 property 4940940, (3) update `credentials/ga4-service-account.json`, (4) Kate provides her SSH password for Kilmurry patching.
- **Effort:** Low (15 min with Jonny's Google Cloud access).

## 🟡 Improve

### 3. Active Memory Plugin — Solve the Multi-Agent Context Problem
- **Intel:** Today's community intel highlights ongoing complaints about "stateless" context loss when routing tasks between agents. v2026.4.10's new Active Memory plugin introduces a dedicated memory sub-agent that runs before every main reply, automatically pulling in relevant preferences, context, and past details. GitHub issue #50263 also requests persona file injection for `sessions_spawn`.
- **Our exposure:** We run 6 agents. Jonny explicitly chose agent isolation (no shared memory), but the context loss between sessions is real — especially for the Orchestrator delegating to Wrench/Prism. Active Memory could give each agent better recall within its own sessions without breaking isolation.
- **Recommended action:**
  1. After upgrading to v2026.4.10, enable Active Memory on the `main` agent first as a trial.
  2. Test: Does it reduce the "I don't remember that" problem in long Orchestrator sessions?
  3. If successful, roll out to `sitemgr` and `marketing` agents.
  4. Document the setup in `consultancy/playbooks/` — this becomes a selling point for client deployments.
- **Effort:** Low (config change post-upgrade, ~20 min to enable and test).

## 🟢 Opportunities

### 4. DigitalOcean 1-Click Deploy — Streamline Client Onboarding
- **Intel:** DigitalOcean published an official guide for deploying OpenClaw via 1-Click Application (Droplet Marketplace) and App Platform. Three deployment paths documented: manual Droplet, 1-Click, and App Platform.
- **Our exposure/opportunity:** We're building an AI consultancy targeting SMEs. Our current playbook is manual npm installs with SSH. The DO 1-Click path could cut client deployment time from hours to minutes. Combined with our Docker standardisation recommendation (already in MEMORY.md), this gives us a tiered offering: (1) DO 1-Click for budget clients, (2) Docker-compose on their own VPS for mid-tier, (3) fully managed multi-agent setups for premium.
- **Recommended action:**
  1. Spin up a test DO 1-Click deployment ($6/mo, kill after testing).
  2. Document: What works out of the box? What needs customisation? Can we pre-bake our agent configs?
  3. Write a consultancy playbook: `consultancy/playbooks/do-1click-deployment.md`
  4. This becomes the "fast start" tier in our service menu.
- **Effort:** Medium (2-3 hours to test and document).
- **Research:** The DO guide covers all three paths. TemperStack has a complementary tutorial. Minimum viable: 2GB Droplet ($12/mo) — 1GB is insufficient with additional services. Swap can bridge temporarily.

### 5. OpenClaw MCP Integrations — Client-Specific Automation Templates
- **Intel:** Community project `openclaw-xhs` uses MCP to let OpenClaw read and track trends on Xiaohongshu. Microsoft exploring similar agent frameworks for M365. The MCP pattern is becoming the standard way to extend OpenClaw into external platforms.
- **Our exposure/opportunity:** For Kilmurry Lodge, we could build an MCP integration that connects OpenClaw to their booking system (Freetobook/Beds24) to automate rate checks, availability responses, and review monitoring. For Leamy Maths, an MCP for WooCommerce membership management would replace the manual browser automation we're currently doing.
- **Recommended action:**
  1. Review the `openclaw-xhs` repo as an MCP template architecture.
  2. Scope a "Kilmurry Booking MCP" — connect to their booking API, expose availability/pricing/reviews as MCP tools.
  3. Add to consultancy pitch deck: "Custom MCP integrations" as a premium service tier.
- **Effort:** High (1-2 days to build a prototype MCP, but high client value).

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 2 opportunities)
- Estimated total implementation effort: ~5-6 hours (excluding Kilmurry access block and MCP prototype)
- **Priority recommendation:** Upgrade to v2026.4.10 first — it's a 15-minute task on main VPS that closes a known SSRF vulnerability, unlocks Active Memory, and unblocks further improvements. Then prep the Wednesday meeting agenda (GA4 key + Kilmurry SSH access) so both blockers get resolved in one conversation with Jonny.
