from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.absence import AbsenceCreate, AbsenceResponse
from src.models.schemas.absence import AbsenceStatus
from src.core.database import get_session
from src.dependencies import get_absenceservice

router = APIRouter()


@router.post("/", response_model=AbsenceResponse)
async def create(
    payload: AbsenceCreate,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_absenceservice),
):
    return await repo.create(payload=payload, session=session)


@router.get("/", response_model=list[AbsenceResponse])
async def get_all(
    session: AsyncSession = Depends(get_session), repo=Depends(get_absenceservice)
):
    return await repo.get_all(session=session)


@router.patch("/{id}/status", response_model=AbsenceResponse)
async def set_status(
    id: int,
    status: AbsenceStatus,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_absenceservice),
):
    return await repo.set_status(id=id, status=status, session=session)
