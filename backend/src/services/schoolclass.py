from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.dto.schoolclass import SchoolClassCreate, SchoolClassResponse
from src.models.schemas import SchoolClass
from typing import List


class SchoolClassService:
    async def _get_obj_by_id(self, id: int, session: AsyncSession) -> SchoolClass:
        res = await session.execute(select(SchoolClass).where(SchoolClass.id == id))
        obj = res.scalar_one_or_none()
        if obj is None:
            raise HTTPException(status_code=404, detail="class not found")
        return obj

    async def create(
        self, payload: SchoolClassCreate, session: AsyncSession
    ) -> SchoolClassResponse:
        data = payload.model_dump()
        obj = SchoolClass(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return SchoolClassResponse.model_validate(obj)

    async def get_all(self, session: AsyncSession) -> List[SchoolClassResponse]:
        res = await session.execute(select(SchoolClass).order_by(SchoolClass.id))
        objs = res.scalars().all()
        return [SchoolClassResponse.model_validate(obj) for obj in objs]

    async def retrieve(self, id: int, session: AsyncSession) -> SchoolClassResponse:
        obj = await self._get_obj_by_id(id=id, session=session)
        return SchoolClassResponse.model_validate(obj)
