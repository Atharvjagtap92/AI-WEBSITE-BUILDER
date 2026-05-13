from pydantic import BaseModel
from typing import List, Dict


class WebsiteGenerateSchema(BaseModel):

    business_name: str
    industry: str
    services: List[str]
    audience: str
    tone: str


class WebsiteSaveSchema(BaseModel):

    project_name: str
    website_json: Dict