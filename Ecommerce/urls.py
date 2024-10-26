from django.urls import path
from .views import usuario
from .views import cargar_categorias, listar_productos, ver_carrito, listar_pedidos

app_name = 'Ecommerce'


urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('pedidos/', listar_pedidos, name='listar_pedidos'),
    path('loginview/', usuario.login_view, name='login_view'),
    path('login/', usuario.login, name='login'),
    path('logout/', usuario.logout, name='logout'),
    path('register/', usuario.register, name='register'),
]