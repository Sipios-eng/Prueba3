#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import FormularioRegistrousuarioRegistrado, ProductoForm, ContactoForms
from .models import producto, Carrito, CarritoItem, Apedido
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)

#-----
def producto_list(request):
    productos = producto.objects.all()
    return render(request, 'CRUD/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'CRUD/producto_add.html', {'form': form})

def producto_update(request, id_producto):
    producto_obj = get_object_or_404(producto, id_producto=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES,instance=producto_obj)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto_obj)
    return render(request, 'CRUD/producto_edit.html', {'form': form})

def producto_delete(request, id_producto):
    producto_obj = get_object_or_404(producto, id_producto=id_producto)
    if request.method == 'POST':
        producto_obj.delete()
        return redirect('producto_list')
    return render(request, 'CRUD/producto_delete.html', {'producto': producto_obj})


#----
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistrousuarioRegistrado(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
    else:
        form = FormularioRegistrousuarioRegistrado()
    return render(request, 'accounts/registro.html', {'form': form})

def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            return render(request, 'accounts/loginuser.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'accounts/loginuser.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def venta(request):
    productos = producto.objects.all()
    return render(request,'Venta.html',{'productos':productos})

@login_required
def agregar_al_carrito(request, id_producto):
    producto_obj = get_object_or_404(producto, id_producto=id_producto)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto_obj)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, id_item):
    carrito_item = get_object_or_404(CarritoItem, id=id_item, carrito__user=request.user)
    carrito_item.delete()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    print(total)
    return render(request, 'ver_carrito.html', {'items': items, 'total': total})


def Contacto(request):
    if request.method == 'POST':
        form = ContactoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'Contacto.html', {'form': form, 'success': True})
    else:
        form = ContactoForms()
    return render(request, 'Contacto.html', {'form': form, 'success': False})
