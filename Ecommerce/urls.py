from django.urls import path
#from . import views
from .views import cargar_categorias, listar_productos, ver_carrito, listar_pedidos

app_name = 'Ecommerce'

#urlpatterns = [

#    path('', views.cargar_categorias, name='index'),
#    #path('', views.index, name='index'),
#    path('login', views.login, name='login'),
#    path('register', views.register, name='register'),

#]

urlpatterns = [
    path('', cargar_categorias, name='index'),
    path('productos/', listar_productos, name='listar_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('pedidos/', listar_pedidos, name='listar_pedidos'),
]