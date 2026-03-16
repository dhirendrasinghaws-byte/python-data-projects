import requests

def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.45&longitude=77.03&current_weather=true"

    response = requests.get(url)

    data = response.json()

    return data