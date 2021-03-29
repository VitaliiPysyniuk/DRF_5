from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from .serializers import UserRegisterSerializer
from user_profile.serializers import ProfileSerializer, ShortProfileSerializer
from user.serializers import UserSerializer
UserModel = get_user_model()


class RegisterUserView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        name = self.request.data.get('name', None)
        surname = self.request.data.get('surname', None)
        age = self.request.data.get('age', None)
        profession = self.request.data.get('profession', '')
        photo = self.request.data.get('photo', None)

        if name and surname and age:
            data = {'name': name, 'surname': surname, 'age': age, 'profession': profession, 'user': user.id}
            if photo:
                data['photo'] = photo
                profile = ProfileSerializer(data=data)
            else:
                profile = ShortProfileSerializer(data=data)
            profile.is_valid(raise_exception=True)
            profile.save()


class ActivateUserView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        token = self.request.query_params.get('token')
        try:
            token = RefreshToken(token)
            pk = token.payload.get('user_id')
            token.blacklist()
        except TokenError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(UserModel, pk=pk)
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


