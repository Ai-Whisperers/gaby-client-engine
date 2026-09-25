# 07 — Legacy Reactivation Pack

> **Gaby's historical patient base, unified, cross-matched, and converted into an actionable reactivation pipeline.**
> Built 2026-09-24 from scanned notebooks + 2026 digital system export + Google Sheet "Agenda Odontológica Consolidada - Abril 2026".

## What this is

The paper notebooks (`L.pdf` / `Lunes-2/3.pdf`) are Gaby's **old practice agenda** ("Consultorio P.J.L.", written in a recycled 2015/16 planner) — 152 paper appointments with clinical notes (FDI tooth numbers, treatment plans, insurer per patient). Cross-matched against the 2026 digital system (342 patients) and the April/May digitization sheet, they unify into a **501-patient master database**. Only 15 patients appear in both eras — the rest are a dormant legacy base of **403 reactivation opportunities**.

## The numbers

| Metric | Value |
|---|---|
| Unique patients (all eras) | **501** |
| Legacy-only patients (old practice) | 139 of 152 (zero match with 2026 system) |
| Patients in BOTH eras (loyal) | 15 |
| Reactivation opportunities | **403** |
| — P1: treatment left half-done | 3 (no phone on file) |
| — P2: 2026 dropout with phone ready | 244 |
| — P3: legacy, insurer known | 156 |
| Social-profile candidates found (public web) | **189** for 116 dedup'd legacy patients |
| Historical insurer mix (P3) | MOPC 44 · Presidencia/Gab. Civil 28 · BNF 19 · Diputados 16 · Rel. Exteriores 14 |

## Files

| File | What | How to use |
|---|---|---|
| `pacientes_maestro.csv` | 501 unified patients (source flags, era, visits, insurers, notes) | Single source of truth. Never rebuild — append. |
| `reactivacion_prioridad.csv` | 403 rows: priority P1/P2/P3, phone, cédula, message hook | Gaby works top-down, 30 min/week. |
| `agenda_consolidada_2026.csv` | April (124 paper + 132 digital) + May unified agenda | Operational history. |
| `pctes_2026_clean.csv` | Cleaned 2026 system export (601 appointments) | Raw reference. |
| `cuaderno_transcripcion.md` | Page-by-page notebook transcription | Clinical continuity when legacy patients return. |
| `social/revisar_gaby.csv` | 189 public-profile candidates → Gaby confirms SI/NO/dudoso | **Confirm before any contact. Never contact without her SI.** |

## The play (in order)

1. **P2 WhatsApp batch** — 244 numbers ready today. One message: *"Hola [nombre], la Dra. González te saludaba — notamos que quedaste pendiente de una visita. Tenemos disponibilidad esta semana, ¿agendamos?"*
2. **P1 half-treatment rescue** — Gaby names the 3 patients herself (highest conversion in dentistry: "te lo terminamos").
3. **P3 legacy** — Gaby reviews the 156 names (she'll remember faces); classic message: *"Volví con consultorio propio (Ometz Dental), atiendo tu seguro"*. Realistic 5–10% conversion = 8–15 returning patients.
4. **Social candidates** — only where phone is missing: Gaby marks SI on `social/revisar_gaby.csv`, outreach happens via platform DM with the same message.

## Strategic notes

- **Insurer intelligence:** her historical base is institutional (state employees: MOPC, Presidencia, BNF, Diputados); her current base is private (ASISMED 305, MDS 104). The old book proves she already knows the state-employee market — Ometz Dental can register as institutional provider and she has 100+ past patients who'd qualify.
- **Clinical continuity:** the 23 fichas digitized in the Google Sheet document treatments (perno-coronas, carillas, rehabilitations) — professional memory most clinics lose when changing systems.
- **Privacy rules:** this data is health-adjacent PII. No outreach without Gaby's explicit confirmation. Social candidates were collected from public search metadata only (no profile scraping, no contact data recorded).

## Provenance

- Notebooks scanned → transcribed page-by-page (`cuaderno_transcripcion.md`) → cross-checked against Google Sheet ground truth (real names corrected handwriting readings).
- Master unification: fuzzy name-matching (token overlap, alias merge of spelling variants), 145 sheet entries → 116 unique legacy persons → batched into 9 research lots.
- 189 candidates found via public web-search metadata in 11 subagent batches (3 retried after API 429s). Zero profile pages opened; no phones/emails/addresses recorded from the web.
