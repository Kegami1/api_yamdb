from rest_framework import permissions

from api_users.constants import RESERVED_KEYWORD_ME


class AdminOnly(permissions.BasePermission):
    """
    Разрешение работы с пользователями только администратору.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            path = '/' + RESERVED_KEYWORD_ME + '/'
            if path in request.path:
                return True
            return (
                request.user.is_superuser
                or request.user.is_admin
            )
