from shiny import App, reactive, render, ui
from random import randint
from datetime import datetime

from dashboard.cards import temperature_card, humidity_card
from dashboard.graphs import temperature_graph, humidity_graph
from alerts.alert_system import check_alerts
from location.location_selector import location_selector
from theme.theme_config import theme_toggle
from weather.weather_prediction import weather_condition
from analytics.stats import calculate_stats


locations = {
    "Pune": {"temp": (27, 32), "humidity": (60, 75)},
    "Hyderabad": {"temp": (30, 38), "humidity": (45, 65)},
    "Bengaluru": {"temp": (22, 29), "humidity": (60, 78)},
    "Chennai": {"temp": (32, 39), "humidity": (65, 85)},
    "Mumbai": {"temp": (28, 34), "humidity": (70, 90)},
    "Delhi": {"temp": (34, 42), "humidity": (35, 55)},
    "Kolkata": {"temp": (30, 37), "humidity": (65, 85)},
    "Ahmedabad": {"temp": (33, 41), "humidity": (35, 55)},
    "Guwahati": {"temp": (24, 31), "humidity": (70, 90)},
    "Jaipur": {"temp": (32, 40), "humidity": (30, 50)},
}


def make_history(location):

    t_range = locations[location]["temp"]
    h_range = locations[location]["humidity"]

    temps = [
        randint(t_range[0], t_range[1])
        for _ in range(10)
    ]

    humids = [
        randint(h_range[0], h_range[1])
        for _ in range(10)
    ]

    return temps, humids


initial_temp, initial_humidity = make_history(
    "Pune"
)


app_ui = ui.page_fluid(

    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="style.css"
        )
    ),

    ui.output_ui("theme_page"),

    ui.div(

        ui.div(

            ui.h1(
                "🌎 Smart IoT Dashboard",
                style="""
                    margin:0;
                    font-size:52px;
                    font-weight:800;
                    letter-spacing:1px;
                    text-align:center;
                    font-family:'Segoe UI', sans-serif;
                    color:#0f172a;
                    text-shadow:
                        0 2px 8px rgba(0,0,0,0.08);
                """
            ),

            style="""
                flex:1;
                display:flex;
                justify-content:center;
                align-items:center;
            """
        ),

        ui.div(

            ui.output_ui("theme_toggle_ui"),

            ui.div(
                ui.output_ui("sensor_status"),

                style="""
                    margin-top:70px;
                """
            ),

            style="""
                position:relative;
                display:flex;
                flex-direction:column;
                align-items:flex-end;
            """
        ),

        style="""
            display:flex;
            justify-content:space-between;
            align-items:flex-start;
            width:100%;
            margin-bottom:20px;
        """
    ),

    ui.br(),

    location_selector(),

    ui.br(),

    ui.layout_columns(
        ui.output_ui("temp_card"),
        ui.output_ui("humidity_card_ui"),
        col_widths=[6, 6]
    ),

    ui.hr(),

    ui.h2("🌡️ Environmental Conditions"),
    ui.output_text("weather_status"),

    ui.hr(),

    ui.h2("🚨 Alerts"),
    ui.output_ui("alerts"),

    ui.hr(),

    ui.h2("📊 Analytics"),
    ui.output_ui("analytics_cards"),

    ui.hr(),

    ui.h2("📈 Temperature Graph"),
    ui.output_plot("temp_plot"),

    ui.hr(),

    ui.h2("💧 Humidity Graph"),
    ui.output_plot("humidity_plot"),

    ui.hr(),

    ui.h3("🕒 Last Updated"),
    ui.output_text("last_updated"),

    ui.br(),

    ui.download_button(
        "download_excel",
        "📥 Download Excel Report"
    ),
)


