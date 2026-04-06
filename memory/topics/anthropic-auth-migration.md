# Anthropic Auth Migration (2026-04-04)

## Timeline
- **2026-04-04 ~19:00 UTC:** Anthropic enforced billing change — Claude subscriptions no longer cover third-party tools (OpenClaw).
- **2026-04-04 19:07 UTC:** Confirmed both profiles (`anthropic:claw`, `anthropic:work`) use `sk-ant-oat` prefix = OAuth Access Tokens (subscription-based). NOT API keys.
- **2026-04-04 23:07 UTC:** OAuth tokens still working 4h post-cutoff. Rollout may be gradual.
- **2026-04-05 morning:** Still working as of session startup (Opus serving this session).

## Current State
- Tokens work but could die any time as rollout continues.
- Fallback chain: Opus(sub) → Opus(work) → OpenRouter/Opus → Sonnet → Gemini → GPT-5.4 → GPT-4o
- OpenRouter profile is API-key based — will keep Opus/Sonnet accessible at higher per-token cost.

## Action Needed
1. Jonny: console.anthropic.com → API Keys → create new API key
2. Claim transition credit (Settings > Usage, available until April 17)
3. Update auth-profiles.json to use the new API key
4. Estimated monthly API cost: $100-300

## Pricing Reference
- Opus 4.6: $5/$25 per MTok (66% cheaper than Opus 4.0)
- Sonnet 4.6: much cheaper, used for sitemgr/marketing agents
