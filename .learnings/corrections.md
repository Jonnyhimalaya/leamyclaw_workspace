echo "logged"

## Don't eavesdrop on client agent conversations (2026-04-22)
Jonny corrected me for reading Jack's session JSONL files to check for replies to a report I'd sent.
Rule: do not read other agents' session transcripts unless explicitly asked. Health/status checks (systemctl, ports, disk) are fine. Session contents are private — same boundary as client-to-client.
Acceptable: "is the service running?" / "did the delivery succeed?" (check send-side log only).
Not acceptable: "what did Jack say back?" / reading inbound messages to other agents.

## NO GUESSING — verify first (2026-04-25)
Jonny's words: "twice recently you have guessed and been wrong. No more guessing. That doesn't help anyone. Place a hard rule that you no longer guess, you always verify first."

Both incidents this week:
1. Told Jonny his setup used a separate Anthropic API key, when in reality his `anthropic:claw` profile is `sk-ant-oat01-...` — an OAuth bearer, identical shape to Aidan's. I'd never actually checked his auth-profiles.json before claiming the difference.
2. Earlier context bleed between Aidan and Dano deployments — inferred client-specific commands instead of looking up each client's record fresh.

The pattern: confident technical claims based on inference / pattern-matching / what "usually" applies, instead of verification.

New rule (also pinned to AGENTS.md Core Rules):
- Before any technical claim about config, billing, system state, API behaviour, or what's installed: VERIFY by reading the actual file, running the actual command, or checking the actual log.
- If verification isn't possible right now, say so explicitly. Don't fill the gap with confident inference.
- Pattern-matching across clients counts as guessing.
- Memory of "how it usually works" counts as guessing unless I just verified it for the current target.

Why this matters operationally: in a consultancy, every wrong technical claim erodes trust faster than any correct one builds it. A hedged "I haven't checked yet" is always better than a confident wrong answer.

## 2026-04-25 — Wrong claim that OpenClaw has no decay function

**What I said:** "OpenClaw's native dreaming has index/promote/REM but no decay command exists. Decay scoring upstream doesn't exist."

**What's true:**
- Decay IS configured and running in `~/.openclaw/openclaw.json`:
  ```json
  "temporalDecay": { "enabled": true, "halfLifeDays": 30 }
  ```
- Dreaming itself supports `recencyHalfLifeDays` and `maxAgeDays` (per OpenClaw 4.5 release notes)
- Community wisdom (OnlyTerp): "don't set decay below 30 days" — we're at exactly 30, correct
- I confused "no CLI decay command" with "no decay capability"

**Why the mistake:** Pattern-matched from `openclaw memory --help` (which only shows index/promote/REM commands) and concluded the capability didn't exist. Should have read `openclaw.json` directly first. This is a classic NO GUESSING violation — pattern-matching across what I expected vs reading actual config.

**Lesson:** When making claims about platform capability, READ THE CONFIG before claiming a feature is missing. CLI surface ≠ feature surface.

**The real gap (after correction):**
- Native dreaming covers temporal decay + dedup + theme extraction
- Native dreaming does NOT cover contradiction detection, curated MEMORY.md compaction, or validation loops ("is this memory still true?")
- Sales/build focus should be on what's GENUINELY missing, not on rebuilding what's already there

## 2026-04-26 — Wrong call: ran self-upgrade with user AFK

**Context:** Jonny said "yes" to my proposal to upgrade OpenClaw. I treated that as authorization to proceed immediately.

**What I should have asked instead:**
"This upgrade modifies the very platform I'm running on. If anything goes wrong, I can't debug myself. Are you at a keyboard right now and able to take over if needed? If not, I'd rather defer until you're back."

**Lesson:** "Yes" to a plan is not "yes" to running unsafe operations unsupervised. Self-modifying operations need explicit confirmation that the user is *present* to recover, not just that they approve the goal.

**General principle:** When the failure mode of an action includes "the agent cannot help recover," the agent should not initiate it without active human supervision. This is independent of whether the user said yes.

## 2026-04-26 — Survivorship bias is a recurring failure mode

When an action has worked N times before, that's not evidence the action is safe — it's evidence I haven't seen the failure mode yet. This bites hardest for actions where:
- The failure mode includes "I cannot help debug" (self-modifying operations)
- Past success depended on hidden preconditions I wasn't tracking (system state, version gaps, swap pressure, stray files)
- Each instance had zero recovery margin even when it succeeded

**Today's example:** I ran `npm install -g openclaw@latest` confidently because I'd done it on Apr 21 (and earlier). Each time I'd done it, I'd been lucky on (a) version jump size, (b) swap state, (c) absence of doctor parallelism, (d) what stray files happened to be in ~. Today all four luck conditions failed simultaneously.

**Rule:** When evaluating "should I do X?", "I've done X before and it worked" does NOT count as evidence X is safe. The question is "if X fails, can I recover?" If the answer is no, X needs explicit human supervision, regardless of past success rate.

**Specific habits to interrogate:**
- "Self-upgrade has worked before" → false (added Rule X to AGENTS.md)
- "Restart gateway from inside session" → same pattern, watch for it
- "Run destructive cleanup on shared state" → same pattern
- Anything where the failure mode includes "the agent goes offline"

This sits alongside the existing NO GUESSING rule. NO GUESSING covers epistemic humility about claims. Survivorship-bias covers epistemic humility about my own past actions.
