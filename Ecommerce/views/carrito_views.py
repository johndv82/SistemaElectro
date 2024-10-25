from django.shortcuts import render
from ..models import Carrito, ItemCarrito

def ver_carrito(request):
    carrito = request.user.carrito  # Asumimos que el usuario ya tiene un carrito creado
    return render(request, 'carrito.html', {'carrito': carrito})