from rest_framework.viewsets import ModelViewSet

from .models import Producto, Categoria
from .serializers import (
    ProductoSerializer,
    CategoriaSerializer
)


class ProductoViewSet(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer