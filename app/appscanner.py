from pyzbar.pyzbar import decode

class QRScanner:
    def scan(self, frame):
        qr_codes = decode(frame)
        results = []

        for qr in qr_codes:
            results.append(qr.data.decode("utf-8"))

        return results
