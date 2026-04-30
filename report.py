import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use("Agg")

df = pd.read_csv("bugs.csv")
report = df.groupby("assignee").agg(

report.to_csv("report.csv", index=False)
report.plot( x="severity" , y="total_bugs", kind="bar", title="Bugs by Severity",legend=False, color="#065A82")
plt.tight_layout()
plt.savefig("chart.png")
)
