
from django.db import models

class Operador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models. CharField(max_length=50)
    numeroTrabajador = models.PositiveIntegerField(default=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    numeroDocumento = models.PositiveBigIntegerField(default=True)

    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.PositiveIntegerField(default=True)
    fecha = models.DateField()
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def detalles_factura(self):
        return DetallesFactura.objects.filter(facturaId=self)

    def __str__(self):
        return str(self.numero)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    precio = models.PositiveBigIntegerField(default=True)

    def detalles_factura(self):
        return DetallesFactura.objects.filter(productoId=self)

    def __str__(self):
        return self.nombre

class DetallesFactura(models.Model):
    id = models.AutoField(primary_key=True)
    facturaId = models.ForeignKey(Factura, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProducto = models.PositiveIntegerField(default=True)
    precioProducto = models.PositiveIntegerField(default=True)
    descuentoProducto = models.PositiveIntegerField(default=True)
    total = models.PositiveIntegerField(default=True)

    def __str__(self):
        return f'{self.facturaId} - {self.productoId}'
