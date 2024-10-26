from django.urls import path
#from . import views
from .views import cargar_categorias, listar_productos, ver_carrito, listar_pedidos
from .views.categoria_views import index
from Ecommerce.views import categoria_views
from .views import categoria_views

#app_name = 'Ecommerce'

urlpatterns = [
    path('', index, name='index'),
    path('', categoria_views.index, name='index'),
    path('productos/', listar_productos, name='listar_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('pedidos/', listar_pedidos, name='listar_pedidos'),
    path('categoria/', categoria_views.cargar_categorias, name='cargar_categorias'),
]