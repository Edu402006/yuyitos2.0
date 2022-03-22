from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .models import Proveedores
from .models import Cliente
from .models import Contacto
from .forms import ContactoForm, ProductoForm, ProveedoresForm, ClienteForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import  permission_required

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
           login(request, user)
           messages.success(request, "Te has registrado correctamente")
           return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#Contacto
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def Listar_contacto(request):
    contacto = Contacto.objects.all()
    data = {
        'contacto': contacto
    }
    return render(request, 'app/contacto/listar.html', data)

@permission_required('app.change_producto')
def modificar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    data = {
        'form': ContactoForm(instance=contacto)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance=contacto, files=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_contacto")
        data["form"] = formulario
    return render(request, 'app/contacto/modificar.html', data)
@permission_required('app.delete_producto')
def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_contacto")

#Productos
@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)
@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)
@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario
    return render(request, 'app/producto/modificar.html', data)
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")

#Proveedores
@permission_required('app.add_producto')
def agregar_proveedores(request):
    data = {
        'form': ProveedoresForm()
    }
    if request.method == 'POST':
        formulario = ProveedoresForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/proveedores/agregar.html', data)
@permission_required('app.view_producto')
def listar_proveedores(request):
    proveedores = Proveedores.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'app/proveedores/listar.html', data)
@permission_required('app.change_producto')
def modificar_proveedores(request, id):
    proveedores = get_object_or_404(Proveedores, id=id)
    data = {
        'form': ProveedoresForm(instance=proveedores)
    }
    if request.method == 'POST':
        formulario = ProveedoresForm(data=request.POST, instance=proveedores, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_proveedores")
        data["form"] = formulario
    return render(request, 'app/proveedores/modificar.html', data)
@permission_required('app.delete_producto')
def eliminar_proveedores(request, id):
    proveedores = get_object_or_404(Proveedores, id=id)
    proveedores.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_proveedores")

#Cliente
@permission_required('app.add_cliente')
def agregar_cliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = formulario
    return render(request, 'app/cliente/agregar.html', data)
@permission_required('app.view_cliente')
def listar_cliente(request):
    cliente = Cliente.objects.all()
    data = {
        'cliente': cliente
    }
    return render(request, 'app/cliente/listar.html', data)
@permission_required('app.change_cliente')
def modificar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    data = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'modificado correctamente')
            return redirect(to="listar_cliente")
        data["form"] = formulario
    return render(request, 'app/cliente/modificar.html', data)
@permission_required('app.delete_cliente')
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_cliente")

