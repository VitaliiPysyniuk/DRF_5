from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from user_profile.serializers import ProfileSerializer
UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = UserModel.objects.create_user(**validated_data)
        except ValueError as msg:
            raise ValidationError(msg)
        return user



