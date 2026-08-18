from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.schoolclass import SchoolClassResponse, SchoolClassCreate
from src.core.database import get_session
from src.dependencies import get_schoolclassservice

router = APIRouter()


@router.post("/", response_model=SchoolClassResponse, status_code=201)
async def create(
    payload: SchoolClassCreate,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_schoolclassservice),
):
    return await repo.create(payload=payload, session=session)


@router.get("/", response_model=list[SchoolClassResponse])
async def get_all(
    session: AsyncSession = Depends(get_session), repo=Depends(get_schoolclassservice)
):
    return await repo.get_all(session=session)


@router.get("/{id}", response_model=SchoolClassResponse)
async def retrieve(
    id: int,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_schoolclassservice),
):
    return await repo.retrieve(id=id, session=session)
