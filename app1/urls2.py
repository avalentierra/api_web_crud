
from rest_framework import routers
from .api import *

router=routers.DefaultRouter()
router.register('api/app1/categorias', CategoriaViewSet ),
router.register('api/app1/direciones', DireccionViewSet ),
router.register('api/app1/descripciones', DescripcionViewSet ),
router.register('api/app1/descuentosventas', DescuentoVentaViewSet),
router.register('api/app1/descuentoscompras', DescuentoCompraViewSet),
router.register('api/app1/productos', ProductoViewSet),
router.register('api/app1/colores', ColorViewSet ),
router.register('api/app1/tamaños', TamañoViewSet ),
router.register('api/app1/clientes', ClienteViewSet),
router.register('api/app1/vendedores', VendedorViewSet),
router.register('api/app1/proveedores', ProveedorViewSet),
router.register('api/app1/facturaventa', FacturaVentaViewSet),
router.register('api/app1/facturaventaproductos', FacturaVentaProductoViewSet),
router.register('api/app1/facturacompra', FacturaCompraViewSet),
router.register('api/app1/facturacompraproducto', FacturaCompraProductoViewSet),


urlpatterns=router.urls
