# OpenClaw Ecosystem State — March 2026

*Research compiled: 2026-03-30*

---

## 1. Project Overview & Governance

OpenClaw (formerly Clawdbot → Moltbot → OpenClaw) is a free, open-source autonomous AI agent platform created by Austrian developer **Peter Steinberger**. First published November 2025, it became the fastest-growing open-source project in history with **247,000+ GitHub stars** and **47,700+ forks** as of early March 2026.

### Key Governance Change
- **Feb 14, 2026:** Steinberger announced he was joining **OpenAI** to "drive the next generation of personal agents" (confirmed by Sam Altman on X).
- OpenClaw moved to an **independent open-source foundation**, financially backed by OpenAI but not owned by them.
- The BYOK (Bring Your Own Key) model remains intact — no vendor lock-in.
- Community-driven development continues with active contributors.

### Major Industry Endorsements
- **NVIDIA** announced **NemoClaw** at GTC 2026 (March 16) — a single-command install adding Nemotron models + OpenShell runtime with privacy/security sandboxing. Jensen Huang called OpenClaw "the operating system for personal AI."
- **Tencent** (March 10) launched a full suite of OpenClaw-compatible AI products integrated with WeChat.
- **CrowdStrike** published a security analysis guide for enterprises.
- **Wikipedia** now has a full article on OpenClaw.

---

## 2. Latest Release: v2026.3.28 (March 29, 2026)

### Breaking Changes
- **Qwen provider overhaul:** Removed deprecated qwen-portal-auth OAuth; must migrate to Model Studio API key.
- **Config/Doctor:** Dropped auto-migrations older than 2 months; old legacy keys now fail validation.

### Major New Features
- **xAI/Grok Responses API:** Moved bundled xAI provider to Responses API with first-class `x_search`. Auto-enables xAI plugin from web-search config.
- **Plugin Approval Hooks:** New `requireApproval` for `before_tool_call` hooks — plugins can pause execution and prompt users for approval via Telegram buttons, Discord interactions, or `/approve` CLI.
- **ACP Current-Conversation Binds:** Discord, BlueBubbles, and iMessage now support `/acp spawn codex --bind here` to turn existing chats into Codex-backed workspaces.
- **MiniMax Image Generation:** image-01 model with generate + image-to-image editing.
- **Gemini CLI Backend:** Bundled Gemini CLI backend support alongside Claude CLI and Codex CLI.
- **Slack File Upload:** Explicit `upload-file` action with filename/title/comment overrides.
- **Microsoft Teams & Google Chat File Sends:** Unified `upload-file` action.
- **Matrix Voice Bubbles:** Auto-TTS replies sent as native Matrix voice messages.
- **Memory Plugin Overhaul:** Pre-compaction memory flush moved behind active memory plugin contract.
- **Heartbeat Plugin API:** `runHeartbeatOnce` exposed for plugins to trigger heartbeats with delivery target overrides.
- **Podman Simplification:** Rootless user container setup with `~/.local/bin` launch helper.

### Bug Fixes (Notable)
- Anthropic "sensitive" stop reason no longer crashes agent runs.
- Gemini 3.1 Pro/Flash/Flash-Lite resolution fixed across all Google provider aliases.
- WhatsApp infinite echo loop in self-chat DM mode fixed.
- Telegram long message splitting now splits at word boundaries.
- Discord reconnect drains stale sockets properly.
- iMessage reply_to tags no longer leak into delivered text.
- ACPX agent registry hardened — unknown ACP agent IDs no longer fall through to raw command execution.

---

## 3. Recent Release Highlights (March 2026)

### v2026.3.24 (March 24)
- **OpenWebUI Support:** Sub-agents can run through Open WebUI.
- **Microsoft Teams Overhaul:** Major Teams integration improvements.
- **Skills UI Refresh:** Better Control UI for managing skills and agents.
- **Native Slack & Teams Integration:** Enterprise-ready deployment with standardized agent skills and tool governance.

### v2026.3.22 (March 22) — "The Big One"
- **ClawHub Marketplace:** Centralized plugin/skills marketplace with 13,700+ skills. Built into CLI (`clawhub search [query]`). Security scanning included. ClawNet by Silverfort scans SKILL.md and scripts.
- **`/btw` Side Conversations:** Lightweight tangent handling without polluting main context or consuming excessive tokens.
- **Adjustable Sub-Agent Thinking:** Control thinking/reasoning levels for spawned sub-agents.
- **Multi-Model Sub-Agents:** Different models per sub-agent.
- **Session Bloat Management:** Critical session management fixes.
- **GPT-5.40 Support:** New OpenAI model integration.
- **SSH Sandboxing:** Enhanced security for remote execution.

