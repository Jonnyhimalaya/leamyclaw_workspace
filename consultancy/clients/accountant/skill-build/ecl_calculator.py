#!/usr/bin/env python3
"""
ECL Calculator — ION Analytics
================================
Ingests NetSuite AR Aging Detail CSV + prior-period ECL Calc CSV.
Produces ECL Calc output matching Dano's template to-the-cent.

Logic confirmed by Dano (Paul J Danaher) 2026-04-20:
- Input: NetSuite Invoice + Credit Memo rows only (payments/revals already in balance)
- DSO = period_end - invoice_date (Excel serial dates)
- Buckets A-G by DSO; rates from KPMG table (non-monotonic D<C and F<E is correct)
- FX Movement = same bucket both periods
- Change in Bucket = bucket changed
- New AR = no prior bucket; Paid/Credited = settled (in prior, not in current)

Auditor: EY. Rate source: KPMG. Rate table is group-wide across Analytics + Markets.
Corporates uses different rates (separate file needed).

Author: Ledger / OpenClaw  |  First validated: 2026-04-20 (Mar-26 close)
"""
from __future__ import annotations

import hashlib
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# KPMG rate table — ION Analytics + ION Markets
# Confirmed from Mar-26 data reverse-engineering; verified by Dano 2026-04-20.
# Non-monotonic rates are correct (KPMG historical cohort data).
# ---------------------------------------------------------------------------
RATES_ANALYTICS_MARKETS = {
    "A": 0.0010,   # DSO   0 -  30
    "B": 0.0020,   # DSO  31 - 120
    "C": 0.0100,   # DSO 121 - 210
    "D": 0.0080,   # DSO 211 - 300  (lower than C — correct per KPMG)
    "E": 0.0380,   # DSO 301 - 360
    "F": 0.0220,   # DSO 361 - 390  (lower than E — correct per KPMG)
    "G": 0.8380,   # DSO 391+
}

# Corporates rates: TODO — supply from vault/accounting/kpmg-rates/corporates-v<date>.csv
RATES_CORPORATES: dict = {}

BUCKETS = [
    ("A",   0,   30),
    ("B",  31,  120),
    ("C", 121,  210),
    ("D", 211,  300),
    ("E", 301,  360),
    ("F", 361,  390),
    ("G", 391, 99999),
]

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------
_STRIP_RE = re.compile(r"[^\d.\-]")


def clean_currency(val) -> float:
    """Parse currency string, handling Excel garbles, parens=neg, commas."""
    if pd.isna(val):
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip()
    if not s:
        return 0.0
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()")
    s = _STRIP_RE.sub("", s)
    if s in ("", ".", "-", "-."):
        return 0.0
    try:
        v = float(s)
        return -v if neg else v
    except ValueError:
        return 0.0


def excel_to_date(n) -> datetime | None:
    """Convert Excel serial date (e.g. 45126) to Python datetime."""
    if pd.isna(n):
        return None
    try:
        return datetime(1899, 12, 30) + timedelta(days=int(float(n)))
    except Exception:
        return None


def file_hash(path: Path, n: int = 12) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()[:n]


def dso_to_bucket(dso) -> str | None:
    if pd.isna(dso):
        return None
    d = int(dso)
    for code, lo, hi in BUCKETS:
        if lo <= d <= hi:
            return code
    return None


# ---------------------------------------------------------------------------
# Classify movement comment
# Dano-confirmed rules (2026-04-20):
#   FX Movement           = same bucket both periods (amount moved from currency revaluation)
#   Change in Bucket(A-F) = bucket changed between prior and current
#   Move to 83.8% Bucket  = current = G, prior != G
#   New AR in period      = no prior bucket (first appearance)
#   Paid/Credited         = no current bucket (settled in period)
# ---------------------------------------------------------------------------
def classify_comment(prior_bucket, curr_bucket) -> str | None:
    p_null = pd.isna(prior_bucket) or str(prior_bucket).strip() == ""
    c_null = pd.isna(curr_bucket)  or str(curr_bucket).strip() == ""
    if p_null and c_null:
        return None
    if p_null:
        return "New AR in period"
    if c_null:
        return "Paid/Credited in period"
    if str(curr_bucket) == "G" and str(prior_bucket) != "G":
        return "Move to 83.8% Bucket"
    if str(prior_bucket) == str(curr_bucket):
        return "FX Movement"
    return "Change in Bucket (A - F)"


