from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.attendance import AttendanceCreate, AttendanceResponse
from src.models.schemas.attendance import AttendanceEventType, AttendanceSource
from src.core.database import get_session
from src.dependencies import get_attendanceservice, get_studentservice
from src.services.scanner import QRScannerService

router = APIRouter()

scanner = QRScannerService()


@router.post("/scan", response_model=AttendanceResponse)
async def scan(
    file: UploadFile,
    event_type: AttendanceEventType,
    session: AsyncSession = Depends(get_session),
    student_service=Depends(get_studentservice),
    attendance_service=Depends(get_attendanceservice),
):
    data = await file.read()
    token = scanner.decode(data)
    student = await student_service.get_by_qr_token(token=token, session=session)
    return await attendance_service.create(
        student_id=student.id,
        event_type=event_type,
        source=AttendanceSource.SCANNER,
        session=session,
    )


@router.get("/", response_model=list[AttendanceResponse])
async def get_all(
    session: AsyncSession = Depends(get_session), repo=Depends(get_attendanceservice)
):
    return await repo.get_all(session=session)
