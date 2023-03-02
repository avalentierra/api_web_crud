
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from app1.models import *

# Create your views here.

class HomeInicio():
    def index(sefl):
        PlantillaPrincipal=get_template('index.html')
        return HttpResponse(PlantillaPrincipal.render())
    def indexReturn(sefl):
        PlantillaPrincipal=get_template('index.html')
        return HttpResponse(PlantillaPrincipal.render())
        
class GestionarDireccion(HttpResponse):
    def gestionarDireciones(request):
        listadoDirecciones=Direccion.objects.all()
        return render(request, "registrar_direccion.html", {"direcciones":listadoDirecciones})

    def registrarDireciones(request):
        
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        cciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        nueva_direcion=Direccion.objects.create(direccion=direccionD, barrio_sector=barrioD, ciudad=cciudadD,departamento_provincia=departamentoD, codigo_postal=postalD)
        return redirect('/gestionarDirecc')

    def edicionDireciones(request, codigo):
        direccionC=Direccion.objects.get(pk=codigo)
        return render(request, 'editar_direciones.html',{"direccion":direccionC})

    def editarDireccion(request):
        codigoD=request.POST['txtcodigot']
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        ciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        
        direccionObjeto=Direccion.objects.get(pk=codigoD)
        direccionObjeto.direccion=direccionD
        direccionObjeto.barrio_sector=barrioD
        direccionObjeto.ciudad=ciudadD
        direccionObjeto.departamento_provincia=departamentoD
        direccionObjeto.codigo_postal=postalD
        direccionObjeto.save()
        return redirect('/gestionarDirecc')

    def eliminacionDireciones(request, codigo):
        direccion=Direccion.objects.get(pk=codigo)
        direccion.delete()

        return redirect('/gestionarDirecc')

class GestionarCategoria(HttpResponse):
    def gestionarCategorias(request):
        listadoCategorias=Categoria.objects.all()
        return render(request, "registrar_categoria.html", {"categorias":listadoCategorias})

    def registrarCategoria(request):
        nombreC=request.POST['txtCategoriaProducto']
        categoria=Categoria.objects.create(nombre_categoria=nombreC,)
        return redirect('/gestionarCategory')
    
    def edicionCategorias(request, codigo):
        categoriaC=Categoria.objects.get(pk=codigo)
        return render(request, 'editar_categorias.html',{"categoria":categoriaC})

    def editarCategory(request):
        codigoD=request.POST['txtcodigot']
        nombreD=request.POST['txtcategoriat']
        
        direccionObjeto=Categoria.objects.get(pk=codigoD)
        direccionObjeto.nombre_categoria=nombreD
        direccionObjeto.save()
        return redirect('/gestionarCategory')

    def eliminacionDireciones(request, codigo):
        categoria=Categoria.objects.get(pk=codigo)
        categoria.delete()

        return redirect('/gestionarCategory')

class GestionarDescripcion(HttpResponse):
    def gestionarDescripcion(request):
        listadoDescripciones=Descripcion.objects.all()
        return render(request, "registrar_descripcion.html", {"descripciones":listadoDescripciones})

    def registrarDescripcion(request):
        nombreC=request.POST['txtDescripcion']
        descripcion=Descripcion.objects.create(descripcion_producto=nombreC,)
        return redirect('/gestionarDescript')
    
    def edicionDescripciones(request, codigo):
        descripcion=Descripcion.objects.get(pk=codigo)
        return render(request, 'editar_descripciones.html',{"descripcion":descripcion})

    def editarDescripcion(request):
        codigoD=request.POST['txtcodigot']
        nombreD=request.POST['txtdescripciont']
        
        descripcionObjeto=Descripcion.objects.get(pk=codigoD)
        descripcionObjeto.descripcion_producto=nombreD
        descripcionObjeto.save()
        return redirect('/gestionarDescript')

    def eliminacionDescripciones(request, codigo):
        descripcion=Descripcion.objects.get(pk=codigo)
        descripcion.delete()

        return redirect('/gestionarDescript')

