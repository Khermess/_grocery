from django.db import models


class tiendas(models.Model):
    nombre = models.IntegerField(max_length=200),
    localizacion = models.DecimalField(max_digits=9, decimal_places=6),
    descripcion = models.TextField


class productos(models.Model):
    nombre = models.TextField,
    tienda = models.ForeignKey(tiendas, on_delete=models.CASCADE),
    precio = models.DecimalField(decimal_places=2),
    descripcion = models.TextField,


class tipo_producto(models.Model):
    nombre = models.TextField,
    producto = models.ForeignKey(productos, on_delete=models.CASCADE),
    descripcion = models.TextField
