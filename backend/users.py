from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {
        "message": "IBRAAI User Service"
    }

@router.get("/users/profile")
def profile():
    return {
        "username": "demo_user",
        "role": "user"
    }
