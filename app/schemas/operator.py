from pydantic import BaseModel
from typing import Optional


class OperatorCreate(BaseModel):
    name: str
    max_load: int = 5


class OperatorUpdate(BaseModel):
    is_active: Optional[bool] = None
    max_load: Optional[int] = None


class OperatorResponse(BaseModel):
    id: int
    name: str
    is_active: bool
    max_load: int

    class Config:
        from_attributes = True
