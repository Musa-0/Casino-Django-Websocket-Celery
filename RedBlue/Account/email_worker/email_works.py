import random
import string
from smtplib import SMTPDataError

from django.core.mail import send_mail, EmailMessage

from RedBlue.settings import BASE_URL


def email_send_code_checker(email, code):
    uri = BASE_URL + "account/verification_email/" + code

    subject = "Подтверждение почты"
    body = f"Перейдите по ссылке, чтобы подтвердить свою почту {uri}.\nВнимание никому не отправляйте эту ссылку"
    email_send(email, subject, body)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def email_send(email, subject, body):
    email = EmailMessage(subject, body, to=[email])
    try:
        email.send()
    except(SMTPDataError):
        pass



