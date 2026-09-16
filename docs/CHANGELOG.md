# Changelog

All notable changes to `gaby-client-engine` are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [unreleased] — 2026-09-16 — final catalog assembled

### Added — idea catalogs (v1 + v2 + v3)
- **`docs/ALL-IDEAS-FOR-GABY.md`** (v1, 754 lines, 40 KB) — comprehensive 165-idea reference covering 12 categories, sourced from `dentist/` repo + 8 worldwide dental case studies. Includes North Star metric, risk register, 4-week execution map.
- **`docs/ALL-IDEAS-FOR-GABY-v2-addendum.md`** (v2, 592 lines, 36 KB) — 50 additional ideas from professional services outside dental: hospital remote-second-opinion programs (Ohio: 53% conversion), law-firm SEO (Peak Digital: +412% organic traffic in 18 months), therapist private-practice playbooks, B2B broker referral contracts.
- **`docs/ALL-IDEAS-FOR-GABY-v3-businesses-marketing.md`** (v3, 534 lines, 36 KB) — 60 additional ideas from new-clinic launches, membership-plan business models, Disney-trained patient experience, case-acceptance frameworks, 2026 channel-mix benchmarks with hard numbers.

**Total catalog: ~275 distinct ideas across 12+12+10 categories.**

### Added — operational core (initial commit + gap audit)
- `README.md` — entry point + 5-action plan
- `01-playbook/COMPLETE-PLAYBOOK.md` — 15 prioritized plays + 4-week calendar
- `01-playbook/ANALYSIS.md` — opportunity matrix per play
- `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` — 8 worldwide dental case studies
- `02-outreach-pack/gaby-outreach-pack.csv` — **1,090 pre-scored businesses** within 15 km of Mburucuyá
- `02-outreach-pack/gaby-direct-dental.csv` — 6 dental peers in catchment
- `02-outreach-pack/SCHEMA.md` — column definitions + scoring formula
- `03-messages/gaby-outreach-messages.md` — 6 WhatsApp templates by play
- `04-data-sources/METHODOLOGY.md` — scoring + classification rules
- `04-data-sources/PROVENANCE.md` — data source audit trail
- `04-data-sources/REGENERATION-INSTRUCTIONS.md` — quarterly refresh procedure
- `05-scripts/build_outreach_pack.py` — regenerate CSV from raw data
- `05-scripts/validate_pack.py` — schema validator
- `06-tracking/README.md` — tracker instructions
- `06-tracking/outreach-tracker-template.csv` — empty CRM-lite
- `.github/workflows/validate.yml` — CI schema validation
- `docs/SESSION-AUDIT.md` — gap analysis of what was missing in v1 (became v2 and v3)

### Status

| Verification | Result |
|---|---|
| `git status` | clean working tree |
| `git log` | 5 commits on main |
| `origin/main` ↔ `main` | in sync at `1422608e` |
| `python3 05-scripts/validate_pack.py` | ✓ schema ok, 1090 rows |
| Total files | 20 |
| Total size | ~440 KB |
| Total ideas in catalog | ~275 across 3 docs |

## [0.1.0] — 2026-09-16 — initial commit

### Added
- Repo skeleton with 9 numbered folders + scripts + GitHub Action
- Operational core (outreach CSV + scripts + tracking template)
- Initial playbook (15 prioritized plays)
- Initial idea catalog (165 ideas)

## Source repositories referenced

- [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) — Gaby's 400+ file strategy repo (read-only reference)
- [`Ai-Whisperers/paragu-ai-leads`](https://github.com/Ai-Whisperers/paragu-ai-leads) — private; 6,796 PY businesses dataset (outreach-CSV source)

## Auth & access

- GitHub PAT used to populate the repo: `GITHUB_PAT_AIW_DEPLOY_2026_09_10` (BWS-stored)
- For future refreshes, see `04-data-sources/REGENERATION-INSTRUCTIONS.md`

## Maintenance cadence (recommended)

- **Quarterly** (or before each major outreach push): refresh outreach CSV via Places API re-scrape.
- **Weekly** (after Kiki starts tracking replies): review reply rates, adjust templates.
- **Yearly**: full catalog review for idea staleness; consider v4 research into 2027 dental/regional market shifts.

## Contributors

- Initial research + data extraction: Hermes Agent (hermes@ai-whisperers.com)
- Operator: Gaby + Kiki
- Direction: Iván
