from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.dto.schoolclass import SchoolClassCreate, SchoolClassResponse
from src.models.schemas import SchoolClass
from typing import List


class SchoolClassService:
    async def create(
        self, payload: SchoolClassCreate, session: AsyncSession
    ) -> SchoolClassResponse:
        data = payload.model_dump()
        obj = SchoolClass(**data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession) -> List[SchoolClassResponse]:
        res = await session.execute(select(SchoolClass).order_by(SchoolClass.id))
        objs = res.scalars().all()
        return [SchoolClassResponse.model_validate(obj) for obj in objs]
