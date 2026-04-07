# Anthropic API Migration Guide for OpenClaw Deployments
**Created:** 2026-04-07
**Context:** Anthropic stopped allowing Pro/Max subscriptions for third-party tools (effective April 4, 2026)

## Background
- Claude Pro ($20/mo) and Max ($100-200/mo) subscriptions no longer cover third-party tool usage (OpenClaw, etc.)
- Existing OAuth tokens (`sk-ant-oat` prefix) may still work temporarily but will die as rollout continues
- Transition credit available: equal to monthly plan fee, must claim by April 17, valid 90 days

## Migration Steps (per deployment)

### 1. Claim Transition Credit
- console.anthropic.com → Settings → Usage → "Claim credit"
- Deadline: April 17, 2026
- One-time, per-subscriber

### 2. Create API Key
- console.anthropic.com → Settings → API Keys → Create Key
- Add credits ($50 minimum, claim promo if eligible)

### 3. Configure OpenClaw
```bash
# Add the new API key
openclaw models auth paste-token --provider anthropic --profile-id anthropic:api-key

# Set as priority
openclaw models auth order set --provider anthropic anthropic:api-key

# Restart gateway
sudo systemctl restart openclaw-gateway  # or relevant service name
```

### 4. Verify
- Run a test prompt through each agent that uses Anthropic models
- Check `openclaw models auth list --provider anthropic` to confirm active profile

## Cost Estimates (April 2026 Pricing)
| Model | Input/MTok | Output/MTok | Typical Daily (Light) | Typical Daily (Heavy) |
|-------|-----------|-------------|----------------------|----------------------|
| Opus 4.6 | $5 | $25 | $2-5 | $20-80 |
| Sonnet 4.6 | ~$1 | ~$5 | $0.50-2 | $5-15 |
| Haiku | ~$0.25 | ~$1.25 | $0.10-0.50 | $1-3 |

## Cost Mitigation Strategies
1. **Model tiering:** Use Haiku/Sonnet for routine tasks, Opus only for complex reasoning
2. **Primary provider diversification:** GPT-5.4, Qwen, Gemini as primaries where appropriate
3. **Local models (Ollama):** For cost-sensitive clients, Ollama integration is mature in v2026.4.5
4. **`--max-memory` flags:** Cap agent context to reduce token consumption
5. **Prompt caching:** v2026.4.5 improved caching — reduces repeat-context costs

## Client Communication Template
> We're updating your AI assistant's connection to Claude (the AI model by Anthropic). This is a routine backend change — you won't notice any difference in how your assistant works. We're also optimising costs by routing different tasks to the best-fit model, which keeps your monthly costs predictable.

## Risks
- OAuth tokens could die without warning during gradual rollout
- API billing has no ceiling — set billing alerts at console.anthropic.com
- Community tool `openclaw-billing-proxy` exists but is third-party and not recommended for client deployments

## Lessons Learned
- Always use API keys (not OAuth/subscription tokens) for production/client deployments
- Multi-provider fallback chains are essential resilience
- Provider billing changes can happen fast — 3 days from announcement to enforcement
