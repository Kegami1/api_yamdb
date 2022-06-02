from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import MyTokenObtainPairView, UserApiViewSet, UserDetail, UserList, UserDetailViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



app_name = 'api_users'
router = routers.DefaultRouter()
router.register(
    r'users/(?P<username>\d+)/',
    UserDetailViewSet,
    basename='user'
)

urlpatterns = [
    # path('', include(router.urls)),

    # path('users/', UserList.as_view(), name='users'),
    # # path('users/<str:username>/', UserDetail.as_view(), name='users-detail'),
    # path('users/me/', UserApiViewSet, name='users-me'),
    # # path('auth/signup'), 
    # path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]