from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from account.views.edit_user import EditUser
from account.views.register_user import Register

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/', Register.as_view(), name='create_user'),
    path('edit-user/', EditUser.as_view(), name='edit_user'),
]
