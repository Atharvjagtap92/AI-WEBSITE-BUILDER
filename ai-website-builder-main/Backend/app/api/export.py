from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.export_service import export_website_zip

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.post("/{project_id}")
def export_project(project_id: int):

    zip_path = export_website_zip(project_id)

    return FileResponse(
        path=zip_path,
        filename="website.zip",
        media_type="application/zip"
    )