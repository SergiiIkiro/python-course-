import csv

with open('users.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for name, email, grade in reader:
        print(f'Name: {name}\n | Email:{email}\n | Grade: {grade}\n ')


from configs import password
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

html_message = ("\n"
                "<head>\n"
                "    <style>\n"
                "        #customstyle {\n"
                "        border: 2px solid red;\n"
                "        border-radius: 25px;\n"
                "        padding: 50px;\n"
                "        }\n"
                "    </style>\n"
                "</head>\n"
                "<body>\n"
                "<div id=\"customstyle\">\n"
                "    <center>\n"
                "        <div style='font-family: Courier; font-weight:normal; padding:20px; font-size: 20px'>\n"
                "<a>Hi %s, tomorrow we will have a planned an electricity outage, please take your devices off.<br> "
                "Thanks in \n "
                "            advance!</a>        \n"
                "            </div>\n"
                "    </center>\n"
                "</div>\n"
                "</body>\n")
sender = 'noreply.storesales@gmail.com'
message = MIMEMultipart()
message['Subject'] = 'Service Outage on 19.11.2021 at 16:00'
message['From'] = sender

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    with open('users.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, m in reader:
            message['To'] = email
            part2 = MIMEText(html_message % name, 'html')
            message.attach(part2)
            server.sendmail(sender, email, message.as_string())
