from fastapi import FastAPI
from app.users import router as users_router

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