class GestionarDescuentoVenta(HttpResponse):
    def gestionarDescuentoV(request):
        listadoDescuentos=DescuentoVenta.objects.all()
        return render(request, "registrar_descuento_venta.html", {"descuentos":listadoDescuentos})

    def registrarDescuentoV(request): 
        porcentaje=request.POST['txtPorcentajeV']
        feccha_inicio=request.POST['txtFechaInicioV']
        feccha_fin=request.POST['txtFechaFinV']
        descuento=DescuentoVenta.objects.create(porcentaje_descuento=porcentaje,fecha_inicio_descuento=feccha_inicio,fecha_fin_descuento=feccha_fin)
        return redirect('/gestionarDescuentoV')
    
    def edicionDescuentosV(request, codigo):
        descuentoC=DescuentoVenta.objects.get(pk=codigo)
        return render(request, 'editar_descuento_venta.html',{"descuento":descuentoC})

    def editarDescuentoV(request):
        codigoD=request.POST['txtcodigot']
        porcentajeD=request.POST['txtporcentajet']
        fecha_inicio=request.POST['txtfechainicio']
        fecha_fin=request.POST['txtfechafin']
        
        descuentoObjeto=DescuentoVenta.objects.get(pk=codigoD)
        descuentoObjeto.porcentaje_descuento=porcentajeD
        descuentoObjeto.fecha_inicio_descuento=fecha_inicio
        descuentoObjeto.fecha_fin_descuento=fecha_fin
        descuentoObjeto.save()
        return redirect('/gestionarDescuentoV')

    def eliminacionDescuentoV(request, codigo):
        descuentoVenta=DescuentoVenta.objects.get(pk=codigo)
        descuentoVenta.delete()

        return redirect('/gestionarDescuentoV')

class GestionarDescuentoCompra(HttpResponse):
    def gestionarDescuentoC(request):
        listadoDescuentos=DescuentoCompra.objects.all()
        return render(request, "registrar_descuento_compra.html", {"descuentos":listadoDescuentos})

    def registrarDescuentoC(request): 
        porcentaje=request.POST['txtPorcentajeC']
        fecha_inicio=request.POST['txtFechaInicioC']
        descuento=DescuentoCompra.objects.create(porcentaje_descuento=porcentaje,fecha_inicio_descuento=fecha_inicio)
        return redirect('/gestionarDescuentoC')
    
    def edicionDescuentosC(request, codigo):
        descuentoC=DescuentoCompra.objects.get(pk=codigo)
        return render(request, 'editar_descuento_compra.html',{"descuento":descuentoC})

    def editarDescuentoC(request):
        codigoD=request.POST['txtcodigot']
        porcentajeD=request.POST['txtporcentajet']
        fecha_inicio=request.POST['txtfechainicio']
        descuentoObjeto=DescuentoCompra.objects.get(pk=codigoD)
        descuentoObjeto.porcentaje_descuento=porcentajeD
        descuentoObjeto.fecha_inicio_descuento=fecha_inicio
        descuentoObjeto.save()
        return redirect('/gestionarDescuentoC')

    def eliminacionDescuentoC(request, codigo):
        descuentoVenta=DescuentoCompra.objects.get(pk=codigo)
        descuentoVenta.delete()

        return redirect('/gestionarDescuentoC')

class GestionarProducto(HttpResponse):
    def gestionarProductos(request):
        listadoProductos=Producto.objects.all()
        return render(request, "registrar_producto.html", {"productos":listadoProductos})

    

    def registrarProducto(request):
        
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']
        categP=request.POST['categ']
        descripP=request.POST['descrip']

        categoriaP=Categoria.objects.get(nombre_categoria=categP)
        descripcionP=Descripcion.objects.get(descripcion_producto=descripP)
        producto=Producto.objects.create(nombre_producto=nombreP, precio_venta_producto=precioP,categoria=categoriaP,descripcion=descripcionP)
        return redirect('/gestionarProduct')

    def edicionProductos(request, codigo):
        productoC=Producto.objects.get(pk=codigo)
        return render(request, 'editar_productos.html',{"producto":productoC})

    def editarProducto(request):
        codigoP=request.POST['txtcodigoProducto']
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']

        categP=request.POST['categ']
        descripP=request.POST['descrip']
   
        categoria=Categoria.objects.get(nombre_categoria=categP)
        descripcion=Descripcion.objects.get(descripcion_producto=descripP)
        productoObjeto=Producto.objects.get(pk=codigoP)
        productoObjeto.nombre_producto=nombreP
        productoObjeto.precio_venta_producto=precioP
        productoObjeto.categoria=categoria
        productoObjeto.descripcion=descripcion
        productoObjeto.save()
        return redirect('/gestionarProduct')

    def eliminacionProductos(request, codigo):
        producto=Producto.objects.get(pk=codigo)
        producto.delete()

        return redirect('/gestionarProduct')

