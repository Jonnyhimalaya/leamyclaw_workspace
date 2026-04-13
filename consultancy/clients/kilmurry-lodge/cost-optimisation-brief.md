# Kilmurry Lodge — Cost Optimisation Brief
_Created: 2026-04-13_

## The Problem
Jack is running Claude Opus 4.6 as his primary model while building Mission Control.
Opus is $15/$75 per MTok. We know from our own experience this is unsustainable for heavy build sessions.
He stated intention to "route cheaper work later" — that later needs to be now.

## What We Found (Direct SSH Inspection — 2026-04-13)
- SSH access confirmed: `clawuser@172.239.98.61`
- OpenClaw version: **v2026.4.2** (needs upgrade to v2026.4.10)
- Primary model confirmed as: **`anthropic/claude-opus-4-6`** (not Sonnet as intended)
- Sessions dir: 43 Codex/ACP session files (these are his TUI/build sessions — no separate TG session files found, TG likely ephemeral)

### Session Bloat — Confirmed Critical
| Session | Messages | Size | Date range |
|---------|----------|------|------------|
| 6fea5e39 | **980 msgs** | **5.2MB** | Apr 5 → Apr 13 (8 days!) |
| 2b42c6b8 | 494 msgs | 525KB | Apr 3+ |
| f71af034 | 146 msgs | 477KB | — |
| a8ba4869 | 125 msgs | 464KB | — |
| fdfed1da | 97 msgs | 397KB | — |

The **980-message / 5.2MB session running for 8 days straight** is the smoking gun. Every single Opus request in that session is sending ~5MB of context tokens. At Opus pricing that is extremely expensive.

## What We Can Do

### 1. Switch Default Model to Sonnet
His openclaw.json likely has:
```json
"models": { "default": "anthropic/claude-opus-4-6" }
```
Should be:
```json
"models": { "default": "anthropic/claude-sonnet-4-6" }
```
Sonnet is $3/$15 per MTok vs Opus $15/$75 — **5x cheaper per token**.
For building/coding/iterating this is the right model. Opus is for strategy and complex reasoning only.

### 2. Session Hygiene — /new Regularly
Building sessions accumulate fast. Each message in a long session adds to context tokens sent.
A 200-message session might be sending 50K+ tokens of context per request.
Rule: /new after every distinct build task. Don't carry a coding session forward.

### 3. Prompt Caching
Upgrade to v2026.4.5+ (fixes CST-017 — broken prompt caching).
With caching enabled, repeated system prompt + long context costs 90% less on cache hits.
His AGENTS.md/SOUL.md/MEMORY.md injection is likely 10-15KB — with caching this is nearly free after the first call in a session.

### 4. Route Build Work to Codex/Claude Code Harness
When building MC features, spawn a sub-agent instead of doing it inline.
Claude Code with `--permission-mode bypassPermissions` runs a focused coding session and exits.
Much cheaper than an ongoing conversational Opus session with large context.

### 5. Audit His openclaw.json Auth Config
Check if failover is configured:
```json
"auth": {
  "order": { "anthropic": ["primary", "backup"] },
  "rateLimitedProfileRotations": 2
}
```
Without this, rate limits cause retries instead of failover — wasted calls.

## Estimated Savings
If Jack switches Opus → Sonnet for day-to-day build work:
- A 100K token session costs €1.50 on Sonnet vs €7.50 on Opus
- Heavy build day (500K tokens): €7.50 vs €37.50
- That's €30/day saved on active build days

## How to Communicate This to Jack
Jonny can share this directly, or KilmurryBot can surface it.
The message is simple: "Opus for thinking, Sonnet for building — switch your default."

## Action Required
- [ ] Jonny mentions to Jack: switch default model to Sonnet in openclaw.json
- [ ] Jack runs /new regularly between build tasks
- [ ] Upgrade Kilmurry OpenClaw to v2026.4.5+ (already on our list for CVE patch anyway)
- [ ] Check if session hygiene note should go into KilmurryBot's AGENTS.md
