import reflex as rx

from frontend.state.editor_state import EditorState


def editor_page():

    return rx.container(

        rx.vstack(

            rx.heading(
                "Website Editor",
                size="8"
            ),

            rx.foreach(

                EditorState.sections,

                lambda section: rx.card(

                    rx.text(
                        section.to(dict)["type"]
                    ),

                    width="100%"
                )
            ),

            spacing="4"
        ),

        padding="2rem"
    )