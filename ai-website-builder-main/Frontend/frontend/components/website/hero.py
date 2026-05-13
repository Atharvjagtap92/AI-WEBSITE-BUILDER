import reflex as rx


def hero_section(data):

    return rx.box(
        rx.heading(data.get("headline"), size="9"),
        rx.text(data.get("subheadline")),
        rx.button(data.get("buttonText")),
        padding="5rem",
        text_align="center"
    )