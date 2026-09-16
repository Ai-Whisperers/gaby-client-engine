# Session Audit — what's in `gaby-client-engine` vs what's missing

> Walked back through every session message and identified each idea, suggestion, and gap. This is the truth-list (no spin), mapped to files in the engine.

## A. What's in the engine today (18 files, 274 KB)

| File | Lines | What it does |
|---|---:|---|
| README.md | 4,997 B | Entry point, 5-action plan |
| .github/workflows/validate.yml | 883 B | CI: schema check on every push |
| 01-playbook/COMPLETE-PLAYBOOK.md | 14,628 B | 15 prioritized plays + 4-week calendar |
| 01-playbook/ANALYSIS.md | 2,440 B | Opportunity matrix per play |
| 01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md | 9,837 B | 8 new ideas from real-world case studies |
| 02-outreach-pack/SCHEMA.md | 3,614 B | Column definitions + scoring formula |
| 02-outreach-pack/gaby-outreach-pack.csv | 215,540 B | **1,090 pre-scored businesses** |
| 02-outreach-pack/gaby-direct-dental.csv | 1,588 B | 6 dental peers in catchment |
| 03-messages/gaby-outreach-messages.md | 4,901 B | 6 WhatsApp templates by play |
| 04-data-sources/METHODOLOGY.md | 3,597 B | Scoring + classification rules |
| 04-data-sources/PROVENANCE.md | 2,385 B | Where every dataset came from |
| 04-data-sources/REGENERATION-INSTRUCTIONS.md | 2,160 B | How to refresh data quarterly |
| 05-scripts/build_outreach_pack.py | 6,069 B | Regenerate CSV from raw Places API |
| 05-scripts/validate_pack.py | 1,937 B | Schema validator |
| 06-tracking/README.md | 2,855 B | Tracker usage instructions |
| 06-tracking/outreach-tracker-template.csv | 833 B | Empty CRM-lite |
| docs/CHANGELOG.md | 2,118 B | Update log |
| .gitignore | 210 B | Excludes trackers + pycache |

## B. Ideas I gave that landed in the engine

These are listed in deliverables above: 9 niche ideas, 5 monetization ideas, 8 worldwide case studies, 7-play opportunity matrix, 6 WhatsApp templates, 4-week calendar.

## C. Ideas mentioned in conversation that did NOT land in the repo

### Group 1 — Already have a doc in the Ometz strategy repo; engine just needs a cross-link
*(These are 1-line cross-link adds, not real missing material.)*

1. **Calendario de marketing 2026** — day-by-day posting schedule for the year. Exists at `dentist/06_MARKETING/calendar/calendario-marketing-2026-completo.md` (referenced by engine but not copied)
2. **Pricing canonical reference** — `dentist/00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` (not duplicated; mentioned in engine as the SSOT)
3. **WhatsApp quick-replies library** — `dentist/08_WHATSAPP/templates/` (12 reusable responses for inbound)
4. **52 pre-armed annual FB posts** — `dentist/06_MARKETING/facebook/52-posts-pre-armados-anuales.md`
5. **26 GBP posts** — `dentist/06_MARKETING/gbp-posts/26-gbp-posts-6-meses.md`
6. **30 reels scripts** — `dentist/06_MARKETING/reels-scripts/30-reels-scripts.md`
7. **7 SEO blog posts (text ready)** — `dentist/06_MARKETING/blog-posts-seo/`
8. **GBP setup guide** — `dentist/06_MARKETING/google-business-profile-setup-guide.md`
9. **Doctoralia + FB page setup instructions** — `dentist/06_MARKETING/`
10. **WhatsApp setup guide** — `dentist/08_WHATSAPP/whatsapp-setup-configuration-guide.md`
11. **Patient retention/recovery playbook** — `dentist/09_TEMPLATES/patient-retention-recovery-playbook.md`
12. **Email templates** — `dentist/06_MARKETING/email-templates.md`
13. **Objection library** — `dentist/08_WHATSAPP/objection-library.md`
14. **Sales pipeline templates** — `dentist/04_SALES/` (3 files)
15. **Corporate service agreement template** — `dentist/05_OPERATIONS/legal-compliance/practice-legal/corporate-service-agreement-micro-sme.md`
16. **Patient intake + consent forms** — `dentist/05_OPERATIONS/clinical-routines/`
17. **Dental-tourism opportunity analysis** — `dentist/01_RESEARCH/dental-tourism-opportunity-analysis.md`
18. **Expat community deep dive** — `dentist/01_RESEARCH/expat-community-deep-dive.md`
19. **Competitor landscape DG09** — `dentist/01_RESEARCH/competitive/DG09_asuncion_dental_competitor_landscape_2026-07-06.md`
20. **Hospital/clubs institutional outreach** — one-pagers exist in `dentist/03_LAUNCH/institutional-sales/`
21. **Influencer marketing ecosystem** — `dentist/06_MARKETING/influencer-marketing-ecosystem.md`
22. **30 niche ideas** — `dentist/docs/30-IDEAS-NO-CONVENCIONALES-NICHO.md`
23. **Risk register** — `dentist/docs/PLANES-CONTINGENCIA-RIESGOS.md`

