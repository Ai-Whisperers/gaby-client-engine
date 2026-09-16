# Outreach Tracker — how to use this

This is a **CRM-lite** for Kiki. Use a copy of `outreach-tracker-template.csv` per quarter (e.g. `outreach-tracker-2026-Q4.csv`).

## Workflow

1. **Copy the template** to a quarter-specific file:
   ```bash
   cp outreach-tracker-template.csv outreach-tracker-2026-Q4.csv
   ```

2. **Import your outreach pack** — most sheets/Excel can open the 1,090-row CSV and you sort/filter by priority + outreach_template.

3. **As you contact each row**, fill in the tracker columns:
   - `contacted_date` (YYYY-MM-DD)
   - `reply_date` (YYYY-MM-DD when first reply received)
   - `reply_status` — pick one: `NO_REPLY` / `REPLIED` / `INTERESTED` / `NOT_INTERESTED` / `BLOCKED` / `WRONG_NUMBER`
   - `next_action` — text describing the next step (e.g., "Schedule coffee Thu 10am")
   - `notes` — anything else worth remembering

4. **Fill only one row per business.** Duplicate contacts to the same place = wasted effort.

## Cadence

- **10 messages/day maximum.** 30 days × 10 = 300 contacts per quarter.
- **Wait ≥48h before re-contacting** anyone who didn't reply (lengthen to 1 week after the third attempt).
- **Always personalize** even when templating. The line `Hola [NAME]` should become `Hola [actual name]`.
- **Reply within 4 hours** during working hours. Speed-to-reply is the #1 conversion lever.

## Targets

| Status | Goal for end of month 1 |
|---|---|
| Contacted | 100 |
| Replies received | 5–10 |
| Interested | 2–5 (i.e. conversion 2–5%) |
| First formal referral agreement | 1 |
| First referred patient | within 60 days of first signed agreement |

If you're hitting >5% interested, scale to 20 messages/day. If <1%, change the message angle.

## What to do when someone replies "I don't have time"

Send a follow-up 7 days later:

> Sin problema, [NOMBRE] — entiendo que el tiempo es limitado. Si te interesa, déjame tu mejor día/hora y me adapto. Si querés que te envíe un PDF de 1 página con lo que ofrezco para que lo veas cuando puedas, decime también. — Gaby

## What to do when someone says "Send info"

Send the WhatsApp message template with a 1-page PDF attached (the second-opinion lead magnet, when it's built).

## What to do when someone says "Not interested, never call again"

Mark `NOT_INTERESTED` and **do not contact again**. The dataset is large enough to absorb the loss.

## Aggregations

At month-end, Kiki should produce a 1-paragraph report:

```
Outreach Q4 2026:
- Contacted: 280 (vs. goal 300)
- Reply rate: 7% (vs. benchmark 5%)
- Interested: 18 businesses
- First signed referral agreement: 2 (Joseph Coiffure, Spa Tiger)
- First patient via referral: [date]

Adjustments for Q1 2027:
- Drop any template with <2% reply rate
- Increase outreach to top 20% priority only (more laser, more replies)
```

This goes into `06-tracking/reports/`.
