import reflex as rx

from frontend.state.auth_state import AuthState


def login_page():

    return rx.center(

        rx.card(

            rx.vstack(

                rx.heading(
                    "Login",
                    size="7"
                ),

                rx.input(
                    placeholder="Email",
                    on_change=AuthState.set_email
                ),

                rx.input(
                    placeholder="Password",
                    type="password",
                    on_change=AuthState.set_password
                ),

                rx.button(
                    "Login",
                    on_click=AuthState.login
                ),

                spacing="4"
            ),

            width="400px",
            padding="2rem"
        ),

        height="100vh"
    )