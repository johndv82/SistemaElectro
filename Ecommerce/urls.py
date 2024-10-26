from django.urls import path
from .views import usuario, producto, carrito

app_name = 'Ecommerce'

urlpatterns = [
    path('productos/', producto.listar_productos, name='productos'),
    path('productos/<int:categoria_id>/', producto.listar_productos, name='productos'),
    path('productos/<int:categoria_id>/<str:busqueda>/', producto.listar_productos, name='productos'),
    path('carrito/', carrito.ver_carrito, name='carrito'),
    path('loginview/', usuario.login_view, name='login_view'),
    path('login/', usuario.login, name='login'),
    path('logout/', usuario.logout, name='logout'),
    path('register/', usuario.register, name='register'),
]