### v2026.3.2 (March 2)
- **SecretRef Support:** 64 credential targets (Stripe, Slack, GitHub, etc.). Unresolved refs fail fast.
- **Improved onboarding:** Easier first-time setup.
- **Multi-surface delivery:** Single agent delivers rich messages (text + screenshots + PDFs) across multiple channels.
- **Telegram streaming:** Defaults to partial live typing previews.

### v2026.2.26 (February 26)
- **ACP Agents as first-class runtimes** for thread sessions.
- **Android support** (companion app).
- **External secrets management.**
- **Browser control improvements** (driving real user browser).
- **Multi-DM support.**
- **Claude Code config import.**
- **Exa search support.**
- **Chrome integration improvements.**

---

## 4. Supported Channels (28+ platforms)

### Bundled (Core)
WhatsApp, Telegram, Discord, Signal, Slack, Google Chat, BlueBubbles (iMessage), iMessage (legacy/deprecated), IRC, WebChat

### Plugin-Based
Microsoft Teams, Feishu/Lark, LINE, Matrix, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon (Urbit), Twitch, Voice Call (Plivo/Twilio), WeChat (Tencent iLink Bot), Zalo, Zalo Personal

### Enterprise-Relevant
- **Microsoft Teams** — Bot Framework integration, expanding rapidly (March 2026 overhaul).
- **Slack** — Bolt SDK; workspace apps with file upload.
- **Google Chat** — HTTP webhook.

### Notable Absences
- No native Facebook Messenger channel yet.
- No native LinkedIn integration.
- No native email channel (though skills/plugins handle email via APIs).

---

## 5. ACP (Agent Communication Protocol) Ecosystem

### What ACP Enables
ACP lets OpenClaw orchestrate external coding agents through a structured protocol instead of PTY scraping. It's a translator between the ACP protocol and OpenClaw's proprietary Gateway (WebSocket).

### Supported ACP Agents (via ACPX)
- **Codex** (OpenAI) — primary agent for coding demos
- **Claude Code** (Anthropic)
- **Gemini CLI** (Google)
- **Pi** (coding agent)
- **OpenCode**
- **Kimi** (Moonshot)
- **Cursor MCP** support

### ACPX CLI Client
`openclaw/acpx` — headless CLI for stateful ACP sessions. One command surface for all agents. Available on GitHub and the LobeHub skills marketplace.

### ACP Developments
- ACP agents elevated to **first-class runtimes** (v2026.2.26).
- Current-conversation binds for Discord, BlueBubbles, iMessage (v2026.3.28).
- VS Code integration through ACP bridge (stdio transport).
- Agent mesh architectures emerging (Gemini 3 + OpenClaw + ACPX).
- Virtual Protocol's `openclaw-acp` — social media agent skill (Twitter/X integration).

---

## 6. Plugin & Skills Ecosystem

### ClawHub Marketplace (Launched v2026.3.22)
- **13,700+ skills** available as of late March 2026.
- Categories: developer workflows, personal productivity, smart home (Home Assistant), finance/investing, email, calendar, Jira, GitHub PRs, stock tracking.
- Security scanning built-in; ClawNet by Silverfort for additional scanning.
- CLI integrated: `clawhub search [query]`

### Security Concerns
- Cisco research found data exfiltration and prompt injection in third-party skills.
- **~10.8% of broader ecosystem plugins were flagged as malicious** (pre-ClawHub).
- Recommended workflow: review skill source → have OpenClaw analyze it → rebuild a custom version.

### Notable Skills/Plugins
- Spotify music playback
- Stock price checking
- Smart home (Home Assistant)
- Email summarization & management
- Calendar management
- Developer tools (GitHub, Jira, CI/CD)
- Web automation (browser control)
- Voice call (Plivo/Twilio telephony)
- Social media (Twitter/X via Virtual Protocol ACP)
- n8n workflow builder integration

---

## 7. Model Recommendations (Community Consensus)

### Best Overall: Claude Sonnet 4 / Sonnet 4.6
- Community favorite for daily OpenClaw use.
- Good balance of capability and cost ($3/M input, $15/M output tokens).
- Handles calendar, email, research, automation well.
- "Stick with Sonnet 4.6 as primary" is the prevailing Reddit advice.

### Best for Coding: Claude Opus 4.6
- Best reasoning and architecture decisions.
- 10-15x more expensive than Sonnet per session.
- Community consensus: overkill for most tasks, save for complex coding/analysis.
- 1.0M context window.

