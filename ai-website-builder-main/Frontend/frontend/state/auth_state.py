import reflex as rx
import requests


class AuthState(rx.State):

    email: str = ""
    password: str = ""
    name: str = ""

    token: str = ""

    @rx.event
    def set_email(self, value: str):
        self.email = value

    @rx.event
    def set_password(self, value: str):
        self.password = value

    @rx.event
    def set_name(self, value: str):
        self.name = value

    async def signup(self):

        payload = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

        requests.post(
            "http://127.0.0.1:8001/auth/signup",
            json=payload
        )

    async def login(self):

        payload = {
            "email": self.email,
            "password": self.password
        }

        response = requests.post(
            "http://127.0.0.1:8001/auth/login",
            json=payload
        )

        data = response.json()

        self.token = data.get(
            "access_token",
            ""
        )