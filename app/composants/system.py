import psutil
from datetime import datetime
import socket
import getpass
import requests
import platform
import subprocess

def get_microsoft_account_email():
    if platform.system() == 'Windows':
        try:
            # Commande PowerShell pour obtenir l'adresse e-mail du compte Microsoft
            command = """
            $ErrorActionPreference = 'Stop'
            $user = [System.Security.Principal.WindowsIdentity]::GetCurrent()
            $sid = $user.User.Value
            $key = "HKLM:\\SOFTWARE\\Microsoft\\IdentityStore\\LogonCache\\" + $sid + "\\*"
            $email = Get-ItemProperty -Path $key | Select-Object -ExpandProperty "UserName"
            $email
            """
            result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
            # Extraire l'adresse e-mail de la sortie
            email = result.stdout.strip()
            if email:
                return email
            else:
                return "Aucune adresse e-mail trouvée pour le compte Microsoft."
        except Exception as e:
            return f"Erreur lors de la récupération de l'adresse e-mail: {e}"
    else:
        return "Non applicable, l'OS n'est pas Windows."

def get_system_info():
    timestamp = datetime.now().strftime('%d %m %Y %H:%M:%S')
    hostname = socket.gethostname()
    user_name = getpass.getuser()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    public_ip = requests.get('https://api.ipify.org').text
    account = get_microsoft_account_email()
    system_info = {
        "timestamp": timestamp,
        "hostname": hostname,
        "user_name": user_name,
        "local_ip": local_ip,
        "public_ip": public_ip,
        "CPU_Usage": f"{psutil.cpu_percent()}%",
        "Memory_Usage": f"{psutil.virtual_memory().percent}%",
        "email": account,
    }

    return system_info
