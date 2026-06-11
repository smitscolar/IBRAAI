from fastapi import FastAPI
from app.users import router as users_router
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IBRAAI API",
    version="1.0.0",
    description="Intelligent Business Research and Artificial Intelligence Platform"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {
        "platform": "IBRAAI",
        "version": "1.0.0",
        "status": "running"
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
        "description": "Intelligent Business Research and Artificial Intelligence Platform",
        "type": "Multi-Agent AI Ecosystem"
    }
