import threading
import smtplib
from email.message import EmailMessage
from app.config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, ADMIN_EMAIL
from app.logger import logger

def send_email(subject: str, body: str, to_email: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        logger.info(f"Email sent to {to_email}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

def send_patient_creation_email(patient):
    subject = f"New Patient Created: {patient.name}"
    body = f"Patient details:\nID: {patient.id}\nName: {patient.name}\nAge: {patient.age}\nDisease: {patient.disease}"
    threading.Thread(target=send_email, args=(subject, body, ADMIN_EMAIL), daemon=True).start()