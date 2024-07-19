#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from.forms import FormularioRegistrousuarioRegistrado


# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)

def login(request):
    context={}
    return render(request,'accounts/login.html',context)

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








