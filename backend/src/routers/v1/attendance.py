from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.dto.attendance import AttendanceCreate, AttendanceResponse
from src.models.schemas.attendance import AttendanceEventType, AttendanceSource
from src.core.database import get_session
from src.dependencies import get_attendanceservice, get_studentservice
from src.services.scanner import QRScannerService

router = APIRouter()

scanner = QRScannerService()


@router.post("/scan", response_model=AttendanceResponse, status_code=201)
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
    payload = AttendanceCreate(
        student_id=student.id, event_type=event_type, source=AttendanceSource.SCANNER
    )
    return await attendance_service.create(
        payload,
        session=session,
    )


@router.get("/", response_model=list[AttendanceResponse])
async def get_all(
    session: AsyncSession = Depends(get_session), repo=Depends(get_attendanceservice)
):
    return await repo.get_all(session=session)


@router.post("/school/scan", response_model=AttendanceResponse, status_code=201)
async def school_scan(
    file: UploadFile,
    session: AsyncSession = Depends(get_session),
    student_service=Depends(get_studentservice),
    attendance_service=Depends(get_attendanceservice),
):
    data = await file.read()
    token = scanner.decode(data)
    student = await student_service.get_by_qr_token(token=token, session=session)
    return await attendance_service.create_school_event(
        student_id=student.id,
        session=session,
    )


@router.get("/students/{student_id}", response_model=list[AttendanceResponse])
async def get_by_student(
    student_id: int,
    session: AsyncSession = Depends(get_session),
    repo=Depends(get_attendanceservice),
):
    return await repo.get_by_student(student_id=student_id, session=session)
