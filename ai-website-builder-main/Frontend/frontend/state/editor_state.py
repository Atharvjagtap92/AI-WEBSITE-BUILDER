import reflex as rx
import requests

from typing import List


class EditorState(rx.State):

    business_name: str = ""

    loading: bool = False

    sections: List[str] = []

    @rx.event
    def set_business_name(
        self,
        value: str
    ):

        self.business_name = value

    @rx.event
    async def generate_website(self):

        self.loading = True

        try:

            response = requests.post(

                "http://127.0.0.1:8001/ai/generate",

                json={

                    "business_name": self.business_name
                }
            )

            # ---------- SAFE JSON ----------

            try:

                data = response.json()

            except Exception as e:

                print("JSON ERROR:")
                print(e)

                self.loading = False

                return

            # ---------- CLEAR OLD DATA ----------

            self.sections = []

            # ---------- LOOP THROUGH AI SECTIONS ----------

            for section in data["sections"]:

                # HERO SECTION

                if section["type"] == "hero":

                    hero_data = (
                        f"HERO|"
                        f"{section['title']}|"
                        f"{section['subtitle']}"
                    )

                    self.sections.append(
                        hero_data
                    )

                # ABOUT SECTION

                elif section["type"] == "about":

                    about_data = (
                        f"ABOUT|"
                        f"{section['content']}"
                    )

                    self.sections.append(
                        about_data
                    )

                # SERVICES SECTION

                elif section["type"] == "services":

                    services = ",".join(
                        section["items"]
                    )

                    services_data = (
                        f"SERVICES|{services}"
                    )

                    self.sections.append(
                        services_data
                    )

                # CTA SECTION

                elif section["type"] == "cta":

                    cta_data = (
                        f"CTA|"
                        f"{section['title']}"
                    )

                    self.sections.append(
                        cta_data
                    )

        except Exception as e:

            print("REQUEST ERROR:")
            print(e)

        self.loading = False