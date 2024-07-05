#urls.py
from django.urls import path
from . import views

urlpatterns = [
#    path('index', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'),
    path('contacto', views.contacto, name='contacto'),
    path('index', views.index, name='index'),
    path('platos', views.platos, name='platos'),
    path('restaurante1', views.restaurante1, name='restaurante1'),
    path('test', views.test, name='test'),
    path('ubicacion', views.ubicacion, name='ubicacion'),

]

