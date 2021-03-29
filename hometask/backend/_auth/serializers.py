from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

from user_profile.serializers import ProfileSerializer
from .utils import Utils

UserModel = get_user_model()


class UserRegisterSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = UserModel.objects.create_user(**validated_data)
            token = Utils.get_activate_token(user)
            data_to_send = {
                'subject': 'Activate new account',
                'body': f'Tap on this link to activate your account\n'
                        f'http://127.0.0.1:8000/api/v1/auth/activate/?token={token}',
                'to': [user.email]
            }
            print(token)
            # Utils.send_email(**data_to_send)
        except ValueError as msg:
            raise ValidationError(msg)
        return user
