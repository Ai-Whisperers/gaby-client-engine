#!/usr/bin/env python3
"""
validate_pack.py — schema check for gaby-outreach-pack.csv.

Fails with exit 1 if any required column is missing or row count is < 1.
Run from CI or manually before commit.
"""
import csv
import sys
from pathlib import Path

REQUIRED_COLS = [
    "business_name","category","subcategory","city","address",
    "phone","whatsapp_url","distance_km","google_rating","google_reviews",
    "has_website","play","priority_score","outreach_template",
]
ALLOWED_PLAY = {
    "DIRECT_DENTAL","ATM_BRUXISMO","ESTETICA_DENTAL","MOMS","B2B_GYM_CORP",
    "EXPAT_HOTEL","ADJACENT_REFER",
}
MIN_ROWS = 100

def fail(msg):
    print(f"VALIDATION FAILED: {msg}", file=sys.stderr)
    sys.exit(1)

def main():
    target = Path(__file__).parent.parent / "02-outreach-pack" / "gaby-outreach-pack.csv"
    if not target.exists():
        fail(f"missing {target}")

    with open(target, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    if not rows:
        fail("0 rows")
    if len(rows) < MIN_ROWS:
        fail(f"{len(rows)} rows (< {MIN_ROWS})")

    cols = rows[0].keys()
    missing = [c for c in REQUIRED_COLS if c not in cols]
    if missing:
        fail(f"missing required columns: {missing}")

    bad_plays = []
    bad_priority = []
    for i, r in enumerate(rows):
        plays = [p for p in r["play"].split(",") if p]
        for p in plays:
            if p not in ALLOWED_PLAY:
                bad_plays.append((i, p))
        try:
            ps = int(r["priority_score"])
            if not 0 <= ps <= 15:
                bad_priority.append((i, ps))
        except ValueError:
            bad_priority.append((i, r["priority_score"]))
    
    if bad_plays:
        fail(f"unknown play values: {bad_plays[:5]}")
    if bad_priority:
        fail(f"invalid priority_score: {bad_priority[:5]}")

    print(f"✓ schema ok, {len(rows)} rows")

if __name__ == "__main__":
    main()
