import reflex as rx


def navbar():

    return rx.hstack(

        rx.heading("AI Website Builder"),

        rx.spacer(),

        rx.link("Dashboard", href="/dashboard"),

        rx.link("Generator", href="/"),

        rx.link("Editor", href="/editor"),

        padding="1rem",

        border_bottom="1px solid #e5e7eb"
    )