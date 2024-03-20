from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FacturaSerializer, ProductoSerializer, DetallesFacturaSerializer, OperadorSerializer, ClienteSerializer, CategoriasSerializer
from .models import Factura, Producto, DetallesFactura, Operador, Cliente, Categorias

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class DetallesFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetallesFactura.objects.all()
    serializer_class = DetallesFacturaSerializer
    
class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer