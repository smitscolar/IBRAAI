from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project
from app.schemas import ProjectCreate

router = APIRouter()


@router.post("/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    new_project = Project(
        title=project.title,
        description=project.description
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db)
):
    return db.query(Project).all()


@router.get("/projects/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted"
    }
