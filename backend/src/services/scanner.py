from fastapi import HTTPException
import numpy as np
import cv2


class QRScannerService:
    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def decode(self, data: bytes) -> str:
        array = np.frombuffer(data, dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_COLOR)

        if image is None:
            raise HTTPException(status_code=400, detail="invalid image")

        token, points, _ = self.detector.detectAndDecode(image)

        if not token:
            raise HTTPException(status_code=404, detail="QR code not found")

        return token
