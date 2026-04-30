import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("bugs.csv")

chart = df.groupby("assignee").agg(total_hours=("hours_to_fix","sum")).reset_index()

chart.plot (x="assignee", y="total_hours", kind="bar",
title="assignee by total hours",
legend=True,color="#065A82")

plt.tight_layout
plt.savefig("chart.png")