"""Generate deterministic SYNTHETIC examples; no employer data used."""
from pathlib import Path
from datetime import date, timedelta
import csv
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/sample/synthetic_hourly.csv"
random.seed(37)
rows = []
for day_idx in range(21):
    day = date(2024, 1, 8) + timedelta(days=day_idx)
    weekend = day.weekday() in (4,5)
    for hour in range(11,21):
        peak = 17 <= hour <= 19
        base = (8 if weekend else 5) + (5 if peak else 0)
        orders = max(0, base + random.randint(-3,3))
        staff = 2.0 if 12 <= hour <= 19 else 1.0
        quality = "needs_review" if (day_idx, hour) in {(2,18),(8,19),(13,13)} else "preliminary"
        rows.append({"date":day.isoformat(),"hour":hour,"positive_orders":orders,
                     "kitchen_staff_hours":staff,"coverage_quality":quality})
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", newline="", encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print(f"Wrote {len(rows)} SYNTHETIC rows to {OUT}")
