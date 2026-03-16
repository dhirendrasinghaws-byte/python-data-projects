import pandas as pd

def load_weather(data):

    df = pd.DataFrame([data])

    df.to_csv("output/weather_data.csv", index=False)

    print("Weather data saved successfully.")