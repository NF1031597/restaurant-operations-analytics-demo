# Methodology and validity boundaries

## General analytical workflow

- Define the unit of analysis as one date × hour.
- Validate input schema, datetimes, duplicate records, and plausible values before aggregation.
- Distinguish orders from items prepared; a positive-value order count is only a proxy for production demand.
- Calculate coverage from fractional shift overlap: thirty minutes within an hour represents 0.5 staff-hours.
- Flag incomplete or ambiguous time entries. Never interpret unknown staffing as zero.
- Use an outer date-hour merge to retain order hours without matched staffing and staffed hours without orders.
- Use a ratio of totals for aggregation: total eligible orders / total eligible staff-hours, rather than averaging row-level ratios.
- Display sample sizes, source completeness, and uncertainty for weekday-hour comparisons.

## Limitations

Order-opened timestamps are not kitchen completion times. Orders vary by number of items and preparation complexity. People working in customer service or management may split duties. Cleaning, setup, and closing work may be necessary even if no orders are observed. The example does not include service-level or cost outcome measurements.

## Validation before practical use

1. Acquire authorized, complete and documented source data.
2. Verify time-entry issues with a trusted attendance source.
3. Add item-level demand, duty allocation, and service-time observations where permitted.
4. Compare alternative schedules through a controlled, monitored pilot.

**All current public visualizations and calculations use synthetic data. No practical staffing recommendation or financial outcome is claimed.**
