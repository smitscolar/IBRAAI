from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class UserLogin(BaseModel):
    username: str
