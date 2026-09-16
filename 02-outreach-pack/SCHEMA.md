# CSV Schema — `02-outreach-pack/gaby-outreach-pack.csv`

Master outreach file. **1,090 rows** as of last refresh. Generated from `Ai-Whisperers/paragu-ai-leads/data/processed/paraguay_priority_{a,b}.csv`.

## Columns

| Column | Type | Notes |
|---|---|---|
| `business_name` | string | Display name from Google Maps |
| `category` | string | High-level bucket |
| `subcategory` | string | Granular vertical |
| `city` | string | District, e.g. "Asunción", "Lambaré" |
| `address` | string | Full street address (often a Plus Code if no street available) |
| `phone` | string | Raw phone as captured (Paraguay conventions vary) |
| `whatsapp_url` | URL | Pre-built `https://wa.me/<number>` link ready to open in any browser |
| `distance_km` | float | Kilometers from `Auditores de la Guerra del Chaco 617, Mburucuyá` (-25.314, -57.610) |
| `google_rating` | float | Google Maps star rating (0–5, may be empty if unrated) |
| `google_reviews` | int | Review count (used as reputation proxy) |
| `has_website` | "YES"/"NO" | "NO" used as a sales pitch: "we'll build one" |
| `play` | list | One or more of: `DIRECT_DENTAL`, `ATM_BRUXISMO`, `ESTETICA_DENTAL`, `MOMS`, `B2B_GYM_CORP`, `EXPAT_HOTEL` — comma-separated |
| `priority_score` | int 0–15 | Heuristic sum of distance + reviews + plays. Sort on this descending. |
| `outreach_template` | enum | Which of the 6 WhatsApp templates to use |

## Priority score formula

```
prio = 0
if km <= 2:    prio += 5
elif km <= 5:  prio += 4
elif km <= 10: prio += 3
else:          prio += 2

if reviews >= 200: prio += 5
elif reviews >= 100: prio += 4
elif reviews >= 50:  prio += 3
elif reviews >= 30:  prio += 2

# Play weights
prio += 4 if "DIRECT_DENTAL" in plays else 0
prio += 3 if "MOMS"         in plays else 0
prio += 2 if "ATM_BRUXISMO" in plays else 0
prio += 2 if "ESTETICA_DENTAL" in plays else 0
prio += 3 if "B2B_GYM_CORP" in plays else 0
prio += 4 if "EXPAT_HOTEL"  in plays else 0
```

Max score = **15** (e.g. 2 km + 200+ reviews + DIRECT_DENTAL + EXPAT_HOTEL).

## Outreach template mapping

| `outreach_template` | Message in `03-messages/gaby-outreach-messages.md` |
|---|---|
| `DENTAL_COLLEAGUE` | Section 1 |
| `MOMS_HIDROBABY` | Section 2 |
| `ATM_BRUXISMO` | Section 3 |
| `ESTETICA_SONRISA` | Section 4 |
| `GYM_BOCA_GUARD` | Section 5 |
| `EXPAT_HOTEL` | Section 6 |
| `ADJACENT_GENERAL` | Pick the closest of Sections 3/4 by category |

## Data quality caveats

- **Phone formatting varies.** Paraguay uses `(021) XXXX YYY` for Asunción landlines and `09XX XXX XXX` for mobiles. The `whatsapp_url` column normalizes these but the raw `phone` may have inconsistencies.
- **Distance is straight-line (haversine).** Driving distance is 1.2–1.5× longer typically.
- **Reviews and ratings may be stale** by 5–10% as of file date (`docs/CHANGELOG.md` lists refresh dates).
- **No IG handles.** Adding them requires manual lookup of the top-50 entries.
- **No WhatsApp numbers (only phone).** Manual confirmation needed before first outreach — the dataset doesn't tell us if a phone has WhatsApp.

## Slice examples

```bash
# Top 10 by priority, all plays
head -1 gaby-outreach-pack.csv  # header for column indices
awk -F, 'NR>1 && $13 != "" {print $13 " " $1}' gaby-outreach-pack.csv | sort -nr | head -10

# All dental-direct rows within 5 km
awk -F, 'NR==1 || ($8 <= 5 && $12 ~ /DIRECT_DENTAL/)' gaby-outreach-pack.csv

# All HidroBaby / MOMS rows
awk -F, 'NR==1 || ($12 ~ /MOMS/)' gaby-outreach-pack.csv

# All businesses within 2 km with 100+ reviews
awk -F, 'NR==1 || ($8 <= 2 && $10 >= 100)' gaby-outreach-pack.csv
```
