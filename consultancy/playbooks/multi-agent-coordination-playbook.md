# Multi-Agent Coordination Playbook
**Version:** 1.0 — 2026-04-02
**Status:** Proven (POC deployed on Leamy Maths server)
**Pattern:** Sequential filesystem handoff

---

## The Pattern

Two or more agents with different models run sequentially. Each agent writes output to a shared drop folder. The next agent reads the previous output and builds on it.

```
Agent A (Model X) → writes to shared/drop.md
    ↓ (time delay)
Agent B (Model Y) → reads shared/drop.md → produces final output → delivers
```

### Why This Works
- **Model specialisation:** Each agent uses the best model for its task (e.g., Grok for X/Twitter search, Sonnet for synthesis)
- **Cost optimisation:** Cheap models handle cheap tasks, expensive models handle complex ones
- **Fault isolation:** If Agent A fails, Agent B still runs with whatever data is available
- **No API complexity:** Filesystem is the coordination layer — no message queues, no webhooks
- **Auditable:** Every intermediate artifact is a file you can inspect

### Architecture Diagram
```
┌─────────────────┐     filesystem      ┌─────────────────┐     telegram
│  Scout (Grok)   │ ──── write ────→    │  Main (Sonnet)  │ ──── deliver ────→ Human
│  x_search only  │   intel-drops/      │  web + merge    │   final report
│  5:50am daily   │   x-scan.md        │  6:00am daily   │
└─────────────────┘                     └─────────────────┘
```

---

## Implementation Details

### 1. Shared Drop Folder
```bash
# Create shared folder accessible to all agents
mkdir -p /path/to/workspace/intel-drops

# If agents have separate workspaces, symlink:
ln -sf /shared/workspace/intel-drops /agent-workspace/intel-drops
```