> **Fix:** add a `docs/INDEX-OF-DENTIST-STRATEGY-FILES.md` with one-line descriptions and GH URLs for each. ~30 min.

### Group 2 — Discussed but not implemented (would build with another session)
*(Each is a 1-3 file add. Total: 2-4 hours of work.)*

24. **Single PRICING.md file** — bundling three productized offers (segunda-opinión escrita, ATM/bruxismo consult, custom mouthguards). Currently scattered across `dentist/06_MARKETING/`, `COMPLETE-PLAYBOOK.md`, and `corporate-dental-benefits-program.md`.
25. **InterNations "trusted service provider" email template** — referenced in COMPLETE-PLAYBOOK.md Week 1 #4 but no actual template.
26. **Hotel concierge in-person pitch script** — referenced in Week 2 but no script. ~30 lines.
27. **Coaching 1:1 syllabus / curriculum** — referenced as Y2 idea but no operational doc. 6-session outline × topic × deliverables.
28. **Insurance/broker pitch doc** — Sanatorio Migone, Hospital Británico, prepagas. ~1 page.
29. **PR pitch for ABC/La Nacion/Ultima Hora** — 1-page pitch to send to a journalist. ~30 lines.
30. **Patient case-study template** — consent form + photography protocol + writeup format. ~50 lines.

### Group 3 — Acknowledged as gaps, not built
*(Each needs a deliberate decision before building.)*

31. **Paraguay-business canonical repo** — discussed at length. Recommendation was "use existing canonical home in platform/leads-api/, don't build new." Status: not built (matches recommendation).
32. **Google Maps scraping for dental (200+ entries)** — declined on ToS. Recommendation: re-run Places API with `keyword=dental clinic`. **Status: not executed; requires API key from BWS + your explicit approval of ~$5-15 spend.**
33. **IG/Instagram handle enrichment** — declined at scale (IG ToS). **Status: not built; disclosed as gap in METHODOLOGY.md and PROVENANCE.md.**
34. **WhatsApp number validation** — disclosed as known data-quality gap. **Could fix in 1h with a manual QA pass through the top-50 rows.**

### Group 4 — New ideas I raised that aren't yet documented anywhere
*(These are mine; user feedback is welcome before committing.)*

35. **Data refresh cron job** — the script `build_outreach_pack.py` exists but no Hermes cron wraps it. A 30-min add. **Idea: add a quarterly cron that refreshes the CSV and opens a PR automatically.**
36. **Risk register cross-link** — `dentist/docs/PLANES-CONTINGENCIA-RIESGOS.md` exists. Engine never points to it.
37. **Operator runbook for Kiki** — who's Kiki, what hours does she work, what's her response-time SLA? Engine assumes but never says. **Add `OPERATIONS-RUNBOOK.md`.**
38. **Hermes/workflow integration** — which AI agent in the AIW org is responsible for executing engine tasks? (See the `aiw-org-review` repo for the org map.) Engine doesn't declare ownership.
39. **Dashboard spec** — week-over-week trend visible to Kiki. CSV is fine for the first month; once she has 100 rows of tracker data she needs a summary.
40. **Security/access model** — the B2B leads CSV has phone numbers of 1,090 PY businesses. Who can read it? **Add `SECURITY.md`.**

### Group 5 — Things NOT done that you asked for

41. **Repo for all Paraguay businesses (general catalog)** — answer was "don't build, the existing 4 fragments are enough." But you asked for it specifically. **Could revisit if you want — would be a 4-6 hour build using same data but indexed by vertical.**
42. **Google Maps data for general client prospecting** — declined on ToS. **Alternative: re-run Places API with broader keywords** (`keyword="clinic"+"asuncion"`, radius 30km) for ~$30.

### Group 6 — Things we discussed that didn't need files

43. **Instagram follower scraping for Gaby** — declined; documented in chat. No artifact required.
44. **Live ometzdental.com site edits** — recommended in playbook but execution is Gaby/Kiki's task, not repo content.

---

## D. Quick fix candidates (ordered by leverage-to-effort)

| # | Item | Effort | Value |
|---|---|---|---|
| 1 | `docs/INDEX-OF-DENTIST-STRATEGY-FILES.md` — cross-link to all the docs in `dentist/` repo | 30 min | High (orchestrator only needs README + this index) |
| 2 | `01-playbook/PRICING.md` — bundle 3 productized offers with prices | 30 min | High (you can copy-paste from a customer email) |
| 3 | `01-playbook/PR-PITCH.md` — 1-page media pitch | 30 min | Med |
| 4 | `01-playbook/INTER-NATIONS-APPLICATION.md` — English email template | 15 min | High (actionable today) |
| 5 | `01-playbook/HOTEL-GUARANI-SCRIPT.md` — concierge in-person pitch | 30 min | High (actionable today) |
| 6 | `01-playbook/COACHING-SYLLABUS.md` — 6 sessions × topic × deliverable | 1 hour | Med (Y2) |
| 7 | `06-tracking/OPERATOR-RUNBOOK.md` — Kiki persona, hours, SLAs | 30 min | High |
| 8 | `06-tracking/DASHBOARD-SPEC.md` — week-over-week trend visibility | 1 hour | Med |
| 9 | `SECURITY.md` — access control for B2B CSV | 15 min | Med |
| 10 | `.github/workflows/refresh-data.yml` — quarterly CSV refresh via GH Action | 1 hour | Med |
| 11 | `06-tracking/outreach-tracker-template.csv` → add **case_study_consent_form.csv** | 30 min | Med |
| 12 | Append `INSURANCE-PITCH.md` — 3 insurance/prepaga pitch templates | 1 hour | Med |

