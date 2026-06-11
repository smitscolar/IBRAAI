from fastapi import APIRouter
from app.schemas import UserCreate, UserLogin
from app.auth import create_access_token

router = APIRouter()

fake_users = []

@router.get("/users")
def get_users():
    return fake_users

@router.post("/register")
def register(user: UserCreate):
    new_user = {
        "username": user.username,
        "email": user.email
    }

    fake_users.append(new_user)

    return {
        "message": "User registered successfully",
        "user": new_user
    }

@router.post("/login")
def login(user: UserLogin):
    token = create_access_token({
        "sub": user.username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/users/profile")
def profile():
    return {
        "username": "demo_user",
        "role": "user"
    }
