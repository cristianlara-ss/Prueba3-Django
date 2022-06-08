from django.urls import path
from .views import index, admindj, contactanos, registro, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro1, carrito

urlpatterns = [
    path('', index, name="index"),
    path('contactanos/', contactanos, name="contactanos"),
    path('admindj/', admindj, name="admindj"),
    path('registro/', registro, name="registro"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro-per/', registro1, name="registro1"),
    path('carrito/', carrito, name="carrito"),
    
]