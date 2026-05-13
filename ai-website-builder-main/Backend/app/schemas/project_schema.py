from pydantic import BaseModel
from typing import Dict


class ProjectCreate(BaseModel):
    project_name: str
    website_json: Dict