from email.message import EmailMessage
import ssl
import smtplib



email_sender = 'ebooking@shahibu.com'
email_password = 'Hr{Y,st!j}r8'

email_reciever = 'eliok5128@gmail.com'

subject = "Dont forget to subscribe"
body = """
When you watch  a video please hit the subscrie button
And remember to folleow us on wwww.facebook.com/ellyok
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('mail.shahibu.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

    