# Anthropic Third-Party Billing Policy Change — April 2026

## Summary
Effective April 4, 2026 (3PM ET), Anthropic no longer covers third-party tool usage (OpenClaw, Cursor, Windsurf, etc.) under Claude Pro/Max subscriptions. Usage must go through API keys or "extra usage" pay-as-you-go billing.

## What Changed
- Subscription OAuth tokens blocked from third-party harnesses
- Subscription still covers: claude.ai, Claude Code, Claude Cowork
- Third-party tools require: separate API key OR "extra usage" enabled on account
- One-time transition credit offered (= monthly subscription price), redeemable by April 17, 2026

## Why It Happened
- Heavy agent users (OpenClaw, agentic pipelines) consuming 6-8x what human subscribers use
- Subscriptions oversold capacity assuming human usage patterns
- Anthropic prioritising their own product ecosystem (Claude Code, Cowork)

## API Pricing (as of March 2026)
| Model | Input/MTok | Output/MTok | Notes |
|-------|-----------|-------------|-------|
| Opus 4.6 | $5 | $25 | 66% cheaper than Opus 4.0/4.1 |
| Sonnet 4.6 | ~$3 | ~$15 | Good for high-volume agent tasks |
| Haiku 4.5 | ~$0.80 | ~$4 | Price floor, fast tasks |

## Cost Optimisation Levers
- **Prompt caching:** 50% discount on cached input tokens
- **Batch processing:** 50% discount for non-real-time workloads
- **Model selection:** Use Haiku/Sonnet for routine tasks, Opus only for complex reasoning
- **Token efficiency:** Shorter system prompts, compressed context

## Impact on Multi-Agent Deployments
- Each agent in a pipeline generates its own token costs
- Our 5-agent setup (Orchestrator + Sitemgr + Marketing + Scout + Content) could cost $100-300/month at typical usage
- Scout already uses xAI (Grok), not affected
- Content agent uses OpenAI (GPT-5.4), not affected
- Primary impact: Orchestrator (Opus), Sitemgr (Sonnet), Marketing (Sonnet), Strategist (Opus)

## Client Advisory
For clients running OpenClaw with Anthropic models:
1. Verify auth method (subscription OAuth vs API key)
2. Switch to API keys before enforcement date
3. Claim transition credit
4. Implement model routing: expensive models for complex tasks only
5. Consider multi-provider strategy to avoid single-vendor lock-in

## Consultancy Positioning
This is a recurring pattern: subscription arbitrage gets closed. Position our consultancy as helping clients navigate these transitions proactively. This won't be the last time a provider changes billing terms.
