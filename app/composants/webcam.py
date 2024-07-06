import cv2
import base64
from datetime import datetime
import socket

"""
Take a photo using the webcam and return it as a base64 string along with the filename.

The filename is generated based on the current timestamp and the hostname of the machine.
The photo is saved as a JPEG file.

Returns:
    tuple: A tuple containing the base64 encoded string of the photo and the filename.
"""
def take_webcam_photo():
    timestamp = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    hostname = socket.gethostname()
    filename = f"{timestamp}_webcam_{hostname}.jpg"
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    base64_string = ""
    if ret:
        _, buffer = cv2.imencode('.jpg', frame)
        base64_string = base64.b64encode(buffer).decode('utf-8')
    cam.release()

    return base64_string, filename
