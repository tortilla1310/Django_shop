from urllib.parse import urljoin
from email import message
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key]
    )
    subject = "Подтвердите учетную запись"
    messahge = f"""
        Для подтверждения учетной записи {user.username} на портале
        {settings.DOMAIN_NAME} перейдите по ссылке: 
        {urljoin(settings.DOMAIN_NAME, verify_link)}
    """
    send_mail(subject, message, "noreply@localhost", [user.email])
