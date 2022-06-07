from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import UserRole


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class MeAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return (request.user.is_superuser
                    or request.user.role == UserRole.ADMIN)


class AuthorAdminModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True
        if request.user.is_superuser:
            return True
        if (
                request.user.is_authenticated
                and request.user.role == UserRole.ADMIN
        ):
            return True
        if (
                request.user.is_authenticated
                and request.user.role == UserRole.MODERATOR
        ):
            return True
