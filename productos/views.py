from rest_framework.viewsets import ModelViewSet

from .models import Producto, Categoria

from .serializers import (
    ProductoSerializer,
    CategoriaSimpleSerializer,
    CategoriaDetalleSerializer
)


class ProductoViewSet(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return CategoriaDetalleSerializer

        return CategoriaSimpleSerializer