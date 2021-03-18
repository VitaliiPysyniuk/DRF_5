from django.db import models

from user.models import UserModel


def upload_to(instance, filename):
    return f'{instance.user.email}/profile_photos/{filename}'


class ProfileModel(models.Model):
    class Meta:
        db_table = 'user_profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    profession = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=upload_to)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')


