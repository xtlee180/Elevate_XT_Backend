from datetime import datetime
from pydantic import BaseModel
from app.models.project import DifficultyLevel, ProjectStatus


class ProjectCreate(BaseModel):
    # defines what a user is ALLOWED to send in POST /projects
    title: str
    # required — request fails with 422 if missing
    description: str | None = None
    # optional (can be left out or null)
    difficulty: DifficultyLevel = DifficultyLevel.beginner
    # optional, defaults to beginner, must be one of the 3 valid values

    # no owner_id, status, or id here on purpose —
    # those are set by the server, not the user

class ProjectResponse(BaseModel):
    # defines what the API sends BACK to the client
    id: int
    title: str
    description: str | None
    difficulty: DifficultyLevel
    status: ProjectStatus
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
        # lets this schema build itself from a SQLAlchemy object directly