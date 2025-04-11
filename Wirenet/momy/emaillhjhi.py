import json
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
SENDGRID_API_KEY = "MK1SG.8VNJnn8aTkCb_u4Rq_ZOzQ.k2KrpXN3j5EEyLG9OCtC16VCcLxY9jx1ZxnUkjV-brY"  # अपनी API Key सुरक्षित रखें
RECEIVER_EMAIL = "piyushmodgil9@gmail.com"
SENDER_EMAIL = "spaceanomalydetect@gmail.com"
LOW_BATTERY_THRESHOLD = 20
HIGH_RADIATION_THRESHOLD = 800

# TelemetryData structure to hold telemetry information
class TelemetryData:
    def __init__(self, battery_level, radiation_level, signal_strength, transfer_status, alert=None):
        self.battery_level = battery_level
        self.radiation_level = radiation_level
        self.signal_strength = signal_strength
        self.transfer_status = transfer_status
        self.alert = alert

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

# Function to send email alert
def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, "your_email_password")  # इसे सुरक्षित रखें
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
telemetry = TelemetryData(15, 900, "Strong", "In Progress", "High Radiation Alert")
send_email("Anomaly Detected!", telemetry.to_json())
