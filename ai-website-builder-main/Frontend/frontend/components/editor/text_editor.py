import reflex as rx


def text_editor(label: str, value: str):

    return rx.vstack(

        rx.text(label),

        rx.text_area(
            value=value,
            width="100%"
        )
    )