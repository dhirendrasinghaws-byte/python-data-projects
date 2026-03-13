import pandas as pd

# load dataset
df = pd.read_csv("C:/Users/thera/OneDrive/Desktop/python-data-projects/Job-market-analyzer/data/job_skills.csv")

print("First rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())

print("\nMost demanded skills:\n")
print(df.loc[df["skill_abr"].value_counts().head(10)])

top_skills = df["skill_abr"].value_counts().head(10)

print("\nTop Skills:\n")
print(top_skills)

# save report
top_skills.to_csv("C:/Users/thera/OneDrive/Desktop/python-data-projects/Job-market-analyzer/output/top_skills_report.csv")