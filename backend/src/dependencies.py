from src.services.schoolclass import SchoolClassService
from src.services.student import StudentService
from src.services.qr import QRService


def get_schoolclassservice():
    return SchoolClassService()


def get_studentservice():
    return StudentService()


def get_qrservice():
    return QRService()
