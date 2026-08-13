from fastapi import APIRouter
from .schoolclass import router as SchoolclassRouter
from .student import router as StudentRouter

api_router = APIRouter()

api_router.include_router(SchoolclassRouter, prefix="/classes", tags=["classes"])
api_router.include_router(StudentRouter, prefix="/students", tags=["students"])
