# Regeneration Instructions

When the dataset becomes stale (every quarter, or before a major outreach push), follow this procedure.

## Step 1 — Check data freshness

```bash
# From /tmp/probe/leads/data/processed/
ls -la paraguay_priority_a.csv paraguay_priority_b.csv
# If older than 90 days, regenerate
```

## Step 2 — Re-scrape via Google Places API (optional, dental-centric)

The original `paragu-ai-leads` repo was filtered to beauty/wellness. For dental leads you need a separate run:

```bash
# Approximate — adapt based on current google-places scraper signature
python3 scripts/scrape_nationwide.py \
  --keyword "dental clinic" \
  --center "-25.314,-57.610" \
  --radius_km 15 \
  --output /tmp/dental_raw.csv
```

Cost: ~$5–15 in Places API credit (against the $200/mo free tier). Time: 2–4 hours for full Asunción metro.

## Step 3 — Re-classify and re-score

Run `05-scripts/build_outreach_pack.py` which:

1. Reads the raw CSV
2. Classifies each row into plays (same keyword logic as `04-data-sources/METHODOLOGY.md`)
3. Computes priority scores (same formula)
4. Generates `whatsapp_url` per row
5. Writes `02-outreach-pack/gaby-outreach-pack.csv`

```bash
python3 05-scripts/build_outreach_pack.py \
  --input /tmp/dental_raw.csv \
  --output 02-outreach-pack/gaby-outreach-pack.csv \
  --combine-with /tmp/beauty_raw.csv  # include the beauty for adjacent plays
```

## Step 4 — Schema validation

```bash
python3 05-scripts/validate_pack.py
# Should print "✓ schema ok, 1090 rows"
```

CI runs this automatically on every push (`.github/workflows/validate.yml`).

## Step 5 — Commit and push

```bash
git add 02-outreach-pack/gaby-outreach-pack.csv
git commit -m "refresh: outreach pack from Q4 2026 re-scrape"
git push origin main
```

## When NOT to refresh

- **Phones, addresses, reviews change slowly.** Quarterly is fine for the existing CSV.
- **If you're doing a one-off outreach to the top 50** in the current CSV, no need to regenerate first. Use what you have.
- **If you only want to test the methodology** on new data, use a small (50-row) sample first to avoid accidentally spamming the wrong catchment.
