"""Portfolio-safe hourly demand demo on SYNTHETIC data only."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data/sample/synthetic_hourly.csv"
if not source.is_file():
    raise FileNotFoundError("Generate demo data first: python src/generate_sample_data.py")
df = pd.read_csv(source, parse_dates=["date"])
expected = {"date", "hour", "positive_orders", "kitchen_staff_hours", "coverage_quality"}
assert expected.issubset(df.columns)
assert not df.duplicated(["date", "hour"]).any()
valid = df.loc[df["coverage_quality"].eq("preliminary") & df["kitchen_staff_hours"].gt(0)].copy()
valid["weekday"] = valid["date"].dt.day_name()
summary = valid.groupby(["weekday","hour"],as_index=False).agg(
    orders=("positive_orders", "sum"), staff_hours=("kitchen_staff_hours", "sum"),
    days=("date", "nunique"))
summary["orders_per_staff_hour"] = summary["orders"] / summary["staff_hours"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
pivot = summary.pivot(index="weekday",columns="hour",values="orders_per_staff_hour").reindex(days)
arr = np.ma.masked_invalid(pivot.to_numpy(dtype=float))
fig,ax=plt.subplots(figsize=(11,5))
im=ax.imshow(arr,aspect="auto",cmap="YlOrBr")
ax.set_xticks(range(len(pivot.columns)),[f"{x}:00" for x in pivot.columns])
ax.set_yticks(range(len(days)),days)
ax.set_title("SYNTHETIC EXAMPLE — Orders per kitchen staff-hour")
ax.set_xlabel("Hour")
fig.colorbar(im,ax=ax,label="Example orders / staff-hour")
fig.tight_layout()
output = ROOT / "outputs/demo_workload_heatmap.png"
output.parent.mkdir(exist_ok=True)
fig.savefig(output,dpi=150)
plt.close(fig)
print(f"Analyzed {len(valid)} synthetic date-hour records; chart: {output}")
