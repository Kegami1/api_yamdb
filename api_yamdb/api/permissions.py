from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated,
                                        SAFE_METHODS)
from rest_framework.response import Response


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class MeAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.user.role == 'admin' or request.user.is_superuser)

