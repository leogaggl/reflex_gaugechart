"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from reflex_gaugechart import Gaugechart
from rxconfig import config
import reflex as rx


filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    nr_of_levels = rx.Var.create(5)
    percent_value = rx.Var.create(0.6)
    pass

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Test your custom component by editing ",
                rx.code(filename),
                font_size="2em",
            ),
            Gaugechart(id="test_chart_01", nrOfLevels=State.nr_of_levels, percent=State.percent_value),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
