from fastapi import APIRouter, HTTPException
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
        "email": user.email,
        "password": user.password
    }

    fake_users.append(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }

@router.post("/login")
def login(user: UserLogin):

    found_user = next(
        (
            u for u in fake_users
            if u["username"] == user.username
            and u["password"] == user.password
        ),
        None
    )

    if not found_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

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
