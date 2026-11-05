# Synthetic data dictionary

The CSV in `data/sample/` is fully synthetic. It demonstrates a date-hour fact table. Nothing in the file should be interpreted as a real organization's operational history.

| Field | Definition |
|---|---|
| `date` | Illustrative local service date |
| `hour` | Beginning of the one-hour interval, 0–23 |
| `positive_orders` | Generated count of positive-value order events |
| `kitchen_staff_hours` | Generated staff-hours available in an interval |
| `coverage_quality` | `preliminary` or `needs_review` |

`positive_orders / kitchen_staff_hours` is a **diagnostic** ratio. Rows marked `needs_review` are excluded from denominator-based comparisons in the example. The generator uses a fixed random seed so results can be reproduced.
