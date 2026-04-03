# Playbook: Raw/Derived Vault Pattern
**Source:** Andrej Karpathy, April 2 2026 (30K likes)
**Post:** https://x.com/karpathy/status/2039805659525644595

---

## The Pattern

Separate **authoritative source material** from **LLM-compiled knowledge**. Never mix them.

```
vault/
├── raw/          ← Untouched source material. Sacred. Agent never edits.
│   ├── emails/       (client emails, briefs, requirements)
│   ├── exports/      (CSV, JSON, API dumps, bookmark exports)
│   ├── screenshots/  (UI captures, competitor pages)
│   ├── transcripts/  (meeting notes, call recordings)
│   └── docs/         (PDFs, contracts, brand guidelines)
│
├── wiki/         ← LLM-compiled, interlinked, regenerable from raw/
│   ├── topics/       (consolidated knowledge by theme)
│   ├── decisions/    (key decisions with rationale)
│   ├── lessons/      (what broke, how we fixed it)
│   └── people/       (contacts, accounts, identities)
│
└── outputs/      ← Deliverables derived from wiki/
    ├── playbooks/    (reusable client playbooks)
    ├── reports/      (generated reports, audits)
    └── plans/        (action plans, implementation specs)
```

## Why It Matters

- **Raw is the single source of truth.** If wiki gets stale or contradictory, regenerate from raw.
- **Wiki is disposable.** It's a derived artifact. Delete and rebuild if needed.
- **Backlinks from wiki → raw.** Every wiki entry cites its source: `Source: raw/emails/kate-brief-2026-04-03.md`
- **Agent maintains wiki, human curates raw.** Clear ownership boundary.

## The Linting Step

Periodically (add to autoDream or a weekly cron), the agent scans wiki/ for:
- Contradictions between entries
- Stale information (dates > 30 days with no update)
- Missing connections (topics that should cross-reference but don't)
- Orphaned entries (wiki pages with no raw source)

## When to Use

- **New client onboarding:** Start with raw/ (their emails, docs, exports). Build wiki/ from it.
- **Research projects:** Raw bookmarks/articles → compiled research wiki → action plans
- **Kilmurry build:** Kate's email = raw. Our implementation spec = wiki. Deliverables = outputs.

## When NOT to Use

- Don't retroactively restructure an existing working vault (e.g., our current Leamy workspace)
- Small projects that fit in a single file don't need this separation
- If the raw source IS the deliverable (e.g., a config file), skip the indirection

## Karpathy's Key Quotes

- "I maintain and carefully curate all the data in raw/, which is authoritative, and the derived wiki is kept separate and maintains backlinks to original content."
- "Every question to a frontier LLM spawns a team of LLMs to iteratively construct an entire ephemeral wiki, lint it, loop... then write a full report."
- "Room for an incredible new product instead of a hacky collection of scripts."

---

*Apply this to every new client workspace from day one.*
