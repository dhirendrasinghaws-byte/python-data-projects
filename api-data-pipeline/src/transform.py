def transform_weather(data):

    weather = data["current_weather"]

    transformed_data = {
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "winddirection": weather["winddirection"],
        "time": weather["time"]
    }

    return transformed_data