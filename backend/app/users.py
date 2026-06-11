from fastapi import APIRouter

router = APIRouter()

fake_users = []

@router.get("/users")
def get_users():
    return fake_users

@router.post("/register")
def register(username: str, email: str):
    user = {
        "username": username,
        "email": email
    }

    fake_users.append(user)

    return {
        "message": "User registered",
        "user": user
    }

@router.get("/users/profile")
def profile():
    return {
        "username": "demo_user",
        "role": "user"
    }
