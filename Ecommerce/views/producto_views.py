from django.shortcuts import render, redirect
from ..models import Producto
from django.contrib import messages

def listar_productos(request):
    token = request.session.get('auth_token')
    
    if not token:
        return redirect('Ecommerce:login_view')
    
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'product.html', {'productos': productos})
