from pydantic import BaseModel
from typing import Optional


class LeadIdentifiers(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    external_id: Optional[str] = None


class LeadResponse(BaseModel):
    id: int
    email: Optional[str]
    phone: Optional[str]
    external_id: Optional[str]

    class Config:
        from_attributes = True
