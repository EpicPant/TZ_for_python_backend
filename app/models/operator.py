from sqlalchemy import Boolean, Integer, String  # ← добавь String здесь!
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Operator(Base):
    __tablename__ = "operators"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String, index=True, nullable=False
    )  # Теперь String определён
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    max_load: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
