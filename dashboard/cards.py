from shiny import ui


def temperature_card(temp, dark_mode=False):

    bg = "#1e1e1e" if dark_mode else "#ffffff"

    color = "#ffffff" if dark_mode else "#111111"

    border = (
        "1px solid #333"
        if dark_mode
        else "1px solid #e0e0e0"
    )

    return ui.div(

        ui.p(
            "🌡️ Temperature",
            style=f"""
                margin:0;
                font-size:18px;
                font-weight:600;
                color:{'#ffffff' if dark_mode else '#111111'};
            """
        ),

        ui.h1(
            f"{temp} °C",
            style=f"""
                margin:8px 0 0 0;
                font-size:42px;
                color:{color};
            """
        ),

        style=f"""
            background-color:{bg};
            color:{color};
            border:{border};
            border-radius:16px;
            padding:24px 28px;
            box-shadow:0 2px 12px rgba(0,0,0,0.08);
        """
    )


def humidity_card(humidity, dark_mode=False):

    bg = "#1e1e1e" if dark_mode else "#ffffff"

    color = "#ffffff" if dark_mode else "#111111"

    border = (
        "1px solid #333"
        if dark_mode
        else "1px solid #e0e0e0"
    )

    return ui.div(

        ui.p(
            "💧 Humidity",
            style=f"""
                margin:0;
                font-size:18px;
                font-weight:600;
                color:{'#ffffff' if dark_mode else '#111111'};
            """
        ),

        ui.h1(
            f"{humidity} %",
            style=f"""
                margin:8px 0 0 0;
                font-size:42px;
                color:{color};
            """
        ),

        style=f"""
            background-color:{bg};
            color:{color};
            border:{border};
            border-radius:16px;
            padding:24px 28px;
            box-shadow:0 2px 12px rgba(0,0,0,0.08);
        """
    )