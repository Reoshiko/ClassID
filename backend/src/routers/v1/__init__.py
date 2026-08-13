from fastapi import APIRouter
from .schoolclass import router as SchoolclassRouter
from .student import router as StudentRouter
from .scanner import router as QRScannerRouter
from .attendance import router as AttendanceRouter

api_router = APIRouter()

api_router.include_router(SchoolclassRouter, prefix="/classes", tags=["classes"])
api_router.include_router(StudentRouter, prefix="/students", tags=["students"])
api_router.include_router(QRScannerRouter, prefix="/scanner", tags=["scanner"])
api_router.include_router(AttendanceRouter, prefix="/attendance", tags=["attendance"])
