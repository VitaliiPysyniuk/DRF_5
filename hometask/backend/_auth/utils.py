from datetime import timedelta

from django.core import mail
from rest_framework_simplejwt.tokens import RefreshToken


class UserActivateToken(RefreshToken):
    lifetime = timedelta(days=30)


class Utils:
    @staticmethod
    def send_email(subject, body, to, **kwargs):
        print(to[0])
        email = mail.EmailMessage(subject, body, to=to, **kwargs)
        email.send()

    @staticmethod
    def get_activate_token(user):
        token = UserActivateToken().for_user(user).access_token
        return token

