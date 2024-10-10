from django.core.mail import send_mail
from django.conf import settings

def email_send(title, message, recipients):
    send_mail(
        title,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        fail_silently=False,
    )