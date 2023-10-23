import smtplib
from email.mime.text import MIMEText
from numpy import loadtxt
from time import sleep
from random import uniform

def send_email(subject, body, email_addr):
    #Your gmail account
    gmail_user = 'youraccount@gmail.com'
    #Your app password (Google Account Parameter -> Security -> 2-Step Verification -> App Passwords)
    gmail_password = 'xxxxxxxxxxxxxxxx'

    msg = MIMEText(body)
    msg['From'] = 'Your cute name'
    msg['To'] = email_addr
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, email_addr, msg.as_string())
        server.close()

        print(f'Email sent to {email_addr}')

    except Exception as e:
        print(f'Failed to send email: {e}')

content = open('content.txt').read()
title = 'The email title'

mailing_list = loadtxt('mailing_list.csv', dtype='str', comments='#')

for mail in mailing_list:
    send_email(title, content, mail)
    sleep(uniform(1, 5))
