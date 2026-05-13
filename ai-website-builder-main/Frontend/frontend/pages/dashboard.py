import reflex as rx

from frontend.state.project_state import ProjectState


def dashboard_page():

    return rx.container(

        rx.vstack(

            rx.heading(
                "Dashboard",
                size="8"
            ),

            rx.foreach(

                ProjectState.projects,

                lambda project: rx.card(

                    rx.text(
                        project.to(dict)["project_name"]
                    ),

                    width="100%"
                )
            ),

            spacing="4"
        ),

        padding="2rem"
    )