from sqlalchemy import Column, Integer, JSON, String, ForeignKey
from app.db.database import Base


class Website(Base):

    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    website_json = Column(JSON)

    theme = Column(JSON)

    seo_data = Column(JSON)

    status = Column(String(50), default="draft")