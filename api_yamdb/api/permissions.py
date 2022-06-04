from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated,
                                        SAFE_METHODS)
from rest_framework.response import Response


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


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
                and request.user.is_admin
        ):
            return True
        elif (
                request.user.is_authenticated
                and request.user.is_moderator
        ):
            return True
