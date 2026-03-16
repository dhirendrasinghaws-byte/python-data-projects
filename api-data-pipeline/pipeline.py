from src.extract import extract_weather
from src.transform import transform_weather
from src.load import load_weather
from src.visualize import create_chart


def run_pipeline():

    print("Extracting weather data...")
    data = extract_weather()

    print("Transforming data...")
    transformed_data = transform_weather(data)

    print("Loading data...")
    load_weather(transformed_data)

    print("Pipeline completed successfully!")

    print("Creating chart...")
    create_chart()

if __name__ == "__main__":
    run_pipeline()