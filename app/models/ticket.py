from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"), nullable=False)
    assigned_operator_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("operators.id"), nullable=True
    )
    status: Mapped[str] = mapped_column(
        String, default="open", nullable=False
    )  # ← String
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
