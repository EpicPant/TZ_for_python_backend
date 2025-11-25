from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadResponse
from sqlalchemy import select

router = APIRouter(prefix="/leads", tags=["leads"])


@router.get("/", response_model=list[LeadResponse])
async def get_leads(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Lead))
    return result.scalars().all()
