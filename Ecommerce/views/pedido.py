from django.shortcuts import render, redirect, get_object_or_404
from ..models import Pedido, ItemPedido, Producto, Carrito, ItemCarrito
from ..decorators import token_required

@token_required
def procesar_pedido(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    items_carrito = carrito.items.all() 

    if not items_carrito:
        return redirect('Ecommerce:carrito')

    # Crear el pedido
    pedido = Pedido.objects.create(usuario=request.user)

    for item_carrito in items_carrito:
        ItemPedido.objects.create(
            pedido=pedido,
            producto=item_carrito.producto,
            cantidad=item_carrito.cantidad,
            precio=item_carrito.producto.precio
        )

    pedido.calcular_total()

    # Vaciar el carrito
    carrito.items.all().delete()

    return redirect('Ecommerce:ver_pedidos')


@token_required
def ver_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-creado_en') 
    return render(request, 'pedidos.html', {'pedidos': pedidos})