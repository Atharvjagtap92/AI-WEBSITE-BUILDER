async def generate_business_images(data):

    business_name = data.get("business_name")
    industry = data.get("industry")

    images = [
        {
            "title": f"{business_name} Banner",
            "url": "https://placehold.co/1200x600"
        },
        {
            "title": f"{industry} Service Image",
            "url": "https://placehold.co/600x400"
        }
    ]

    return images