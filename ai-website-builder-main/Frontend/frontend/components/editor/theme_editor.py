import reflex as rx


def theme_editor():

    return rx.vstack(

        rx.heading("Theme Settings"),

        rx.input(type="color"),

        rx.select(
            ["Inter", "Roboto", "Poppins"]
        )
    )