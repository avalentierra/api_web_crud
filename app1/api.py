from .models import *

from rest_framework import viewsets, permissions
from .serializers import *

class DireccionViewSet(viewsets.ModelViewSet):
    queryset=Direccion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=DireccionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CategoriaSerializer

    
class DescripcionViewSet(viewsets.ModelViewSet):
    queryset=Descripcion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=DescripcionSerializer

    
class DescuentoVentaViewSet(viewsets.ModelViewSet):
    queryset=DescuentoVenta.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=DescuentoVentaSerializer

class DescuentoCompraViewSet(viewsets.ModelViewSet):
    queryset=DescuentoCompra.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=DescuentoCompraSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProductoSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset=Color.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ColorSerializer

class TamañoViewSet(viewsets.ModelViewSet):
    queryset=Tamaño.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TamañoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ClienteSerializer

    
class VendedorViewSet(viewsets.ModelViewSet):
    queryset=Vendedor.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=VendedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset=Proveedor.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProveedorSerializer

class FacturaVentaViewSet(viewsets.ModelViewSet):
    queryset=FacturaVenta.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=FacturaVentaSerializer

class FacturaVentaProductoViewSet(viewsets.ModelViewSet):
    queryset=FacturaVentaProducto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=FacturaVentaProductoSerializer

class FacturaCompraViewSet(viewsets.ModelViewSet):
    queryset=FacturaCompra.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=FacturaCompraSerializer

class FacturaCompraProductoViewSet(viewsets.ModelViewSet):
    queryset=FacturaCompraProducto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=FacturaCompraProductoSerializer

    