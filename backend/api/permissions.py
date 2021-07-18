from rest_framework.permissions import BasePermission, SAFE_METHODS


# write a permission only for super user
class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    """
    The user is author of object or superuser, or request is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            # get access to superuser
            request.user.is_authenticated and request.user.is_superuser or
            # get access to author of object(article)
            request.user.is_authenticated and request.user == obj.author
        )


class IsSuperuserOrAuthorReadOnly(BasePermission):
    """
    The user is author of object or superuser, or request is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated \
                and request.user.is_staff:
            return True
        return bool(
            # get access to superuser
            request.user.is_authenticated and request.user.is_superuser
        )
