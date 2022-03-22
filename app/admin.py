from django.contrib import admin
from .models import Familia, Producto, Proveedores, Marca, Contacto, Cliente

# Register your models here.

admin.site.register(Familia)
admin.site.register(Producto)
admin.site.register(Proveedores)
admin.site.register(Marca)
admin.site.register(Contacto)
admin.site.register(Cliente)
