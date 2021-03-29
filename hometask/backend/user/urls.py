from django.urls import path

from .views import ListUsersView, CreateUserProfileView, DeleteUserView, UpdateUserToAdminView, \
    RetrieveUserView, UpdateUserProfileView

urlpatterns = [
    path('', ListUsersView.as_view(), name='all_users'),
    # path('add/', CreateUserView.as_view(), name='new_user'),
    path('info/', RetrieveUserView, name='show_user'),
    path('del/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
    path('admin/<int:pk>/', UpdateUserToAdminView.as_view(), name='change_status'),
    path('<int:pk>/profile/', CreateUserProfileView.as_view(), name='create_user_profile'),
    path('<int:pk>/update/', UpdateUserProfileView.as_view(), name='update_user_profile')

]
