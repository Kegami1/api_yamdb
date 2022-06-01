from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, чтобы разрешить его редактирование
    только владельцам объекта.
    """

    def has_permission(self, request, view):
        return (
                request.user.user_role == 'ADMIN'
            )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ADMIN'

   