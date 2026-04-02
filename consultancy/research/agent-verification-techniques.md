# Agent Verification & Accuracy Techniques
**Date:** 2026-04-02
**Status:** Research → Implementation Candidates
**Context:** Claude Code leak revealed 29-30% false claims rate on Claude 4.6. Community developing verification patterns.

---

## The Problem

LLMs hallucinate. Agents acting on hallucinations cause real damage — wrong guest info sent, incorrect prices quoted, bad data in reports. The Claude Code source leak confirmed Anthropic's own internal benchmarks show a **29-30% false claims rate** on Claude 4.6 (up from 16.7% in v4). This isn't getting better automatically — we need architectural solutions.

---

## Community Patterns (from X/Twitter research, April 2026)

### 1. Planner → Worker → Verifier Loop
**Source:** Community best practices, Boris Cherny's workflow
**Pattern:**
```
Planner Agent → breaks task into phases (max 5 files per phase)
    ↓
Worker Agents → execute in parallel (git worktrees for isolation)
    ↓
Verifier Agent → runs tests, type-checks, cross-model review
    ↓ (fail?)
Loop back to Worker with specific fixes
```
**Key insight:** Phase-gating prevents compounding errors. Don't let Phase 2 start until Phase 1 is verified.

### 2. Cross-Model Verification ("Good Cop / Bad Cop")
**Source:** Multiple X posts, growing community pattern
**Pattern:** One model generates, a different model critiques.
```
Claude (creative/generator) → draft output
    ↓
GPT or Grok (skeptical/reviewer) → fact-check, challenge assumptions
    ↓
Final output only if both agree
```
**Why it works:** Different models have different failure modes. Claude might hallucinate a fact that GPT catches, and vice versa. Cross-model review catches errors that same-model review misses.

### 3. Ground Truth vs Hints (Skeptical Memory)
**Source:** KAIROS leak analysis, community CLAUDE.md patterns
**Pattern:** Tag all stored information with confidence levels:
- `[GROUND TRUTH]` — verified, immutable (e.g., "Kilmurry Lodge has 109 rooms")
- `[HINT]` — probably true, verify before using (e.g., "Jack prefers morning briefings at 7am")
- `[UNVERIFIED]` — agent-generated, treat with suspicion

Agent must verify HINT-tagged info against sources before acting on it.

### 4. Learnings File (Self-Improving Accuracy)
**Source:** OpenClaw community soul.md patterns
**Pattern:** Maintain an `AGENT_LEARNINGS.md` that agents read every session:
```markdown
## Mistakes Log
- 2026-04-01: Sent email with wrong checkout date. Root cause: read cached data instead of live PMS.
  → RULE: Always fetch live data for guest-facing communications.
- 2026-03-28: Generated revenue report with double-counted group bookings.
  → RULE: Deduplicate booking IDs before summing revenue.
```
After every error, append the mistake + the rule. Agent reads this before every task. Over time, accuracy improves because the agent has a growing list of "don't do this" rules specific to the deployment.

### 5. Citation-Required Mode
**Source:** Anti-hallucination prompting best practices
**Pattern:** Force agents to cite sources for every factual claim:
```
"Every claim needs [direct quote + file/line or URL]. 
If you cannot cite a source, say 'I don't have enough info' — do not invent."
```
Simple but effective. Reduces hallucination by forcing the model to ground claims in retrievable evidence.

### 6. AgentRepEngine (Slow-Walk Detection)
**Source:** @AgentRepEngine on X
**Pattern:** Detects agents that "pretend to work" — claiming task completion without actually doing anything. Uses behavioral analysis:
- 0% false positives, 86.67% true positives
- 100% slow-walk detection
**Relevance:** Our Advisor cron already does lightweight version of this (reviews daily logs for errors). Could be enhanced.

### 7. UViiVE Verifiable Pipelines
**Source:** Biotech company running OpenClaw fleet for scientific research
**Pattern:** "Verification as a Service" — custom pipeline that:
- Cross-validates agent outputs against known datasets
- Propagates "emergent behaviors" across fleet (verified good patterns spread, bad patterns get flagged)
- Claims to outperform OpenAI, Claude, and Grok on hallucination detection
**Status:** Academic (medRxiv preprint). Interesting concept but not directly usable yet.

---

## Implementation Plan for Our System

### Phase 1: Quick Wins (This Week)

#### A. Citation Mode for Reports
Add to any agent doing research or reporting:
```
VERIFICATION RULE: For every factual claim, include the source (URL, file path, or data point).
If you cannot verify a claim, prefix it with [UNVERIFIED].
Never state something as fact without a source.
```
**Where:** Intel sweep prompts, marketing reports, any client-facing output.
**Cost:** Zero — just prompt engineering.