**Total: ~7 hours, 12 small files added.**

---

## E. What would a v2 repo look like?

If we built v2 of `gaby-client-engine` after this session, the structure would become:

```
gaby-client-engine/
├── (existing 18 files)
├── docs/
│   ├── INDEX-OF-DENTIST-STRATEGY-FILES.md       (NEW)
│   └── INSURANCE-PITCH.md                       (NEW)
├── 01-playbook/
│   ├── (existing 3 files)
│   ├── PRICING.md                                (NEW)
│   ├── PR-PITCH.md                               (NEW)
│   ├── INTER-NATIONS-APPLICATION.md              (NEW)
│   ├── HOTEL-GUARANI-SCRIPT.md                   (NEW)
│   └── COACHING-SYLLABUS.md                      (NEW)
├── 06-tracking/
│   ├── (existing 2 files)
│   ├── OPERATOR-RUNBOOK.md                       (NEW)
│   ├── DASHBOARD-SPEC.md                         (NEW)
│   └── case-study-consent-form.csv               (NEW)
├── SECURITY.md                                    (NEW)
└── .github/workflows/
    ├── validate.yml                              (existing)
    └── refresh-data.yml                          (NEW)
```

That brings the repo to ~30 files, all matching the playbook + lessons + operational needs identified today.

---

## F. Other "ideas mentioned in conversation" not in any artifact

| Idea from chat | Where it lives now |
|---|---|
| Specific dental clinic in 1.09 km, Odontologia Miranda | `01-playbook/ANALYSIS.md` (referenced), NOT yet in gaby-direct-dental.csv |
| Hotel Guarani concierge 4.19 km | `01-playbook/COMPLETE-PLAYBOOK.md` Tier 2 #8, but 4 km number not in outreach CSV |
| 6 client blockers from Gaby (calle, fecha, WA, RUC, MSPBS, CM) | Listed in 01-playbook + dentist/MASTER-TODO but no separate "blockers-tracker.csv" |
| Dr. Mike Varshavski 25M-follower case study | `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` #2 mentioned briefly (implicit in #1 — "brand human") |
| Zack Chug 3K→200K story | `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` #7 (mentioned in synthesized #7 Instagram reel system) |
| Pearl AI 30-50% referral finding | Quote in `01-playbook/COMPLETE-PLAYBOOK.md` (mentioned), not in LESSONS doc |
| ROOT Periodontics 29% lift case | Mentioned in COMPLETE-PLAYBOOK MD informally, no formal LESSON doc |
| Picasso Dental Vietnam 65% conversion | `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` #1 (full case study) |
| Mill Creek Dental smile giveaway | `01-playbook/LESSONS-FROM-DENTISTS-WORLDWIDE.md` #3 (case study) |
| OECD/expat dental case for ARGENTINA/UY | Recommended re-run dental scrape — recommended, not executed |
| Saudi-style dental tourism (sterilization, GCC trust) | Implicit in dental-tourism-opportunity link (G1 #17) |
| Telegram channels for dental education | Not covered anywhere |
| TikTok strategy | Briefly in #7 LESSONS as "IG Reels" but no separate TikTok note |

---

## G. The honest ranking

If you want a single answer to "what's most missing":

**The two biggest gaps in the engine are:**

1. **The 23 cross-link docs in Group 1** — they all live in `Ai-Whisperers/dentist` and are great, but the engine reads as a fresh repo that doesn't point anywhere. The `INDEX-OF-DENTIST-STRATEGY-FILES.md` would solve this in 30 minutes.

2. **The 6 actionable scripts in Group 2** (InterNations email, hotel concierge, pricing page, PR pitch, coaching syllabus, insurance pitch) — these are the things Kiki or Gaby can *use tomorrow* to send real outreach.

After those, the engine would feel complete for Y1 execution.

## H. What to actually do next

| If you have this much time | Do this |
|---|---|
| **30 min** | Add `docs/INDEX-OF-DENTIST-STRATEGY-FILES.md` |
| **2 hours** | Add the 5 actionable scripts in Group 2 (`PRICING.md`, `INTER-NATIONS-APPLICATION.md`, `HOTEL-GUARANI-SCRIPT.md`, `PR-PITCH.md`, `OPERATOR-RUNBOOK.md`) + the index file |
| **6 hours** | Add everything in Group 2 + Group 4 (the 5 operational docs) + run a dental-specific Places API scrape to give Gaby a real 200+ dental list |
| **$5-15** | (separate budget decision) Run the Places API for dental as discussed |

Pick one and tell me which to do next.
