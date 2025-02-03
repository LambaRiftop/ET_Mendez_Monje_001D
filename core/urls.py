from django.urls import path
from .views import *

urlpatterns=[
    #paginas que se muestran en la base general
    path('', home, name='index'),
    path('info', info, name='info'),
    path('galeria', galeria, name='galeria'),
    path('catalogo', catalogo, name='catalogo'), #catalogo puede o no aparecer en el navbar

    #metodos de registro y login de usuatio (obviamente tambien el logout)
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('exit', logout, name='exit'),

    #CRUD del admin de la pagina
    path('admin_panel', admin_panel, name='admin_panel'),
    path('adminCRUD', adminCRUD, name='adminCRUD'),
    path('crear_producto', crear_producto, name='crear_producto'),
    path('editar_producto/<int:id>', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>', eliminar_producto, name='eliminar_producto'),

    #pagina de la tienda mas metodos para realizar la compra
    path('tienda', tienda, name='tienda'),
    path('agregar/<id>', agregar, name="agregar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('restar/<id>', restar, name="restar"),
    path('limpiar/', limpiar, name="limpiar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('eliminar-articulo/<id>/', eliminar_articulo, name='eliminar_articulo'),
]