import reflex as rx

from frontend.state.editor_state import EditorState


# ---------- HERO ----------

def hero_section(section):

    parts = section.split("|")

    title = parts[1]

    subtitle = parts[2]

    return rx.box(

        rx.vstack(

            rx.heading(
                title,
                size="9",
                color="white"
            ),

            rx.text(
                subtitle,
                size="5",
                color="#CBD5E1"
            ),

            rx.button(
                "Get Started",
                color_scheme="violet",
                size="4"
            ),

            spacing="5",
            align="center"
        ),

        background="linear-gradient(135deg,#111827 0%,#4F46E5 100%)",

        padding="6rem",

        border_radius="24px",

        width="100%"
    )


# ---------- ABOUT ----------

def about_section(section):

    content = section.split("|")[1]

    return rx.box(

        rx.vstack(

            rx.heading(
                "About Us",
                size="8"
            ),

            rx.text(
                content,
                color="gray",
                size="4"
            ),

            spacing="4",
            align="start"
        ),

        background="white",

        padding="3rem",

        border_radius="24px",

        width="100%"
    )


# ---------- SERVICES ----------

def services_section(section):

    content = section.split("|")[1]

    return rx.box(

        rx.vstack(

            rx.heading(
                "Our Services",
                size="8"
            ),

            rx.text(
                content,
                color="gray",
                size="5"
            ),

            spacing="4",
            align="start"
        ),

        background="white",

        padding="3rem",

        border_radius="24px",

        width="100%"
    )


# ---------- CTA ----------

def cta_section(section):

    title = section.split("|")[1]

    return rx.box(

        rx.vstack(

            rx.heading(
                title,
                size="8",
                color="white"
            ),

            rx.button(
                "Contact Us",
                color_scheme="violet",
                size="4"
            ),

            spacing="5",
            align="center"
        ),

        background="#111827",

        padding="5rem",

        border_radius="24px",

        width="100%"
    )


# ---------- MAIN PAGE ----------

def generator_page():

    return rx.box(

        rx.vstack(

            rx.heading(
                "AI Website Builder",
                size="9"
            ),

            rx.text(
                "Generate websites dynamically using Gemini AI",
                color="gray",
                size="5"
            ),

            rx.hstack(

                rx.input(

                    placeholder="Enter Business Name",

                    width="500px",

                    on_change=EditorState.set_business_name
                ),

                rx.button(

                    "Generate Website",

                    loading=EditorState.loading,

                    color_scheme="violet",

                    on_click=EditorState.generate_website
                ),

                spacing="4"
            ),

            rx.foreach(

                EditorState.sections,

                lambda section:

                rx.cond(

                    section.contains("HERO"),

                    hero_section(section),

                    rx.cond(

                        section.contains("ABOUT"),

                        about_section(section),

                        rx.cond(

                            section.contains("SERVICES"),

                            services_section(section),

                            cta_section(section)
                        )
                    )
                )
            ),

            spacing="8",

            width="100%",

            max_width="1400px"
        ),

        background="#F1F5F9",

        min_height="100vh",

        padding="3rem"
    )