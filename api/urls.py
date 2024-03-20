from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Factura', views.FacturaViewSet)
router.register(r'Producto', views.ProductoViewSet)
router.register(r'DetalleFactura', views.DetallesFacturaViewSet)
router.register(r'Operador', views.OperadorViewSet)
router.register(r'Cliente', views.ClienteViewSet)
router.register(r'Categoria', views.CategoriasViewSet)

urlpatterns = [
    path('', include(router.urls))
]