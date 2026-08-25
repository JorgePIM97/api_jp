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


class ProductoViewSet(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return [IsAuthenticated()]

        return [IsAdminUser()]


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()

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