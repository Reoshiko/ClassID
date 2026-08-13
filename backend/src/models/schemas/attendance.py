from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, String, func, Enum as SQLEnum
from .base import Base
from datetime import datetime
from enum import Enum


class AttendanceEventType(str, Enum):
    SCHOOL_ENTER = "school_enter"
    SCHOOL_EXIT = "school_exit"
    LESSON_PRESENT = "lesson_present"
    BOARDING_PRESENT = "boarding_present"


class AttendanceSource(str, Enum):
    CAMERA = "camera"
    TEACHER = "teacher"
    SCANNER = "scanner"


class AttendanceEvent(Base):
    __tablename__ = "attendance_events"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"), nullable=False, index=True
    )
    event_type: Mapped[AttendanceEventType] = mapped_column(
        SQLEnum(AttendanceEventType), nullable=False
    )
    source: Mapped[AttendanceSource] = mapped_column(
        SQLEnum(AttendanceSource), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False, index=True
    )
    student: Mapped["Student"] = relationship(back_populates="attendance_events")
