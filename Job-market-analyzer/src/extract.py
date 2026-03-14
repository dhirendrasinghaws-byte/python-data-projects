import pandas as pd

def extract_data():
    print("Extracting dataset...")

    df = pd.read_csv("C:/Users/thera/OneDrive/Desktop/python-data-projects/Job-market-analyzer/data/job_skills.csv")

    print("Total rows in dataset:", df.info())

    return df
