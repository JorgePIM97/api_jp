from django.urls import path
from .views import ProductosView, ProductoDetalleView


urlpatterns = [
    path(
        'productos/',
        ProductosView.as_view()
    ),

    path(
        'productos/<int:id>/',
        ProductoDetalleView.as_view()
    ),
]