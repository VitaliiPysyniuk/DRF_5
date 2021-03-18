from django.conf.urls.static import static
from django.urls import path, include

from django_hometask_5 import settings

urlpatterns = [
    path('api/v1/', include('api.api_versions.api_v1'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
