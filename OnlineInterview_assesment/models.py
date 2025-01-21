from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

    @validator("role")
    def validate_role(cls, v):
        if v not in ["user", "librarian"]:
            raise ValueError("Role must be either 'user' or 'librarian'")
        return v

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str

class BookCreate(BaseModel):
    title: str
    author: str

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    is_available: bool

    class Config:
        orm_mode = True

class BorrowRequest(BaseModel):
    book_id: int
    due_date: str