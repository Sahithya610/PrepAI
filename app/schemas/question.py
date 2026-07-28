from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Optional

class QuestionCreate(BaseModel):
    question_text : str

class QuestionWithAnswer(BaseModel):
    question_text : str
    user_answer: str

class QuestionResponse(BaseModel):
    id : UUID
    session_id : UUID
    question_text : str
    user_answer : Optional[str] = None
    ai_feedback : Optional[str] = None
    score : Optional[int] = None
    created_at : datetime
    model_config = {"from_attributes": True}

class SubmitAnswer(BaseModel):
    user_answer: str