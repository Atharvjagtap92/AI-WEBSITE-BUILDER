import reflex as rx


def faq_section(data):

    return rx.box(
        rx.foreach(
            data.get("items", []),
            lambda item: rx.accordion.root(
                rx.accordion.item(
                    header=item["question"],
                    content=item["answer"]
                )
            )
        )
    )