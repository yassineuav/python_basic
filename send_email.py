from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()

message["from"] = "Yassine Khaidouch by Python mime"
message["to"] = "khaidouchyassine@gmail.com"
message["subject"] = "test email from mime"
message.attach(MIMEText("Body ..."))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("root", "root")
    smtp.send_message(message)
    print("sent...")
