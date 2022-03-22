from django.db import models

# Create your models here.

class Familia(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_barra = models.IntegerField()
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    descripcion = models.TextField()
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)
    fecha_vencimiento = models.DateField()
    stock = models.IntegerField()
    stock_critico = models.IntegerField()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    nombre_completo = models.CharField(max_length=50)
    rut = models.IntegerField()
    direccion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre_completo

opciones_consultas = [
    [0, "Consulta"],
    [1, "Sugerencia"],
    [2, "Reclamo"],
    [3, "Fiado"],
    [4, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre



