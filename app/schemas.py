from pydantic import BaseModel, EmailStr
from datetime import datetime

class FormBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class FormCreate(FormBase):
    pass

class FormOut(FormBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
