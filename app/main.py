import cv2


from app.camera import Camera
from app.scanner import QRScanner
from app.database import Database
camera = Camera()
scanner = QRScanner()
database = Database()

count = 0

while True:
    ret, frame = camera.read()
    if not ret:
        break

    qr_codes = scanner.scan(frame)

    for code in qr_codes:
        count += 1
        database.insert(code)
        print(f"QR: {code} | Total: {count}")

    cv2.putText(frame, f"Count: {count}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Shoe QR Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
