# Scout Report — March 28, 2026 — Morning

## 🚨 Action Required

- **OpenClaw v2026.3.22 breaking changes** — Legacy Chrome extension relay path removed from Browser/Chrome MCP. Run `openclaw doctor --fix` after updating to migrate browser config. If using browser automation skills, verify they still work.
- **Plugin install behaviour changed** — `openclaw plugins install <package>` now checks ClawHub first before npm. Could affect any custom plugin scripts.
- **`openclaw update` now verbose** — explicitly says "up to date" when already on latest. Minor UX improvement, no action needed.
- **Azure AI Foundry fix** — custom endpoints (*.services.ai.azure.com) kept on chat-completions path instead of being forced to Responses API. Relevant if using Azure-hosted models.

## 🔧 Our Stack

- **Latest stable:** OpenClaw v2026.3.23 (patch) / v2026.3.23-2 (follow-up). Stabilisation release after the heavy v2026.3.22.
- **Beta:** v2026.3.22-beta.1 on npm beta tag — skip unless testing.
- Key fix in v2026.3.23: Plugin SDK stabilisation, browser attach fixes, Qwen provider refresh.
- Full migration docs: https://docs.openclaw.ai/install/migrating
- ClawHub now the primary plugin source: https://docs.openclaw.ai/tools/clawhub

## 🤖 Agentic Ecosystem

- **Windsurf/Codeium** overhauled pricing (March 19): switched from credits to daily/weekly quotas. Relevant to us? No — we use Claude Code / OpenClaw, not Windsurf directly.
- **Claude Code changelog** — multi-line input navigation improved (up/down arrows now move cursor vs. history). Minor UX polish. Relevant to us? Yes — we use Claude Code daily; subtle but welcome.
- No major new agentic orchestration patterns spotted in last 12 hours.

## ⭐ Notable Releases

- **Claude Mythos (Anthropic)** — Leaked and confirmed by Anthropic (March 26-27). Described as a "step change" in capabilities. Not yet released publicly; in testing. Source: [Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) / [Mashable](https://mashable.com/article/claude-mythos-ai-model-anthropic-leak). **Watch closely** — if this rolls into Claude API, it'll affect our model costs and capabilities.
- **Google Gemini 3.1 Flash Live** — shipped, multimodal voice model. Relevant to us? Low for now — not in our stack.
- **Meta TRIBE v2** — open-source "brain AI" (neuroscience-flavoured). Research interest only.

## 📡 Trends & Intel

- AI coding tool cost is becoming a real concern — blog coverage of $150-400/mo spend for devs using 2-3 tools. We're well-positioned with OpenClaw as a unified platform.
- Google Gemini pushing chat history import from other chatbots (chatGPT migration tool). Consumer play, not directly relevant.
- Claude Mythos leak suggests Anthropic's next flagship is closer than expected. May reshape pricing tiers.

---
*Saved: /home/jonny/.openclaw/workspace/artifacts/2026-03-28/radar-morning.md*
