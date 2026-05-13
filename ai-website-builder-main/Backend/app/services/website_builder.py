class WebsiteBuilder:

    @staticmethod
    def hero_section(data):

        return {
            "type": "hero",
            "headline": data.get("headline"),
            "subheadline": data.get("subheadline"),
            "buttonText": data.get("buttonText")
        }

    @staticmethod
    def about_section(data):

        return {
            "type": "about",
            "title": data.get("title"),
            "description": data.get("description")
        }

    @staticmethod
    def services_section(items):

        return {
            "type": "services",
            "items": items
        }

    @staticmethod
    def faq_section(items):

        return {
            "type": "faq",
            "items": items
        }

    @staticmethod
    def cta_section(data):

        return {
            "type": "cta",
            "headline": data.get("headline"),
            "buttonText": data.get("buttonText")
        }