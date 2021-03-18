from django.urls import path, include

urlpatterns = [
    path('auth/', include('_auth.urls')),
    path('users/', include('user.urls'))
]
