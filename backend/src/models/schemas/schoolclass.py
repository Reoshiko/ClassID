from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base


class SchoolClass(Base):
    __tablename__ = "school_classes"

    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    students: Mapped[list["Student"]] = relationship(
        back_populates="school_class", cascade="all, delete-orphan"
    )
