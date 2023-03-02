from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Descripcion)
admin.site.register(DescuentoVenta)
admin.site.register(DescuentoCompra)
admin.site.register(Producto)
admin.site.register(Color)
admin.site.register(Tamaño)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Proveedor)
admin.site.register(FacturaVenta)
admin.site.register(FacturaVentaProducto)
admin.site.register(FacturaCompra)
admin.site.register(FacturaCompraProducto)


