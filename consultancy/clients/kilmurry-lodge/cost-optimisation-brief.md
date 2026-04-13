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

## Revised Strategy — Claude Code for Building (2026-04-13)

Jack wants to stay on Opus. That's fine — the real win is a workflow change.

### Key Finding from SSH Inspection
- Jack **has used Claude Code** before (3 sessions in March, in `~/.claude/projects/-home-clawuser-mission-control/`)
- Claude Code is **not installed in PATH** — currently only accessible via `npx`
- Claude Code has **no credentials file** — unclear what auth it was using
- Jack has **OpenAI Codex OAuth** already authenticated (ChatGPT Plus subscription) — the Codex harness is available
- Anthropic auth is `mode: token` (API key = billable) NOT subscription OAuth

### The Right Architecture
```
KilmurryBot (Opus via API — orchestrates, decides, directs)
    ↓ spawns
Claude Code (via Anthropic subscription — builds, writes files, iterates)
```

Bot stays on Opus but only for:
- Strategy and planning
- Short directives ("build this feature", "fix this bug")
- Reviewing output

Claude Code handles:
- All file writing and editing
- All code iteration
- Build/test loops

### What Needs to Happen
- [ ] **Install Claude Code properly:** `npm install -g @anthropic-ai/claude-code` (into `~/.npm-global`)
- [ ] **Auth Claude Code to Anthropic subscription** (not API key) — Jack needs to run `claude` and authenticate with his Anthropic account login (not API key)
- [ ] **Wire ACP harness in openclaw.json** — enable `acp` section to allow the bot to spawn Claude Code sessions
- [ ] **Add to KilmurryBot AGENTS.md** — rule: "For any file writing or code building, spawn Claude Code via ACP harness instead of doing it inline"
- [ ] **Jack does /new now** — kill that 980-msg session
- [ ] Upgrade Kilmurry OpenClaw to v2026.4.10 (CVE patch + prompt cache fix)

### Same Pattern We Use
This is exactly the Opus-thinks-Sonnet-clicks pattern from our own setup, just with Claude Code instead of Wrench. Bot spends tokens on decisions, not on writing 200 lines of TypeScript.
