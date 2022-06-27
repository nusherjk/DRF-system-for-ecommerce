from email import message
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsSelforAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

            # Instance must have an attribute named `owner`
        # if request.user.is_authenticated:
        #     return True
        return obj.id == request.user.id
        # return False


class IsProviderOrReadOnly(BasePermission):
    #for role based users for future purpose.
    message = "you need to be a provider."
    edit_methods = ('POST', 'PUT')
    def has_permission(self, request, view):

        if(not request.user.is_authenticated):
            return False
        
        if request.user.is_Provider:
            return True

        # return obj.user == request.user.id
        return False
    
