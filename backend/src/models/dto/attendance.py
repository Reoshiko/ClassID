from src.models.schemas.attendance import AttendanceEventType, AttendanceSource
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class AttendanceCreate(BaseModel):
    student_id: int
    event_type: AttendanceEventType
    source: AttendanceSource


class AttendanceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    student_id: int
    event_type: AttendanceEventType
    source: AttendanceSource
    created_at: datetime
