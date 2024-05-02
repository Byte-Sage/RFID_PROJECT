import sys
from email.message import EmailMessage
import ssl 
import smtplib

def send_email(email_receiver):
    email_sender = 'devanshmathur0348@gmail.com'
    email_password = 'numt prls psex lbki'
    subject = 'Attendance Low'
    body = "Please take care of your attendance it is below 75% now"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

if __name__ == "__main__":
    email_receiver = sys.argv[1]  # Get the email address from command line arguments
    send_email(email_receiver)
