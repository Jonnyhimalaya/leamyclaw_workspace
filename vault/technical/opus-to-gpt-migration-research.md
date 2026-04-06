# Opus → GPT-5.4 Migration Research
_Compiled: 2026-04-06 from X/Twitter community, Meta-Harness paper, OpenClaw maintainer guidance_

## TL;DR

The community consensus is clear: **GPT-5.4 is a viable main brain with the right harness tuning.** It's cheaper, faster, and less verbose than Opus — but feels "dead" or "passive" out of the box without 3-5 specific prompt/config tweaks. The gap isn't in raw capability, it's in initiative and personality. That's fixable.

**Key insight from the Meta-Harness paper (Stanford/MIT, arXiv:2603.28052):** The same model with different harnesses shows up to **6x performance variation** (27% vs 76%). Harness engineering > model selection. A well-tuned GPT-5.4 can outperform a lazily-configured Opus.

---

## Known GPT-5.4 Strengths (vs Opus)
- **Coding/execution**: Excellent, especially Codex variant. Tool use is strong.
- **Speed**: Noticeably faster response times
- **Cost**: 50%+ cheaper than Opus API; 5x larger context window
- **Verbosity**: Less wordy by default — "just gets shit done, no asking questions"
- **Math/strategy/debugging**: Wins ~7/12 benchmark categories

## Known GPT-5.4 Weaknesses (vs Opus)
- **Initiative/proactivity**: The big one. Opus tries alternative paths when blocked; GPT waits to be told.
- **Personality/conversational feel**: Feels "mechanical" or "caveman" without SOUL.md tuning
- **Complex orchestration**: Weaker at multi-step reasoning chains without explicit thinking budget
- **"Fake execution" bug**: GPT sometimes says it did something without actually doing it — needs explicit "verify actions" rules

---

## Critical Config Fixes (Do Before Switching)

### 1. Disable OpenAI Personality Overlay
Our current setting is `friendly` — this is a known cause of "caveman mode" (terse, fragmented responses) when it clashes with SOUL.md.

```bash
# Check current
openclaw config get plugins.entries.openai.config.personality
# → "friendly" (our current)

# Fix: turn it off so SOUL.md controls personality
openclaw config set plugins.entries.openai.config.personality off
```

Source: Vincent Koc (OpenClaw maintainer) — direct fix recommendation.

### 2. Enable Reasoning/Thinking
GPT-5.4 without thinking enabled feels passive. Community reports "very good results" with higher thinking levels.

```bash
# In openclaw.json or via config
# Set thinking to high/xhigh for complex tasks
# Default "off" or "fast" makes it feel shallow
```

For our setup: Enable thinking for main agent, keep it off for sub-agents (cost control).

### 3. SOUL.md Anti-GPT Rules
GPT needs **explicit** instructions that Opus infers. Add to SOUL.md:

```markdown
## GPT-Specific Guardrails
- **Verify every action.** Don't say you did something — actually do it, then confirm.
- **Try alternatives when blocked.** If approach A fails, try B and C before asking.
- **Read .learnings/ before any task.** Check corrections.md and ERRORS.md first.
- **No hedging.** Have opinions. Don't say "it depends" without then picking one.
- **Be proactive.** If you see something that needs doing, mention it. Don't wait to be asked.
```

### 4. Strengthen the Learnings Loop
We already have `.learnings/` with 28 lines — good foundation. Community pattern:

- **Two-strike rule**: Same mistake twice → auto-promote to AGENTS.md as permanent rule
- **Pre-task scan**: Agent reads .learnings/ before every non-trivial task
- **Weekly prune**: Promote recurring patterns, archive resolved ones

### 5. AGENTS.md Under 300 Lines
Community tip: Keep AGENTS.md lean. Ours is currently comprehensive — worth auditing for GPT where every token in system prompt costs more attention.

---

## Migration Checklist

### Pre-Switch
- [ ] Backup workspace (git commit + push)
- [ ] Set OpenAI personality to `off`
- [ ] Add GPT-specific guardrails to SOUL.md
- [ ] Add "read .learnings/ first" rule to AGENTS.md
- [ ] Enable thinking/reasoning in config
- [ ] Review AGENTS.md for bloat (target <300 lines)

### The Switch
- [ ] Change `agents.defaults.model` to `openai/gpt-5.4`
- [ ] Ensure OpenAI API key is configured
- [ ] Restart gateway: `openclaw gateway restart`
- [ ] Start new session: `/new`

### Post-Switch Validation
- [ ] Test: Complex multi-step task (e.g., "research X, write doc, commit")
- [ ] Test: Personality/voice (does it sound like us or generic ChatGPT?)
- [ ] Test: Tool use (browser, exec, file ops)
- [ ] Test: Memory read/write cycle
- [ ] Test: Proactivity (does it notice things without being asked?)
- [ ] Test: Error recovery (give it a task that will partially fail)
- [ ] Compare: Run identical task on both models, evaluate side-by-side

### Ongoing Tuning (Week 1-2)
- [ ] Monitor .learnings/ growth — promote patterns after 2 strikes
- [ ] Adjust thinking level based on quality observations
- [ ] Iterate SOUL.md weekly based on voice drift
- [ ] Consider hybrid: Opus API for orchestration-only, GPT for execution (if budget allows)

---

## Hybrid Option (If Pure GPT Falls Short)

Some community members recommend keeping Opus as orchestrator with GPT sub-agents:

```yaml
agents:
  defaults:
    model: anthropic/claude-opus-4.6  # Orchestrator (reasoning)
  subagents:
    coder: openai/gpt-5.4-codex      # Execution
    general: openai/gpt-5.4           # General tasks
```

**For us**: This defeats the cost-saving purpose. We should try pure GPT first and only fall back to hybrid if quality is genuinely unacceptable after 1-2 weeks of tuning.

---

## The Meta-Harness Insight (What Actually Matters)

From Stanford/MIT's Meta-Harness paper:
- Same model, different harness = **6x performance gap**
- Claude Haiku 4.5 jumped **+7.7 accuracy points** and **4x fewer tokens** with better harness
- Raw execution traces > LLM summaries (15+ point median loss from signal compression)

**What this means for us**: The quality gap between Opus and GPT-5.4 is smaller than the gap between a good harness and a bad one. Our investment should be in:
1. SOUL.md / AGENTS.md precision
2. .learnings/ feedback loop
3. Conditional context routing (don't load everything every time)
4. Explicit completion criteria for tasks
5. Edit-time linting / progress files for long tasks

---

## Community Quotes (Vibe Check)

> "GPT-5.4 got better. We moved on." — OpenClaw release notes

> "GPT 5.4 in Hermes feels like Opus in OpenClaw" — suggesting harness > model

> "Day and night better for execution/cost vs pre-ban, but feels like a sidegrade in personality until tuned"

> "Completely different animal with Senior Engineer SOUL.md — kills verbosity, just ships"

> "Forcing brain on xhigh thinking... very good results"

> "3-5 prompt lines turns GPT passive → Opus-like proactivity"

---

## Sources
- Meta-Harness paper: arXiv:2603.28052 (Stanford/MIT)
- Vincent Koc (OpenClaw maintainer): personality config fix
- Vox migration writeup (Claude → GPT-5.4)
- Multiple community migration reports (March-April 2026)
- ClawChief architecture patterns (Ryan Carson)
- Self-Improving Agent pattern (ClawHub, 318k installs)
