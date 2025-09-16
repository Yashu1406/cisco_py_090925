import os

DB_URL = os.getenv("DB_URL", "sqlite:///db.sqlite")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.mailtrap.io")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your_mailtrap_username")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_mailtrap_password")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@hospital.com")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 10))