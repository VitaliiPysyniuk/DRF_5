from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, \
    DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from user_profile.serializers import ProfileSerializer
from .models import UserModel
from .serializers import UserSerializer
from .permissions import IsSuperuser


class ListUsersView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CreateUserProfileView(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class UpdateUserToAdminView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        print(user.is_staff)
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class UpdateUserProfileView(UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        auth_user = self.request.user

        if auth_user.id == user.id:
            if auth_user.is_staff:
                return [IsSuperuser()]
            return [IsAuthenticated()]
        elif auth_user.is_staff and user.is_staff:
            return [IsSuperuser]
        return [IsAdminUser()]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        return user.profile


