from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_users.permissions import AdminOnly, UserOwner
from api_users.serializers import (UserAdminSerializer, UserGetTokenSerializer,
                                   UserSerializer, UserSignupSerializer)
from users.models import User


@api_view(['POST'])
@permission_classes((AllowAny, ))
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.initial_data['username']
        if username == 'me':
            return Response(
                'me - запрещенный username',
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        user = get_object_or_404(User, username=username)
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Получение кода подтверждения',
            f'{username}, Ваш код подтверждения: {confirmation_code}.',
            'from@example.com',
            [serializer.initial_data['email']],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def get_token(request):
    serializer = UserGetTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = get_object_or_404(
            User,
            username=serializer.initial_data['username']
        )
        if default_token_generator.check_token(
            user,
            serializer.initial_data['confirmation_code']
        ):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AdminOnly,)
    lookup_field = 'username'

    @action(methods=['get', 'patch'], detail=False, url_path='me')
    def user_me(self, request):
        user = get_object_or_404(User, username=self.request.user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=self.request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.path == '/api/v1/users/me/':
            return (UserOwner(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        username = serializer.validated_data['username']
        if username == 'me':
            raise ValidationError('me - запрещенный username')
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.user.role == 'admin':
            return UserAdminSerializer
        return UserSerializer
