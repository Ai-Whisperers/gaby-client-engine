---
# gaby-client-engine

> **Client-acquisition operations for Ometz Dental — Dra. Gabriella González Pane** (Mburucuyá / Asunción, Paraguay).
> Operational counterpart to the strategy repo [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist).
> Where `dentist` is the encyclopedia, this repo is **the calendar and the spreadsheet**.

**Audience:** Gaby (the dentist), Kiki (operations), Iván (orchestration), and any AI agent running outreach on behalf of the practice.

---

## What this repo is

Single home for everything executable about getting patients in the door at Ometz Dental:

1. **12-week execution calendar** — what to do this week, who does it, what it costs (`01-playbook/COMPLETE-PLAYBOOK.md`).
2. **1,090-row outreach pack** — pre-scored businesses within ~15 km of Mburucuyá, WhatsApp URLs ready (`02-outreach-pack/`).
3. **6 WhatsApp templates** — one per outreach play: colleague, moms, ATM-bruxismo, estética, gym, expat-hotel (`03-messages/`).
4. **15 prioritized growth plays** + 8 case-study ideas from real dentists worldwide (`01-playbook/`).
5. **CRM-lite tracker** — empty template for Kiki to log replies / sent / converted (`06-tracking/`).
6. **~275-idea catalog** in three evolutive docs (`docs/ALL-IDEAS-FOR-GABY*.md`).
7. **Full provenance** — where every dataset, lead, and message came from (`04-data-sources/`).
8. **Automation** — Python scripts to rebuild the pack and validate schema in CI (`05-scripts/` + `.github/workflows/`).

## What this repo is NOT

- **Not** the strategy repo. Read [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) for the 400-file strategic encyclopedia. This repo points to specific files there instead of duplicating.
- **Not** a CRM. Use a spreadsheet derived from `02-outreach-pack/gaby-outreach-pack.csv`.
- **Not** legal or compliance advice. MSPBS regulations live in `dentist/05_OPERATIONS/legal-compliance/`.

---

## How to navigate (by audience & time budget)

| If you are… | Read this | Time |
|---|---|---|
| **New here (anyone)** | This README → then `01-playbook/COMPLETE-PLAYBOOK.md` | 5 + 15 min |
| **Gabi (the dentist)** | `01-playbook/COMPLETE-PLAYBOOK.md` §"This week" + `02-outreach-pack/gaby-direct-dental.csv` | 15 min |
| **Kiki (operations)** | `02-outreach-pack/SCHEMA.md` → `03-messages/gaby-outreach-messages.md` → `06-tracking/README.md` | 20 min |
| **Iván / an AI agent** | `04-data-sources/PROVENANCE.md` → `04-data-sources/METHODOLOGY.md` → `04-data-sources/REGENERATION-INSTRUCTIONS.md` | 15 min |
| **Want the full idea universe** | `docs/ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md` (most actionable) → v2 → v1 | 75 min |

## Quick start (5 minutes)

```bash
# Open the master outreach pack
less 02-outreach-pack/gaby-outreach-pack.csv

# Find your top 10 leads by priority_score (column 13)
head -1 02-outreach-pack/gaby-outreach-pack.csv
awk -F',' 'NR>1 {print $13","$1}' 02-outreach-pack/gaby-outreach-pack.csv | sort -nr | head -10

# Pick the WhatsApp template per row's outreach_template column (col 14)
cat 03-messages/gaby-outreach-messages.md

# Track replies (copy per quarter)
cp 06-tracking/outreach-tracker-template.csv 06-tracking/outreach-tracker-2026-Q4.csv
```

---

## Folder layout (full)

