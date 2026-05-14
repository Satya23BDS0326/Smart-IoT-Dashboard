def weather_condition(temp, humidity):

    if temp > 38:
        return "🔥 Heatwave"

    elif humidity > 80:
        return "🌧️ Rain Possible"

    elif temp < 24:
        return "🌫️ Cold Climate"

    else:
        return "☀️ Pleasant Weather"