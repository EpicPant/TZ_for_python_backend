from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.source import Source
from app.schemas.source import SourceCreate, SourceResponse
from sqlalchemy import select

router = APIRouter(prefix="/sources", tags=["sources"])


@router.post("/", response_model=SourceResponse)
async def create_source(data: SourceCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(Source).where(Source.name == data.name))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Source already exists")
    source = Source(name=data.name)
    db.add(source)
    await db.commit()
    await db.refresh(source)
    return source


@router.get("/", response_model=list[SourceResponse])
async def list_sources(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Source))
    return result.scalars().all()
