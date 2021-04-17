from rest_framework import permissions


class IsSelforAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

            # Instance must have an attribute named `owner`.
        return obj.id == request.user.id


class IsProviderOrReadOnly(permissions.BasePermission):
    #for role based users for future purpose.
    pass
