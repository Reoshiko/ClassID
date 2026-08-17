from pydantic import BaseModel, ConfigDict
from src.models.schemas.absence import AbsenceStatus
from datetime import date


class AbsenceCreate(BaseModel):
    student_id: int
    reason: str
    date_from: date
    date_to: date


class AbsenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    student_id: int
    reason: str
    date_from: date
    date_to: date
    status: AbsenceStatus
