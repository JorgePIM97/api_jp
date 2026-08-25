from rest_framework.routers import DefaultRouter

from .views import (
    ProductoViewSet,
    CategoriaViewSet
)


router = DefaultRouter()

router.register(
    'productos',
    ProductoViewSet,
    basename='productos'
)

router.register(
    'categorias',
    CategoriaViewSet,
    basename='categorias'
)


urlpatterns = router.urls