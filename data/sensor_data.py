import random

sensor_data = {
    "Pune": {"temp": (27, 32), "humidity": (60, 75)},
    "Hyderabad": {"temp": (30, 38), "humidity": (45, 65)},
    "Bengaluru": {"temp": (22, 29), "humidity": (60, 78)},
    "Chennai": {"temp": (32, 39), "humidity": (65, 85)},
    "Mumbai": {"temp": (28, 34), "humidity": (70, 90)},
    "Delhi": {"temp": (34, 42), "humidity": (35, 55)},
    "Kolkata": {"temp": (30, 37), "humidity": (65, 85)},
    "Ahmedabad": {"temp": (33, 41), "humidity": (35, 55)},
    "Guwahati": {"temp": (24, 31), "humidity": (70, 90)},
    "Jaipur": {"temp": (32, 40), "humidity": (30, 50)}
}

def generate_sensor_data(location):

    ranges = sensor_data.get(location, {"temp": (25, 35), "humidity": (50, 70)})

    temp = random.randint(ranges["temp"][0], ranges["temp"][1])
    humidity = random.randint(ranges["humidity"][0], ranges["humidity"][1])

    return {
        "temp": temp,
        "humidity": humidity,
    }
