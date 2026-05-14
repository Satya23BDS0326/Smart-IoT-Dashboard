from shiny import ui

def location_selector():

    return ui.card(

        ui.h3("Location Selector"),

        ui.input_select(
            "location",
            "Select Location",
            {
                "Vijayawada": "Vijayawada",
                "Hyderabad": "Hyderabad",
                "Chennai": "Chennai",
                "Bangalore": "Bangalore"
            }
        ),

        class_="custom-card"
    )