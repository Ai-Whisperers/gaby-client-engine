# Gaby (Ometz Dental) — Outreach Analysis from paragu-ai-leads dataset

**Source:** `Ai-Whisperers/paragu-ai-leads` (private BWS-accessed), 6,796 Paraguay businesses, scraped Apr→Aug 2026 via Google Places API.
**Anchor:** Gaby's clinic @ Auditores de la Guerra del Chaco 617, Mburucuyá, Asunción (-25.314, -57.610).

## 7 Plays (summary)

| # | Play | Volume in catchment (≤15km, phone, ≥30 reviews) | Highest-leverage target |
|---|---|---:|---|
| 1 | Direct dental | 14 entries in 30 km | Odontologia Miranda Estética Dentofacial (1.09 km, no web) |
| 2 | ATM / Bruxismo feeders | 96 entries in 8 km | Spa Tiger, Beauty & Spa Body Line, Barbas Barbershop (347 rev) |
| 3 | Estética dental feeders | 66 entries in 5 km | Joseph Coiffure (1,274 rev), Brow Bar (404), Velours (230) |
| 4 | Mums / pregnant | 5 entries (HidroBaby cluster) | HidroBaby chain 1,309 reviews combined |
| 5 | B2B corporate | 88 entries in 15 km | Los Barberos de López (2,169), Club Guaraní (1.35 km) |
| 6 | Expat / hotel | 24 entries in 30 km | Hotel Guaraní (4,559 rev, 4.19 km) |
| 7 | Gym boca-guard | ~30 with 100+ revs | AVENTURA, Qanttum, Ritmo, MegaSport |

## Three non-obvious findings

1. **2.5 km vacancy zone** — areas with population density + ZERO adjacent health businesses = where Gaby's "segunda opinión" gets uncontested patient acquisition
2. **78% have NO website** — out of 6,796 businesses only 1,491 have one. Gaby's existing web presence is a competitive moat
3. **Luque, Villa Hayes, Ñemby, Mariano Roque centro are EMPTY in the data** — possibly underserved dental markets

## Deliverables in this dir

- `gaby-outreach-pack.csv` — 200+ rows pre-scored for outreach, columns = outreach_play + priority_score + WhatsApp-ready URL
- `gaby-direct-dental.csv` — 14 dental entries in 30 km catchment, the peer/colleague target list
- `gaby-outreach-messages.md` — 6 WhatsApp templates mapped to outreach_play (open in any text editor)

## Limitations / Next Steps

- **Beauty-filter bias:** 28 dental entries total across 3,960 Priority A; one targeted dental scrape would yield 200+ entries ($5–15 in Places API calls)
- **Stale data:** last refinement 2026-08-10; phones verified manually
- **No IG handles:** adds 30 min/lead for IG-targeted outreach

## Limitation reminder

The dataset is at most 5+ weeks old (last push 2026-08-10). Phones are still mostly valid; review counts may be off by 10–20%.