```
gaby-client-engine/                                21 files · ~440 KB total
├── README.md                                       (this file — entry point)
├── INDEX.md                                        navigation index with line counts
├── .gitignore                                      excludes __pycache__ + per-quarter trackers
├── .github/workflows/
│   └── validate.yml                                runs validate_pack.py on every push
├── 01-playbook/                                    strategy — what to do
│   ├── COMPLETE-PLAYBOOK.md                        15 prioritized plays + 4-week calendar (257 lines)
│   ├── ANALYSIS.md                                 opportunity matrix per play — 7 plays × 30 metrics
│   └── LESSONS-FROM-DENTISTS-WORLDWIDE.md          8 case studies (Dr. Mike, Zack Chug, Pearl AI, Mill Creek, Picasso, …)
├── 02-outreach-pack/                               data — who to contact
│   ├── gaby-outreach-pack.csv                      **1,090 pre-scored businesses** near Mburucuyá (215 KB)
│   ├── gaby-direct-dental.csv                      6 dental peers in catchment (colleague referrals)
│   └── SCHEMA.md                                   column definitions + priority-score formula
├── 03-messages/                                    copy — what to say
│   └── gaby-outreach-messages.md                   6 WhatsApp templates mapped to 6 plays
├── 04-data-sources/                                audit — where it came from
│   ├── PROVENANCE.md                               data source audit trail (BWS PAT, source URLs)
│   ├── METHODOLOGY.md                              scoring + classification rules
│   └── REGENERATION-INSTRUCTIONS.md                quarterly refresh procedure
├── 05-scripts/                                     automation — keep it fresh
│   ├── build_outreach_pack.py                      regenerates 02-outreach-pack from raw data
│   └── validate_pack.py                            schema validator (run by CI)
├── 06-tracking/                                    ops — log what happened
│   ├── README.md                                   tracker workflow + cadence
│   └── outreach-tracker-template.csv               empty CRM-lite template
├── assets/                                         (placeholder for future printable assets)
└── docs/                                           deep reference
    ├── CHANGELOG.md                                repo change history (Keep-a-Changelog 1.1.0)
    ├── SESSION-AUDIT.md                            gap analysis of v1 → drove v2 and v3
    ├── ALL-IDEAS-FOR-GABY.md                       v1: 165 ideas, 12 categories (within-repo + dental cases)
    ├── ALL-IDEAS-FOR-GABY-v2-addendum.md           v2: 50 ideas from professional services (law/therapy/hospital)
    └── ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md   v3: 60 ideas from new-clinic launches + 2026 channel benchmarks
```

**Catalog total:** ~275 distinct ideas across the three `ALL-IDEAS-FOR-GABY*` files. Read in order `v1 → v2 → v3`. If you read only one, read v3.

---

## The 5 things to do this week

Drawn from `01-playbook/COMPLETE-PLAYBOOK.md`:

| # | Action | Owner | Cost |
|---|---|---|---|
| 1 | Fix WA phone number on ometzdental.com (site has `595981146759`, SSOT says `595987126790`) | Web team | ₲0 |
| 2 | Claim Google Business Profile listing | Kiki | ₲0 |
| 3 | Get 6 blockers from Gaby (calle, fecha, WA, RUC, MSPBS, community manager) | Gaby | ₲0 |
| 4 | First 5 colleague coffees (Group A in `dentist/03_LAUNCH/referral-program/01-list-target-colleagues-asuncion.md`) | Gaby | Coffee |
| 5 | Send 10 WhatsApp outreach messages from `02-outreach-pack/gaby-outreach-pack.csv` (top `priority_score` first) | Kiki | ₲0 |

Targets after month 1 (per `06-tracking/README.md`): 100 contacted · 5–10 replies · 2–5 interested · 1 formal referral agreement · first referred patient within 60 days of signed agreement.

## Outreach-pack schema at a glance

The CSV has 14 columns. The two that matter operationally:

- `priority_score` (col 13, 0–30) — sort descending; the top ~10% are the week-1 list.
- `outreach_template` (col 14) — which template to use in `03-messages/gaby-outreach-messages.md`.

Full schema + scoring formula in `02-outreach-pack/SCHEMA.md`; methodology in `04-data-sources/METHODOLOGY.md`.

## Provenance summary

- **Strategy encyclopedia:** [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) (400+ files, Gaby's own planning)
- **Business dataset:** [`Ai-Whisperers/paragu-ai-leads`](https://github.com/Ai-Whisperers/paragu-ai-leads) (private, 6,796 PY businesses)
- **Live site:** https://ometzdental.com
- **Contact:** +595 987 126 790 (canonical SSOT per `dentist/config/variables-central.md`)

See `04-data-sources/PROVENANCE.md` for the full audit trail.

## Related repos

- [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) — public, 400+ file strategic encyclopedia
- [`Ai-Whisperers/paragu-ai-leads`](https://github.com/Ai-Whisperers/paragu-ai-leads) — private, 6,796 PY businesses (raw outreach source)
- [`IvanWeissVanDerPol/ai-medica-paraguay`](https://github.com/IvanWeissVanDerPol/ai-medica-paraguay) — Paraguay × open-source medical AI (sister research repo)

## Status

```
✓ 21 files committed and pushed to origin/main
✓ CI validation passes (schema ok, 1090 rows)
✓ ~275 ideas cataloged across 3 docs
✓ Working tree clean
```

Last refreshed: see `docs/CHANGELOG.md` (most recent entry: 2026-09-16 — final catalog assembled).

## License

Private — Ai-Whisperers + Dra. González Pane use only.