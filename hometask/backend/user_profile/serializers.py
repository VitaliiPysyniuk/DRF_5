from rest_framework.serializers import ModelSerializer

from .models import ProfileModel


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = ['name', 'surname', 'age', 'profession', 'photo', 'user']


class ShortProfileSerializer(ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = ['name', 'surname', 'age', 'profession', 'user']


