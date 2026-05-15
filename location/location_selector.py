from shiny import ui

def location_selector():

    return ui.card(

        ui.h3("Location Selector"),

        ui.input_select(
            "location",
            "Select Location",
            {
                
                "Pune": "Pune",
                "Hyderabad": "Hyderabad",
                "Bengaluru": "Bengaluru",
                "Chennai": "Chennai",
                "Mumbai": "Mumbai",
                "Delhi": "Delhi",
                "Kolkata": "Kolkata",
                "Ahmedabad": "Ahmedabad",
                "Guwahati": "Guwahati",
                "Jaipur": "Jaipur"
            
            }
        ),

        class_="custom-card"
    )
