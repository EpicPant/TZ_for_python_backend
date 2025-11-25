from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .operator import Operator
    from .source import Source


class OperatorSourceConfig(Base):
    __tablename__ = "operator_source_configs"
    __table_args__ = (
        UniqueConstraint("operator_id", "source_id", name="uq_operator_source"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id"), nullable=False)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"), nullable=False)
    weight: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
