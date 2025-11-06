from mail import send_gmail
from config import to_address 
result = send_gmail(
    to_address, 
    "Masood - Test Subject from masood - 06-11-2025", "Hello from Python!",
    attachment_path="/Users/masoosha/Desktop/sc")

print("Mail sent successfully?" , result)