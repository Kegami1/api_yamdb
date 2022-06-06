from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated,
                                        SAFE_METHODS)
from rest_framework.response import Response


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class MeAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            return (request.user.is_superuser or request.user.role == 'admin')


class AuthorAdminModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif obj.author == request.user:
            return True
        elif request.user.is_superuser:
            return True
        elif (
                request.user.is_authenticated
                and request.user.role == 'admin'
        ):
            return True
        elif (
                request.user.is_authenticated
                and request.user.role == 'moderator'
        ):
            return True