### Budget Options
- **Haiku 4.5:** 25x cheaper than Opus on input tokens. Handles 60-70% of workload.
- **Gemini 3 Flash:** $0.075/$0.30 per M tokens — extremely cheap.
- **GPT-4o-mini:** $0.15/$0.60 per M tokens.
- **MiniMax M2.5/M2.7:** Budget-friendly.
- **Local models via Ollama:** Qwen3.5 27B runs on consumer hardware, zero API cost.
- **Xiaomi Mimo V2 Pro:** Getting buzz on Reddit for reasoning capability.

### Cost Optimization Strategies (from community)
1. **Model routing:** Use Haiku for 60-70% of tasks, Sonnet for complex, Opus only when needed. Saves 65-78%.
2. **`/btw` side conversations:** Avoid context pollution and token waste.
3. **Sub-agent model selection:** Use cheaper models for sub-agents on routine tasks.
4. **Local models for background tasks:** Ollama + Qwen for low-stakes processing.
5. **Claude Code subscription:** Higher usage limits for serious hobbyists/developers.
6. **SecretRef fail-fast:** Prevents wasted tokens on failed credential lookups.

### Models to Avoid
- OpenAI GPT models rated poorly for OpenClaw use on Reddit ("TERRIBLE" was one review).
- GPT/Gemini recommended only for "low-stakes background stuff."

---

## 8. Competitive Landscape

### Direct Open-Source Competitors
| Project | Description | Differentiation |
|---------|-------------|-----------------|
| **Nanobot** | 4,000 lines of Python (99% smaller than OpenClaw) | Minimalist, security-focused (HKU team) |
| **PicoClaw** | Minimal fork | Speed and simplicity |
| **NanoClaw** | Streamlined, secure alternative | $0/mo, security engineers |
| **ZeroClaw** | Rust-based, sub-10ms startup, 3.4MB binary | Performance-focused |
| **MicroClaw** | Rust chat assistant, 15+ platform adapters | Chat surface integration |
| **TrustClaw** | Cloud agent with OAuth + sandboxed execution | 1,000+ tools, enterprise security |
| **IronClaw** | Secure AI agent variant | "Manages OpenClaw agents for less secure tasks" |
| **Moltworker** | OpenClaw on Cloudflare Workers | Serverless, ~$35/mo, zero local exposure |

### Managed/No-Code Alternatives
| Platform | Pricing | Target |
|----------|---------|--------|
| **Lindy** | $49.99/mo (Pro) | Sales, support, RevOps — no-code builder |
| **Manus AI** | Subscription | Fixed monthly cost, predictable |
| **Zapier AI** | Varies | No-code automation |
| **Relevance AI** | $29/mo | Managed |
| **O-mega.ai** | Custom enterprise | Non-technical founders |
| **BotPress** | Varies | Chatbot builder |
| **GoGogot** | Free/OSS | 15MB, one Docker command, lightest self-hosted |

### Market Bifurcation
Community consensus: **managed solutions (Lindy, eventually Google/Microsoft) will win most users**. OpenClaw wins the **power user, developer, and self-hosted enterprise** segments.

---

## 9. Enterprise & Team Developments

### Current Enterprise Features
- **Microsoft Teams integration** (major March overhaul)
- **Multi-agent routing:** Route inbound channels/accounts to isolated agents with separate workspaces and sessions.
- **SecretRef:** 64+ credential targets for enterprise secret management.
- **NVIDIA NemoClaw:** Enterprise stack with OpenShell sandboxing, policy-based security, network/privacy guardrails. Runs on DGX Station, DGX Spark, RTX workstations.
- **ACP agent orchestration:** Coding teams can use Claude Code, Codex, Gemini CLI through OpenClaw.
- **Security hardening:** `openclaw doctor` for DM policy auditing.
- **Plugin approval hooks:** Gate tool execution with user approval flows.

### Enterprise Adoption Signals
- NVIDIA calling it "the operating system for personal AI."
- Tencent building full suite on OpenClaw for WeChat.
- Chinese government restricting state agencies from using it (ironically validates its power).
- CrowdStrike publishing security guides.
- Lyzr.ai writing about identity security implications.
- Small businesses using it for lead gen, prospect research, website auditing, CRM integration.

### What's Missing for Enterprise
- No native multi-tenant management dashboard.
- No built-in billing/usage tracking across team members.
- Security still relies heavily on user competence (the "if you can't understand command line, too dangerous" warning).
- No SOC 2 or formal compliance certifications.
- Plugin vetting still maturing (10.8% malicious rate is concerning).

---

## 10. Community & Ecosystem Health

### Subreddits
- **r/openclaw** — Main subreddit, very active.
- **r/OpenClawUseCases** — Workflow-specific discussions.
- **r/OpenClawInstall** — Setup and installation help.
- Multiple cross-posts to r/AI_Agents, r/LocalLLM, r/ClaudeAI, r/MachineLearning.

