from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.visualize import create_chart

def run_pipeline():

    print("Extracting dataset...")
    df = extract_data()

    print("Transforming data...")
    top_skills = transform_data(df)

    print("Saving report...")
    load_data(top_skills)

    print("Creating chart...")
    create_chart()

if __name__ == "__main__":
    run_pipeline()