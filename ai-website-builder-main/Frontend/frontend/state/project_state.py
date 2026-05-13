import reflex as rx
import requests
from typing import List, Dict


class ProjectState(rx.State):

    projects: List[Dict] = []

    @rx.event
    async def load_projects(self):

        response = requests.get(
            "http://127.0.0.1:8001/projects/"
        )

        self.projects = response.json()