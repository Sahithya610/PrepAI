from pydantic import BaseModel, ValidationError, Field, EmailStr
from datetime import datetime
from enum import Enum
import uuid
from uuid import UUID

#object.model_dump()
#object.model_dump_json(indent=2)
#pydantic has default type conversion
#Field(default_factory=list)

class DifficultyEnum(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

#session schemas
class SessionCreate(BaseModel):
    title : str = Field(..., min_length=3, max_length=100)
    role : str = Field(..., example="Backend Engineer")
    difficulty : DifficultyEnum = DifficultyEnum.medium

class SessionUpdate(BaseModel):
    title : str | None = None
    role : str | None = None
    difficulty : str | None = None

class SessionResponse(BaseModel):
    id : UUID
    title : str
    role : str
    difficulty : DifficultyEnum
    status : str
    created_at : datetime

    model_config = {"from_attributes": True}
