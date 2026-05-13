import reflex as rx


def services_section(data):

    return rx.box(
        rx.foreach(
            data.get("items", []),
            lambda item: rx.card(
                rx.heading(item["title"]),
                rx.text(item["description"])
            )
        )
    )