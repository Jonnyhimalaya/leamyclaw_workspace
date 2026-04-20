# ECL Schema Analysis — ION Analytics Mar-26

**Source:** `ECL_March_2026---216e4ea9-f6bf-40cc-b45e-d9a15814bc75.csv` (exported from the "ECL Calc" tab)
**Rows:** 6,832 invoice / credit-memo lines
**Period end:** 31/03/2026

## Column schema (24 cols)

| # | Column | Notes |
|---|---|---|
| 0 | Subsidiary | Legal entity that issued invoice (14 distinct) |
| 1 | Company Name | Customer |
| 2 | Country Name | Customer country |
| 3 | Transaction Type | Invoice (6,102) / Credit Memo (730) |
| 4 | Invoice Date | `dd/mm/yyyy` |
| 5 | Due Date | `dd/mm/yyyy` |
| 6 | Invoice No | |
| 7 | Memo | NetSuite memo (Salesforce ref etc.) |
| 8 | Invoice Memo | concat(invoice_no, memo) |
| 9 | Age | days since **due** date (period_end − due) — can be negative |
| 10 | Invoice CCY | Currency of invoice |
| 11 | Amount Due (Foreign CCY) | Messy — mix of `"$1,234.56"`, `"£1,234"`, `1234.56`, `"¤"` garbles |
| 12 | Amount Due (Func Currency) | USD? GBP? converted — this is the basis for ECL |
| 13 | Bucket Feb-26 | Prior period bucket |
| 14 | DSO | Days Since Invoice date (period_end − invoice date) — **this drives bucket** |
| 15 | Bucket | Current period bucket (A–G) |
| 16 | Rate | Display-rounded rate (2dp, so misleading) |
| 17 | ECL Amount Mar-26 | **Current period provision €** |
| 18 | ECL Amount Feb-26 | Prior period provision € |
| 19 | ECL Movement | Mar − Feb |
| 20 | Date | Period tag (all rows = "Mar") |
| 21 | Comment | Movement classifier (5 values) |
| 22 | Account Owner | Sales rep / owner |
| 23 | Entity: [IONO2C] Salesforce Account ID | SF ID |

## Aging bucket rules (confirmed from data)

| Bucket | DSO range | **Real Rate** (from ECL/Amt, not display "Rate" column) |
|---|---|---|
| A | 0 – 30 | 0.10% |
| B | 31 – 120 | 0.20% |
| C | 121 – 210 | 1.00% |
| D | 211 – 300 | 0.80% |
| E | 301 – 360 | 3.80% |
| F | 361 – 390 | 2.20% |
| G | 391+ | **83.80%** |

**⚠️ Anomalies to flag to Dano:**
- Bucket D (211–300d) rate (0.80%) < Bucket C (121–210d) rate (1.00%) — rates are NOT monotonic
- Bucket F (361–390d) rate (2.20%) < Bucket E (301–360d) rate (3.80%) — same pattern
- These look like KPMG-derived loss rates from historical cohort data, not simple aging percentages
- Rate table appears to apply **group-wide** (same across all 14 subsidiaries) — no per-division split
- The "Rate" column in sheet is display-rounded to 2dp which MASKS the actual rates (e.g. shows 0.00 for 0.10%, 0.01 for both 1.00% AND 0.80%). **Do not trust the Rate column.**

## Comment (movement classifier) logic

| Comment | Count | Rule (inferred) |
|---|---|---|
| Change in Bucket (A – F) | 2,370 | Bucket changed OR ECL Amount moved within a non-G bucket (includes within-bucket drift) |
| FX Movement | 2,169 | Specifically: row is in Bucket G both periods, non-functional currency |
| Paid/Credited in period | 1,437 | Current bucket is blank (settled/credited this period) |
| New AR in period | 762 | Feb bucket is blank (first appearance) |
| Move to 83.8% Bucket | 94 | Moved TO Bucket G from non-G in current period |

**60% of rows match naive classification rules — the remaining 40% have a more nuanced rule** (e.g. "Change in Bucket" includes within-bucket FX drift when the base currency is functional; "FX Movement" is reserved for Bucket G). **Ask Dano to confirm the exact rules before we codify.**

## Reconciliation

| Metric | Value |
|---|---|
| Outstanding AR total (Func CCY) | € 144,827,778 |
| ECL Mar-26 total | € 12,883,077 |
| ECL Feb-26 total | € 14,219,872 |
| Movement | −€ 1,336,795 |
| Bucket G (83.8% rate) as % of total ECL | ~85% of provision sits in G despite only 33% of row count |

**The Bucket G concentration is the single most important driver of the provision.**

## Amount-column messiness (parser will need to be robust)

Sample values from `Amount Due (Func Currency)` column:
```
"$3,036.53 "
"15192.63"
"�8,113.60"       ← corrupted char (Excel currency symbol)
"$10,560.06 "
"($26,007.93)"    ← parens = negative
"($6,445.25)"
```

Cleaning pipeline: strip currency symbols ($ £ € and garbled bytes), strip commas, convert `(x)` → `-x`, strip whitespace.

## Proposed ECL Calculator Skill Logic

**Input:** NetSuite Master Data export (CSV or XLSX) + prior-period ECL output (for comparison)

**Pipeline:**
1. Ingest + clean amounts (handle currency noise, garbled UTF-8)
2. Compute `DSO = period_end - invoice_date` per row
3. Apply bucket lookup (A–G) from DSO
4. Apply rate lookup (versioned KPMG table from `vault/accounting/kpmg-rates/`)
5. Calculate `ECL Amount = Amount Due (Func CCY) × rate`
6. Compare to prior-period sheet → classify Comment
7. Output: reconciled Excel matching Dano's template, including:
   - Per-invoice lines
   - Summary by subsidiary + bucket
   - Movement analysis with classification
   - Metadata block (source hash, rate version, timestamp, period end, input/output totals reconciliation)

**Expected build time:** 4–6 hours once Dano confirms the flag questions below.

## 🔴 Questions for Dano (need before v1 build)

1. **Rate inversion** — is it correct that Bucket D (0.80%) < Bucket C (1.00%) and Bucket F (2.20%) < Bucket E (3.80%)? Or am I reading the rates wrong?
2. **Comment rule** — distinction between "Change in Bucket (A-F)" and "FX Movement" in rows where the bucket didn't change? Is "FX Movement" reserved for Bucket G or for non-functional-currency invoices specifically?
3. **Amount column cleanup** — are the garbled characters (e.g. `"�8,113.60"`) the original Excel currency symbols that didn't survive CSV export, or genuine data corruption? (They were likely `$`/`£`/`€` originally.)
4. **What was the rate table source?** One group-wide table or per-entity/per-division? I see one global table but the voice note mentioned three divisions.
5. **What's the "Date" column supposed to vary by?** All rows show "Mar" — is this just a period tag, or does it sometimes hold the FX rate reference date?

## Output template specification (from Dano's sample)

- Single tab called **ECL Calc**
- Header row at row 2 with column titles (row 1 is period-end metadata)
- Row 1 header metadata layout: `...,31/03/2026,,," <ECL Mar> "," <ECL Feb> ","<movement> "`
- No subtotals in the body — subtotals are separate pivot sheet in the source
- Currency formatting with thousand separators + parens for negatives
- All numeric values kept at line level, aggregations done via pivot elsewhere
