from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(db: Session, project_data: ProjectCreate, owner_id: int) -> Project:
    # owner_id comes in as a separate argument, NOT from project_data —
    # this is where we enforce "you can only create projects for yourself"

    new_project = Project(
        title=project_data.title,
        description=project_data.description,
        difficulty=project_data.difficulty,
        owner_id=owner_id,
        # status isn't set here — the model's default (not_started) applies
    )

    db.add(new_project)
    # stages the new row, doesn't hit the database yet

    db.commit()
    # actually writes it to the database

    db.refresh(new_project)
    # pulls back server-generated fields (id, created_at) so the object
    # we return actually has them filled in, not just None

    return new_project


def get_projects_for_user(db: Session, owner_id: int) -> list[Project]:
    # fetch only the logged-in user's own projects — never all projects
    # in the database, that would leak everyone's data to everyone
    return db.query(Project).filter(Project.owner_id == owner_id).all()