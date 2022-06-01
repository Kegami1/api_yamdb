from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Разрешение работы с пользователями только администратору.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_superuser or
            request.user.user_role == 'ADMIN'
        )

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return (
            request.user.is_superuser or
            request.user.user_role == 'ADMIN'
        )


class UserOwner(permissions.BasePermission):
    """
    Разрешение пользователю работы со своим аккаунтом.
    """

    # def has_permission(self, request, view):
    #     return (
    #         request.user.is_superuser or
    #         request.user.user_role == 'ADMIN'
    #     )

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return (
            obj.username == request.user
        )
