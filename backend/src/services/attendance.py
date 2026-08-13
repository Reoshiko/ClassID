from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.dto.attendance import AttendanceCreate, AttendanceResponse
from src.models.schemas import AttendanceEvent, Student
from src.models.schemas.attendance import AttendanceEventType, AttendanceSource
from typing import List


class AttendanceService:
    async def create(
        self, payload: AttendanceCreate, session: AsyncSession
    ) -> AttendanceResponse:
        student = await session.scalar(
            select(Student).where(Student.id == payload.student_id)
        )
        if student is None:
            raise HTTPException(status_code=404, detail="student not found")
        data = payload.model_dump()
        obj = AttendanceEvent(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return AttendanceResponse.model_validate(obj)

    async def get_all(self, session: AsyncSession) -> List[AttendanceResponse]:
        res = await session.execute(
            select(AttendanceEvent).order_by(AttendanceEvent.id)
        )
        objs = res.scalars().all()
        return [AttendanceResponse.model_validate(obj) for obj in objs]
