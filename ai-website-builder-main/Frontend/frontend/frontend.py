import reflex as rx

from frontend.pages.generator import generator_page


app = rx.App(

    theme=rx.theme(

        appearance="light",

        accent_color="violet",

        radius="large"
    )
)


app.add_page(

    generator_page,

    route="/"
)