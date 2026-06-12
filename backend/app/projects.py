from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project
from app.schemas import ProjectCreate

router = APIRouter()


# CREATE PROJECT
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


# GET ALL PROJECTS
@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db)
):
    return db.query(Project).all()


# GET PROJECT BY ID
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


# UPDATE PROJECT
@router.put("/projects/{project_id}")
def update_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    existing_project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not existing_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    existing_project.title = project.title
    existing_project.description = project.description

    db.commit()
    db.refresh(existing_project)

    return {
        "message": "Project updated successfully",
        "project": existing_project
    }


# DELETE PROJECT
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
