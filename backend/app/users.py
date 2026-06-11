from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.auth import create_access_token
from app.security import hash_password, verify_password

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        for user in users
    ]


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    found_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not found_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user.password,
        found_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token({
        "sub": found_user.username
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
