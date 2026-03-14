from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


def run_pipeline():

    df = extract_data()

    top_skills = transform_data(df)

    load_data(top_skills)


if __name__ == "__main__":
    run_pipeline()