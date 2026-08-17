from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, String, Enum as SQLEnum
from datetime import date
from enum import Enum
from .base import Base


class AbsenceStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AbsenceRequest(Base):
    __tablename__ = "absence_requests"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"), nullable=False, index=True
    )
    reason: Mapped[str] = mapped_column(String(255), nullable=False)
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[AbsenceStatus] = mapped_column(
        SQLEnum(AbsenceStatus), nullable=False, default=AbsenceStatus.PENDING
    )
    student: Mapped["student"] = relationship()
