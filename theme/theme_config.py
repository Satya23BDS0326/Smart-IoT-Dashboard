from shiny import ui

def theme_toggle(dark_mode=False):

    icon = "🌙" if dark_mode else "☀️"

    return ui.div(

        ui.input_action_button(
            "theme_btn",
            icon,
            class_="theme-toggle-btn"
        ),

        style="""
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        """
    )