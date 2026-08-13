from src.services.schoolclass import SchoolClassService
from src.services.student import StudentService
from src.services.attendance import AttendanceService


def get_schoolclassservice():
    return SchoolClassService()


def get_studentservice():
    return StudentService()


def get_attendanceservice():
    return AttendanceService()
