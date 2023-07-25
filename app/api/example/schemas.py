from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ExampleCreateSchema(BaseModel):
    id: Optional[UUID] = None
    name: str
    active: bool

    class Config:
        from_attributes = True #formerly orm_mode


class ExampleSchema(ExampleCreateSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
