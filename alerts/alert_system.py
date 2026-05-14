def check_alerts(temp, humidity):

    alerts = []

    if temp > 38:
        alerts.append("High Temperature Alert — Temp exceeds 38°C")

    if temp < 20:
        alerts.append("Low Temperature Alert — Temp below 20°C")

    if humidity > 80:
        alerts.append("High Humidity Alert — Humidity exceeds 80%")

    if humidity < 30:
        alerts.append("Low Humidity Alert — Humidity below 30%")

    return alerts