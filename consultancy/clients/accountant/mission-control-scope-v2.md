# Dano Mission Control — Scope v2 (post Dano input 2026-04-21)

## What changed from v1

Dano's answers revealed:
- **Audience for the ECL workbook is mgr + EY auditors** — they care about movement + drivers, NOT grand total
- **EY concentrates on professional services contracts** (% completion, fixed fees) — not ECL
- **IFRS 15 SSP compliance gap** — ION recognises on sales price not standalone selling price, technical flaw material for any future IPO
- **SSP data extraction is NOT easy** — NetSuite + bespoke ION system + 1000s of SKUs. Multi-week effort to extract.
- **1000 active PS contracts** tracked in Kimble with monthly cost-to-complete reviews
- **Year-end Dec 2026, audit Jan 2027** — primary deadline pressure
- **Private tool.** Only Dano sees this MC. No-one else in ION has IFRS 15 depth to engage.

## Revised build priority

**Phase 1 (build now):** ECL-focused MC — covers monthly mechanical work + audit defence
**Phase 2 (after SSP data extractable):** SSP Compliance panel — the IPO-readiness audit-defence deliverable
**Phase 3 (stretch):** PS Contract tracker (Kimble integration or CSV-import)

SSP moves to Phase 2 explicitly — Dano confirmed "will take time to get data". Build the delivery vessel (MC) first, plug SSP analyser in when data arrives.

---

## Phase 1 Panels (build plan)

### 🔴 Panel 1 — Period-Close Status Board (top)
Current period state, at a glance.

- Current period: **"Apr-26 close — 9 days to month-end"**
- Inputs per division (Analytics / Markets / Corporates):
  - NetSuite AR Aging export: ✅ received (hash + timestamp) / ⏳ awaited / ⚠️ stale
  - Prior ECL Calc: locked reference
  - Rate table: current version + date
- Last run summary card: date, division, rows, ECL current, movement, flag count
- **No action buttons** — Dano acts via Telegram to Ledger

### 🔴 Panel 2 — Movement Explainer (the real value)
**This is the panel Dano's audience actually looks at.** Not just trend — explanation.

Three sections:
1. **Top 10 customer movers this period** — name, bucket prev→curr, $ movement, one-line "why" (classifier)
2. **Driver breakdown** — total movement decomposed by comment classifier:
   - $X from FX movement (currency revaluation)
   - $Y from bucket changes (aging pressure)
   - $Z from new AR in period (inflow)
   - $W from paid/credited (outflow)
   - $V from Move to 83.8% bucket (aging tip point)
3. **"Explain to auditors" export** — one-click PDF/email-ready summary with those bullets in auditor-speak

### 🔴 Panel 3 — 12-Month ECL Trend
Historical context + pattern spotting.

- Table: month × total ECL × movement × Bucket G % × active row count × exclusion amount
- Per-row sparkline beside total ECL
- Division filter (All / Analytics / Markets / Corporates)
- Click row → that period's Movement Explainer

### 🔴 Panel 4 — Flags, Exclusions & EY Queue
The audit-attention panel.

- Dealogic LLC exclusions (current + trend): count + $ + "deliberate policy" note
- Credit memo anomalies flag (EY-challenged item)
- Ledger-raised flags from recent runs
- **EY query log** — manually maintained: question | raised | status | answered-by | evidence link
- Tag/filter by topic (PS contracts / SSP / ECL / Other)

### 🟡 Panel 5 — SSP Compliance (Phase 2, scaffolded in v1)
Empty placeholder with clear "awaiting data" state. When Dano extracts SKU + invoice data, this lights up:

- Per-SKU SSP distribution (median, IQR, outliers)
- Compliance verdict per SKU (observable / residual / needs-fresh-evidence)
- Cumulative revenue mis-recognition estimate
- "Defence pack" export for EY

Deferred until Dano extracts data. **Scaffold the placeholder now** so it's visible as a roadmap item.

### 🟢 Panel 6 — PS Contracts Watchlist (Phase 3)
Eventual Kimble/CSV integration. Kimble has the data (timesheets, cost-to-complete, % complete). 1000 active contracts is too many for a scrollable list — filter to those with:
- % complete > 80%
- Recent cost-to-complete revision
- Contract value > threshold

Deferred. Placeholder only.

---

## Ledger skills roadmap (separate from MC panels)

- `ecl-calculator` — ✅ built, validated
- `ifrs15-contract-reviewer` — Phase 1b: bake Dano's bespoke checklist (contract value, performance obligations, heavy-discount flag, PS % completion treatment, SSP allocation status)
- `ssp-analyzer` — Phase 2: depends on data extract
- `ps-completion-tracker` — Phase 3: depends on Kimble export format

---

## Tech stack decisions

- **Next.js 14** (App Router) + Tailwind — same pattern as Jack/Kate's MC
- **SQLite** for the EY query log (only writable table; the rest is read-only file watching)
- **Node file watchers** on `~/.openclaw/workspace/outbox/ecl/*.xlsx` — parse Reconciliation sheet to populate trend data
- **No LLM calls in the dashboard** — it's a view over Ledger's output artefacts
- **Port 3334** on Dano's Linode
- **Tailscale-only access** for v1 (Dano confirmed this is fine, desktop primary)
- **systemd service** for boot persistence
- **Git-backed** workspace (same pattern as Kilmurry)

---

## Build order (session plan)

### Session 1 (this or next): Foundation + Panel 1
- Next.js scaffold on server
- systemd service
- Tailscale binding
- Period-Close Status Board working end-to-end
- Ledger's last run auto-populates

### Session 2: Panels 2 + 3
- Parse Reconciliation sheets from outbox/ecl/
- 12-month trend table with sparklines
- Movement Explainer with top 10 movers + driver breakdown
- Export-to-email-text button

### Session 3: Panel 4 + scaffolds
- Flags/Exclusions from Flags sheet parsing
- EY query log CRUD (SQLite)
- Placeholder panels for SSP + PS Contracts with "awaiting data" messaging
- Polish pass + Dano first-use

---

## Open decisions for Jonny

1. **Build under which repo?** New `Jonnyhimalaya/dano-mission-control` private repo, or co-locate under existing infra? Suggestion: new private repo, matches the per-client pattern you use for Kilmurry (`Jonnyhimalaya/Kilmurry` + `Jonnyhimalaya/kilmurry-kate`).
2. **Tailscale setup.** Dano needs the Tailscale client on his Windows laptop + added to your tailnet. Easy but one-time friction — confirm he's OK with that vs public URL + password.
3. **Auth.** If Tailscale-only, zero auth needed (tailnet is the gate). If public, need a password.
4. **Session scope.** Do you want all three sessions above this week, or space them out?

## Open commitments to Dano

- Log SSP compliance gap as known exposure in his workspace memory
- Flag year-end Dec 2026 / EY audit Jan 2027 as a deadline marker on MC
- When SSP data is extractable, pick up the analyser build immediately
