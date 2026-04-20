# ECL Calculator — Full Pipeline Design
**Status:** Pending confirmation from Dano on 5 open questions (see ecl-schema-analysis.md)

## Inputs (per period close)
1. **NetSuite AR Aging Detail export** (CSV)
   - Report name: `MI PACK RP: A/R Aging Detail (excl ICO - ECL PD)`
   - `As of <period-end>`
   - Rows contain mix of transaction types, **dates as Excel serial numbers**
   - Columns: Subsidiary, Company Name, Country, Transaction Type, Invoice Date, Due Date, Invoice No, Memo, Age, Invoice CCY, Amount Due (Foreign), Amount Due (Func CCY), Salesforce ID
   - Typical size: ~10,000 rows
2. **Prior-period ECL Calc tab** (CSV/XLSX)
   - Used for: Bucket Feb-26, ECL Feb-26, movement classification
3. **Current KPMG rate table** (versioned in `vault/accounting/kpmg-rates/current-v<date>.csv`)

## Transaction Type Handling (from NetSuite)

| Transaction Type | Count (Mar) | Treatment |
|---|---|---|
| Invoice | 4,741 | Core AR line — included in ECL |
| Credit Memo | 654 | Negative AR line — included (reduces provision) |
| Currency Revaluation | 3,770 | **Aggregated into parent invoice** — not separate ECL line |
| Payment | 1,416 | Reduces outstanding — impact already in `Amount Due` |
| Journal | 69 | Adjustments — inspect individually, most settle out |
| Deposit | 1 | Rare adjustment |
| Customer Refund | 1 | Rare adjustment |

**Key rule:** Group by `(Subsidiary, Company Name, Invoice No, Memo)` → sum `Amount Due (Func CCY)`. A row with non-zero net after aggregation becomes an ECL line. Zero-net means invoice was settled in period.

## Pipeline

### Stage 1 — Ingest & normalise NetSuite export
```python
1. Skip first 6 header rows (report title + metadata)
2. Header is row 7 (13 columns)
3. Convert Excel serial dates (e.g. 45126) to real dates
4. Clean currency noise in Amount fields (handle '$', '£', '€', '¤' garbles, parens=neg)
5. Strip whitespace and trailing nulls
6. Drop "Total" footer row if present
```

### Stage 2 — Aggregate to invoice level
```python
1. Group by (Subsidiary, Company Name, Invoice No, Memo)
2. Sum Amount Due (Func CCY) across all related entries
3. Keep first-seen Invoice Date, Due Date, Invoice CCY
4. Drop rows where aggregated amount rounds to 0.00 (fully settled in period)
5. Warn on any "Journal" rows with blank Company Name — escalate to Dano
```

### Stage 3 — Compute DSO and bucket
```python
1. DSO = period_end_date - invoice_date  (in days)
2. Bucket lookup:
     A:   0 - 30
     B:  31 - 120
     C: 121 - 210
     D: 211 - 300
     E: 301 - 360
     F: 361 - 390
     G: 391+
3. Rate lookup from KPMG table → bucket → rate
4. ECL = Amount Due (Func CCY) × rate
```

### Stage 4 — Reconcile with prior period
```python
1. Join to prior-period ECL file on (Subsidiary + Invoice No + Memo)
2. Carry forward: Bucket Feb-26, ECL Amount Feb-26
3. Classify movement (Comment column):
     - New AR in period:     Feb bucket blank, current non-blank
     - Paid/Credited:        current bucket blank, Feb non-blank (invoice must still appear as aging=0)
     - Move to 83.8% Bucket: current = G, Feb != G
     - FX Movement:          (see Q2 for Dano — currently suspected: Bucket G both periods)
     - Change in Bucket:     anything else with non-zero movement
4. Movement = ECL Mar - ECL Feb
```

### Stage 5 — Output Excel matching Dano's template
```
Workbook: ION_A_ECL_<YYYY-MM>_<run-timestamp>.xlsx

Sheet 1: "ECL Calc"
  Row 1: metadata (period end, totals)
  Row 2: headers (24 columns matching Dano's current layout)
  Row 3+: per-invoice data

Sheet 2: "Summary"
  Pivot: Subsidiary × Bucket → count, outstanding €, ECL €
  Subtotals, grand total

Sheet 3: "Movement Analysis"
  Pivot: Comment classifier × Subsidiary → movement €, row count
  Highlights rows where |movement| > threshold for review

Sheet 4: "Reconciliation"
  - Source file SHA256 hash
  - Period end date
  - Rate table version + path
  - Run timestamp (UTC)
  - Input NetSuite row count + total
  - Post-aggregation row count + total
  - Final ECL line count + total
  - Diff vs prior period
  - Any rows flagged for human review

Sheet 5: "Flags"
  All rows requiring human attention:
    - Journals with blank Company Name
    - Amount parser fallbacks (garbled currency codes)
    - New invoices with negative age (future-dated)
    - Movement > 3× threshold per customer
```

## Excel Serial Date Conversion

NetSuite exports dates as numbers (45126 = 2023-07-15). Excel epoch is 1899-12-30.

```python
from datetime import datetime, timedelta
def xl_serial_to_date(n):
    return datetime(1899, 12, 30) + timedelta(days=int(n))
```

## Currency Cleaner (Robust)

```python
import re
def clean_currency(val):
    if pd.isna(val) or val == '':
        return 0.0
    s = str(val).strip()
    # Handle parentheses (negative)
    neg = s.startswith('(') and s.endswith(')')
    s = s.strip('()')
    # Strip any non-numeric except . and -
    s = re.sub(r'[^\d.\-]', '', s)
    if not s or s in ('-','.','-.'):
        return 0.0
    val = float(s)
    return -val if neg else val
```

## Validation Against Dano's Known-Good Output

For Mar-26 close:
- Input NetSuite rows: 10,653
- After aggregation + zero-filter: expect ~5,395 Invoice/Credit Memo rows
- Plus 1,437 "Paid/Credited" rows carried from Feb (rollforward)
- Total ECL Calc rows: 6,832 ✓
- Grand total ECL Mar-26: €12,883,053 ✓
- Grand total ECL Feb-26: €14,219,833 ✓
- Movement: −€1,336,780 ✓

**Acceptance criterion: our calc output must match all four of the above within €1 tolerance.**

## Risks / Unknowns

1. **Credit memo offset logic** — 24% of rows don't reconcile simply (NS sum ≠ ECL amount). The biggest mismatches are Credit Memos. Need Dano to walk through one example.
2. **Rate inversion anomalies** (D<C, F<E) — need Dano to confirm these are genuine KPMG rates.
3. **FX Movement vs Change in Bucket** distinction — 60% of rows have ambiguous classifier.
4. **Rate table scope** — one group-wide table or division-specific? Voice note said 3 divisions; data shows 1 table.
5. **NetSuite export format stability** — if the 6-row header changes, or a new Transaction Type appears, the skill must flag rather than silently drop rows.

## Build Path

1. ✅ Schema analysis complete (this doc + ecl-schema-analysis.md)
2. ⏸️ Pending: Dano confirms 5 open questions
3. 📝 Build `skills/ecl-calculator/main.py` — Stage 1-5 pipeline
4. 📝 Build `skills/ecl-calculator/SKILL.md` — description for agent routing
5. 📝 Build test harness — run against Mar-26 input, diff vs Mar-26 known-good output
6. 📝 Iterate until diff = zero
7. 📝 Deploy to Dano's machine (still open Windows-local vs server architecture)
8. 📝 Run Apr-26 close live; Dano reviews; sign-off
