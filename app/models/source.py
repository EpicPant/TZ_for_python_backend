from sqlalchemy import String  # ← обязательно!
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
