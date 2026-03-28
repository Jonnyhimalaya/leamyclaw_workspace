# Artifacts Protocol

## What Are Artifacts?
Structured deliverables that agents produce as proof of work. Every significant task should leave a trail — not just a chat message.

## Artifact Types

### 📸 Screenshots (before/after)
- **When:** Any visual change to the website (page edits, membership adds, form changes, landing page updates)
- **How:** Take a browser screenshot BEFORE the change, do the work, take AFTER screenshot
- **Format:** PNG, named descriptively

### 📋 Reports
- **When:** Analytics reviews, scout scans, marketing audits, weekly summaries
- **How:** Write findings as a markdown file, not just chat text
- **Format:** Markdown with headers, metrics, and recommendations

### 📝 Task Plans
- **When:** Complex or risky tasks (bulk operations, ad campaign changes, anything Tier 2+)
- **How:** Write a short plan BEFORE starting: what will change, how many items, rollback plan
- **Format:** Markdown, brief (under 200 words)

## File Structure

```
/home/jonny/.openclaw/workspace/artifacts/
  YYYY-MM-DD/
    {agent}-{task-slug}.md                    (plan + completion summary)
    {agent}-{task-slug}-before.png            (pre-change screenshot)
    {agent}-{task-slug}-after.png             (post-change screenshot)
```

### Naming Convention
- Agent prefix: `wrench-`, `prism-`, `radar-`, `pixel-`, `main-`
- Task slug: short kebab-case description (`membership-add-7980`, `weekly-report-w14`, `morning-scan`)
- Keep it human-readable

### Examples
```
2026-03-28/
  wrench-membership-add-7980.md
  wrench-membership-add-7980-before.png
  wrench-membership-add-7980-after.png
  prism-weekly-report-w13.md
  radar-morning-scan.md
  pixel-instagram-easter-post.md
```

## Artifact Markdown Template

```markdown
# {Task Title}
**Agent:** {name} | **Date:** {YYYY-MM-DD HH:MM UTC} | **Status:** {planned|completed|failed}

## Plan
- What: {brief description}
- Scope: {how many items / what pages / what changes}
- Risk: {low|medium|high}

## Result
- {What was done}
- {How many items affected}
- {Any issues encountered}

## Screenshots
- Before: `{filename}-before.png`
- After: `{filename}-after.png`
```

## Rules
1. **Artifacts are saved to disk, never loaded into agent context** — no bloat
2. **Screenshots are mandatory for visual site changes** — no exceptions
3. **Reports replace ephemeral chat dumps** — if it's worth analysing, it's worth saving
4. **Task plans required for Tier 2+ changes** — anything that modifies customer-facing content
5. **The orchestrator decides what needs an artifact** — agents don't artifact every trivial action
6. **Date folders are created on demand** — don't pre-create empty ones

## ⚠️ Anti-Microtasking Rule (CRITICAL)

**One artifact per job, not per step.**

A job is the whole task as delegated: "add 23 students to plan #7980" = ONE artifact with ONE before screenshot, ONE after screenshot, ONE summary.

**NOT** 23 individual artifacts. **NOT** a screenshot after each student. **NOT** a plan for each row.

**The test:** If you're about to create a second artifact for the same delegation, stop. You're microtasking. Combine into one.

**Examples:**
- ✅ `wrench-membership-add-7980.md` — covers all 23 students, one before/after pair
- ❌ `wrench-membership-add-7980-student-1.md`, `wrench-membership-add-7980-student-2.md` ...
- ✅ `prism-weekly-report-w14.md` — one report covering all metrics
- ❌ `prism-ga4-sessions.md`, `prism-ga4-conversions.md`, `prism-ga4-traffic.md` ...
- ✅ `radar-morning-scan.md` — one scan report
- ❌ `radar-twitter-check.md`, `radar-github-check.md`, `radar-docs-check.md` ...

**Bulk operations:** Screenshot the starting state, do ALL the work, screenshot the end state. The summary lists everything that happened in between.
