from django.shortcuts import render, redirect, get_object_or_404
from ..models import Producto, Categoria
from ..decorators import token_required

@token_required
def listar_productos(request, categoria_id=0, busqueda=""):
    categorias = Categoria.objects.all()
    usuario = request.user
    
    if categoria_id == 0:
        productos = Producto.objects.all()
    else:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)

    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    context = {
        'categorias': categorias,
        'productos': productos,
        'categoria_id': categoria_id,
        'texto_input': busqueda,
        'usuario':usuario
    }
    return render(request, 'product.html', context)