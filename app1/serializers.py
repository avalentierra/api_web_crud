from rest_framework import serializers
from .models import *

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Direccion
        fields =('codigo_d','direccion', 'barrio_sector','ciudad','departamento_provincia','codigo_postal')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Categoria
        fields =('id','nombre_categoria')

class DescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Descripcion
        fields =('id','descripcion_producto')
class DescuentoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model =DescuentoVenta
        fields =('id','porcentaje_descuento','fecha_inicio_descuento','fecha_fin_descuento')

class DescuentoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model =DescuentoCompra
        fields =('id','porcentaje_descuento','fecha_inicio_descuento')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Producto
        fields =('id','nombre_producto','precio_venta_producto','categoria','descripcion')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Color
        fields =('id','nombre_color')

class TamañoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tamaño
        fields =('id','nombre_tamaño')
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cliente
        fields =('identificacion','nombre_cliente','apellidos_cliente','telefono_cliente','correo_cliente', 'direccion')

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Vendedor
        fields =('identificacion','nombres_vendedor','apellidos_vendedor','telefono_vendedor', 'rut_vendedor', 'direccion')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Proveedor
        fields =('identificacion','nombres_proveedor','apellidos_proveedor','telefono_proveedor','correo_proveedor','rut_proveedor','direccion')

class FacturaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model =FacturaVenta
        fields =('id','cliente','vendedor')
        read_only_fields=('fecha_factura',)

class FacturaVentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =FacturaVentaProducto
        fields =('id','factura','producto', 'descuento', 'cantidad')

class FacturaCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model =FacturaCompra
        fields =('id','proveedor')
        read_only_fields=('fecha_compra',)

class FacturaCompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =FacturaCompraProducto
        fields =('id','compra','producto','cantidad', 'descuento')






