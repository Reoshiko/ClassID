from src.services.schoolclass import SchoolClassService
from src.services.student import StudentService
from src.services.attendance import AttendanceService
from src.services.absence import AbsenceService


def get_schoolclassservice():
    return SchoolClassService()


def get_studentservice():
    return StudentService()


def get_attendanceservice():
    return AttendanceService()


def get_absenceservice():
    return AbsenceService()
