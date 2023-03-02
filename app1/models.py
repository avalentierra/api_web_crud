
from django.db import models

# Create your models here.
class Direccion(models.Model):
    codigo_d=models.BigAutoField(primary_key=True)
    direccion=models.CharField(max_length=100)
    barrio_sector=models.CharField(max_length=75)
    ciudad=models.CharField(max_length=50)
    departamento_provincia=models.CharField(max_length=100)
    codigo_postal=models.IntegerField()

    
    def __str__(self):
        texto="{0}, {1}, {2}, {3}, {4},{5}"
        return texto.format(self.codigo_d, self.direccion, self.barrio_sector, self.ciudad, self.departamento_provincia,self.codigo_postal)

class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)

    def __str__(self):
        texto="{0}"
        return texto.format(self.nombre_categoria)

class Descripcion(models.Model):
    descripcion_producto=models.CharField(max_length=250)

    def __str__(self):
        texto="{0}"
        return texto.format(self.descripcion_producto)

class DescuentoVenta(models.Model):
    porcentaje_descuento=models.IntegerField()
    fecha_inicio_descuento=models.DateField()
    fecha_fin_descuento=models.DateField()
    def __str__(self):
        texto="porcentaje: {0}, inicio: {1}, fin: {2}"
        return texto.format(self.porcentaje_descuento,self.fecha_inicio_descuento,self.fecha_fin_descuento)

class DescuentoCompra(models.Model):
    porcentaje_descuento=models.IntegerField()
    fecha_inicio_descuento=models.DateField(auto_now_add=True)
    def __str__(self):
        texto="porcentaje: {0}, inicio: {1}"
        return texto.format(self.porcentaje_descuento,self.fecha_inicio_descuento)

class Producto(models.Model):
    nombre_producto=models.CharField(max_length=50)
    precio_venta_producto=models.IntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    descripcion=models.ForeignKey(Descripcion,on_delete=models.RESTRICT)

    def __str__(self):
        texto="{0}, (precio:{1}), (categoria:{2}), {3}"
        return texto.format(self.nombre_producto, self.precio_venta, self.categoria, self.descripcion)

class Color(models.Model):
    nombre_color=models.CharField(max_length=20)

    def __str__(self):
        texto="color: {0} "
        return texto.format(self.nombre_color)

class Tamaño(models.Model):
    nombre_tamaño=models.CharField(max_length=20)

    def __str__(self):
        texto="tamaño: {0} "
        return texto.format(self.nombre_tamaño)

class Cliente(models.Model):
    identificacion=models.CharField(max_length=10, primary_key=True)
    nombres_cliente=models.CharField(max_length=100)
    apellidos_cliente=models.CharField(max_length=100)
    telefono_cliente=models.CharField(max_length=12)
    correo_cliente=models.EmailField()
    direccion=models.ForeignKey(Direccion,on_delete=models.RESTRICT)

    def __str__(self):
        texto="{0} {1}, {2}, {3}, {4},{5}"
        return texto.format(self.identificacion, self.nombres_cliente, self.apellidos_cliente, self.telefono_cliente, self.correo_cliente,self.direccion)

class Vendedor(models.Model):
    identificacion=models.CharField(max_length=10, primary_key=True)
    nombres_vendedor=models.CharField(max_length=100)
    apellidos_vendedor=models.CharField(max_length=100)
    telefono_vendedor=models.CharField(max_length=12)
    rut_vendedor=models.CharField(max_length=20)
    direccion=models.ForeignKey(Direccion,on_delete=models.RESTRICT)

    def __str__(self):
        texto="{0} {1}, {2}, {3}, {4}"
        return texto.format(self.nombres_vendedor, self.apellidos_vendedor, self.telefono_vendedor, self.rut_vendedor,self.direccion)

class Proveedor(models.Model):
    identificacion=models.CharField(max_length=10, primary_key=True)
    nombres_proveedor=models.CharField(max_length=100)
    apellidos_proveedor=models.CharField(max_length=100)
    telefono_proveedor=models.CharField(max_length=12)
    correo_proveedor=models.EmailField()
    rut_proveedor=models.CharField(max_length=20)
    direccion=models.ForeignKey(Direccion,on_delete=models.RESTRICT)

    def __str__(self):
        texto="{0} {1}, {2}, {3}, {4}, {5},{6}"
        return texto.format(self.nombres_proveedor, self.apellidos_proveedor, self.telefono_proveedor, self.correo_proveedor, self.rut_proveedor, self.direccion)






class FacturaVenta(models.Model):
    fecha_factura=models.DateField(auto_now_add=True)
    cliente=models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    vendedor=models.ForeignKey(Vendedor, on_delete=models.RESTRICT)
    def __str__(self):
        texto="{0} {1}"
        return texto.format(self.fecha_factura, self.cliente)

class FacturaVentaProducto(models.Model):
    factura=models.ForeignKey(FacturaVenta, on_delete=models.RESTRICT)
    producto=models.ForeignKey(Producto, on_delete=models.RESTRICT)
    descuento=models.ForeignKey(DescuentoVenta, on_delete=models.RESTRICT)
    cantidad_producto=models.IntegerField()

    def __str__(self):
        texto="{0} {1} {2} {3}"
        return texto.format(self.factura, self.producto, self.descuento, self.cantidad_producto)

class FacturaCompra(models.Model):
    fecha_compra=models.DateField(auto_now_add=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
    

    def __str__(self):
        texto="{0}, {1}"
        return texto.format(self.fecha_compra, self.proveedor)

class FacturaCompraProducto(models.Model):

   
    compra=models.ForeignKey(FacturaCompra, on_delete=models.RESTRICT)
    producto=models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad_producto=models.IntegerField()
    descuento=models.ForeignKey(DescuentoCompra, on_delete=models.RESTRICT)

    def __str__(self):
        texto="{0}, {1}, {2}, {3}"
        return texto.format(self.compra, self.producto, self.cantidad_producto,self.descuento)


 
 