from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .lead import LeadIdentifiers


class TicketCreate(BaseModel):
    lead_identifiers: LeadIdentifiers
    source_id: int
    content: Optional[str] = None


class TicketResponse(BaseModel):
    id: int
    lead_id: int
    source_id: int
    assigned_operator_id: Optional[int]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
