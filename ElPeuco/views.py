#views.py
from django.shortcuts import render


# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)

def contacto(request):
    context={}
    return render(request,'contacto.html',context)

def carrito(request):
    context={}
    return render(request,'carrito.html',context)

def platos(request):
    context={}
    return render(request,'platos.html',context)

def restaurante1(request):
    context={}
    return render(request,'restaurante1.html',context)

def test(request):
    context={}
    return render(request,'test.html',context)

def ubicacion(request):
    context={}
    return render(request,'ubicacion.html',context)








