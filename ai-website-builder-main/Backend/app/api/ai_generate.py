from fastapi import APIRouter

from app.core.gemini import model

import json


router = APIRouter()


@router.post("/generate")
async def generate_website(data: dict):

    business_name = data.get(
        "business_name",
        "Business"
    )

    prompt = f"""

    Create a modern business website structure.

    Business Name:
    {business_name}

    Return ONLY valid JSON.

    JSON format:

    {{
      "sections": [

        {{
          "type": "hero",
          "title": "title",
          "subtitle": "subtitle"
        }},

        {{
          "type": "about",
          "content": "about content"
        }},

        {{
          "type": "services",
          "items": [
            "service1",
            "service2",
            "service3"
          ]
        }},

        {{
          "type": "cta",
          "title": "cta title"
        }}

      ]
    }}

    """

    try:

        response = model.generate_content(
            prompt
        )

        text = response.text

        # REMOVE MARKDOWN

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        text = text.strip()

        result = json.loads(text)

        return result

    except Exception as e:

        print("GEMINI ERROR:")
        print(e)

        # FALLBACK DATA

        return {

            "sections": [

                {
                    "type": "hero",
                    "title": f"Welcome to {business_name}",
                    "subtitle": "AI Generated Website"
                },

                {
                    "type": "about",
                    "content": "Professional business website generated using AI."
                },

                {
                    "type": "services",
                    "items": [
                        "Web Design",
                        "AI Solutions",
                        "Business Growth"
                    ]
                },

                {
                    "type": "cta",
                    "title": "Start Your Journey Today"
                }
            ]
        }