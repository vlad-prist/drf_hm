from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверка на модератора."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модераторы").exists()


class IsOwner(permissions.BasePermission):
    """Проверка на автора."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

#
# class IsUserOwner(permissions.BasePermission):
#
#     def has_permission(self, request, obj):
#         if request.user == obj:
#             return True
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj == request.user
