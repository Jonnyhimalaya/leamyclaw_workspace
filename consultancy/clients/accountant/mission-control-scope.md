# Dano Mission Control — v1 Scope Document

**Purpose:** Single-pane-of-glass web dashboard for Dano's revenue recognition operation. Complements Ledger (the Telegram bot) by providing durable visual state — things that are easier to see than to ask about.

**Audience:** Dano only (single user). Occasional sharing with audit/review (EY, Dano's manager).

**Host:** Dano's Linode (172.237.126.222), dedicated port (proposed 3334), Tailscale-only access for v1.

**Status:** Scoping document for sign-off. Nothing built yet.

---

## Design principles

1. **Audit-grade.** Every number shown must be traceable to a source file + timestamp. This may be shown to EY. No "vibes" data.
2. **Calm, not loud.** This is finance, not marketing. Numbers + small sparklines beat big charts. No animations.
3. **Read-only to start.** Actions stay in Ledger (Telegram). MC shows state, Ledger changes it. Clear separation.
4. **Month-cycle native.** The UI should make Dano's period-close rhythm obvious — where are we in the month, what's pending, what's done.
5. **Ship small.** V1 = 3 sections, ship next session, iterate. Not 10 sections, ship in 3 weeks.

---

## Proposed sections (ranked by value)

### 🔴 TIER 1 — ESSENTIAL (v1, first ship)

#### 1. Period-Close Status Board
**The one panel Dano would actually check.** Pinned at top.

Shows:
- **Current period**: "Apr 26 close" with countdown to month-end
- **Inputs checklist** (per division):
  - NetSuite AR Aging export — received ✅ / awaited ⏳ / stale ⚠️
  - Prior ECL Calc reference — locked ✅
  - Power BI "126 KPMG" report — received ✅ / awaited ⏳
  - KPMG rate table — current version + date
- **Latest ECL run**: date, division, total, movement, flag count (clickable → detail)
- **Button-less status** — displays what Ledger has done; Dano acts via Telegram

**Data source:** `outbox/ecl/` file listings + `memory/period-close-YYYY-MM.md` + file-watch on `inbox/`

#### 2. ECL Trend (12 months)
Historical context — answers "are we getting better or worse?"

Shows:
- **Table**: 12 rows × (month, total ECL $, movement $, Bucket G %, active invoice count, excluded amount)
- **Tiny sparkline** next to total ECL column
- **Division filter** (Analytics / Markets / Corporates / All)
- **Click a row** → summary view of that period's breakdown

**Data source:** Parse all `outbox/ecl/*.xlsx` Reconciliation sheets (they already carry the audit trail)

#### 3. Flags & Exclusions
The audit-attention panel.

Shows:
- **Dealogic LLC exclusions** (current period): row count + outstanding $ + "deliberate policy — confirmed Dano 2026-04-20"
- **Credit memo anomalies**: count + examples (EY challenged these, needs visibility)
- **Recent flags** from Ledger runs (unknown transaction types, future-dated invoices, >3× customer movement)
- **EY query log** (manually maintained for now): question | raised-date | status | answered-by | evidence-link

**Data source:** Flags sheet from latest workbook + dedicated `vault/ey-queries/` directory

### 🟡 TIER 2 — VALUABLE (v1.5, iterate after Dano uses Tier 1)

#### 4. Contract Review Queue (IFRS 15)
When sales lands a new contract, Dano pastes it in → Ledger runs five-step review → status tracked here.

- Contract list: customer, date received, status (pending / in-review / flagged / cleared)
- Per-contract card: five-step summary, obligations, recognition pattern, any flags, Dano's sign-off

#### 5. Ledger Activity Log
- Runs this week/month
- Questions asked + distilled answers
- Every file processed with SHA256 + timestamp (audit evidence)
- Learnings added this week (from corrections.md / LEARNINGS.md)

### 🟢 TIER 3 — NICE-TO-HAVE (maybe never)

#### 6. Reference Quick-Access
- IFRS 15 five-step rendered nicely
- KPMG rate table with version history
- ECL methodology v1.0 doc
- Search box over vault/

*Skip reason: Dano can ask Ledger the same questions on Telegram, faster.*

#### 7. Board Reporting Export
- One-click export of period summary as PDF/Excel for board decks
- Include ECL trend chart, movement drivers, key numbers

*Revisit if Dano says "I present this to the board monthly."*

---

## Questions for Dano (this is where his insight matters)

Please ask him:

**Big picture:**
1. If you only checked this dashboard once a week, **what would you want to see at a glance**? (One answer — the single most important thing.)
2. What do you currently do in Excel that's painful and could live here instead?
3. Do you ever share your ECL workbook with anyone (manager, auditor, finance director)? If so, what do they look at first?

**Period-close cadence:**
4. When does your close actually start? Is it the day NetSuite export is available, or earlier?
5. What are the hard deadlines — group reporting, submission to board, audit sign-off?
6. What inputs land late and cause stress? (Is Power BI always late? Is NetSuite sometimes incomplete?)

**Audit specifics:**
7. Does EY have specific recurring questions or a standard query list, or is it ad-hoc?
8. How often does EY ask about specific invoices / customers / adjustments — weekly, monthly, quarterly?
9. Is there a "EY has asked about these 5 things, haven't answered yet" list you maintain anywhere?

**ECL specifics:**
10. Do you track the Dealogic LLC exclusion anywhere visible, or just in your head? Would explicit tracking help explain it when challenged?
11. What's the single metric you watch most closely month to month? (Total ECL? Movement? Bucket G? Specific customer?)
12. When ECL movement is big, what do you look at first to understand why?

**Contract reviews (Phase 2):**
13. How often do new contracts hit your desk for IFRS 15 review? Weekly? Quarterly?
14. Is there a template/checklist you already use, or is each one bespoke?
15. Who else sees your review output — internal sales, legal, finance director?

**Practical:**
16. Windows laptop — Chrome? Edge? Both fine?
17. Do you ever want to look at the dashboard on your phone, or is this desktop-only?
18. Is Tailscale access OK (small client installed, sign in once), or should we use a login page at a public URL?

---

## Wireframe (text)

```
╔═════════════════════════════════════════════════════════════════╗
║  Dano's Mission Control                    [Settings] [Ledger→] ║
╠═════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  ┌─ PERIOD-CLOSE STATUS ────────────────────────────────────┐  ║
║  │ Apr 26 close — 10 days to month-end                     │  ║
║  │                                                          │  ║
║  │ INPUTS:     ANALYTICS   MARKETS    CORPORATES           │  ║
║  │  NetSuite    ⏳ await   ⏳ await   — (rate TBD)         │  ║
║  │  Prior ECL   ✅ Mar-26  ✅ Mar-26  —                    │  ║
║  │  Power BI    ⏳ await   ⏳ await   —                    │  ║
║  │  Rate table  ✅ v2026-04 ✅ v2026-04 ⚠️ missing        │  ║
║  │                                                          │  ║
║  │ LAST RUN:                                                │  ║
║  │  Mar-26 close · Analytics · 6,832 rows · $12.88M ECL     │  ║
║  │  Movement −$1.34M · 0 flags · Apr 20 21:08 UTC          │  ║
║  └──────────────────────────────────────────────────────────┘  ║
║                                                                 ║
║  ┌─ ECL TREND (Analytics) ──────────────────┐                  ║
║  │ Month   Total     Move     Bucket G%     │                  ║
║  │ Mar-26  $12.88M  −$1.34M    85%   ▂▄▅▇  │                  ║
║  │ Feb-26  $14.22M  +$0.xxM    xx%   ▂▄▅   │                  ║
║  │ Jan-26  $xx.xxM   …         xx%   ▂▄    │                  ║
║  │ …                                         │                  ║
║  └──────────────────────────────────────────┘                  ║
║                                                                 ║
║  ┌─ FLAGS & EXCLUSIONS ───────────────────────────────────────┐ ║
║  │ Dealogic LLC exclusions (policy):                         │ ║
║  │   511 rows · $7.0M outstanding · confirmed by you 20 Apr │ ║
║  │                                                            │ ║
║  │ Credit memo anomalies (EY attention):                      │ ║
║  │   xxx rows this period                                     │ ║
║  │                                                            │ ║
║  │ Recent Ledger flags: (none this period)                    │ ║
║  │                                                            │ ║
║  │ EY open queries: 0                                         │ ║
║  └────────────────────────────────────────────────────────────┘ ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## Build plan (post sign-off)

**Session 1 (estimated 2-3 hours):**
- Next.js skeleton on port 3334
- systemd service for the web app
- Nginx reverse proxy or Tailscale-only binding
- Period-Close Status Board (read from outbox/ + memory/)
- Basic styling, mobile-responsive

**Session 2:**
- ECL Trend panel (parse all Reconciliation sheets)
- Flags & Exclusions panel

**Session 3:**
- Polish, Dano's first-use feedback
- Phase 2 decision

**Stopping rule:** Don't add a section until Dano explicitly asks for it. Resist the temptation to pre-build beyond what he uses.
