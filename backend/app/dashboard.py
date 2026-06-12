from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Project

router = APIRouter()


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):
    total_users = db.query(User).count()
    total_projects = db.query(Project).count()

    return {
        "total_users": total_users,
        "total_projects": total_projects,
        "api_status": "healthy"
    }
