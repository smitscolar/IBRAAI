from fastapi import FastAPI

from app.database import Base, engine
from app.users import router as users_router
from app.projects import router as projects_router

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
        "description": "Intelligent Business Research and Artificial Intelligence Platform"
    }
