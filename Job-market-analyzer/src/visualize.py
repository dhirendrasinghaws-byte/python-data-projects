import pandas as pd
import matplotlib.pyplot as plt

# load report
df = pd.read_csv("output/top_skills_report.csv")

# create bar chart
plt.bar(df["skill_abr"], df["count"])

plt.title("Top 10 Most Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Job Demand")

plt.xticks(rotation=45)

# save chart
plt.savefig("output/top_skills_chart.png")

# show chart
plt.show()