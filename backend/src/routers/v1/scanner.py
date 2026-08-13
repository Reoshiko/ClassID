from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.student import StudentResponse
from src.core.database import get_session
from src.dependencies import get_studentservice
from src.services.scanner import QRScannerService

router = APIRouter()

scanner = QRScannerService()


@router.post("/", response_model=StudentResponse)
async def scan(
    file: UploadFile,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_studentservice),
):
    data = await file.read()
    token = scanner.decode(data)
    return await repo.get_by_qr_token(token=token, session=session)
