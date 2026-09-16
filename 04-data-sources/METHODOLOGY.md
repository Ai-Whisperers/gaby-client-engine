# Methodology — How the outreach pack was built

## Source data

Two CSVs from `Ai-Whisperers/paragu-ai-leads` (private repo, accessed via BWS-stored PAT `GITHUB_PAT_AIW_DEPLOY_2026_09_10`):

- `data/processed/paraguay_priority_a.csv` — **3,960 rows** (Priority A)
- `data/processed/paraguay_priority_b.csv` — **2,836 rows** (Priority B)

Combined: 6,796 businesses. Header columns:

```
name, category, subcategory, city, neighborhood, address,
lat, lng, phone, website, rating, total_reviews, has_website,
deep_score, priority, types
```

## Filters applied

| Filter | Value | Reason |
|---|---|---|
| lat/lng non-empty | Required | Needed for distance calculation |
| Distance from Mburucuyá | ≤ 15 km | Walking/driving distance for the catchment |
| Has phone | Required | No phone = no outreach possible |
| Reviews | Mixed (≥30 for general, ≥0 for dental) | Dental entry quota too thin to filter by reviews |

## Distance calculation

Haversine formula centered on **Gaby's clinic** (-25.314, -57.610):

```
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)² + cos(lat1) cos(lat2) sin(dlon/2)²
    return R * 2 atan2(sqrt(a), sqrt(1-a))
```

Output filtered to ≤15 km straight-line. Driving distance is 1.2–1.5× longer typically.

## Play classification

Each business gets one or more of 6 plays based on category + name + subcategory text matching:

| Play | Triggers on keywords |
|---|---|
| `DIRECT_DENTAL` | dental, dentist, odont, ortodon, implante, endodon, prostodonc, maxilofacial, "clínica dental" |
| `ATM_BRUXISMO` | spa, kinesiolog, fisioterapia, yoga, pilates, wellness, rehabilit, atm |
| `ESTETICA_DENTAL` | estétic, estetic, facial, belleza, sonrisa, smile, whitening, blanquea, carilla, depilacion |
| `MOMS` | baby, bebe, bebé, hidrobaby, maternal, embaraz, mama |
| `B2B_GYM_CORP` | gimnasio, gym, spinning, crossfit, pilates, yoga (only if reviews ≥ 100) |
| `EXPAT_HOTEL` | hotel, hostel, boutique, lodg, resort |

Multiple plays per business is allowed (comma-separated in `play` column).

## WhatsApp URL generation

```python
def to_wa(phone):
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 9 and digits.startswith("0"):
        digits = "595" + digits[1:]
    elif len(digits) == 9 and not digits.startswith("595"):
        digits = "595" + digits
    return f"https://wa.me/{digits}"
```

For Paraguay landlines (`(021) XXXX YYY`), the normalization sometimes produces a wrong number. **Manual confirmation recommended** before first outreach on landline numbers.

## Priority score

See `02-outreach-pack/SCHEMA.md` for the formula.

## Limitations

1. **Beauty/wellness filter bias.** The original dataset is scraped for beauty/wellness verticals. The dental entries present (28 in priority A + 55 in priority B = 83 total) are mostly miscategorized "clinica" with "dental" in passing. A targeted re-scrape for `keyword=dental` would surface 200–500 entries.
2. **No social handles (Instagram, etc.)** — manual lookup needed.
3. **No WhatsApp number validation** — phone ≠ WhatsApp in PY. Some numbers won't load.
4. **5+ weeks of staleness** since the dataset was last refined (Aug 10, 2026). Refresh quarterly.
5. **78% of entries have no website** — that's the *sales pitch* for many of them, but it also means baseline marketing hygiene is low (weak content, no SEO presence), so outreach response rates may be lower than for well-marketed venues.
