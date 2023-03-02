from django.urls import path
from  app1.views import *
from rest_framework import routers
from .api import *
urlpatterns = [
   
    path('',HomeInicio.index),
    path('sotre/',HomeInicio.indexReturn,name='Home'),

    path('gestionarDirecc/', GestionarDireccion.gestionarDireciones, name='gt_direcciones'),
    path('registrarDirecc/', GestionarDireccion.registrarDireciones),
    path('edicionDireciones/<codigo>', GestionarDireccion.edicionDireciones),
    path('editarDirecc/', GestionarDireccion.editarDireccion),
    path('eliminacionDireciones/<codigo>',GestionarDireccion.eliminacionDireciones),

    path('gestionarCategory/', GestionarCategoria.gestionarCategorias, name='gt_categorias'),
    path('registrarCategory/', GestionarCategoria.registrarCategoria),
    path('edicionCategorias/<codigo>', GestionarCategoria.edicionCategorias),
    path('editarCategory/', GestionarCategoria.editarCategory),
    path('eliminacionCategorias/<codigo>',GestionarCategoria.eliminacionDireciones),


    path('gestionarDescript/', GestionarDescripcion.gestionarDescripcion, name='gt_descripciones'),
    path('registrarDescript/', GestionarDescripcion.registrarDescripcion),
    path('edicionDescripciones/<codigo>', GestionarDescripcion.edicionDescripciones),
    path('editarDescript/', GestionarDescripcion.editarDescripcion),
    path('eliminacionDescripciones/<codigo>',GestionarDescripcion.eliminacionDescripciones),

    path('gestionarDescuentoV/', GestionarDescuentoVenta.gestionarDescuentoV, name='gt_descuentosV'),
    path('registrarDescuentoV/', GestionarDescuentoVenta.registrarDescuentoV),
    path('edicionDescuentosVentas/<codigo>', GestionarDescuentoVenta.edicionDescuentosV),
    path('editarDescuentoV/', GestionarDescuentoVenta.editarDescuentoV),
    path('eliminacionDescuentosVentas/<codigo>',GestionarDescuentoVenta.eliminacionDescuentoV),


    path('gestionarDescuentoC/', GestionarDescuentoCompra.gestionarDescuentoC, name='gt_descuentosC'),
    path('registrarDescuentoC/', GestionarDescuentoCompra.registrarDescuentoC),
    path('edicionDescuentosCompras/<codigo>', GestionarDescuentoCompra.edicionDescuentosC),
    path('editarDescuentoC/', GestionarDescuentoCompra.editarDescuentoC),
    path('eliminacionDescuentosCompras/<codigo>',GestionarDescuentoCompra.eliminacionDescuentoC),


    path('gestionarProduct/', GestionarProducto.gestionarProductos, name='gt_productos'),
    path('registrarProduct/', GestionarProducto.registrarProducto),
    path('edicionProductos/<codigo>', GestionarProducto.edicionProductos),
    path('editarProduct/', GestionarProducto.editarProducto),
    path('eliminacionProductos/<codigo>',GestionarProducto.eliminacionProductos ),
    path('datosCategoria/',JsonData.DatosCategoria,name='datosCategoria'),
    path('datosDescripcion/',JsonData.DatosDescripcion,name='datosDescripcion'),


    path('gestionarColor/', GestionarColor.gestionarColores, name='gt_colores'),
    path('registrarColor/', GestionarColor.registrarColor),
    path('edicionColores/<codigo>', GestionarColor.edicionColores),
    path('editarColor/', GestionarColor.editarColor),
    path('eliminacionColores/<codigo>',GestionarColor.eliminacionColores),

    path('gestionarTaman/', GestionarTamaño.gestionarTamans, name='gt_tamans'),
    path('registrarTaman/', GestionarTamaño.registrarTaman),
    path('edicionTamans/<codigo>', GestionarTamaño.edicionTamans),
    path('editarTaman/', GestionarTamaño.editarTaman),
    path('eliminacionTamans/<codigo>',GestionarTamaño.eliminacionTamans),

    path('gestionarClient/', GestionarCliente.gestionarClientes, name='gt_clientes'),
    path('registrarClient/', GestionarCliente.registrarCliente),
    path('edicionClientes/<codigo>', GestionarCliente.edicionClientes),
    path('editarClient/', GestionarCliente.editarCliente),
    path('eliminacionClientes/<codigo>',GestionarCliente.eliminacionClientes),
    path('datosDireciones/',JsonData.DatosDirecion,name='datosDireciones'),

    path('gestionarVended/', GestionarVendedor.gestionarVendedores, name='gt_vendedores'),
    path('registrarVended/', GestionarVendedor.registrarVendedor),
    path('edicionVendedores/<codigo>', GestionarVendedor.edicionVendedores),
    path('editarVended/', GestionarVendedor.editarVendedor),
    path('eliminacionVendedores/<codigo>',GestionarVendedor.eliminacionVendedores),
    path('datosDireciones/',JsonData.DatosDirecion,name='datosDireciones'),

    path('gestionarProveedor/', GestionarProveedor.gestionarProveedores, name='gt_proveedores'),
    path('registrarProveedor/', GestionarProveedor.registrarProveedor),
    path('edicionProveedores/<codigo>', GestionarProveedor.edicionProveedores),
    path('editarProveedor/', GestionarProveedor.editarProveedor),
    path('eliminacionProveedores/<codigo>',GestionarProveedor.eliminacionProveedores),
    path('datosDireciones/',JsonData.DatosDirecion,name='datosDireciones'),
  

]

