from django.shortcuts import render
from ..models import Pedido

def listar_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos.html', {'pedidos': pedidos})
