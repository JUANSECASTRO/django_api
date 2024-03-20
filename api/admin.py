
from django.contrib import admin
from .models import Factura, Producto, DetallesFactura, Operador, Cliente, Categorias

admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(DetallesFactura)
admin.site.register(Operador)
admin.site.register(Cliente)
admin.site.register(Categorias)