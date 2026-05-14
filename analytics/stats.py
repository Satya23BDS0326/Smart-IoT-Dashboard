def calculate_stats(temp_history, humidity_history):

    return {
        "avg_temp": round(sum(temp_history) / len(temp_history), 1),

        "max_temp": max(temp_history),

        "min_temp": min(temp_history),

        "avg_humidity": round(
            sum(humidity_history) / len(humidity_history),
            1
        ),
    }