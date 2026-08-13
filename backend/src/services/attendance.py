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

    async def get_last_school_event(
        self, student_id: int, session: AsyncSession
    ) -> AttendanceEvent | None:
        res = await session.execute(
            select(Student)
            .where(
                Student.id == student_id,
                AttendanceEvent.event_type.in_(
                    AttendanceEventType.SCHOOL_ENTER, AttendanceEventType.SCHOOL_EXIT
                ),
            )
            .order_by(AttendanceEvent.created_at.desc())
            .limit(1)
        )
        return res.scalar_one_or_none()

    async def create_school_event(
        self, student_id: int, session: AsyncSession
    ) -> AttendanceResponse:
        obj = await session.scalar(select(Student).where(Student.id == student_id))
        if obj is None:
            raise HTTPException(status_code=404, detail="student not found")
        last_event = await self.get_last_school_event(
            student_id=student_id, session=session
        )
        if (
            last_event is None
            or last_event.event_type == AttendanceEventType.SCHOOL_EXIT
        ):
            event_type = AttendanceEventType.SCHOOL_ENTER
        else:
            event_type = AttendanceEventType.SCHOOL_EXIT

        payload = AttendanceCreate(
            student_id=student_id,
            event_type=event_type,
            source=AttendanceSource.SCANNER,
        )

        return await self.create(payload=payload, session=session)
