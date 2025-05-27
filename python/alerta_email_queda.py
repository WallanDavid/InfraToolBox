import smtplib
from email.message import EmailMessage
import subprocess

def check_ping(host="8.8.8.8"):
    try:
        subprocess.check_output(["ping", "-n", "1", host], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

if not check_ping():
    msg = EmailMessage()
    msg.set_content("🚨 ALERTA: O host 8.8.8.8 está fora do ar.")
    msg["Subject"] = "Alerta de Queda"
    msg["From"] = "seu@email.com"
    msg["To"] = "destinatario@email.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("seu@email.com", "SENHA")
        smtp.send_message(msg)
