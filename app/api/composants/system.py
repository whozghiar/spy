import psutil
from datetime import datetime
import socket
import getpass
import requests

def get_system_info():
    timestamp = datetime.now().strftime('%d %m %Y %H:%M:%S')
    hostname = socket.gethostname()
    user_name = getpass.getuser()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    public_ip = requests.get('https://api.ipify.org').text
    system_info = {
        "timestamp": timestamp,
        "hostname": hostname,
        "user_name": user_name,
        "local_ip": local_ip,
        "public_ip": public_ip,
        "CPU_Usage": f"{psutil.cpu_percent()}%",
        "Memory_Usage": f"{psutil.virtual_memory().percent}%",
    }

    return system_info
