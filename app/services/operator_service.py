from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from app.models.operator import Operator
from app.models.operator_source_config import OperatorSourceConfig
from app.models.ticket import Ticket
from typing import List, Tuple


class OperatorService:
    @staticmethod
    async def get_available_operators_for_source(
        db: AsyncSession, source_id: int
    ) -> List[Tuple[Operator, int]]:
        active_count_subq = (
            select(Ticket.assigned_operator_id, func.count().label("active_count"))
            .where(Ticket.status == "open")
            .group_by(Ticket.assigned_operator_id)
            .subquery()
        )

        stmt = (
            select(
                Operator, OperatorSourceConfig.weight, active_count_subq.c.active_count
            )
            .join(OperatorSourceConfig, Operator.id == OperatorSourceConfig.operator_id)
            .join(
                active_count_subq,
                active_count_subq.c.assigned_operator_id == Operator.id,
                isouter=True,
            )
            .where(
                and_(
                    Operator.is_active == True,
                    OperatorSourceConfig.source_id == source_id,
                )
            )
        )

        result = await db.execute(stmt)
        rows = result.all()

        available = []
        for op, weight, active_count in rows:
            current_load = active_count or 0
            if current_load < op.max_load:
                available.append((op, weight))
        return available