#### B. Learnings File
Create `AGENT_LEARNINGS.md` in workspace root:
```markdown
# Agent Learnings — Error Log & Rules
Read this file at the start of every task. These are hard-won lessons.

## Rules
1. Always fetch live data for anything guest/user-facing — never use cached/remembered values
2. Verify membership status AFTER creating WooCommerce memberships (wcm-active check)
3. Never assume API responses are complete — check pagination
4. Meta API budgets are in cents — divide by 100 for display

## Mistake Log
(append new entries here)
```
**Where:** Main workspace + each agent workspace.
**Cost:** Zero — file creation + prompt update.

#### C. Advisor Upgrade → Verification Agent
Our existing Advisor cron (every 6h) already reviews daily logs. Upgrade it:
```
ADDITIONAL CHECKS:
- Flag any entry where an agent claims "done" without evidence of verification
- Flag numerical claims that seem implausible (e.g., "0 sessions" when we had ads running)
- Flag any action taken on cached/stale data
- Check if AGENT_LEARNINGS.md was updated after any errors today
```
**Cost:** Minimal — enhanced prompt on existing cron.

### Phase 2: Cross-Model Verification (Next Sprint)

#### D. Review Pipeline for Client-Facing Outputs
For anything that goes to a client (Kilmurry reports, marketing analyses):
```
Agent A (Sonnet) → generates report → writes to drafts/
    ↓
Agent B (Grok or GPT) → reads report + original data → flags:
  - Unsupported claims
  - Mathematical errors  
  - Tone/appropriateness issues
  - Missing context
    ↓
If flags found → Agent A revises
If clean → deliver to client
```
**Implementation:** Same filesystem handoff pattern as intel sweep.
**Cost:** ~2x per report (two model calls). Worth it for client-facing work.

#### E. Ground Truth Registry
Create `GROUND_TRUTH.md` per client:
```markdown
# Kilmurry Lodge — Verified Facts
Last verified: 2026-04-02

## Property
- Rooms: 109
- Location: Castletroy, Limerick (near UL)
- Type: Family-run business hotel
- GM: Jack

## Operations  
- Check-in: 3pm, Check-out: 11am
- Restaurant capacity: 120
- Conference rooms: 3 (names: ...)

## Pricing
- [Updated weekly from PMS data]
```
Agents MUST cross-reference this file for any guest/client-facing claims. If a fact isn't in Ground Truth, it must be flagged as unverified.

### Phase 3: Automated Verification Loop (Month 2)

#### F. Post-Action Verification Cron
After any agent takes an action (sends email, updates website, creates membership), a verification agent checks:
```
1. Did the action actually happen? (check the system, don't trust the log)
2. Is the result correct? (spot-check values)
3. Were there side effects? (anything unexpected change?)
```
**Example for Leamy:** After adding a WooCommerce membership:
- Verify user exists ✓
- Verify membership plan is correct ✓  
- Verify status is wcm-active (not draft/pending) ✓
- Verify the user can actually access the content ✓

#### G. Confidence Scoring
Add to agent output format:
```
## Finding
[CONFIDENCE: HIGH] Revenue increased 12% MoM (source: GA4 report, verified)
[CONFIDENCE: MEDIUM] Competitor dropped rates by €15 (source: single Booking.com check)
[CONFIDENCE: LOW] Guest satisfaction improved (source: 2 recent reviews, small sample)
```
Allows the human to quickly assess which findings to trust.

---

## Kilmurry-Specific Applications

| Workflow | Verification Technique | Why |
|----------|----------------------|-----|
| Morning briefing | Citation mode + ground truth | Guest-facing info must be accurate |
| Review responses | Cross-model review (Sonnet drafts, Grok reviews) | Reputation risk from bad responses |
| Pricing recommendations | Ground truth registry + confidence scoring | Financial impact |
| Competitive intel | Citation required + cross-model verification | Decisions based on competitor data |
| Maintenance reports | Post-action verification | Safety/liability concerns |

---

## Tools to Evaluate

| Tool | What It Does | Priority |
|------|-------------|----------|
| AgentRepEngine | Detects agents pretending to work | Medium — our Advisor covers basics |
| opik-openclaw | Observability for agent pipelines | High — would help debug verification failures |
| BOTCHA | Reasoning stress test for agents | Low — more relevant for public-facing agents |
| UViiVE pipeline | Verifiable scientific outputs | Watch — academic, not ready for production |

---

## Key Principle

> **Verification cost should scale with stakes.**
> 
> - Internal notes → no verification needed
> - Team reports → citation mode
> - Client-facing outputs → cross-model review
> - Financial/legal actions → full verification loop + human approval
> 
> Don't spend $0.10 verifying a $0.01 decision.
