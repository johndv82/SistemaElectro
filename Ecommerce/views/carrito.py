from django.shortcuts import render, redirect, get_object_or_404
from ..models import Producto, Carrito, ItemCarrito
from ..decorators import token_required
from django.contrib import messages

@token_required
def ver_carrito(request):
    print(request.user)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.obtener_precio_total() for item in items)
    context = {
        'carrito': carrito,
        'items': items,
        'total': total
    }
    return render(request, 'cart.html', context)

@token_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_created:
        item.cantidad += 1
    item.save()
    messages.success(request, 'Producto Agregado al Carrito')
    return redirect('Ecommerce:productos')

@token_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    messages.success(request, 'Producto Eliminado al Carrito')
    return redirect('Ecommerce:carrito')