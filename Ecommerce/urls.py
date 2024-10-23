from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    path('', views.cargar_categorias, name='index'),
]