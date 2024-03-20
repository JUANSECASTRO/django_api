# Generated by Django 5.0 on 2023-12-07 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('numeroDocumento', models.PositiveBigIntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('numeroTrabajador', models.PositiveIntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.PositiveIntegerField(default=True)),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.operador')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.PositiveBigIntegerField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesFactura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadProducto', models.PositiveIntegerField(default=True)),
                ('precioProducto', models.PositiveIntegerField(default=True)),
                ('descuentoProducto', models.PositiveIntegerField(default=True)),
                ('total', models.PositiveIntegerField(default=True)),
                ('facturaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.factura')),
                ('productoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
            ],
        ),
    ]
