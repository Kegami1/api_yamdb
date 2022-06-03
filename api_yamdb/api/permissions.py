from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated,
                                        SAFE_METHODS)
from rest_framework.response import Response


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS