from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.student import StudentCreate, StudentResponse
from src.core.database import get_session
from src.dependencies import get_studentservice

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=StudentResponse)
async def create(
    payload: StudentCreate,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_studentservice),
):
    return await repo.create(payload=payload, session=session)


@router.get("/", response_model=list[StudentResponse])
async def get_all(
    session: AsyncSession = Depends(get_session), repo=Depends(get_studentservice)
):
    return await repo.get_all(session=session)


@router.get("/{id}", response_model=StudentResponse)
async def retrieve(
    id: int,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_studentservice),
):
    return await repo.retrieve(id=id, session=session)
