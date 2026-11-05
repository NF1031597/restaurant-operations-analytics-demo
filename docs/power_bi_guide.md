# Power BI extension plan (synthetic data only)

Power BI has **not yet been completed** for this public example. A later extension could import `data/sample/synthetic_hourly.csv` and create:

- A date-hour workload matrix, filtered to quality-approved intervals.
- Cards for total synthetic order events, available staff-hours, and share of uncertain intervals.
- A weekday-hour heatmap with visible observation counts.

Suggested measure, after importing the example as `FactHours`:

```dax
Demo Orders per Staff-Hour =
DIVIDE(
    CALCULATE(SUM(FactHours[positive_orders]), FactHours[coverage_quality] = "preliminary"),
    CALCULATE(SUM(FactHours[kitchen_staff_hours]), FactHours[coverage_quality] = "preliminary")
)
```

Use only the synthetic dataset and do not publish screenshots or dashboard exports containing non-public business information.