def server(input, output, session):

    dark_mode = reactive.value(False)

    previous_location = reactive.value(
        "Pune"
    )

    temp_history = reactive.value(
        initial_temp
    )

    humidity_history = reactive.value(
        initial_humidity
    )

    sensor_values = reactive.value({
        "temp": initial_temp[-1],
        "humidity": initial_humidity[-1],
    })

    @reactive.effect
    @reactive.event(input.theme_btn)
    def _toggle_theme():

        dark_mode.set(
            not dark_mode.get()
        )

    @output
    @render.ui
    def theme_toggle_ui():

        return theme_toggle(
            dark_mode.get()
        )

    @output
    @render.ui
    def sensor_status():

        bg = "#111827" if dark_mode.get() else "#ffffff"

        return ui.div(

            ui.p(
                "🟢 Temperature Sensor → Online",
                style="""
                    margin:0;
                    font-size:13px;
                    font-weight:600;
                    color:#2ecc71;
                """
            ),

            ui.p(
                "🟢 Humidity Sensor → Online",
                style="""
                    margin:6px 0;
                    font-size:13px;
                    font-weight:600;
                    color:#2ecc71;
                """
            ),

            ui.p(
                "🟢 Cloud Sync → Active",
                style="""
                    margin:0;
                    font-size:13px;
                    font-weight:600;
                    color:#38bdf8;
                """
            ),

            style=f"""
                background:{bg};
                border:1px solid #334155;
                padding:14px 18px;
                border-radius:14px;
                box-shadow:0 2px 10px rgba(0,0,0,0.08);
                min-width:280px;
            """
        )

    @output
    @render.ui
    def theme_page():

        if dark_mode.get():

            return ui.tags.style("""

                body {
                    background-color:#0f172a !important;
                    color:#ffffff !important;
                }

                h1,h2,h3,h4,h5,p,label,span {
                    color:#ffffff !important;
                }

                .card,
                div[style*="background-color:#ffffff"] {

                    background-color:#111827 !important;

                    color:#ffffff !important;

                    border:1px solid #334155 !important;
                }

                select,
                button {

                    background-color:#111827 !important;

                    color:#ffffff !important;

                    border:1px solid #334155 !important;
                }

                button span,
                button,
                a,
                a span {

                    color:#ffffff !important;
                }

                hr {
                    border-color:#334155 !important;
                }

            """)

        return ui.tags.style("""

            body {
                background-color:#f5f7fa !important;
                color:#111111 !important;
            }

        """)

    @reactive.effect
    def _update_sensor():

        reactive.invalidate_later(30)

        location = input.location()

        t_range = locations[location]["temp"]

        h_range = locations[location]["humidity"]

        if location != previous_location.get():

            new_temps, new_humids = make_history(
                location
            )

            temp_history.set(new_temps)

            humidity_history.set(
                new_humids
            )

            previous_location.set(location)

        else:

            temps = temp_history.get()

            humids = humidity_history.get()

            temps.append(
                randint(
                    t_range[0],
                    t_range[1]
                )
            )

            humids.append(
                randint(
                    h_range[0],
                    h_range[1]
                )
            )

            if len(temps) > 15:
                temps.pop(0)

            if len(humids) > 15:
                humids.pop(0)

            temp_history.set(temps)

            humidity_history.set(humids)

        sensor_values.set({
            "temp": temp_history.get()[-1],
            "humidity": humidity_history.get()[-1],
        })

    @output
    @render.ui
    def temp_card():

        return temperature_card(
            sensor_values.get()["temp"],
            dark_mode.get()
        )

    @output
    @render.ui
    def humidity_card_ui():

        return humidity_card(
            sensor_values.get()["humidity"],
            dark_mode.get()
        )

    @output
    @render.text
    def weather_status():

        data = sensor_values.get()

        if data["temp"] >= 38:
            weather = "High Temperature Conditions"

        elif data["temp"] >= 30:
            weather = "Warm & Dry Conditions"

        elif data["temp"] >= 24:
            weather = "Moderate Conditions"

        else:
            weather = "Cool & Humid Conditions"

        return weather

    @output
    @render.ui
    def alerts():

        data = sensor_values.get()

        alert_list = check_alerts(
            data["temp"],
            data["humidity"]
        )

        if not alert_list:

            return ui.p(
                "Environment Normal",
                style="""
                    color:#22c55e;
                    font-weight:bold;
                """
            )

        return ui.div(
            *[
                ui.p(
                    f"{a}",
                    style="""
                        color:#ef4444;
                        font-weight:bold;
                    """
                )
                for a in alert_list
            ]
        )

    @output
    @render.ui
    def analytics_cards():

        stats = calculate_stats(
            temp_history.get(),
            humidity_history.get()
        )

        return ui.layout_columns(

            ui.div(
                ui.h4("🌡 Avg Temp"),
                ui.h2(
                    f"{stats['avg_temp']} °C"
                ),
                class_="card"
            ),

            ui.div(
                ui.h4("🔥 Max Temp"),
                ui.h2(
                    f"{stats['max_temp']} °C"
                ),
                class_="card"
            ),

            ui.div(
                ui.h4("❄ Min Temp"),
                ui.h2(
                    f"{stats['min_temp']} °C"
                ),
                class_="card"
            ),

            ui.div(
                ui.h4("💧 Avg Humidity"),
                ui.h2(
                    f"{stats['avg_humidity']} %"
                ),
                class_="card"
            ),

            col_widths=[3, 3, 3, 3]
        )

    @output
    @render.plot
    def temp_plot():

        fig = temperature_graph(
            temp_history.get(),
            dark_mode.get()
        )

        return fig

    @output
    @render.plot
    def humidity_plot():

        fig = humidity_graph(
            humidity_history.get(),
            dark_mode.get()
        )

        return fig

    @output
    @render.text
    def last_updated():

        return datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )

    @render.download(
        filename="sensor_report.xlsx"
    )
    def download_excel():

        import pandas as pd

        from openpyxl.styles import (
            Font,
            Alignment
        )

        location = input.location()

        data = sensor_values.get()

        if data["temp"] >= 38:
            weather = "High Temperature Conditions"

        elif data["temp"] >= 30:
            weather = "Warm & Dry Conditions"

        elif data["temp"] >= 24:
            weather = "Moderate Conditions"

        else:
            weather = "Cool & Humid Conditions"

        alerts_list = check_alerts(
            data["temp"],
            data["humidity"]
        )

        if alerts_list:
            alert_text = ", ".join(alerts_list)
        else:
            alert_text = "Normal"

        stats = calculate_stats(
            temp_history.get(),
            humidity_history.get()
        )

        timestamp = datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )

        df = pd.DataFrame({

            "Location": [location],

            "Temperature (°C)": [
                data["temp"]
            ],

            "Humidity (%)": [
                data["humidity"]
            ],

            "Environmental Conditions": [
                weather
            ],

            "Alerts": [
                alert_text
            ],

            "Average Temp (°C)": [
                stats["avg_temp"]
            ],

            "Average Humidity (%)": [
                stats["avg_humidity"]
            ],

            "Timestamp": [
                timestamp
            ]

        })

        with pd.ExcelWriter(
            "sensor_report.xlsx",
            engine="openpyxl"
        ) as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name="Sensor Report"
            )

            worksheet = writer.sheets[
                "Sensor Report"
            ]

            for row in worksheet.iter_rows():

                for cell in row:

                    cell.alignment = Alignment(
                        horizontal="left"
                    )

            for cell in worksheet[1]:

                cell.font = Font(
                    bold=True
                )

            for column_cells in worksheet.columns:

                max_length = 0

                column = column_cells[
                    0
                ].column_letter

                for cell in column_cells:

                    try:
                        if len(
                            str(cell.value)
                        ) > max_length:

                            max_length = len(
                                str(cell.value)
                            )

                    except:
                        pass

                adjusted_width = (
                    max_length + 5
                )

                worksheet.column_dimensions[
                    column
                ].width = adjusted_width

        with open(
            "sensor_report.xlsx",
            "rb"
        ) as f:

            yield f.read()


app = App(app_ui, server)
