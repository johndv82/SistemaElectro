from django.shortcuts import render
from .models import Categoria

# Create your views here.
def cargar_categorias(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    return render(request, 'index.html', {'categorias': categorias})