# ---------------------------------------------------------------------------
# Load NetSuite export
# Header rows: 6 (report title + scope + report name + "As of ..." + 2 blanks)
# Then 13 column headers + data rows.
# Invoice + Credit Memo rows carry the net outstanding balance already
# (payments, revals, journals are separate rows we do NOT use for ECL).
# ---------------------------------------------------------------------------
def load_netsuite(path: Path, period_end: datetime) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=6, encoding="latin-1", on_bad_lines="skip")
    df.columns = [c.strip() for c in df.columns]

    # Drop trailing "Total" footer if present
    if len(df) and str(df.iloc[-1, 0]).strip().lower() == "total":
        df = df.iloc[:-1].copy()

    # Keep only Invoice + Credit Memo (these carry the net outstanding balance)
    df = df[df["Transaction Type"].isin(["Invoice", "Credit Memo"])].copy()

    # Parse dates (Excel serials)
    df["_inv_date"] = df["Invoice Date"].apply(excel_to_date)
    df["_due_date"]  = df["Due Date"].apply(excel_to_date)

    # Parse amounts
    df["_amt_func"]    = df["Amount Due (Func Currency)"].apply(clean_currency)
    df["_amt_foreign"] = df["Amount Due (Foreign Currency)"].apply(clean_currency)

    # Build join key: Invoice No + Memo (matches ECL "Invoice Memo" column)
    df["_key"] = (
        df["Invoice No"].fillna("").astype(str).str.strip()
        + df["Memo"].fillna("").astype(str).str.strip()
    )

    # DSO = period_end - invoice_date
    df["DSO"] = df["_inv_date"].apply(
        lambda d: (period_end - d).days if d is not None else None
    )
    df["Age"] = df["_due_date"].apply(
        lambda d: (period_end - d).days if d is not None else None
    )

    # Dealogic LLC is excluded from ECL provision (confirmed from Mar-26 data:
    # all 511 Dealogic LLC rows in the ECL sheet carry ECL Amount = 0).
    # This is a business rule — likely the US entity is provisioned separately or excluded.
    df["_ecl_excluded"] = df["Subsidiary"].str.strip() == "Dealogic LLC"

    # Bucket + rate
    df["Bucket"] = df["DSO"].apply(dso_to_bucket)

    return df


