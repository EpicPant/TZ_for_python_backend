from sqlalchemy.ext.asyncio import AsyncSession
from app.models.ticket import Ticket
from app.schemas.lead import LeadIdentifiers
from app.services.lead_service import LeadService
from app.services.operator_service import OperatorService
from app.services.assignment_service import AssignmentService
from app.models.source import Source


class TicketService:
    @staticmethod
    async def create_ticket(
        db: AsyncSession, lead_identifiers: LeadIdentifiers, source_id: int
    ) -> Ticket:
        source = await db.get(Source, source_id)
        if not source:
            raise ValueError("Source not found")

        lead = await LeadService.get_or_create_lead(db, lead_identifiers)
        candidates = await OperatorService.get_available_operators_for_source(
            db, source_id
        )
        operator = AssignmentService.select_operator_weighted(candidates)

        ticket = Ticket(
            lead_id=lead.id,
            source_id=source_id,
            assigned_operator_id=operator.id if operator else None,
            status="open",
        )
        db.add(ticket)
        await db.commit()
        await db.refresh(ticket)
        return ticket
