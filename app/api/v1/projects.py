from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import create_project, get_projects_for_user

router = APIRouter(prefix="/projects", tags=["Projects"])
# prefix means every route below is under /projects — e.g. "" becomes POST /projects


@router.post("/", response_model=ProjectResponse)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    # this is the SAME dependency your /auth/me route already uses —
    # it reads the JWT from the request header and returns the real,
    # logged-in User row. If there's no valid token, this rejects
    # the request with 401 before your function body even runs.
):
    return create_project(db, project, owner_id=current_user.id)
    # current_user.id comes from the verified token, not from the request
    # body — this is the actual enforcement point we talked about earlier


@router.get("/", response_model=list[ProjectResponse])
def list_my_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_projects_for_user(db, owner_id=current_user.id)
    # only ever returns THIS user's projects, never everyone's