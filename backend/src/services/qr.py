from io import BytesIO
import qrcode


class QRService:
    def generate(self, data: str) -> BytesIO:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image()
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
