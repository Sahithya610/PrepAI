from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime

#object.model_dump()
#object.model_dump_json(indent=2)
#pydantic has default type conversion
#Field(default_factory=list)
class UserCreate(BaseModel):
    email : EmailStr
    username : str = Field(..., min_length=3, max_length=50)
    password : str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    username : str
    created_at : datetime

#session schemas
class SessionCreate(BaseModel):
    title : str
    role : str
    difficulty : str

class SessionUpdate(BaseModel):
    title : str | None = None
    role : str | None = None
    difficulty : str | None = None

class SessionResponse(BaseModel):
    id : int
    user_id : int
    title : str
    role : str
    difficulty : str
    status : str
    created_at : datetime

class QuestionCreate(BaseModel):
    question_text : str

class QuestionWithAnswer(BaseModel):
    question_text : str
    user_answer: str

class QuestionResponse(BaseModel):
    question_text : str
    user_answer : str
    ai_feedback : str
    score : int

class Token(BaseModel):
    access_token : int
    token_type : str

class TokenData(BaseModel):
    email : EmailStr
