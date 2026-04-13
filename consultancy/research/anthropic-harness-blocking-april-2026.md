# Anthropic Harness Blocking — April 2026

## What Happened
Starting April 4, 2026 (12pm PT / 8pm BST), Anthropic stopped allowing Claude subscription limits for third-party harnesses including OpenClaw. Key impacts:

1. **Subscription blocking:** Subscriptions no longer cover OpenClaw usage — requires "Extra Usage" (pay-as-you-go) billing
2. **Prompt-level filtering:** Prompts mentioning OpenClaw trigger 400 errors, even on API billing
3. **Account suspensions:** Some users (including OpenClaw creator Peter Steinberger) temporarily banned for "suspicious activity"
4. **First-party harness blocking:** Not just third-party — even first-party harness use was blocked

## OpenClaw's Response
- Removed Claude CLI support from OpenClaw
- Recommends API keys or alternative providers
- Actively shifting to multi-provider support (GPT-5.4, Qwen, Gemma, local models)

## Community Recommendations
- Use Anthropic API keys (not subscription) for continued access
- Migrate agent workloads to GPT-5.4, Gemini, or open-source models
- Keep Anthropic for ad-hoc Claude usage, not production agent loops
- Local models (Gemma 4 12B, Llama 3.3 70B) viable for cost-sensitive deployments

## Impact on Our Setup
- sitemgr (Wrench) and marketing (Prism) both run Sonnet 4-6
- API billing partially protects us from subscription-tier blocking
- Prompt-level filtering is the higher risk — if system prompts reference OpenClaw internals, agents may fail
- Migration path: Gemini 3.1 Pro (cheaper, already our strategist model) or GPT-5.4 (our main/content model)

## Consultancy Implication
- Any client pitch involving Anthropic models needs a failover plan
- Standard deployment template should include multi-model configuration
- Gemma 4 (Apache 2.0, 12B, ~7GB RAM) is the recommended budget/compliance tier — no vendor lock-in risk

## Sources
- HN: https://news.ycombinator.com/item?id=47633396
- X: Multiple posts from @steipete and community (April 3-11, 2026)
- Price Per Token community: https://pricepertoken.com/leaderboards/openclaw
