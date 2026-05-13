from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.project import Project
from app.db.session import get_db
from app.schemas.project_schema import ProjectCreate

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):

    project = Project(
        project_name=data.project_name,
        website_json=data.website_json,
        user_id=1
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@router.get("/")
def get_projects(db: Session = Depends(get_db)):

    return db.query(Project).all()