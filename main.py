import pandas as pd

df = pd.read_csv["bugs.csv"]

by_sev = df.groupby("severity")[
    "bug_id"].count()
print(by_sev)
by_sev = by_sev.reset_index()
by_sev.colums = [
    "severity", "count"]
print(by_sev)