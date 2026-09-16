---
# gaby-client-engine

> Client-acquisition operations for **Ometz Dental — Dra. Gabriella González Pane** (Asunción, Paraguay).
> Operational counterpart to the strategy repo [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist). Where `dentist` is the encyclopedia, this repo is the **calendar and the spreadsheet**.

**Audience:** Gaby, Kiki (operations), Iván (orchestration), and any AI agent running outreach on behalf of the practice.

## What this repo is

This is the single home for everything executable related to getting patients in the door at Ometz Dental:

1. **The 12-week execution calendar** — what to do this week, who does it, what it costs
2. **The 1,090-row outreach pack** — pre-scored businesses within 15 km of Mburucuyá
3. **WhatsApp message templates** — 6 by play (colleague, moms, ATM, estética, gym, expat-hotel)
4. **The complete playbook** — 15 prioritized growth plays + 8 new-from-case-studies ideas
5. **Tracking template** — CRM-lite for Kiki to log replies / sent / converted
6. **Provenance** — where every dataset, lead, and message came from

## What this repo is NOT

- **Not** the strategy repo. Read [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) for the 400-file strategic encyclopedia. This repo points to specific files there instead of duplicating.
- **Not** a CRM. Use a spreadsheet derived from `02-outreach-pack/gaby-outreach-pack.csv`.
- **Not** legal or compliance advice. MSPBS regulations live in `dentist/05_OPERATIONS/legal-compliance/`.

## Folder layout

```
gaby-client-engine/
├── README.md                          ← you are here
├── 01-playbook/
│   ├── COMPLETE-PLAYBOOK.md          ← the 15 prioritized plays + 4-week calendar
│   ├── ANALYSIS.md                    ← opportunity matrix per play
│   └── LESSONS-FROM-DENTISTS-WORLDWIDE.md  ← 8 new ideas from real-world cases
├── 02-outreach-pack/
│   ├── gaby-outreach-pack.csv         ← 1,090 pre-scored businesses, WhatsApp URLs ready
│   ├── gaby-direct-dental.csv         ← 6 dental peers in catchment (colleague referrals)
│   └── SCHEMA.md                      ← column definitions + scoring formula
├── 03-messages/
│   └── gaby-outreach-messages.md      ← 6 WhatsApp templates by outreach_play
├── 04-data-sources/
│   ├── PROVENANCE.md                  ← where every dataset came from
│   ├── METHODOLOGY.md                 ← scoring formula + classification rules
│   └── REGENERATION-INSTRUCTIONS.md   ← how to refresh the data when stale
├── 05-scripts/
│   ├── build_outreach_pack.py         ← regenerates 02-outreach-pack from raw data
│   └── validate_pack.py               ← CSV schema validator
├── 06-tracking/
│   ├── outreach-tracker-template.csv  ← empty CRM-lite for Kiki
│   └── README.md                      ← how to fill the tracker
├── .github/workflows/
│   └── validate.yml                   ← fails CI on missing required columns
├── docs/
│   └── CHANGELOG.md                   ← update log
└── assets/
    └── gaby-playbook.pdf              ← optional printable version
```

## Quick start (5 minutes)

```bash
# Open the master outreach pack
less 02-outreach-pack/gaby-outreach-pack.csv

# Find your top 10 leads
head -1 02-outreach-pack/gaby-outreach-pack.csv  # header
sort -t, -k12 -nr 02-outreach-pack/gaby-outreach-pack.csv | head -10

# Pick a WhatsApp template per row's outreach_template column
cat 03-messages/gaby-outreach-messages.md

# Track replies
cp 06-tracking/outreach-tracker-template.csv 06-tracking/outreach-tracker-2026-Q4.csv
```

## The 5 things to do this week

Drawn from `01-playbook/COMPLETE-PLAYBOOK.md`:

| # | Action | Owner | Cost |
|---|---|---|---|
| 1 | Fix WA phone number on ometzdental.com (site has `595981146759`, SSOT says `595987126790`) | Web team | 0 |
| 2 | Claim Google Business Profile listing | Kiki | 0 |
| 3 | Get 6 blockers from Gaby (calle, fecha, WA, RUC, MSPBS, community manager) | Gaby | 0 |
| 4 | First 5 colleague coffees (Group A in `dentist/03_LAUNCH/referral-program/01-list-target-colleagues-asuncion.md`) | Gaby | Coffee |
| 5 | Send 10 WhatsApp outreach messages from `02-outreach-pack/gaby-outreach-pack.csv` (top priority_score first) | Kiki | 0 |

## Provenance summary

- **Strategy encyclopedia:** [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) (400+ files, Gaby's own planning)
- **Business dataset:** [`Ai-Whisperers/paragu-ai-leads`](https://github.com/Ai-Whisperers/paragu-ai-leads) (private, 6,796 PY businesses)
- **Live site:** https://ometzdental.com
- **Contact:** +595 987 126 790 (canonical SSOT per `config/variables-central.md`)

See `04-data-sources/PROVENANCE.md` for full audit trail.

## License

Private — Ai-Whisperers + Dra. González Pane use only.
