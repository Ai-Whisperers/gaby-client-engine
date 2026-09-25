# gaby-client-engine — Index

> **The complete operational playbook for Ometz Dental (Dra. Gabriella González Pane).**
> Operational counterpart to the strategy repo [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist).

## Where to start

- **First time?** Read `README.md` (entry point + 5-action plan)
- **Want the master playbook?** Open `01-playbook/COMPLETE-PLAYBOOK.md`
- **Want every idea we know about?** Read the idea catalog trilogy in `docs/` (v1 → v2 → v3)
- **Want the outreach data?** Open `02-outreach-pack/gaby-outreach-pack.csv`
- **Want WhatsApp scripts?** Open `03-messages/gaby-outreach-messages.md`

## File-by-file index

### Top-level

| File | What it does |
|---|---|
| `README.md` | Entry point. 5-action plan for Week 1. |
| `INDEX.md` (this file) | Navigation index. |
| `.gitignore` | Excludes `__pycache__/` and per-quarter trackers. |

### `01-playbook/` — strategic playbooks

| File | What | Lines |
|---|---|---:|
| `COMPLETE-PLAYBOOK.md` | 15 prioritized growth plays + 4-week execution calendar | 367 |
| `ANALYSIS.md` | Opportunity matrix per play (7 plays × 30 metrics) | 75 |
| `LESSONS-FROM-DENTISTS-WORLDWIDE.md` | 8 case studies from real dentists worldwide (Dr. Mike, Zack Chug, Pearl AI, Mill Creek, Picasso Dental, etc.) | 220 |

### `02-outreach-pack/` — the prospect list

| File | What | Size |
|---|---|---|
| `gaby-outreach-pack.csv` | **1,090 businesses** near Mburucuyá, pre-scored for outreach | 215 KB |
| `gaby-direct-dental.csv` | 6 dental peers in 30 km catchment | 2 KB |
| `SCHEMA.md` | Column definitions + priority-score formula | 90 |

### `03-messages/` — WhatsApp templates

| File | What |
|---|---|
| `gaby-outreach-messages.md` | 6 WhatsApp templates mapped to 6 outreach plays |

### `04-data-sources/` — provenance + reproducibility

| File | What |
|---|---|
| `PROVENANCE.md` | Where every dataset came from (BWS PAT, GitHub source URLs) |
| `METHODOLOGY.md` | Scoring + classification rules used to build the outreach pack |
| `REGENERATION-INSTRUCTIONS.md` | Quarterly refresh procedure (script + steps) |

### `05-scripts/` — automation

| Script | Purpose |
|---|---|
| `build_outreach_pack.py` | Regenerate the 1,090-row CSV from raw Places API export (~6 KB) |
| `validate_pack.py` | Schema validator (run by CI on every push) |

### `06-tracking/` — outreach ops

| File | What |
|---|---|
| `README.md` | How to use the tracker (workflow + cadence) |
| `outreach-tracker-template.csv` | Empty CRM-lite template (one row per business contacted) |

### `07-legacy-reactivation/` — the historical patient base (added 2026-09-24)

Gaby's old-practice notebooks unified with the 2026 system into a 501-patient master DB → 403 prioritized reactivation opportunities + 189 social-profile candidates. Start with `07-legacy-reactivation/README.md`.

| File | What |
|---|---|
| `README.md` | The full story, numbers, and the 4-step play |
| `pacientes_maestro.csv` | 501 unified patients — single source of truth |
| `reactivacion_prioridad.csv` | 403 opportunities, P1/P2/P3 with phones + message hooks |
| `agenda_consolidada_2026.csv` | April+May 2026, paper+digital unified (309 rows) |
| `pctes_2026_clean.csv` | Cleaned 2026 digital system export (601 appointments) |
| `cuaderno_transcripcion.md` | Page-by-page notebook transcription (clinical continuity) |
| `social/revisar_gaby.csv` | 201 public-profile candidates — Gaby confirms SI/NO before ANY contact |

### `docs/` — deep reference

| File | What | Lines | Size |
|---|---|---:|---:|
| `CHANGELOG.md` | Repo change history | 70+ | – |
| `SESSION-AUDIT.md` | Gap analysis of what was missing in v1 (led to v2 + v3) | 240 | 14 KB |
| `ALL-IDEAS-FOR-GABY.md` (v1) | 165 ideas, 12 categories (within-repo + dental cases) | 754 | 40 KB |
| `ALL-IDEAS-FOR-GABY-v2-addendum.md` (v2) | 50 ideas from professional services (law/therapy/hospital) | 592 | 36 KB |
| `ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md` (v3) | 60 ideas from new-clinic launches + business models + 2026 channel benchmarks | 534 | 36 KB |
| `INDEX.md` (this file) | Navigation | 100 | ~6 KB |

**Catalog total:** ~275 distinct ideas across the three `ALL-IDEAS-FOR-GABY*` files.

### `.github/workflows/`

| File | What |
|---|---|
| `validate.yml` | Runs `05-scripts/validate_pack.py` on every push. Fails PR if schema breaks. |

## How to navigate the 3 idea catalogs

The catalogs are designed to be read in order — each builds on the previous:

```
docs/ALL-IDEAS-FOR-GABY.md                            ← v1: within-repo + dental case studies
        ↓ builds on
docs/ALL-IDEAS-FOR-GABY-v2-addendum.md                ← v2: professional services (law/therapy/hospital)
        ↓ builds on
docs/ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md   ← v3: new-clinic launches + business models + 2026 benchmarks
```

If you only read one file, read v3 (the most actionable for Gaby's specific business-model gaps).

## Reading time

| File | Audience | Reading time |
|---|---|---|
| `README.md` | Gaby, Kiki, Iván, any new viewer | 5 min |
| `01-playbook/COMPLETE-PLAYBOOK.md` | Gaby (deciding what to do this week) | 15 min |
| `02-outreach-pack/SCHEMA.md` | Kiki (using the CSV) | 5 min |
| `03-messages/gaby-outreach-messages.md` | Kiki (sending the messages) | 10 min |
| `docs/ALL-IDEAS-FOR-GABY.md` (v1) | Strategic reference (skim) | 30 min |
| `docs/ALL-IDEAS-FOR-GABY-v2-addendum.md` (v2) | Strategic reference (skim) | 25 min |
| `docs/ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md` (v3) | Strategic reference (skim) | 25 min |

## Status as of 2026-09-16

```
✓ All work committed
✓ Pushed to origin/main
✓ CI validation passes (schema ok, 1090 rows)
✓ Branch in sync with remote
✓ Working tree clean
✓ 20 files, ~440 KB
✓ Catalog: ~275 ideas across 3 docs
```

## Linked projects

- [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) (public, 400+ files) — strategic encyclopedia
- [`Ai-Whisperers/paragu-ai-leads`](https://github.com/Ai-Whisperers/paragu-ai-leads) (private, 6,796 businesses) — source dataset
- Live: https://ometzdental.com (live site; references repo through `contact` + `pricing` JSON)
