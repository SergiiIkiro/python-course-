import csv

from configs import password
import smtplib
import ssl
from configs import html_message

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

html_message = html_message
sender = 'noreply.storesales@gmail.com'
users = ['innovationsolutions2019@gmail.com', 'sanchezs@ukr.net']
message = MIMEMultipart()
message['Subject'] = 'Store updates'
message['From'] = sender

context = ssl.create_default_context()
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465,
                      context=context) as server:  # створення захищеного з'єднання з сервером
    server.login(user=sender, password=password)  # логування користувача до сервера
    server.ehlo()
    server.sendmail(sender, users, message.as_string())
