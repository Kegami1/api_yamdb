from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api_users.views import MyTokenObtainPairView, UserApiViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


app_name = 'api_users'
router = routers.DefaultRouter()
router.register(
    r'users',
    UserApiViewSet,
    basename='user'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    
    # path('v1/auth/signup'), 
    path('v1/auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]