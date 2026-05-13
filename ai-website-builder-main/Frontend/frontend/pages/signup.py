import reflex as rx

from frontend.state.auth_state import AuthState


def signup_page():

    return rx.center(

        rx.card(

            rx.vstack(

                rx.heading(
                    "Signup",
                    size="7"
                ),

                rx.input(
                    placeholder="Name",
                    on_change=AuthState.set_name
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
                    "Signup",
                    on_click=AuthState.signup
                ),

                spacing="4"
            ),

            width="400px",
            padding="2rem"
        ),

        height="100vh"
    )