### 2. Cron Scheduling
- Agent A runs at T-10 minutes (gives it time to complete)
- Agent B runs at T (reads A's output, does its own work, merges)
- Timeout on Agent A should be < the gap between A and B

### 3. Handoff File Format
Use markdown with clear structure so Agent B can parse reliably:
```markdown
# [Scan Type] — YYYY-MM-DD
## Findings
### [Finding Title]
- **What:** Description
- **Why it matters:** Relevance
- **Source:** URL
```

### 4. Graceful Degradation
Agent B's prompt must handle missing/empty handoff files:
> "If the handoff file is missing or empty, note it and proceed with your own findings only."

---

## POC Results (Leamy Maths, 2026-04-02)

| Phase | Agent | Model | Duration | Task |
|-------|-------|-------|----------|------|
| 1 | Scout/Radar | xai/grok-3-mini | 40s | X/Twitter search via x_search |
| 2 | Orchestrator | claude-sonnet-4-6 | 118s | Web search + merge + deliver |
| **Total** | | | **~3 min** | Full intel sweep |

**Key metrics:**
- Scout cost: ~$0.003 per run
- Main cost: ~$0.05 per run (Sonnet, with tool calls)
- Total daily cost: ~$0.053 — significantly cheaper than running everything on Opus (~$0.15)

---

## Variations

### A. Fan-Out (Parallel → Merge)
Multiple agents run simultaneously, each covering different sources. A final agent merges all outputs.
```
Agent A (Grok)  → intel-drops/twitter.md  ─┐
Agent B (Grok)  → intel-drops/reddit.md   ─┼─→ Agent C (Sonnet) → final report
Agent C (GPT)   → intel-drops/news.md     ─┘
```
**Caveat:** Requires careful timing. All fan-out agents must complete before the merge agent runs.

### B. Pipeline (Sequential Enrichment)
Each agent enriches the previous agent's output:
```
Agent A → raw data → Agent B → analysis → Agent C → recommendations → deliver
```

### C. Review Loop (Draft → Critique → Revise)
```
Agent A (creative) → draft.md → Agent B (critical) → review.md → Agent A reads review → final.md
```
**Caveat:** Requires 3 cron slots. More complex but produces higher quality output.

---

## Kilmurry Lodge — Proposed Multi-Agent Workflows

### 1. Morning Briefing Pipeline
**Problem:** Jack needs a daily briefing covering multiple data sources.
**Pattern:** Sequential (same as our intel sweep)

```
6:00am → Scout (Grok): Scan TripAdvisor, Google Reviews, Booking.com for new reviews
         → writes: intel-drops/reviews-overnight.md

6:10am → Main (Sonnet): Read reviews + check weather + check local events + occupancy data
         → Merge into daily briefing
         → Deliver to Jack's Telegram
```

**Agent A (Scout/Grok):** Web scraping for new reviews — fast, cheap, perfect for structured extraction.
**Agent B (Main/Sonnet):** Synthesis — combines reviews with weather, events, occupancy into an actionable morning brief.

**Value:** Jack walks in at 7am knowing: any bad reviews to address, today's weather (affects walk-in traffic), local events (UL matches, conferences), occupancy status.

### 2. Review Response Pipeline
**Problem:** Hotel reviews need timely, personalised responses.
**Pattern:** Draft → Review (two agents)

```
Trigger: New review detected (via morning scan or webhook)

Agent A (Sonnet): Draft a response considering:
  - Review sentiment and specific complaints/praise
  - Hotel's voice and brand guidelines
  - Previous responses (don't repeat)
  → writes: drafts/review-response-{id}.md

Agent B (Opus — only for negative reviews): Quality check:
  - Tone appropriate? Addresses all concerns?
  - Any legal/liability issues?
  - Suggests edits if needed
  → writes: drafts/review-response-{id}-reviewed.md
  → Delivers to Jack for approval before posting
```

**Cost optimisation:** Opus only runs for negative reviews (the high-stakes ones). Positive review responses go straight to Jack with just Sonnet.

### 3. Competitive Intel Sweep
**Problem:** Kilmurry needs to know what nearby competitors are doing.
**Pattern:** Fan-out → Merge

```
Weekly (Sunday 6am):

Scout A (Grok): Scan competitor hotel prices on Booking.com for next 30 days
  → intel-drops/competitor-prices.md

Scout B (Grok): Scan competitor Google/TripAdvisor reviews from past week
  → intel-drops/competitor-reviews.md

Main (Sonnet): Merge both + add analysis:
  - Price comparison (are we above/below market?)
  - Sentiment comparison (are competitors improving/declining?)
  - Recommendations (adjust pricing? address common complaints?)
  → Deliver weekly competitive report to Jack
```

### 4. Event-Driven Occupancy Alerts
**Problem:** When occupancy drops below threshold, proactive marketing should kick in.
**Pattern:** Monitor → Alert → Action

```
Daily 9am:

Agent A (Grok): Check occupancy for next 14 days (from PMS data or manual input)
  → writes: intel-drops/occupancy-forecast.md

Agent B (Sonnet): If any dates < 60% occupancy:
  - Draft social media post highlighting availability
  - Suggest rate adjustment
  - Draft email to corporate accounts
  → Deliver recommendations to Jack
  → If approved, Content agent posts to social
```

### 5. Maintenance & Housekeeping Coordination
**Problem:** Recurring tasks need tracking without expensive hotel management software.
**Pattern:** Sequential enrichment

```
Daily 7am:

Agent A (Grok): Read today's checkout list + maintenance log
  → writes: intel-drops/daily-ops.md

Agent B (Sonnet): Generate:
  - Housekeeping priority list (checkouts first, then stayovers)
  - Maintenance tasks due today
  - Any guest special requests from booking notes
  → Deliver to operations Telegram group
```

---

## Implementation Checklist (For Any Client)

- [ ] Identify workflows with multiple data sources or stages
- [ ] Map each stage to the cheapest capable model
- [ ] Create shared drop folder with symlinks to all agent workspaces
- [ ] Set up cron schedule with appropriate gaps between stages
- [ ] Ensure graceful degradation (each agent handles missing inputs)
- [ ] Test full pipeline end-to-end before deploying
- [ ] Monitor first week for timing issues (Agent A taking longer than expected)
- [ ] Document the pipeline in client's architecture schematic

---

## Lessons Learned

1. **10-minute gap between agents is generous.** Our Scout completes in 40s. A 5-minute gap would work, but 10 gives buffer for API slowness.
2. **Filesystem handoff > API coordination.** Simple, debuggable, no extra infrastructure.
3. **`--no-deliver` on intermediate agents.** Only the final agent delivers to the human.
4. **Symlinks solve the workspace isolation problem.** Agents keep separate workspaces for security, shared folder for coordination.
5. **Graceful degradation is non-negotiable.** If Scout fails, Main should still produce a useful (if incomplete) report.
6. **The LiveSessionModelSwitchError bug (pre-2026.3.28) blocked this pattern entirely.** Verify the client's OpenClaw version supports multi-model agents before proposing this architecture.
