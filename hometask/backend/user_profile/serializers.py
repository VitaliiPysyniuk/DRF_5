from rest_framework.serializers import ModelSerializer

from .models import ProfileModel


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = ['id', 'name', 'surname', 'age', 'profession', 'photo', 'user']
