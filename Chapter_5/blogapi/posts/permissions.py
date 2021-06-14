# class BasePermission(object):
#     """
#     A base class from which all permission classes should be inherit.
#     """
#     def has_permission(self, request, view):
#         """
#         Return 'True' if permission is granted, 'False' otherwise.
#         """
#         return True

#     def has_object_permission(self, request, view, obj):
#         """
#         Return 'True' if permision is granted, 'False' otherwise.
#         """
#         return True

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author  == request.user