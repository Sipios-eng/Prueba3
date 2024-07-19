#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/registro', views.registro, name='registro'),
    path('accounts/loginuser', views.loginuser, name='loginuser'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('CRUD/producto_list/', views.producto_list, name='producto_list'),
    path('CRUD/producto_delete/<path:id_producto>/', views.producto_delete, name='producto_delete'),
    path('CRUD/producto_add/', views.producto_create, name='producto_add'),
    path('CRUD/producto_edit/<path:id_producto>/', views.producto_update, name='producto_edit'),

]

