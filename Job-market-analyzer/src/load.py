import os

def load_data(top_skills):

    print("Saving report...")

    os.makedirs("output", exist_ok=True)

    top_skills.to_csv("output/top_skills_report.csv")

    print("Report saved successfully.")