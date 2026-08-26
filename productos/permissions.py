from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Los métodos de solo lectura están permitidos
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # El administrador puede modificar cualquier producto
        if request.user.is_staff:
            return True

        # Un usuario normal solo puede modificar sus propios productos
        return obj.creado_por == request.user