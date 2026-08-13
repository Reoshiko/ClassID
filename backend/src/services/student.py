from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.dto.student import StudentCreate, StudentResponse
from src.models.schemas import Student
from typing import List


class StudentService:
    async def _get_obj_by_id(self, id: int, session: AsyncSession) -> Student:
        res = await session.execute(select(Student).where(Student.id == id))
        obj = res.scalar_one_or_none()
        if obj is None:
            raise HTTPException(status_code=404, detail="student not found")
        return obj

    async def create(
        self, payload: StudentCreate, session: AsyncSession
    ) -> StudentResponse:
        data = payload.model_dump()
        obj = Student(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession) -> List[StudentResponse]:
        res = await session.execute(select(Student).order_by(Student.id))
        objs = res.scalars().all()
        return [StudentResponse.model_validate(obj) for obj in objs]

    async def retrieve(self, id: int, session: AsyncSession) -> StudentResponse:
        obj = await self._get_obj_by_id(id=id, session=session)
        return StudentResponse.model_validate(obj)

    async def get_qr_token(self, id: int, session: AsyncSession):
        obj = await self._get_obj_by_id(id=id, session=session)
        return obj.qr_token
