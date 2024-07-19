#urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/registro', views.registro, name='registro'),
    path('accounts/loginuser', views.loginuser, name='loginuser'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('CRUD/producto_list/', views.producto_list, name='producto_list'),
    path('CRUD/producto_delete/<path:id_producto>/', views.producto_delete, name='producto_delete'),
    path('CRUD/producto_add/', views.producto_create, name='producto_add'),
    path('CRUD/producto_edit/<path:id_producto>/', views.producto_update, name='producto_edit'),
    path('venta', views.venta, name='Venta'),
    path('ver_carrito', views.ver_carrito, name='ver_carrito'),
    path('ver_carrito/agregar/<int:id_producto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/eliminar/<int:id_item>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('Contacto/', views.Contacto, name='Contacto')    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
