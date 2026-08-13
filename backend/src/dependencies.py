from src.services.schoolclass import SchoolClassService
from src.services.student import StudentService


def get_schoolclassservice():
    return SchoolClassService()


def get_studentservice():
    return StudentService()
