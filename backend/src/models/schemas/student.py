from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from .base import Base
import uuid


class Student(Base):
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=False)
    middle_name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    class_id: Mapped[int] = mapped_column(
        ForeignKey("school_classes.id", ondelete="CASCADE"), nullable=False
    )
    qr_token: Mapped[str] = mapped_column(
        String(36),
        unique=True,
        index=True,
        nullable=False,
        default=lambda: str(uuid.uuid4()),
    )
    school_class: Mapped["SchoolClass"] = relationship(back_populates="students")
    attendance_events: Mapped[list["AttendanceEvent"]] = relationship(
        back_populates="student", cascade="all, delete-orphan"
    )
