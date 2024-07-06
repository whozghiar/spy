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
    timestamp = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
    hostname = socket.gethostname()
    filename = f"{timestamp}_screenshot_{hostname}.png"
    screenshot = pyautogui.screenshot()

    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    base64_string = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

    return base64_string, filename
