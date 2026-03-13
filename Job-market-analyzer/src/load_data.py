import pandas as pd

df = pd.read_csv("C:/Users/thera/OneDrive/Desktop/python-data-projects/Job-market-analyzer/data/jobs.csv")

print("Dataset:\n")
print(df)

print("\nHighest Salary Job:\n")
print(df.loc[df["salary"].idxmax()])

print("\nJobs per City:\n")
print(df["location"].value_counts())

print("\nMost Demanded Skill:\n")
print(df["skills"].value_counts())

