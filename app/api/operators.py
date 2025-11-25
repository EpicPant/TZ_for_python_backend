from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.operator import Operator
from app.schemas.operator import OperatorCreate, OperatorUpdate, OperatorResponse
from app.models.operator_source_config import OperatorSourceConfig
from app.models.source import Source
from sqlalchemy import select

router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("/", response_model=OperatorResponse)
async def create_operator(data: OperatorCreate, db: AsyncSession = Depends(get_db)):
    op = Operator(name=data.name, max_load=data.max_load)
    db.add(op)
    await db.commit()
    await db.refresh(op)
    return op


@router.get("/", response_model=list[OperatorResponse])
async def list_operators(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Operator))
    return result.scalars().all()


@router.patch("/{op_id}", response_model=OperatorResponse)
async def update_operator(
    op_id: int, data: OperatorUpdate, db: AsyncSession = Depends(get_db)
):
    op = await db.get(Operator, op_id)
    if not op:
        raise HTTPException(404, "Operator not found")
    if data.is_active is not None:
        op.is_active = data.is_active
    if data.max_load is not None:
        op.max_load = data.max_load
    await db.commit()
    await db.refresh(op)
    return op


@router.post("/assign-to-source", status_code=201)
async def assign_operator_to_source(
    operator_id: int,
    source_id: int,
    weight: int = 10,
    db: AsyncSession = Depends(get_db),
):
    # Проверим, что оператор и источник существуют
    op = await db.get(Operator, operator_id)
    src = await db.get(Source, source_id)
    if not op or not src:
        raise HTTPException(404, "Operator or Source not found")

    config = OperatorSourceConfig(
        operator_id=operator_id, source_id=source_id, weight=weight
    )
    db.add(config)
    await db.commit()
    return {"message": "Assigned successfully"}
