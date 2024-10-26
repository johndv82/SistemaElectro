from django.shortcuts import render
from ..models import Categoria, Producto

def cargar_categorias(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    return render(request, 'index.html', {'categorias': categorias})


def index(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria_id')  # Obtiene la categoría seleccionada desde el menú
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()[:4]  # Muestra algunos productos como "Nuevos Productos" al inicio

    context = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'index.html', context)