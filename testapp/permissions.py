from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGetOrPatch(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        allowed_methods = ['GET', 'PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False


class namePermission(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        if username.lower() == 'zeeshan':
            return True
        elif username != '' and len(username) %2 == 0 and request.method in SAFE_METHODS:
            return True
        else:
            return False
             
