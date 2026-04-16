# Anthropic Claude Billing Migration — OpenClaw Deployments
**Date:** 2026-04-16
**Status:** Active — affects all OpenClaw clients using Claude

## What Changed
- **April 4, 2026:** Claude Pro/Max/Team subscriptions no longer cover usage through third-party harnesses (OpenClaw, ACP, etc.)
- Subscriptions now only cover Anthropic's own products: Claude.ai, Claude Code (native), Cowork
- Third-party usage requires: (a) "extra usage bundles" or (b) direct API key billing

## Transition Offers (Expiring)
- One-time credit = 1 month's subscription price (e.g., $200 for Max)
- **Redemption deadline: April 17, 2026**
- 30% discount on pre-purchased extra usage bundles (temporary)

## Migration Paths (Ranked by Reliability)

### 1. API Key Billing (Recommended)
- Create Anthropic API key at console.anthropic.com
- Add to OpenClaw config: `ANTHROPIC_API_KEY=sk-ant-...`
- Pay-per-token, no rate limit games
- **Pro:** Clean, future-proof, no TOS risk
- **Con:** Can be expensive for heavy agentic use (Opus 4.6 especially)

### 2. Extra Usage Bundles
- Pre-purchase token bundles via Anthropic dashboard
- 30% discount currently available
- Still uses subscription login (not API key)
- **Pro:** Cheaper than raw API if you buy in bulk
- **Con:** Still tied to Anthropic account management, discount may expire

### 3. Cowork Bridge (Sub-Safe Workaround)
- OpenClaw writes JSON outputs to shared file
- Claude Cowork (official app) reads/processes/responds
- Uses subscription limits directly (not third-party harness)
- ~15 min setup on Mac
- **Pro:** Uses existing sub, no extra cost
- **Con:** Clunky, Mac-only, latency, brittle

### 4. Provider Switching
- Codex provider (bundled in v2026.4.10): `codex/gpt-*` models with managed auth
- GPT-5.4 via OpenAI (our primary model already)
- Local models: Gemma 4 12B via Ollama (good for budget tiers)
- **Pro:** Eliminates Anthropic dependency entirely
- **Con:** Model quality differences for certain tasks

### 5. OAuth Proxies (NOT Recommended for Clients)
- Dario, OpenClaude, various GitHub proxy projects
- Route through local proxy using PKCE OAuth
- **Risk:** TOS violation, Anthropic may enforce further, breakable at any time
- **Never recommend to clients**

## Cost Modelling Framework
For client consultations, model:
- Current subscription cost/month
- Estimated token usage (check OpenClaw usage stats)
- API cost at current rates (input/output token pricing)
- Extra usage bundle cost with 30% discount
- Alternative model cost (GPT-5.4, Codex, local)

## Our Client Impact
- **Jack (Kilmurry):** ACP harness used Claude Max team sub → broken since April 4. Migrate to API key or Codex provider.
- **Our own setup:** Already on API billing (GPT-5.4 primary). Strategist runs on Opus API. Impact minimal for us directly.

## Consultancy Opportunity
- Every OpenClaw user on Claude is affected
- Write public migration guide → lead generation
- Offer paid "billing migration audit" (1-hour, review usage, model costs, recommend path)
- Time-sensitive: community attention peaks now, fades in 2-3 weeks
