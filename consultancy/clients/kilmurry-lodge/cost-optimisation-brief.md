# Kilmurry Lodge — Cost Optimisation Brief
_Created: 2026-04-13_

## The Problem
Jack is running Claude Opus 4.6 as his primary model while building Mission Control.
Opus is $15/$75 per MTok. We know from our own experience this is unsustainable for heavy build sessions.
He stated intention to "route cheaper work later" — that later needs to be now.

## What We Can't Check Directly
- No SSH access to Kilmurry server (clawuser password never provided)
- MC API is firewalled to Jack's Tailscale IPs only
- Can't inspect live session sizes or token counts remotely

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
