from django.contrib import admin
from .models import Categoria, Producto, Carrito, ItemCarrito, Pedido, ItemPedido, Envio


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'creado_en', 'actualizado_en')
    list_filter = ('categoria', 'creado_en', 'actualizado_en')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}

class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 1

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'creado_en')
    inlines = [ItemCarritoInline]

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'estado', 'creado_en', 'total')
    list_filter = ('estado', 'creado_en')
    inlines = [ItemPedidoInline]

class EnvioAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'direccion', 'ciudad', 'codigo_postal', 'pais', 'estado', 'enviado_en', 'fecha_entrega')
    list_filter = ('estado', 'enviado_en', 'fecha_entrega')
    search_fields = ('direccion', 'ciudad', 'codigo_postal', 'pais')

# Registro de los modelos en el administrador
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Envio, EnvioAdmin)
