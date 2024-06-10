import mimetypes
import smtplib
from email.message import EmailMessage



email_sender = 'ebooking@shahibu.com'
email_password = 'Hr{Y,st!j}r8'

email_reciever = ['eliok5128@gmail.com']

body = """\
Hellooo man i hope this message
 finds you well pushing on with your daily routine
"""


# HTML body
html_body = """\
<!DOCTYPE html>
<html>
    <body style="backgorund-color:light-blue;">
        <div style="width:400px; padding:20px; margin:10px auto;">
            <h1 style=" color:black; background-color:pink;"> this is a greeting text</h1>
            <p>Hello my good friend. i hope you are doing good</p>
            <p>Hello my good friend. i hope you are doing good</p>
            <p>Hello my good friend. i hope you are doing good</p>
        </div>
    </body>
</html>
"""

msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_reciever
msg['Subject'] =  'Email attachment'

msg.set_content(body)
msg.add_alternative(html_body, subtype='html')
# attaching image file
files = ['image1.jpg', 'image2.jpg', 'FINAL PROJECT DOCUMENTATION.pdf']

for file in files:
    with open(file, 'rb') as image:
        file_data = image.read()
        file_name = image.name

        mime_type, _ = mimetypes.guess_type(file_name)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        maintype, subtype = mime_type.split('/', 1)

    
    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)


with smtplib.SMTP_SSL('mail.shahibu.com', 465) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(msg)


