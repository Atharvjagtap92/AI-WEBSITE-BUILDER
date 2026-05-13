import reflex as rx


def about_section(data):

    return rx.box(
        rx.heading(data.get("title")),
        rx.text(data.get("description")),
        padding="2rem"
    )