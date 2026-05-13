import reflex as rx


def project_card(project):

    return rx.card(

        rx.vstack(

            rx.heading(project["project_name"]),

            rx.text(
                f"Project ID: {project['id']}"
            ),

            rx.button("Open Project")
        ),

        width="300px",
        padding="1rem"
    )