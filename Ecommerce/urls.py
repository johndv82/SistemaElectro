from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
]