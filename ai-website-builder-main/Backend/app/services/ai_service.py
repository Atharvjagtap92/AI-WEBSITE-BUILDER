import json

from app.core.gemini import model


async def generate_website(data):

    prompt = f"""
    Generate website content in JSON format.

    Business Name: {data['business_name']}
    Industry: {data['industry']}
    Services: {data['services']}
    Audience: {data['audience']}
    Tone: {data['tone']}

    Return valid JSON only.

    Structure:
    {{
        "theme": {{
            "primaryColor": "",
            "font": ""
        }},
        "sections": [
            {{
                "type": "hero",
                "headline": "",
                "subheadline": "",
                "buttonText": ""
            }},
            {{
                "type": "about",
                "title": "",
                "description": ""
            }},
            {{
                "type": "services",
                "items": []
            }},
            {{
                "type": "faq",
                "items": []
            }},
            {{
                "type": "cta",
                "headline": ""
            }}
        ]
    }}
    """

    response = model.generate_content(prompt)

    cleaned = response.text.replace("```json", "").replace("```", "")

    return json.loads(cleaned)