from datetime import datetime
import base64
import socket
import io
import pyautogui



"""
 Take a screenshot and return it as a base64 string along with the filename.
 
    The filename is generated based on the current timestamp and the hostname of the machine.
    The screenshot is saved as a JPEG file.
    
    Returns: tuple: A tuple containing the base64 encoded string of the screenshot and the filename.
"""
def take_screenshot():
    timestamp = datetime.now().strftime('%d %m %Y %H:%M:%S')
    hostname = socket.gethostname()
    screenshot = pyautogui.screenshot()

    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='PNG')  # Sauvegarde du screenshot dans l'objet BytesIO
    base64_string = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')  # Encodage en base64

    screenshot_info = {
        "timestamp": timestamp,
        "hostname": hostname,
        "image": base64_string
    }

    return screenshot_info
