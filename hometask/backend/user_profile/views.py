from rest_framework.generics import ListAPIView, ListCreateAPIView

from .models import ProfileModel
from .serializers import ProfileSerializer


class ListProfileView(ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

