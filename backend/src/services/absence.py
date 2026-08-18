from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.dto.absence import AbsenceCreate, AbsenceResponse
from src.models.schemas import AbsenceRequest, Student
from src.models.schemas.absence import AbsenceStatus
from typing import List


class AbsenceService:
    async def create(
        self, payload: AbsenceCreate, session: AsyncSession
    ) -> AbsenceResponse:
        student = await session.scalar(
            select(Student).where(Student.id == payload.student_id)
        )
        if student is None:
            raise HTTPException(status_code=404, detail="student not found")
        data = payload.model_dump()
        obj = AbsenceRequest(**data, status=AbsenceStatus.PENDING)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return AbsenceResponse.model_validate(obj)

    async def get_all(self, session: AsyncSession) -> List[AbsenceResponse]:
        res = await session.execute(
            select(AbsenceRequest).order_by(AbsenceRequest.id.desc())
        )
        objs = await res.scalars().all()
        return [AbsenceResponse.model_validate(obj) for obj in objs]

    async def set_status(
        self, id: int, status: AbsenceStatus, session: AsyncSession
    ) -> AbsenceResponse:
        obj = await session.scalar(
            select(AbsenceRequest).where(AbsenceRequest.id == id)
        )
        if obj is None:
            raise HTTPException(status_code=404, detail="absence request not found")
        obj.status = status
        await session.commit()
        await session.refresh(obj)
        return AbsenceResponse.model_validate(obj)
