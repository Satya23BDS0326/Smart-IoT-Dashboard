import random


locations = {
    "Vijayawada": {"temp": (30, 42), "humidity": (55, 85)},
    "Hyderabad":  {"temp": (25, 38), "humidity": (40, 70)},
    "Chennai":    {"temp": (28, 40), "humidity": (60, 90)},
    "Bangalore":  {"temp": (20, 32), "humidity": (35, 65)},
}


def generate_sensor_data(location):

    ranges = locations.get(location, {"temp": (25, 35), "humidity": (50, 70)})

    temp = random.randint(ranges["temp"][0], ranges["temp"][1])
    humidity = random.randint(ranges["humidity"][0], ranges["humidity"][1])

    return {
        "temp": temp,
        "humidity": humidity,
    }