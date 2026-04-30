import pandas as pd
df = pd.read_csv("bugs.csv")
report = df.groupby("severity").agg(
    total_bugs=("bug_id","count"),
    avg_hours=("hours_to_fix","mean"),
    total_hours=("hours_to_fix","sum")
).reset_index
print(report)