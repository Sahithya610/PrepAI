from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime

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

    model_config = {"from attributes": True}