from django.urls import path
from .views import home, registro, contacto, galeria, agregar_producto, listar_productos, modificar_producto, eliminar_producto,\
agregar_proveedores, listar_proveedores, modificar_proveedores, eliminar_proveedores, agregar_cliente, listar_cliente,\
modificar_cliente, eliminar_cliente, Listar_contacto, modificar_contacto, eliminar_contacto


urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name='contacto'),
    path('listar-contacto/', Listar_contacto, name='listar_contacto'),
    path('modificar-contacto/<id>/', modificar_contacto, name='modificar_contacto'),
    path('eliminar-contacto/<id>/', eliminar_contacto, name='eliminar_contacto'),
    path('galeria/', galeria, name='galeria'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('agregar-proveedores/', agregar_proveedores, name='agregar_proveedores'),
    path('listar-proveedores/', listar_proveedores, name='listar_proveedores'),
    path('modificar-proveedores/<id>/', modificar_proveedores, name='modificar_proveedores'),
    path('eliminar-proveedores/<id>/', eliminar_proveedores, name='eliminar_proveedores'),
    path('agregar-cliente/', agregar_cliente, name='agregar_cliente'),
    path('listar-cliente/', listar_cliente, name='listar_cliente'),
    path('modificar-cliente/<id>/', modificar_cliente, name='modificar_cliente'),
    path('eliminar-cliente/<id>/', eliminar_cliente, name='eliminar_cliente'),
]