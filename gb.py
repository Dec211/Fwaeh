import pandas as pd
by sev = df.groupby("severity")[
    "hours_to_fix"].mean()
    .reset_index()
by_sev.columns = [
    "severity", "avg_hours"]
print(by_sev)