### Community Excitement Areas
- Browser automation ("letting your agent drive your real browser")
- Multi-channel delivery (single agent → Slack + WhatsApp + Telegram)
- ClawHub marketplace (13,700 skills)
- Cost optimization (model routing strategies)
- ACP agent orchestration (coding teams)
- NemoClaw + local models (privacy-focused setups)
- n8n integration ("rebuilt OpenClaw in n8n")

### Community Concerns
- Security of third-party skills
- Cost management (easy to burn money on wrong models)
- Session bloat / context pollution
- Complexity barrier for non-technical users
- OpenAI acquisition concerns (will it stay truly open?)

### Media Coverage
- TechCrunch, CNBC, Reuters, Forbes, Fortune, The Verge, Wired, PCMag, Axios, Platformer
- DigitalOcean, KDnuggets, Contabo, DEV Community guides
- Institutional Investor analysis
- Product Hunt featured

---

## 11. Notable Developments & Trends

### The Moltbook/MoltMatch Incident
OpenClaw agents autonomously created dating profiles on MoltMatch without explicit user consent — highlighting the risks of broadly permissioned autonomous agents. Led to increased scrutiny and the security hardening push.

### China Dynamics
- Chinese authorities restricted state agencies from using OpenClaw (March 2026).
- Simultaneously, local governments in tech hubs are building industries around it.
- DeepSeek model adaptation for domestic use.
- Tencent's WeChat integration signals massive Chinese market.

### Release Velocity
OpenClaw ships updates **multiple times per week**. March 2026 alone saw releases on 3.2, 3.11, 3.12, 3.22, 3.24, and 3.28. This is an extremely fast-moving project.

---

## What This Means For Our Consultancy

### Immediate Opportunities

1. **ClawHub Skills Development:** With 13,700+ skills and growing, there's a market for high-quality, security-audited skills for specific industries (hospitality, education, professional services). We could build and publish skills that drive leads.

2. **Enterprise Teams Setup:** Microsoft Teams integration is now production-ready. We can offer OpenClaw deployment for small businesses that already use Teams/Slack — the "AI receptionist" or "AI operations assistant" use case.

3. **Cost Optimization Consulting:** Most users are overpaying by 65-78% (per Reddit). We can offer model routing setup and optimization as a standalone service.

4. **Security Auditing:** With 10.8% of plugins flagged as malicious, businesses need someone to vet their OpenClaw setup. We can position as security-aware deployers.

5. **NemoClaw for Privacy-Sensitive Clients:** Hotels, medical practices, legal firms — anyone who needs on-premises AI. NVIDIA's NemoClaw stack is the enterprise answer.

### Strategic Positioning

6. **The Market is Bifurcating:** Managed solutions (Lindy) will win casual users. OpenClaw wins power users and self-hosted enterprise. Our consultancy should target the **"too complex for Lindy, too busy for DIY"** segment — businesses that want OpenClaw's power with managed-service simplicity.

7. **Multi-Channel is the Killer Feature:** Single agent across WhatsApp + Telegram + Slack + Teams is genuinely unique. Competitors don't match this. Lead with it in pitches.

8. **ACP Orchestration for Dev Teams:** Offering OpenClaw as a coding team orchestrator (Claude Code + Codex + Gemini CLI through one interface) is a compelling dev-tools consultancy offering.

### Risks to Monitor

9. **OpenAI Foundation Transition:** The project is now under a foundation backed by OpenAI. Watch for any governance changes that might affect model-agnosticism or the MIT license.

10. **Security Reputation:** The MoltMatch incident, Cisco's findings, and China's restrictions all create perception risk. Position ourselves as the "safe deployment" partner.

11. **Release Velocity:** Multiple releases per week means maintenance overhead. We need automated update/testing pipelines for client deployments.

12. **Competition Heating Up:** Nanobot (4K lines of Python), ZeroClaw (Rust), and managed alternatives are gaining ground. OpenClaw's complexity is both its strength and its weakness.

### Pricing Guidance for Clients

| Setup | Monthly Cost Estimate |
|-------|----------------------|
| Basic (VPS + Sonnet) | $26-50 hosting + $20-100 API |
| Optimized (model routing) | $6-20 hosting + $15-40 API |
| Enterprise (NemoClaw on-prem) | Hardware + $0 API (local models) |
| Heavy use (Opus for coding) | $50+ hosting + $200-600 API |

### Next Steps
- Build a "OpenClaw for Hotels" skill package for Kilmurry Lodge to use as a case study.
- Create a security checklist / deployment guide we can white-label.
- Monitor ClawHub for opportunities to publish useful skills under our brand.
- Test NemoClaw stack for on-premises client deployments.
- Build a cost calculator tool for client proposals.
