from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services.ticket_service import TicketService

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/", response_model=TicketResponse)
async def create_ticket(ticket_data: TicketCreate, db: AsyncSession = Depends(get_db)):
    try:
        ticket = await TicketService.create_ticket(
            db=db,
            lead_identifiers=ticket_data.lead_identifiers,
            source_id=ticket_data.source_id,
        )
        return ticket
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
