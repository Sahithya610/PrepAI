from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime
from uuid import UUID

class UserCreate(BaseModel):
    email : EmailStr
    username : str = Field(..., min_length=3, max_length=50)
    password : str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : UUID
    email : EmailStr
    username : str
    created_at : datetime

    model_config = {"from_attributes": True}