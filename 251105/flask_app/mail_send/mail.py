import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mail_send.config import app_password, from_address, to_address
from email import encoders
from email.mime.base import MIMEBase

def send_gmail(to_address, subject, body, attachment_path=None):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if attachment_path: 
            with open(attachment_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={attachement_path.split('/')[-1]}"
            )
            msg.attach(part)
           


        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, app_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Error:", e)
        return False



