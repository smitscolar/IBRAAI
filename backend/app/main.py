from fastapi import FastAPI

from app.database import Base, engine

from app.users import router as users_router
from app.projects import router as projects_router
from app.dashboard import router as dashboard_router
from app.uploads import router as uploads_router
from app.analyze import router as analyze_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IBRAAI API",
    description="Intelligent Business Research and Artificial Intelligence Platform",
    version="1.0.0"
)

# Routers
app.include_router(users_router)
app.include_router(projects_router)
app.include_router(dashboard_router)
app.include_router(uploads_router)
app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IBRAAI API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/about")
def about():
    return {
        "name": "IBRAAI",
        "version": "1.0.0",
        "description": "Business Intelligence & AI Platform"
    }
