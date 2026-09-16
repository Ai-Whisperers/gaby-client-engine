# Provenance — where every dataset came from

Last updated: 2026-09-16

## Data sources

| File | Source repo | Auth | Date scraped | Rows |
|---|---|---|---|---:|
| `02-outreach-pack/gaby-outreach-pack.csv` | `Ai-Whisperers/paragu-ai-leads` (private) | BWS PAT `GITHUB_PAT_AIW_DEPLOY_2026_09_10` | 2026-04 / 2026-08 | 1,090 |
| `02-outreach-pack/gaby-direct-dental.csv` | Same | Same | Same | 6 |
| Strategy cross-refs | `Ai-Whisperers/dentist` (public) | None | 2026-07 | – |
| Live site data | https://ometzdental.com | curl | 2026-09-16 | – |

## Source scripts used

These were *not run again* to produce this repo. They were run inside `Ai-Whisperers/paragu-ai-leads/scripts/` against the Google Places API.

- `scrape_nationwide.py` — main nationwide scrape
- `scrape_beauty_v2.py` — beauty vertical iteration
- `scrape_beauty_final.py` — beauty-vertical polish pass
- `scrape_beauty_expanded.py` — expanded keyword set
- `merge_nationwide.py` — merge per-city files into one
- `deep_analysis.py` — analysis engine
- `src/api_client.py` — Google Places API client (ToS-compliant)
- `src/scraper.py` — generic HTTP scraper (⚠️ potentially Maps-prohibited; not used)
- `src/analyzer.py` — scoring formula

## API billing

The Google Places API has a $200/month free credit (~28,000 place lookups free). Re-running the nationwide scrape for dental would cost ~$5–15 in credit (NOT cash; just consuming the free credit).

Required to refresh:

| Variable | Where to get it | Stored in BWS as |
|---|---|---|
| `GOOGLE_PLACES_API_KEY` | GCP Console → APIs & Services → Credentials | `GOOGLE_PLACES_API_KEY` (search BWS) |

## GitHub PAT for accessing private repos

`Ai-Whisperers/paragu-ai-leads` is **private**. To refresh the data you need a GitHub PAT with `repo` scope.

- Used here: `GITHUB_PAT_AIW_DEPLOY_2026_09_10` from BWS
- This token MUST be loaded into `GITHUB_TOKEN` env var before running the refresh script (see `05-scripts/build_outreach_pack.py`)

## Ometz Dental SSOT

Single source of truth for contact info:

- File: `Ai-Whisperers/dentist/config/variables-central.md`
- Local mirror of values used in this repo's outreach CSV: the WA number `+595 987 126 790` (Tigo chip activated 27 jul 2026). The live ometzdental.com site still uses `595981146759` which is wrong — see `01-playbook/COMPLETE-PLAYBOOK.md` Week 1 Action #1.
