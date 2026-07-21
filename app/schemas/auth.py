from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : EmailStr