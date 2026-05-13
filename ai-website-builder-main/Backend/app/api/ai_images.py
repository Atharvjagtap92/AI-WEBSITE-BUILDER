from fastapi import APIRouter
from app.services.image_service import generate_business_images

router = APIRouter(
    prefix="/ai-images",
    tags=["AI Images"]
)


@router.post("/generate")
async def generate_images(data: dict):

    images = await generate_business_images(data)

    return {
        "success": True,
        "images": images
    }