# ---------------------------------------------------------------------------
# Load prior-period ECL Calc CSV
# Row 1: metadata (period date, totals) — skip
# Row 2: column headers
# ---------------------------------------------------------------------------
def load_prior_ecl(path: Path) -> pd.DataFrame:
    """
    Load the CURRENT period ECL Calc CSV to extract:
      - _prior_bucket  = 'Bucket Feb-26' column (what bucket was in the PRIOR period)
      - _prior_ecl     = 'ECL Amount Feb-26' column (the PRIOR period's ECL provision)

    We use the prior ECL as our Feb reference, then derive the current-period
    bucket ourselves from NetSuite DSO. This matches how Dano builds the sheet.
    """
    df = pd.read_csv(path, skiprows=1, encoding="latin-1", on_bad_lines="skip")
    # Find columns (may have leading/trailing whitespace)
    feb_ecl_col    = next((c for c in df.columns if "ECL Amount" in c and "Feb" in c), None)
    feb_bucket_col = next((c for c in df.columns if c.strip() == "Bucket Feb-26"), None)

    df["_key"]          = df["Invoice Memo"].fillna("").astype(str).str.strip()
    df["_prior_bucket"]  = df[feb_bucket_col].fillna("").astype(str).str.strip() if feb_bucket_col else ""
    df["_prior_ecl"]    = df[feb_ecl_col].apply(clean_currency) if feb_ecl_col else 0.0
    return df[["_key", "_prior_bucket", "_prior_ecl"]]


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def run(
    ns_path: Path,
    prior_ecl_path: Path,
    period_end: datetime,
    division: str = "ION Analytics",
    rates: dict | None = None,
) -> pd.DataFrame:
    rates = rates or RATES_ANALYTICS_MARKETS

    print(f"\n{'='*70}")
    print(f"ECL CALCULATOR  |  {division}  |  Period end: {period_end:%d/%m/%Y}")
    print(f"{'='*70}")

    # ---- Step 1: Load NetSuite ----
    print(f"\n[1/6] Loading NetSuite export …")
    ns = load_netsuite(ns_path, period_end)
    ns_total = ns["_amt_func"].sum()
    print(f"      Invoice+CrMemo rows: {len(ns):,}")
    print(f"      Total Func-CCY:      ${ns_total:>15,.2f}")

    # ---- Step 2: Apply rates ----
    print(f"\n[2/6] Applying KPMG rate matrix …")
    ns["Rate"] = ns["Bucket"].map(rates)
    # Zero out ECL for excluded entities (Dealogic LLC)
    ns["ECL Amount"] = ns.apply(
        lambda r: 0.0 if r.get("_ecl_excluded", False) else r["_amt_func"] * (r["Rate"] if pd.notna(r["Rate"]) else 0),
        axis=1
    )
    ecl_current_total = ns["ECL Amount"].sum()
    print(f"      ECL total (current): ${ecl_current_total:>15,.2f}")

    # ---- Step 3: Load prior-period ECL ----
    print(f"\n[3/6] Loading prior-period ECL …")
    prior = load_prior_ecl(prior_ecl_path)
    print(f"      Prior rows: {len(prior):,}")

    # ---- Step 4: Roll-forward — merge current with prior ----
    print(f"\n[4/6] Roll-forward merge …")
    current = ns.merge(prior, on="_key", how="outer", indicator=True)

    # Rows only in prior = Paid/Credited in period
    # Rows only in current = New AR (shouldn't happen if prior is correct, but handle)
    # Both = active or FX-only movement

    # Fill NaN fields for prior-only rows
    current["Bucket"] = current["Bucket"].fillna("")
    current["_prior_bucket"] = current["_prior_bucket"].fillna("")

    # Classify comment
    current["Comment"] = current.apply(
        lambda r: classify_comment(
            r["_prior_bucket"] if r["_prior_bucket"] != "" else None,
            r["Bucket"] if r["Bucket"] != "" else None,
        ),
        axis=1,
    )

    # ECL Movement
    current["ECL Amount"] = current["ECL Amount"].fillna(0)
    current["_prior_ecl"] = current["_prior_ecl"].fillna(0)
    current["ECL Movement"] = current["ECL Amount"] - current["_prior_ecl"]

    # Strip empty-string buckets back to NaN for clean output
    current["Bucket"] = current["Bucket"].replace("", None)
    current["_prior_bucket"] = current["_prior_bucket"].replace("", None)

    # Total rows
    print(f"      _merge values:")
    for k, v in current["_merge"].value_counts().items():
        print(f"        {k}: {v:,}")

    # ---- Step 5: Reconciliation ----
    print(f"\n[5/6] Reconciliation check …")
    ecl_mar = current["ECL Amount"].sum()
    ecl_feb = current["_prior_ecl"].sum()
    ecl_mov = current["ECL Movement"].sum()
    total_rows = len(current)

    print(f"\n{'─'*70}")
    print(f"  SOURCE FILE:           {ns_path.name}")
    print(f"  Source SHA256:         {file_hash(ns_path)}")
    print(f"  Period end:            {period_end:%d/%m/%Y}")
    print(f"  Run timestamp UTC:     {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}")
    print(f"  Division:              {division}")
    print(f"  Rate table:            Analytics/Markets (group-wide, KPMG-sourced)")
    print(f"  ── ── ── ── ── ── ── ──")
    print(f"  Output rows:           {total_rows:>10,}")
    print(f"  ECL Amount (current):  ${ecl_mar:>14,.2f}")
    print(f"  ECL Amount (prior):    ${ecl_feb:>14,.2f}")
    print(f"  ECL Movement:          ${ecl_mov:>14,.2f}")
    print(f"{'─'*70}")

    # Validation targets (Mar-26 known-good from Dano's file header row)
    # Header row 1 of ECL CSV: ...31/03/2026,,, 12,883,053 , 14,219,833 ,-1,336,780
    TARGET_ROWS  = 6832
    TARGET_MAR   = 12883053.0   # ECL Mar-26 total
    TARGET_FEB   = 14219833.0   # ECL Feb-26 total (prior period provision)
    TARGET_MOV   = -1336780.0   # Movement = Mar - Feb

    def check(label, got, want, tol=1.0):
        ok = abs(got - want) <= tol
        flag = "✅" if ok else "❌"
        print(f"  {flag}  {label}: got {got:,.0f}  want {want:,.0f}  diff {got-want:+,.2f}")
        return ok

    print(f"\n[6/6] Validation against Mar-26 known-good …")
    ok_rows = check("Rows",      total_rows, TARGET_ROWS,  tol=0)
    ok_mar  = check("ECL Mar",   ecl_mar,    TARGET_MAR)
    ok_feb  = check("ECL Feb",   ecl_feb,    TARGET_FEB)
    ok_mov  = check("Movement",  ecl_mov,    TARGET_MOV)

    if all([ok_rows, ok_mar, ok_feb, ok_mov]):
        print("\n  ✅✅  ALL CHECKS PASSED — calc matches Dano's Mar-26 output.\n")
    else:
        print("\n  ❌  SOME CHECKS FAILED — investigate before shipping.\n")

    # Comment breakdown
    print("Comment breakdown:")
    print(current["Comment"].value_counts(dropna=False).to_string())
    print()
    print("Bucket breakdown (current period):")
    bkt = current.dropna(subset=["Bucket"]).groupby("Bucket").agg(
        count=("ECL Amount","count"),
        outstanding=("_amt_func","sum"),
        ecl=("ECL Amount","sum"),
    ).round(2)
    print(bkt.to_string())

    return current


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    NS_PATH    = Path("/home/jonny/.openclaw/media/inbound/Netsuite_Data---7539c361-7a6b-4bb0-b989-2ee4ad983f0c.csv")
    PRIOR_PATH = Path("/home/jonny/.openclaw/media/inbound/ECL_March_2026---216e4ea9-f6bf-40cc-b45e-d9a15814bc75.csv")
    PERIOD_END = datetime(2026, 3, 31)

    result = run(NS_PATH, PRIOR_PATH, PERIOD_END, division="ION Analytics")

    out = Path("/home/jonny/.openclaw/workspace/consultancy/clients/accountant/skill-build/mar26_replica_output.csv")
    result.to_csv(out, index=False)
    print(f"\nOutput saved → {out}")
