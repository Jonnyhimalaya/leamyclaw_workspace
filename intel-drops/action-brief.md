# 🧠 Morning Action Brief — 2026-04-03

## 🔴 Fix Now

### 1. Update to v2026.4.2 — We're One Version Behind with Breaking Changes
- **Intel:** OpenClaw v2026.4.2 released (we're on v2026.4.1). It includes breaking config migrations: xAI `x_search` settings moved from `tools.web.x_search.*` to `plugins.entries.xai.config.xSearch.*`, and Firecrawl `web_fetch` from `tools.web.fetch.firecrawl.*` to `plugins.entries.firecrawl.config.webFetch.*`. A `openclaw doctor --fix` auto-migration is provided.
- **Our exposure:** Checked our config — we only reference xAI as a model provider (`xai/grok-3-mini`), no legacy x_search or Firecrawl paths found. So the breaking changes likely won't bite us. However, staying one version behind means we miss the latest sandbox/transport hardening patches from the post-CVE-flood cleanup.
- **Recommended action:** Run `npm update -g openclaw` to v2026.4.2, then `openclaw doctor --fix` as a safety check. Restart gateway. Takes 5 minutes.
- **Effort:** Low (5 min)

### 2. Our Exec Config Is a Loaded Gun — YOLO Mode + Multi-Agent = Risk
- **Intel:** The March 2026 CVE flood was brutal — 9+ CVEs in 4 days including sandbox boundary bypasses (CVE-2026-32988, CVE-2026-32915), auth bypass letting plugin subagents get root-equivalent access (CVE-2026-32916), and a WebSocket RCE (CVE-2026-25253, CVSS 8.8). Snyk published a full sandbox escape analysis. Community consensus: update to ≥4.2, audit exec permissions, consider SandyClaw/NemoClaw isolation.
- **Our exposure:** **High.** We're running `security: "full"` with `ask: "off"` — every agent can execute arbitrary shell commands without human approval. We run 5 agents (Orchestrator, Wrench, Prism, Radar, Pixel) with different model providers. A prompt injection through any channel (Telegram, a scraped webpage, a malicious X post fed through Scout) could cascade into unrestricted shell execution on our server. We also have SSH credentials, GA4 service account keys, and WP admin access on this box.
- **Recommended action:**
  1. Change exec config to `ask: "on-miss"` (auto-approve known-safe commands, require approval for novel ones) — or at minimum add an allowlist for expected operations.
  2. Move sensitive credentials (GA4 key, SSH keys) into a separate secrets manager or at least restrict file permissions so agent user can't read them.
  3. Consider running agents in sandboxed mode (`sandbox: "require"`) except the main orchestrator.
  4. Audit which agents actually need exec access — Scout and Pixel probably don't.
- **Effort:** Medium (1–2 hours for config changes, longer for full secrets isolation)

## 🟡 Improve

### 3. Kilmurry Lodge Server — Still Exposed After 33 CVEs
- **Intel:** The privilege escalation CVE (patched in 2026.3.28) is now well-documented with community analysis. The threat surface for unpatched OpenClaw instances is growing as attackers have more information.
- **Our exposure:** Kilmurry Lodge server (172.239.98.61) is still running an unknown version — potentially vulnerable to all of the March CVE flood. This has been blocked on Jonny providing the SSH password since it was first flagged. Every day this sits is another day a client server is exposed.
- **Recommended action:** Escalate to Jonny today. Frame it as: "Kate's server may be vulnerable to 9+ documented CVEs including remote code execution. We need the SSH password to audit and patch it. This is a liability issue for the consultancy." If password isn't available, ask Kate's team directly or consider whether the server should be taken offline until it can be verified.
- **Effort:** Low (the ask is low — the block is human, not technical)

### 4. Claude Code Channels — Competitive Threat, But Also Validation
- **Intel:** Anthropic launched Claude Code Channels — letting users control Claude Code sessions remotely via Telegram, Discord, iMessage, WhatsApp through MCP bridges. X community is split: some call it an "OpenClaw killer," others note it loses context on restarts, lacks compaction, supports only 3-4 channels vs OpenClaw's 20+, and has no multi-agent orchestration or persistent memory.
- **Our exposure:** This directly validates our consultancy's core offering but could erode it. Potential clients might say "why do I need your OpenClaw setup when Anthropic gives me this for free?" We need a clear answer.
- **Recommended action:** Write a consultancy comparison doc (`consultancy/research/claude-code-channels-vs-openclaw.md`) covering: (a) what CCC does well (zero-setup for devs, official support, secure pairing), (b) where OpenClaw wins (multi-agent orchestration, persistent memory/soul, 20+ channels, self-hosted sovereignty, custom skills, non-coding use cases like hotel/education), (c) our pitch: "CCC is for solo developers. We build AI operating systems for businesses." Use this in client conversations.
- **Effort:** Medium (1 hour to write the doc, ongoing to refine the pitch)

## 🟢 Opportunities

### 5. Durable Task Flows — Potential Client Upsell Feature
- **Intel:** v2026.4.2 restores the core Task Flow substrate with managed-vs-mirrored sync modes, durable flow state/revision tracking, and child task spawning with sticky cancel intent. This enables background orchestration that persists across sessions.
- **Our exposure:** We're not using Task Flows yet. For Kilmurry Lodge, this could power automated daily workflows (guest check-in prep, review monitoring, social media posting) that survive gateway restarts. For Leamy Maths, it could automate the revision course student tracking (e.g., auto-flag students who paid but haven't attended — currently manual per the todo list).
- **Recommended action:** After updating to v2026.4.2, test Task Flows with a simple use case: automated daily student attendance check against WooCommerce orders. If it works reliably, package it as a consultancy offering: "Always-on background workflows that don't break when your server restarts."
- **Effort:** Medium (2–3 hours to prototype)

## 📋 Summary
- 5 items flagged (2 critical, 1 improvement, 1 competitive intelligence, 1 opportunity)
- Estimated total implementation effort: ~5 hours (excluding Kilmurry which is blocked on human input)
- **Priority recommendation:** Items 1 and 2 first — update to v2026.4.2 and tighten exec permissions. These are 1–2 hours of work that dramatically reduce our attack surface. Then chase Jonny on Kilmurry Lodge SSH access. The competitive positioning doc (item 4) can be done later today or over the weekend.
