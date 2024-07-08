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
    timestamp = datetime.now().strftime('%d %m %Y %H:%M:%S')
    hostname = socket.gethostname()
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        cam.release()
        return {
            "success": False,
            "timestamp": timestamp,
            "hostname": hostname,
            "error": "Failed to open webcam."
        }
    ret, frame = cam.read()
    cam.release()

    if ret:
        try:
            _, buffer = cv2.imencode('.jpg', frame)
            base64_string = base64.b64encode(buffer).decode('utf-8')
            return {
                "success": True,
                "timestamp": timestamp,
                "hostname": hostname,
                "image": base64_string
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    else:
        return {
            "success": False,
            "error": "Failed to capture webcam image."
        }

