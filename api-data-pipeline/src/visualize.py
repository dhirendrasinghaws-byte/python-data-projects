import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/weather_data.csv")

temperature = df["temperature"][0]
windspeed = df["windspeed"][0]

plt.bar(["Temperature", "Wind Speed"], [temperature, windspeed])

plt.title("Current Weather Metrics")
plt.ylabel("Value")

plt.savefig("output/weather_chart.png")
plt.show()