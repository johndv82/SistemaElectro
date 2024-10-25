from django.shortcuts import render
from ..models import Producto

def listar_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'productos.html', {'productos': productos})
