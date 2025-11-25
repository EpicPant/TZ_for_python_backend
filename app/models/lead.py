from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]] = mapped_column(String, index=True, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, index=True, nullable=True)
    external_id: Mapped[Optional[str]] = mapped_column(
        String, index=True, nullable=True
    )
