import reflex as rx


def layout_editor():

    return rx.vstack(

        rx.heading("Layout Settings"),

        rx.select(
            ["Centered", "Split", "Grid"]
        ),

        rx.slider(default_value=[10]),

        width="100%"
    )