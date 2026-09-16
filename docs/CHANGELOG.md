# Changelog

All notable changes to this repo are documented here.

## 2026-09-16 — Initial commit

**What was created:**
- Repo skeleton with 9 numbered folders + scripts + GitHub Action
- `01-playbook/COMPLETE-PLAYBOOK.md` — 15 prioritized plays + 4-week calendar (the master plan)
- `01-playbook/ANALYSIS.md` — opportunity matrix per play
- `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` — 8 new ideas from real-world case studies
- `02-outreach-pack/gaby-outreach-pack.csv` — **1,090 pre-scored businesses** within 15 km of Mburucuyá
- `02-outreach-pack/gaby-direct-dental.csv` — 6 dental peers in 30 km catchment
- `02-outreach-pack/SCHEMA.md` — column definitions + scoring formula
- `03-messages/gaby-outreach-messages.md` — 6 WhatsApp templates by outreach_play
- `04-data-sources/PROVENANCE.md` — where every dataset came from
- `04-data-sources/METHODOLOGY.md` — scoring formula + classification rules
- `04-data-sources/REGENERATION-INSTRUCTIONS.md` — how to refresh the data
- `05-scripts/build_outreach_pack.py` — regenerate the CSV from raw Places API export
- `05-scripts/validate_pack.py` — schema validator
- `06-tracking/outreach-tracker-template.csv` — empty CRM-lite
- `06-tracking/README.md` — tracker usage instructions
- `.github/workflows/validate.yml` — CI schema validation

**Source data:**
- 6,796 businesses from `Ai-Whisperers/paragu-ai-leads` (private, BWS-authed)
- Strategy cross-references from `Ai-Whisperers/dentist` (public)
- Live-site state from `https://ometzdental.com` (curl 2026-09-16)

**Auth:** Used `GITHUB_PAT_AIW_DEPLOY_2026_09_10` from BWS to clone private repo + create the local repo. Final push to GitHub done via [workflow described in this repo's README].

## Maintenance cadence

- **Quarterly** (recommended): re-scrape and refresh `02-outreach-pack/` if running paid outreach. See `04-data-sources/REGENERATION-INSTRUCTIONS.md`.
- **Per outreach push (10+ messages)**: copy `06-tracking/outreach-tracker-template.csv` to a quarter-specific file.
- **Weekly** (after start of outreach): review reply rate and adjust templates.
