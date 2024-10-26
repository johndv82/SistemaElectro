from django.urls import path
from .views import usuario, producto, carrito, pedido

app_name = 'Ecommerce'

urlpatterns = [
    path('productos/', producto.listar_productos, name='productos'),
    path('productos/<int:categoria_id>/', producto.listar_productos, name='productos'),
    path('productos/<int:categoria_id>/<str:busqueda>/', producto.listar_productos, name='productos'),
    path('carrito/', carrito.ver_carrito, name='carrito'),
    path('carrito/<int:producto_id>/', carrito.agregar_al_carrito, name='agregarcarrito'),
    path('eliminarcarrito/<int:item_id>/', carrito.eliminar_del_carrito, name='eliminarcarrito'),
    path('loginview/', usuario.login_view, name='login_view'),
    path('login/', usuario.login, name='login'),
    path('logout/', usuario.logout, name='logout'),
    path('register/', usuario.register, name='register'),
    path('procesarpedido/', pedido.procesar_pedido, name='procesarpedido'),
    path('pedidos/', pedido.ver_pedidos, name='ver_pedidos'),
]