class GestionarColor(HttpResponse):
    def gestionarColores(request):
        listadoColores=Color.objects.all()
        return render(request, "registrar_color.html", {"colores":listadoColores})

    def registrarColor(request):
        
        nombreP=request.POST['txtNombreColor']
        color=Color.objects.create(nombre_color=nombreP)
        return redirect('/gestionarColor')

    def edicionColores(request, codigo):
        color=Color.objects.get(pk=codigo)
        return render(request, 'editar_colores.html',{"color":color})

    def editarColor(request):
        codigoD=request.POST['txtcodigot']
        nombreC=request.POST['txtcolort']
        colorObjeto=Color.objects.get(pk=codigoD)
        colorObjeto.nombre_color=nombreC
        colorObjeto.save()
        return redirect('/gestionarColor')

    def eliminacionColores(request, codigo):
        color=Color.objects.get(pk=codigo)
        color.delete()

        return redirect('/gestionarColor')

class GestionarTamaño(HttpResponse):
    def gestionarTamans(request):
        listadoTamans=Tamaño.objects.all()
        return render(request, "registrar_taman.html", {"tamans":listadoTamans})

    def registrarTaman(request):
        
        nombreP=request.POST['txttamant']
        taman=Tamaño.objects.create(nombre_tamaño=nombreP)
        return redirect('/gestionarTaman')

    def edicionTamans(request, codigo):
        taman=Tamaño.objects.get(pk=codigo)
        return render(request, 'editar_tamans.html',{"taman":taman})

    def editarTaman(request):
        codigoD=request.POST['txtcodigot']
        nombreC=request.POST['txttamant']
        tamanObjeto=Tamaño.objects.get(pk=codigoD)
        tamanObjeto.nombre_tamaño=nombreC
        tamanObjeto.save()
        return redirect('/gestionarTaman')

    def eliminacionTamans(request, codigo):
        taman=Tamaño.objects.get(pk=codigo)
        taman.delete()

        return redirect('/gestionarTaman')

