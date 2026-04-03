# Claude Code Channels vs OpenClaw — Competitive Analysis
**Date:** 2026-04-03
**Status:** Draft — needs refinement with hands-on CCC testing

## What Is Claude Code Channels?
Anthropic's feature allowing users to control live Claude Code sessions remotely via Telegram, Discord, iMessage, and WhatsApp through MCP-based bridges. Launched late March 2026.

## Feature Comparison

| Feature | Claude Code Channels | OpenClaw |
|---------|---------------------|----------|
| **Channels supported** | ~4 (Telegram, Discord, iMessage, WhatsApp) | 20+ (including Slack, Teams, Signal, Matrix, Line, WeChat, Feishu) |
| **Multi-agent orchestration** | No — single Claude session | Yes — multiple agents with different models, roles, handoff |
| **Persistent memory** | No — loses context on restart | Yes — MEMORY.md, vault, compaction, cross-session recall |
| **Self-hosted/sovereign** | No — Anthropic infrastructure | Yes — runs on your hardware, your data stays local |
| **Custom personality (SOUL.md)** | No | Yes — full persona customisation |
| **Skills/plugins** | Limited to Claude Code capabilities | Extensible skill system, ClawHub marketplace |
| **Model flexibility** | Claude only | Any model (Claude, GPT, Grok, Gemini, local via Ollama) |
| **Use cases** | Coding/development | Any — business ops, marketing, education, hospitality, content |
| **Setup complexity** | Low (official integration) | Medium (self-hosted, requires configuration) |
| **Cost** | Anthropic API pricing | Self-hosted + API costs (can use free/cheap local models) |
| **Security model** | Allowlists, pairing | Configurable sandbox, approval hooks, exec policies |

## Where CCC Wins
- Zero-setup for existing Claude Code users
- Official Anthropic support and polish
- Secure pairing model out of the box
- Tight integration with Claude's coding capabilities (filesystem, git)

## Where OpenClaw Wins
- **Breadth:** 20+ channels means businesses can meet customers where they are
- **Depth:** Multi-agent orchestration, persistent memory, custom skills
- **Sovereignty:** Self-hosted, no vendor lock-in, data stays on-premises
- **Flexibility:** Any model, any use case — not limited to coding
- **Business use cases:** Hotels, education, service businesses don't need coding agents — they need operations agents

## Our Consultancy Pitch
> "Claude Code Channels is great for solo developers who want to message their coding assistant. We build AI operating systems for businesses — multiple specialised agents that remember your context, work across all your communication channels, and run on your infrastructure. CCC is a walkie-talkie. We build the control room."

## Action Items
- [ ] Hands-on test of CCC to verify limitations firsthand
- [ ] Prepare a 1-page comparison for client conversations
- [ ] Monitor CCC feature development — if they add persistence/multi-agent, reassess
