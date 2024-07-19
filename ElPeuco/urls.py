#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/registro', views.registro, name='registro'),
    path('accounts/login', views.login, name='login'),
    

]