class GestionarCliente(HttpResponse):
    def gestionarClientes(request):
        listadoClientes=Cliente.objects.all()
        return render(request, "registrar_cliente.html", {"clientes":listadoClientes})

    def registrarCliente(request):
        listaD=list()
        cedula=request.POST['txtIdCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        correo=request.POST['txtcorreo']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        direccionC=Direccion.objects.get(pk=listaD[0])
        cliente=Cliente.objects.create(identificacion=cedula, nombres_cliente=nombre,apellidos_cliente=apellido,telefono_cliente=telefono,correo_cliente=correo,direccion=direccionC  )
        return redirect('/gestionarClient')

    def edicionClientes(request, codigo):
        cliente=Cliente.objects.get(pk=codigo)
        return render(request, 'editar_cliente.html',{"cliente":cliente})

    def editarCliente(request):
        listaD=list()
        cedula=request.POST['txtcodigoCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        correo=request.POST['txtcorreo']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        
        direccionC=Direccion.objects.get(pk=listaD[0])
        cliente=Cliente.objects.get(pk=cedula)
        cliente.nombres_cliente=nombre
        cliente.apellidos_cliente=apellido
        cliente.telefono_cliente=telefono
        cliente.correo_cliente=correo
        cliente.direccion=direccionC
        cliente.save()
        return redirect('/gestionarClient')

    def eliminacionClientes(request, codigo):
        cliente=Cliente.objects.get(pk=codigo)
        cliente.delete()

        return redirect('/gestionarClient')

class GestionarVendedor(HttpResponse):
    def gestionarVendedores(request):
        listadoVendedores=Vendedor.objects.all()
        return render(request, "registrar_vendedor.html", {"vendedores":listadoVendedores})

    def registrarVendedor(request):
        listaD=list()
        cedula=request.POST['txtIdCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        rut=request.POST['txtcorreo']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        direccionC=Direccion.objects.get(pk=listaD[0])
        vendedor=Vendedor.objects.create(identificacion=cedula, nombres_vendedor=nombre,apellidos_vendedor=apellido,telefono_vendedor=telefono,rut_vendedor=rut,direccion=direccionC  )
        return redirect('/gestionarVended')

    def edicionVendedores(request, codigo):
        vendedor=Vendedor.objects.get(pk=codigo)
        return render(request, 'editar_vendedores.html',{"vendedor":vendedor})

    def editarVendedor(request):
        listaD=list()
        cedula=request.POST['txtIdCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        rut=request.POST['txtcorreo']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        
        direccionC=Direccion.objects.get(pk=listaD[0])
        cliente=Vendedor.objects.get(pk=cedula)
        cliente.nombres_vendedor=nombre
        cliente.apellidos_vendedor=apellido
        cliente.telefono_vendedor=telefono
        cliente.rut_vendedor=rut
        cliente.direccion=direccionC
        cliente.save()
        return redirect('/gestionarVended')

    def eliminacionVendedores(request, codigo):
        cliente=Vendedor.objects.get(pk=codigo)
        cliente.delete()

        return redirect('/gestionarVended')

class GestionarProveedor(HttpResponse):
    def gestionarProveedores(request):
        listadoProveedores=Proveedor.objects.all()
        return render(request, "registrar_proveedor.html", {"proveedores":listadoProveedores})

    def registrarProveedor(request):
        listaD=list()
        cedula=request.POST['txtIdCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        correo=request.POST['txtcorreo']
        rut=request.POST['txtrut']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        direccionC=Direccion.objects.get(pk=listaD[0])
        proveedor=Proveedor.objects.create(identificacion=cedula, nombres_proveedor=nombre,apellidos_proveedor=apellido,telefono_proveedor=telefono, correo_proveedor=correo, rut_proveedor=rut,direccion=direccionC  )
        return redirect('/gestionarProveedor')

    def edicionProveedores(request, codigo):
        proveedor=Proveedor.objects.get(pk=codigo)
        return render(request, 'editar_proveedores.html',{"proveedor":proveedor})

    def editarProveedor(request):
        listaD=list()
        cedula=request.POST['txtIdCliente']
        nombre=request.POST['txtNombreCliente']
        apellido=request.POST['txtapellido']
        telefono=request.POST['txttelefono']
        correo=request.POST['txtcorreo']
        rut=request.POST['txtrut']
        direccionCliente=request.POST['direcc']
        listaD =direccionCliente.split(",") 
        
        direccionC=Direccion.objects.get(pk=listaD[0])
        cliente=Proveedor.objects.get(pk=cedula)
        cliente.nombres_proveedor=nombre
        cliente.apellidos_proveedor=apellido
        cliente.telefono_proveedor=telefono
        cliente.correo_proveedor=correo
        cliente.rut_proveedor=rut
        cliente.direccion=direccionC
        cliente.save()
        return redirect('/gestionarProveedor')

    def eliminacionProveedores(request, codigo):
        cliente=Proveedor.objects.get(pk=codigo)
        cliente.delete()

        return redirect('/gestionarProveedor')



class GestionarFacturaVenta(HttpResponse):
    def gestionarProductos(request):
        listadoProductos=Producto.objects.all()
        return render(request, "registrar_producto.html", {"productos":listadoProductos})

    def registrarProducto(request):
        
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']
        categoriaP=request.POST['categ']
      
        categoria=Categoria.objects.get(nombre_categoria=categoriaP)
        producto=Producto.objects.create(nombre_producto=nombreP, precio_producto=precioP,categoria_producto=categoria)
        return redirect('/gestionarProduct')

    def edicionDireciones(request, codigo):
        direccionC=Direccion.objects.get(pk=codigo)
        return render(request, 'editar_direciones.html',{"direccion":direccionC})

    def editarDireccion(request):
        codigoD=request.POST['txtcodigot']
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        ciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        
        direccionObjeto=Direccion.objects.get(pk=codigoD)
        direccionObjeto.direccion=direccionD
        direccionObjeto.barrio_sector=barrioD
        direccionObjeto.ciudad=ciudadD
        direccionObjeto.departamento_provincia=departamentoD
        direccionObjeto.codigo_postal=postalD
        direccionObjeto.save()
        return redirect('/gestionarDirecc')

    def eliminacionDireciones(request, codigo):
        direccion=Direccion.objects.get(pk=codigo)
        direccion.delete()

        return redirect('/gestionarDirecc')





class GestionarFacturaVentaProducto(HttpResponse):
    def gestionarProductos(request):
        listadoProductos=Producto.objects.all()
        return render(request, "registrar_producto.html", {"productos":listadoProductos})

    def registrarProducto(request):
        
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']
        categoriaP=request.POST['categ']
      
        categoria=Categoria.objects.get(nombre_categoria=categoriaP)
        producto=Producto.objects.create(nombre_producto=nombreP, precio_producto=precioP,categoria_producto=categoria)
        return redirect('/gestionarProduct')

    def edicionDireciones(request, codigo):
        direccionC=Direccion.objects.get(pk=codigo)
        return render(request, 'editar_direciones.html',{"direccion":direccionC})

    def editarDireccion(request):
        codigoD=request.POST['txtcodigot']
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        ciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        
        direccionObjeto=Direccion.objects.get(pk=codigoD)
        direccionObjeto.direccion=direccionD
        direccionObjeto.barrio_sector=barrioD
        direccionObjeto.ciudad=ciudadD
        direccionObjeto.departamento_provincia=departamentoD
        direccionObjeto.codigo_postal=postalD
        direccionObjeto.save()
        return redirect('/gestionarDirecc')

    def eliminacionDireciones(request, codigo):
        direccion=Direccion.objects.get(pk=codigo)
        direccion.delete()

        return redirect('/gestionarDirecc')





class GestionarFacturaCompra(HttpResponse):
    def gestionarProductos(request):
        listadoProductos=Producto.objects.all()
        return render(request, "registrar_producto.html", {"productos":listadoProductos})

    def registrarProducto(request):
        
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']
        categoriaP=request.POST['categ']
      
        categoria=Categoria.objects.get(nombre_categoria=categoriaP)
        producto=Producto.objects.create(nombre_producto=nombreP, precio_producto=precioP,categoria_producto=categoria)
        return redirect('/gestionarProduct')

    def edicionDireciones(request, codigo):
        direccionC=Direccion.objects.get(pk=codigo)
        return render(request, 'editar_direciones.html',{"direccion":direccionC})

    def editarDireccion(request):
        codigoD=request.POST['txtcodigot']
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        ciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        
        direccionObjeto=Direccion.objects.get(pk=codigoD)
        direccionObjeto.direccion=direccionD
        direccionObjeto.barrio_sector=barrioD
        direccionObjeto.ciudad=ciudadD
        direccionObjeto.departamento_provincia=departamentoD
        direccionObjeto.codigo_postal=postalD
        direccionObjeto.save()
        return redirect('/gestionarDirecc')

    def eliminacionDireciones(request, codigo):
        direccion=Direccion.objects.get(pk=codigo)
        direccion.delete()

        return redirect('/gestionarDirecc')





class GestionarFacturaCompraProducto(HttpResponse):
    def gestionarProductos(request):
        listadoProductos=Producto.objects.all()
        return render(request, "registrar_producto.html", {"productos":listadoProductos})

    def registrarProducto(request):
        
        nombreP=request.POST['txtNombreProducto']
        precioP=request.POST['txtPrecioProducto']
        categoriaP=request.POST['categ']
      
        categoria=Categoria.objects.get(nombre_categoria=categoriaP)
        producto=Producto.objects.create(nombre_producto=nombreP, precio_producto=precioP,categoria_producto=categoria)
        return redirect('/gestionarProduct')

    def edicionDireciones(request, codigo):
        direccionC=Direccion.objects.get(pk=codigo)
        return render(request, 'editar_direciones.html',{"direccion":direccionC})

    def editarDireccion(request):
        codigoD=request.POST['txtcodigot']
        direccionD=request.POST['txtdirecciont']
        barrioD=request.POST['txtbarrio']
        ciudadD=request.POST['txtciudad']
        departamentoD=request.POST['txtdepartamento']
        postalD=request.POST['txtpostal']
        
        direccionObjeto=Direccion.objects.get(pk=codigoD)
        direccionObjeto.direccion=direccionD
        direccionObjeto.barrio_sector=barrioD
        direccionObjeto.ciudad=ciudadD
        direccionObjeto.departamento_provincia=departamentoD
        direccionObjeto.codigo_postal=postalD
        direccionObjeto.save()
        return redirect('/gestionarDirecc')

    def eliminacionDireciones(request, codigo):
        direccion=Direccion.objects.get(pk=codigo)
        direccion.delete()

        return redirect('/gestionarDirecc')




class JsonData(HttpResponse):

    
    def DatosCategoria(request):
        categoria=list(Categoria.objects.values())
        return JsonResponse(categoria, safe=False)
        
    def DatosDescripcion(request):
        descripcion=list(Descripcion.objects.values())
        return JsonResponse(descripcion, safe=False)

    def DatosDirecion(request):
        direccion=list(Direccion.objects.values())
        return JsonResponse(direccion, safe=False)
        
        

