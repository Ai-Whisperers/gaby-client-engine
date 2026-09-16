#!/usr/bin/env python3
"""
build_outreach_pack.py — regenerate Gaby's outreach CSV from a Places API export.

Stdlib only. Matches 04-data-sources/METHODOLOGY.md.
"""
import argparse, csv, math, sys
from pathlib import Path

GABY_LAT, GABY_LNG = -25.314, -57.610

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def to_wa(phone):
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 9 and digits.startswith("0"):
        digits = "595" + digits[1:]
    elif len(digits) == 9 and not digits.startswith("595"):
        digits = "595" + digits
    return f"https://wa.me/{digits}" if digits else ""

KEYWORDS = {
    "DIRECT_DENTAL": ["dental","dentist","odont","ortodon","implante","endodon","prostodonc","maxilofacial","clinica dental"],
    "ATM_BRUXISMO": ["spa","kinesiolog","fisioterapia","yoga","pilates","wellness","rehabilit","atm"],
    "ESTETICA_DENTAL": ["estetic","facial","belleza","sonrisa","smile","whitening","blanquea","carilla","depilacion"],
    "MOMS": ["baby","bebe","hidrobaby","maternal","embaraz","mama"],
    "B2B_GYM_CORP": ["gimnasio","gym","spinning","crossfit","functional","pilates","yoga"],
    "EXPAT_HOTEL": ["hotel","hostel","boutique","lodg","resort"],
}

def classify(row):
    text = " ".join(str(v) for v in row.values()).lower()
    plays = []
    if any(kw in text for kw in KEYWORDS["DIRECT_DENTAL"]): plays.append("DIRECT_DENTAL")
    if any(kw in text for kw in KEYWORDS["ATM_BRUXISMO"]): plays.append("ATM_BRUXISMO")
    if any(kw in text for kw in KEYWORDS["ESTETICA_DENTAL"]): plays.append("ESTETICA_DENTAL")
    if any(kw in text for kw in KEYWORDS["MOMS"]): plays.append("MOMS")
    if any(kw in text for kw in KEYWORDS["B2B_GYM_CORP"]):
        try: reviews = int(row.get("total_reviews") or 0)
        except: reviews = 0
        if reviews >= 100: plays.append("B2B_GYM_CORP")
    if any(kw in text for kw in KEYWORDS["EXPAT_HOTEL"]): plays.append("EXPAT_HOTEL")
    return plays

def priority_score(distance_km, reviews, plays):
    p = 0
    if distance_km <= 2: p += 5
    elif distance_km <= 5: p += 4
    elif distance_km <= 10: p += 3
    else: p += 2
    if reviews >= 200: p += 5
    elif reviews >= 100: p += 4
    elif reviews >= 50: p += 3
    elif reviews >= 30: p += 2
    if "DIRECT_DENTAL" in plays: p += 4
    if "MOMS" in plays: p += 3
    if "ATM_BRUXISMO" in plays: p += 2
    if "ESTETICA_DENTAL" in plays: p += 2
    if "B2B_GYM_CORP" in plays: p += 3
    if "EXPAT_HOTEL" in plays: p += 4
    return p

OUTREACH_TEMPLATE = {
    "DIRECT_DENTAL": "DENTAL_COLLEAGUE",
    "MOMS": "MOMS_HIDROBABY",
    "ATM_BRUXISMO": "ATM_BRUXISMO",
    "ESTETICA_DENTAL": "ESTETICA_SONRISA",
    "B2B_GYM_CORP": "GYM_BOCA_GUARD",
    "EXPAT_HOTEL": "EXPAT_HOTEL",
}

def outreach_template_for(plays):
    if "DIRECT_DENTAL" in plays: return "DENTAL_COLLEAGUE"
    if "MOMS" in plays: return "MOMS_HIDROBABY"
    if "ATM_BRUXISMO" in plays: return "ATM_BRUXISMO"
    if "ESTETICA_DENTAL" in plays: return "ESTETICA_SONRISA"
    if "B2B_GYM_CORP" in plays: return "GYM_BOCA_GUARD"
    if "EXPAT_HOTEL" in plays: return "EXPAT_HOTEL"
    return "ADJACENT_GENERAL"

OUT_COLS = ["business_name","category","subcategory","city","address","phone","whatsapp_url",
            "distance_km","google_rating","google_reviews","has_website","play",
            "priority_score","outreach_template"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", default="../02-outreach-pack/gaby-outreach-pack.csv")
    ap.add_argument("--center-lat", type=float, default=GABY_LAT)
    ap.add_argument("--center-lng", type=float, default=GABY_LNG)
    ap.add_argument("--radius-km", type=float, default=15)
    ap.add_argument("--min-reviews", type=int, default=30)
    ap.add_argument("--require-phone", action="store_true", default=True)
    args = ap.parse_args()

    with open(args.input, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    out = []
    for r in rows:
        try: lat = float(r.get("lat","0") or 0); lng = float(r.get("lng","0") or 0)
        except: continue
        if not (lat and lng): continue
        km = haversine(args.center_lat, args.center_lng, lat, lng)
        if km > args.radius_km: continue
        phone = (r.get("phone","") or "").strip()
        if args.require_phone and not phone: continue
        try: reviews = int(r.get("total_reviews") or 0)
        except: reviews = 0
        plays = classify(r)
        if not plays and reviews < 50: continue
        prio = priority_score(km, reviews, plays)
        has_web = bool((r.get("website","") or "").strip())
        out.append({
            "business_name": r.get("name","").strip(),
            "category": r.get("category","").strip(),
            "subcategory": r.get("subcategory","").strip(),
            "city": r.get("city","").strip(),
            "address": r.get("address","").strip(),
            "phone": phone,
            "whatsapp_url": to_wa(phone),
            "distance_km": round(km, 2),
            "google_rating": r.get("rating",""),
            "google_reviews": reviews,
            "has_website": "NO" if not has_web else "YES",
            "play": ",".join(plays) if plays else "ADJACENT_REFER",
            "priority_score": prio,
            "outreach_template": outreach_template_for(plays),
        })

    out.sort(key=lambda r: -r["priority_score"])
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore")
        w.writeheader()
        for r in out: w.writerow(r)
    print(f"WROTE {out_path} ({len(out)} rows)")

if __name__ == "__main__":
    main()
