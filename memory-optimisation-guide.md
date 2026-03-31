# Memory Optimisation for OpenClaw Agents

*A practical guide to making your agent remember what matters without burning your budget.*

---

## The Problem

Out of the box, OpenClaw agents forget everything between sessions. The files in your workspace (`MEMORY.md`, daily logs, `SOUL.md`) are your only continuity — but without discipline, they either stay empty (amnesia) or bloat into massive context blobs that cost a fortune on every turn.

The goal: **remember the right things, in the right places, at the right cost.**

---

## Protocol A: Search-First, Write-Last

Add this to `AGENTS.md` so the agent follows it every session:

> **BEFORE** answering any question about past facts, decisions, or preferences:
> 1. Call `memory_search` — never rely solely on conversation history for past context.
> 2. Only skip the search if the answer is obviously within the current session.
>
> **AFTER** every meaningful exchange:
> 3. Ask: *"Does this need to survive the next session?"* → If yes, write it to the correct file immediately. Don't batch writes until session end.

**Why it works:** Most agents either never search their memory (relying on stale context) or never write to it (relying on conversation history that vanishes). This enforces both directions.

**Cost note:** With QMD backend (installed Mar 27, 2026), `memory_search` runs 100% locally via BM25 — zero API cost. Previously used OpenAI embeddings (text-embedding-3-small) which occasionally broke when credits ran out.

---

## Protocol B: File Routing — Know Where Things Go

The agent needs a clear decision tree for *where* to write. Without this, everything ends up in one file (usually MEMORY.md) and it bloats.

Add this routing table to `AGENTS.md`:

| What it is | Where it goes |
|---|---|
| Raw events, task logs, project notes | `memory/YYYY-MM-DD.md` (daily log) |
| Distilled lessons, persistent facts, key preferences | `MEMORY.md` (curated long-term memory) |
| Operational rules, behavioral instructions | `AGENTS.md` |
| Persona, voice, tone, style | `SOUL.md` |

**The Test:** After writing something, ask: *"If I wake up in a brand-new session tomorrow with only these files, will I still behave correctly / have the right context?"* If the answer is no, rewrite or re-route.

**Key principle:** Daily logs are raw notes. MEMORY.md is curated highlights. If your MEMORY.md reads like a diary, it's wrong — it should read like a cheat sheet.

---

## Protocol C: Write-Protection Header

Add this as line 1 of `MEMORY.md`:

```
# WRITE RULE: NEVER overwrite or replace this entire file. Only append new sections. Preserve everything above. Use edit tool only — never write tool.
```

**Why:** LLMs occasionally use the `write` tool (full file replacement) instead of `edit` (surgical append). One bad write can nuke your entire long-term memory. The header acts as a strong instruction against this.

**Where to apply:** MEMORY.md only. Daily logs are low-risk (append-only by nature). SOUL.md should occasionally be rewritten as you evolve — don't protect it.

---

## Protocol D: Dream Cycle (Nightly Consolidation)

Create a cron job that runs nightly (e.g. 2am) on a cheaper model (Sonnet, GPT-4o — not your main expensive model):

**What it does:**
1. Finds daily log files older than 7 days
2. Reads them and extracts anything worth preserving long-term
3. Appends distilled content to MEMORY.md
4. Moves processed logs to `memory/archive/` (never delete — archive)

**OpenClaw cron setup:**
```bash
openclaw cron add \
  --name "dream-cycle" \
  --cron "0 2 * * *" \
  --tz "Your/Timezone" \
  --agent main \
  --model anthropic/claude-sonnet-4-6 \
  --session isolated \
  --thinking medium \
  --timeout-seconds 300 \
  --message "DREAM CYCLE: Read daily logs older than 7 days in memory/. Extract key decisions, lessons, facts, and milestones. Append distilled content to MEMORY.md. Move processed logs to memory/archive/. Skip heartbeat entries, health checks, and routine logs."
```

**Why isolated session:** The consolidation doesn't need your main session's context (and shouldn't pollute it with housekeeping).

**Why a cheaper model:** Summarisation doesn't need your best model. Save the expensive one for real work.

---

## Token Economy Settings

### Compaction Tuning

In `openclaw.json`, tune these values:

```json
{
  "agents": {
    "defaults": {
      "compaction": {
        "mode": "safeguard",
        "reserveTokensFloor": 20000,
        "memoryFlush": {
          "enabled": true,
          "softThresholdTokens": 4000
        }
      }
    }
  }
}
```

- `reserveTokensFloor: 20000` — keeps 20k tokens of headroom so you don't hit context limits mid-turn
- `memoryFlush.softThresholdTokens: 4000` — triggers memory flush earlier, preventing bloated sessions

### Targeted Retrieval

Instruct the agent (in AGENTS.md):
- Use `memory_search` to find relevant snippets (returns small chunks with line numbers)
- Use `memory_get` to pull only the specific lines needed
- Avoid reading entire files unless genuinely necessary

### Session Hygiene

- Start fresh sessions (`/new`) when switching topics — don't let unrelated history accumulate
- Use multi-agent routing for different domains (e.g. one agent for code, another for analytics) so each carries only relevant context
- Monitor session size — alert at 100+ messages, reset at 200+

---

## Memory Search Backend: QMD (Installed Mar 27, 2026)

**What changed:** Replaced the default SQLite + OpenAI embeddings backend with [QMD](https://github.com/tobi/qmd) (by Tobi Lütke, 17k+ GitHub stars). Officially supported by OpenClaw.

**How it works:**
- BM25 full-text keyword search (current mode: `searchMode: "search"`)
- 100% local — no external API calls, no embedding costs, no outages
- Auto-reindexes every 10 minutes (`update.interval: "10m"`)
- Markdown files remain the single source of truth — QMD only reads/indexes them

**Config** (in `openclaw.json`):
```json
{
  "memory": {
    "backend": "qmd",
    "citations": "auto",
    "qmd": {
      "searchMode": "search",
      "includeDefaultMemory": true,
      "update": { "onBoot": true, "interval": "10m" },
      "limits": { "maxResults": 8, "maxSnippetChars": 700, "timeoutMs": 4000 }
    }
  }
}
```

**Upgrade path:** Switch `searchMode` to `"query"` for full hybrid (BM25 + vector + LLM reranking). Requires ~2GB model download and CPU-only inference on this VPS (no GPU). Only worth doing if BM25 recall proves insufficient.

**Other options investigated (parked):**
- **Lossless-Claw (LCM):** Intra-session memory — prevents context bloat by summarising older branches instead of dropping them. Worth adding if 529 overload errors persist.
- **Mem0:** Auto-extracts facts from conversations into its own vector DB. Overkill for now — manual write discipline is working fine.

---

## Quick Checklist

- [ ] Add Protocol A (Search-First, Write-Last) to AGENTS.md
- [ ] Add Protocol B (routing table) to AGENTS.md  
- [ ] Add write-protection header to MEMORY.md
- [ ] Set up Dream Cycle cron job
- [ ] Tune compaction settings in openclaw.json
- [x] ~~Ensure OpenAI API has credits for embeddings~~ → Replaced with QMD (fully local)
- [ ] Add session size monitoring to HEARTBEAT.md

---

*Built from real-world experience running OpenClaw with Claude Opus. These protocols eliminated context bloat, prevented memory loss across sessions, and cut token costs significantly.*
