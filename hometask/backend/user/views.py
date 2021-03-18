from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, \
    DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from user_profile.serializers import ProfileSerializer
from .models import UserModel
from .serializers import UserSerializer


class ListUsersView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        name = self.request.data.get('name', None)
        surname = self.request.data.get('surname', None)
        age = self.request.data.get('age', None)
        profession = self.request.data.get('profession', '')
        photo = self.request.data.get('photo', None)

        if name and surname and age and photo:
            data = {'name': name, 'surname': surname, 'age': age, 'profession': profession, 'photo': photo,
                    'user': user.id}
            profile = ProfileSerializer(data=data)
            profile.is_valid(raise_exception=True)
            profile.save()


class CreateUserProfileView(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class UpdateUserStatusView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(is_staff=True)


class DeleteUserView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class RetrieveUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# class GetUserInfo(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, *args, **kwargs):
#         user = UserSerializer(self.request.user).data
#         return Response(user, status.HTTP_200_OK)
