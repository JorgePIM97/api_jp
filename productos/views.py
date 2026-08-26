from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Producto, Categoria

from .serializers import (
    ProductoSerializer,
    ProductoSimpleSerializer,
    CategoriaSimpleSerializer,
    CategoriaDetalleSerializer
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser


# from rest_framework.permissions import (
#     IsAuthenticated,
#     IsAdminUser
# )

from .permissions import IsOwnerOrAdmin

class ProductoViewSet(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    permission_classes = [
        IsAuthenticated,
        IsOwnerOrAdmin
    ]

    def perform_create(self, serializer):

        serializer.save(
            creado_por=self.request.user
        )
class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()

    def get_permissions(self):

        if self.action in [
            'list',
            'retrieve',
            'productos'
        ]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [
            permission()
            for permission in permission_classes
        ]

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return CategoriaDetalleSerializer

        return CategoriaSimpleSerializer

    @action(
        detail=True,
        methods=['get']
    )
    def productos(self, request, pk=None):

        categoria = self.get_object()

        productos = categoria.productos.all()

        serializer = ProductoSimpleSerializer(
            productos,
            many=True
        )

        return Response(serializer.data)