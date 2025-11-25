from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.lead import Lead
from app.schemas.lead import LeadIdentifiers


class LeadService:
    @staticmethod
    async def get_or_create_lead(
        db: AsyncSession, identifiers: LeadIdentifiers
    ) -> Lead:
        stmt = select(Lead).where(
            (Lead.email == identifiers.email)
            | (Lead.phone == identifiers.phone)
            | (Lead.external_id == identifiers.external_id)
        )
        result = await db.execute(stmt)
        lead: Optional[Lead] = result.scalar_one_or_none()

        if lead is None:
            lead = Lead(
                email=identifiers.email,
                phone=identifiers.phone,
                external_id=identifiers.external_id,
            )
            db.add(lead)
            await db.commit()
            await db.refresh(lead)
        return lead
