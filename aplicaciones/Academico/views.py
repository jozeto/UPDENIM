from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
import xlwt
import pandas as pd
from datetime import datetime
from django.db import transaction
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from decimal import Decimal
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView









class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)




@login_required
def vistaVentas(request): 
    if not request.user.is_staff:
        return render(request,"home.html")
    cliente = Cliente.objects.all()
    vistaVentas = Ventas.objects.all()
    empleado = Empleado.objects.all()
    inventarios=Inventario.objects.all()
    productos = Producto.objects.all() 
    empleado = Empleado.objects.all()
    categoriaproductos=Categoriaproducto.objects.all()
    tallas=Talla.objects.all()
    inventarios=Inventario.objects.all()
    tiposmovimientosint=Tipomovimiento.objects.all()
    ubicacionesinventario=Ubicacioninventario.objects.all()
    inventario = Inventario.objects.all()
    context = {
            "productos": productos,
            "categoriaproductos": categoriaproductos,
            "tallas": tallas,
            "inventarios": inventarios,
            "tiposmovimientosint": tiposmovimientosint,
            "ubicacionesinventario": ubicacionesinventario,
            "empleados": empleado,
            "cliente": cliente,
            "ventas": vistaVentas,
            "inventario":inventario
    }
        
    return render(request, "gestionventas.html", context)
    




@login_required
def home(request):
    return render(request,"home.html")


from .models import Producto  # Importa el modelo Producto

def registrarVenta(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            idProducto = request.POST.get('txtProducto')
            cantidadProductos = int(request.POST.get('txtNombre'))
            descuentoVenta = float(request.POST.get('txtCategoria'))
            precioProducto = float(request.POST.get('txtPrecio'))
            idCliente = int(request.POST.get('txtClientela'))
            idEmpleado = int(request.POST.get('txtEmpleados'))

            # Verificar la existencia del cliente y empleado
            cliente = get_object_or_404(Cliente, pk=idCliente)
            empleado = get_object_or_404(Empleado, pk=idEmpleado)

            # Obtener el objeto Producto
            producto = get_object_or_404(Producto, pk=idProducto)

            # Calcular el total de la venta restando el descuento del precio del producto
            totalVenta = precioProducto * cantidadProductos - descuentoVenta

            # Crear la instancia de la venta
            venta = Ventas.objects.create(
                idEmpleado=empleado,
                idCliente=cliente,
                idProducto=producto,  # Usar el objeto Producto en lugar del ID
                cantidadProductos=cantidadProductos,
                descuentoVenta=descuentoVenta,
                precioProducto=precioProducto,
                TotalVenta=totalVenta
            )

            # Actualizar el inventario
            producto_inventario = get_object_or_404(Inventario, idproductoinv=idProducto)
            producto_inventario.cantidadproductos -= cantidadProductos
            producto_inventario.save()

            messages.success(request, '¡Venta registrada exitosamente!')
        except Exception as e:
            messages.error(request, f'Error al registrar la venta: {str(e)}')


    # Obtener datos necesarios para renderizar la página
    cliente = Cliente.objects.all()
    empleado = Empleado.objects.all()
    productos = Producto.objects.all()
    categoriaproductos = Categoriaproducto.objects.all()
    tallas = Talla.objects.all()
    tiposmovimientosint = Tipomovimiento.objects.all()
    ubicacionesinventario = Ubicacioninventario.objects.all()
    vistaVentas = Ventas.objects.all()
    inventario = Inventario.objects.all()

    context = {
        "productos": productos,
        "categoriaproductos": categoriaproductos,
        "tallas": tallas,
        "tiposmovimientosint": tiposmovimientosint,
        "ubicacionesinventario": ubicacionesinventario,
        "empleados": empleado,
        "cliente": cliente,
        "ventas": vistaVentas,
        "inventario": inventario,
    }

    return render(request, "gestionventas.html", context)






@login_required
def eliminarVenta(request, idVenta):
    
    
    venta = Ventas.objects.get(idVenta=idVenta)
    eliminarVenta = Ventas.objects.all()
    venta.delete()
    messages.success(request, '¡Venta eliminada!')
    return render(request, "gestionVentas.html", {"ventas": eliminarVenta})
@login_required
def eliminarCliente(request, idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    Clientesss = Cliente.objects.all()
    cliente.delete()
    messages.success(request, '¡Cliente eliminadao!') 
    return render(request, "gestionCliente.html", {"cliente": Clientesss})




@login_required
def edicionVenta(request, idVenta):
    venta = Ventas.objects.get(idVenta=idVenta)
    
    
    cliente = Cliente.objects.all()
    inventarios=Inventario.objects.all()
    productos = Producto.objects.all() 
    empleados = Empleado.objects.all()
    categoriaproductos=Categoriaproducto.objects.all()
    tallas=Talla.objects.all()
    inventarios=Inventario.objects.all()
    tiposmovimientosint=Tipomovimiento.objects.all()
    ubicacionesinventario=Ubicacioninventario.objects.all()
    inventario = Inventario.objects.all()
    context = {
            "productos": productos,
            "categoriaproductos": categoriaproductos,
            "tallas": tallas,
            "inventarios": inventarios,
            "tiposmovimientosint": tiposmovimientosint,
            "ubicacionesinventario": ubicacionesinventario,
            "empleado": empleados,
            "cliente": cliente,
            "ventas": venta,
            "inventario":inventario
    
    }
        
    return render(request, "edicionVenta.html", context)
    
@login_required
def edicionCliente(request, idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    
    return render(request, "edicionCliente.html", {"cliente": cliente})
@login_required
def editarCliente(request):
    if request.method == 'POST':
        idCliente = request.POST.get('txtidCliente')
        cupoCredito = request.POST['txtCupo']
        idDocumentoCli = request.POST['txtDocumento']
        idTipoComercio = request.POST['txtComercio']
        idTipoCliente = request.POST['txtTipo']
        
        cliente = Cliente.objects.get(idCliente=idCliente)
        cliente.cupoCredito = cupoCredito
        cliente.idDocumentoCli = idDocumentoCli
        cliente.idTipoCliente = idTipoCliente
        cliente.idTipoComercio = idTipoComercio
        cliente.save()

        cliente = Cliente.objects.all()
        return render(request, "gestionCliente.html", {"cliente": cliente})
    else:
        # Manejar el caso en el que no es un método POST (opcional)
        return HttpResponseNotAllowed(['POST'])

@login_required
def editarVenta(request, idVenta):
    venta = Ventas.objects.get(idVenta=idVenta)

    if request.method == 'POST':
        idEmpleado_id = request.POST['txtEmpleado']
        idcliente_id = request.POST['txtClientela']
        idProducto_id = request.POST['txtProducto']
        cantidadProductos = request.POST['txtCantidad']
        descuentoVenta = request.POST['txtDescuento']
        precioProducto = request.POST['txtPrecio']
        TotalVenta = request.POST['txtVenta']

        cliente = get_object_or_404(Cliente, idcliente=idcliente_id)
        empleado = get_object_or_404(Empleado, idEmpleado=idEmpleado_id)
        producto = get_object_or_404(Producto, idproducto=idProducto_id)

        venta.idEmpleado = empleado
        venta.idCliente = cliente
        venta.idProducto = producto
        venta.cantidadProductos = cantidadProductos
        venta.descuentoVenta = descuentoVenta
        venta.precioProducto = precioProducto

        # Recalcula el precio total de la venta
        precio_total = (Decimal(precioProducto) * Decimal(cantidadProductos)) - Decimal(descuentoVenta)
        venta.TotalVenta = precio_total

        venta.save()

        messages.success(request, '¡Venta actualizada!')

    cliente = Cliente.objects.all()
    empleado = Empleado.objects.all()
    productos = Producto.objects.all()
    categoriaproductos = Categoriaproducto.objects.all()
    tallas = Talla.objects.all()
    tiposmovimientosint = Tipomovimiento.objects.all()
    ubicacionesinventario = Ubicacioninventario.objects.all()
    vistaVentas = Ventas.objects.all()
    inventario = Inventario.objects.all()

    context = {
        "productos": productos,
        "categoriaproductos": categoriaproductos,
        "tallas": tallas,
        "tiposmovimientosint": tiposmovimientosint,
        "ubicacionesinventario": ubicacionesinventario,
        "empleados": empleado,
        "cliente": cliente,
        "ventas": vistaVentas,
        "inventario": inventario,
    }

    return render(request, "gestionventas.html", context)



@login_required
def vistaCliente(request): 
    cliente = Cliente.objects.all()
    persona = Persona.objects.all()
    empleados = Empleado.objects.all()
    cargos = CargoEmpleado.objects.all()
    arls=Arl.objects.all()
    pension=Fondopension.objects.all()
    users=User.objects.all()
    rols=Rol.objects.all()
    genero=Genero.objects.all()
    comercio=Tipocomercio.objects.all()
    tipocliente=Tipocliente.objects.all()
    context = {
        "empleados": empleados,
        "cargos": cargos,
        "arls": arls,
        "pension": pension,
        "users": users,
        "rols": rols,
        "persona": persona,
        "cliente": cliente,
        "genero": genero,
        "comercio":comercio,
        "tipocliente":tipocliente,
        
    }
    
    return render(request, "gestionCliente.html", context)
    
    

@login_required
def registrarCliente(request):
    Clientesss = Cliente.objects.all()
    persona = Persona.objects.all()
    tipos_cliente = Tipocliente.objects.all()  # Obtener todos los tipos de cliente

    if request.method == 'POST':
        idcliente = request.POST.get('idCliente', None)
        cupocredito = request.POST.get('txtCupo', None)
        iddocumento = request.POST.get('txtdocumento', None)
        idtipocomercio_nombre = request.POST.get('txtComercio', None)
        idtipocliente_nombre = request.POST.get('txtTipo', None)  # Obtener el nombre del tipo de cliente

        if cupocredito and iddocumento and idtipocomercio_nombre and idtipocliente_nombre:
            try:
                with transaction.atomic():
                    # Obtener o crear instancia de Contacto
                    contacto, _ = Contacto.objects.get_or_create(telefono=request.POST.get('txttelefono'), correo=request.POST.get('txtcorreo'))

                    # Obtener o crear instancia de Ciudad
                    ciudad, _ = Ciudad.objects.get_or_create(ciudad=request.POST.get('txtciudad'))

                    # Crear instancia de Direccion
                    direccion = Direccion.objects.create(direccion=request.POST.get('txtdireccion'), barrio=request.POST.get('txtbarrio'), idciudad=ciudad)

                    # Obtener o crear instancia de Genero
                    genero_nombre = request.POST.get('txtgenero')
                    genero, _ = Genero.objects.get_or_create(genero=genero_nombre)

                    # Obtener la instancia de Persona correspondiente al documento proporcionado
                    persona_instancia, _ = Persona.objects.get_or_create(iddocumento=iddocumento, primernombre=request.POST.get('txtprimernombre'),
                                                         segundonombre=request.POST.get('txtsegundonombre'), primerapellido=request.POST.get('txtprimerapellido'),
                                                         segundoapellido=request.POST.get('txtsegundoapellido'), idcontacto=contacto, iddireccion=direccion,
                                                         idgenero=genero)

                    # Obtener la instancia de Tipocomercio correspondiente al nombre proporcionado
                    tipocomercio_instancia = get_object_or_404(Tipocomercio, tipocomercio=idtipocomercio_nombre)

                    # Obtener la instancia de Tipocliente correspondiente al nombre proporcionado
                    tipocliente_instancia = Tipocliente.objects.get(tipocliente=idtipocliente_nombre)

                    # Crear instancia de Cliente con los argumentos correctos
                    cliente = Cliente.objects.create(iddocumento=persona_instancia, cupocredito=cupocredito, idtipocomercio=tipocomercio_instancia, idtipocliente=tipocliente_instancia)
                    
                    messages.success(request, '¡Cliente registrado!')

            except IntegrityError as e:
                if 'unique constraint' in str(e):
                    messages.error(request, 'Ya existe un cliente con ese número de documento.')
                else:
                    messages.error(request, f'Error al registrar el cliente: {str(e)}')
        else:
            messages.error(request, 'Faltan datos para registrar el cliente.')

    return render(request, "gestionCliente.html", {"cliente": Clientesss, "persona": persona, "tipos_cliente": tipos_cliente})


@login_required
def login(request):
    return(render(request,'registration/login.html' ))

def exit(request):
    logout(request)
    return redirect('login')
@login_required
def contacto(request):
    
    if not request.user.is_staff:
        # Redirigir a otra página o mostrar un mensaje de error
        return render(request,"home.html")
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        
        recipient_list = ['sebastiansalgado404@gmail.com']
        send_mail(
            'UP DENIM',  # Asunto del correo
            message,  # Cuerpo del correo
            settings.EMAIL_HOST_USER,  # Email del remitente
            [email],  # Lista de destinatarios
            fail_silently=False,
        )
        
        messages.success(request, 'Se ha enviado el correo')
        
    return render(request, 'contacto.html')


def exportar_a_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ventas.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    hoja = wb.add_sheet('Ventas')

    ventas = Ventas.objects.all()
    clientes = Cliente.objects.all()  # Corrección aquí

    # Escribir encabezados
    hoja.write(0, 0, 'ID Venta')
    hoja.write(0, 1, 'Cantidad Productos')
    hoja.write(0, 2, 'Descuento Venta')
    hoja.write(0, 3, 'Precio Producto')
    hoja.write(0, 4, 'ID Cliente')
    hoja.write(0, 5, 'ID Empleado')

    # Escribir datos de ventas
    for row, venta in enumerate(ventas, start=1):
        hoja.write(row, 0, venta.idVenta)
        hoja.write(row, 1, venta.cantidadProductos)
        hoja.write(row, 2, venta.descuentoVenta)
        hoja.write(row, 3, venta.precioProducto)
        hoja.write(row, 4, venta.idCliente_id)  # Cambio aquí
        hoja.write(row, 5, venta.idEmpleado_id)

    wb.save(response)
    return response


def exportar_clientes(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clientes.xls"'

    libro = xlwt.Workbook(encoding='utf-8')
    hoja_clientes = libro.add_sheet('Clientes')

    # Encabezados de clientes
    encabezados_clientes = ['ID Cliente', 'Cupo Crédito', 'ID Documento Cliente', 'ID Tipo Comercio', 'ID Tipo Cliente']
    for col, encabezado in enumerate(encabezados_clientes):
        hoja_clientes.write(0, col, encabezado)

    # Datos de clientes
    clientes = Cliente.objects.all()
    for row, cliente in enumerate(clientes, start=1):
        hoja_clientes.write(row, 0, cliente.idCliente)
        hoja_clientes.write(row, 1, cliente.cupoCredito)
        hoja_clientes.write(row, 2, cliente.idDocumentoCli)
        hoja_clientes.write(row, 3, cliente.idTipoComercio)
        hoja_clientes.write(row, 4, cliente.idTipoCliente)

    libro.save(response)
    return response
def importar_excel(request):
    if request.method == 'POST' and request.FILES['archivo_excel']:
        archivo_excel = request.FILES['archivo_excel']
        df = pd.read_excel(archivo_excel)

        for index, row in df.iterrows():
            try:
                cliente = Cliente.objects.get(idCliente=row.get('ID Cliente'))
            except Cliente.DoesNotExist:
                cliente = None

            # Usar get() con un valor por defecto None para evitar KeyError
            venta, creado = Ventas.objects.get_or_create(
                idVenta=row.get('ID Venta'),
                idEmpleado=row.get('ID Empleado'),
                idProducto=row.get('ID Producto'),
                cantidadProductos=row.get('Cantidad Productos'),
                descuentoVenta=row.get('Descuento Venta'),
                precioProducto=row.get('Precio Producto'),
                TotalVenta=row.get('Total Venta'),
                idCliente=cliente
            )

        # Mostrar un mensaje de éxito
        messages.success(request, 'Datos importados correctamente')

    # Mover la declaración de eliminarVenta aquí para que contenga los datos actualizados
    eliminarVenta = Ventas.objects.all()

    return render(request, "gestionVentas.html", {"ventas": eliminarVenta})



# Lo que hizo el mario.----------------------REGISTRAR EMPLEADO----------------------------------------------------------
def personal(request):
    empleados = Empleado.objects.all()
    cargos = CargoEmpleado.objects.all()
    arls=Arl.objects.all()
    pension=Fondopension.objects.all()
    users=User.objects.all()
    rols=Rol.objects.all()
    persona=Persona.objects.all()
    context = {
        "empleados": empleados,
        "cargos": cargos,
        "arls": arls,
        "pension": pension,
        "users": users,
        "rols": rols,
        "persona": persona,
    }
    
    return render(request, "novedadesPersonal.html", context)


@transaction.atomic
def registrarEmpleado(request):
    if request.method == 'POST':
        # Obtener o crear objetos relacionados
        ciudad, _ = Ciudad.objects.get_or_create(ciudad=request.POST.get('txtciudad'))
        direccion = Direccion.objects.create(direccion=request.POST.get('txtdireccion'), barrio=request.POST.get('txtbarrio'), idciudad=ciudad)

        contacto, _ = Contacto.objects.get_or_create(telefono=request.POST.get('txttelefono'), correo=request.POST.get('txtcorreo'))
        genero_nombre = request.POST.get('txtgenero')
        genero, _ = Genero.objects.get_or_create(genero=genero_nombre)

        cargo_nombre = request.POST.get('txtcargo')
        cargo, _ = CargoEmpleado.objects.get_or_create(cargoEmpleado=cargo_nombre)

        rol, _ = Rol.objects.get_or_create(rol=request.POST.get('txtrolus'))
        eps, _ = Eps.objects.get_or_create(eps=request.POST.get('txteps'))
        arl, _ = Arl.objects.get_or_create(arl=request.POST.get('txtarl'))
        pension, _ = Fondopension.objects.get_or_create(fondoPension=request.POST.get('txtpension'))

        # Obtener o crear usuario
        usuario_nombre = request.POST.get('txtuser')
        password = request.POST.get('txtpassword')
        usuario, _ = Usuario.objects.get_or_create(usuario=usuario_nombre, password=password)

        # Crear persona y empleado
        persona, _ = Persona.objects.get_or_create(iddocumento=request.POST.get('txtdocumento'), primernombre=request.POST.get('txtprimernombre'),
                                         segundonombre=request.POST.get('txtsegundonombre'), primerapellido=request.POST.get('txtprimerapellido'),
                                         segundoapellido=request.POST.get('txtsegundoapellido'), idcontacto=contacto, iddireccion=direccion,
                                         idgenero=genero)

        empleado = Empleado.objects.create(fechaIngreso=request.POST.get('txtfechaingreso'), fechaNacimiento=request.POST.get('txtfechanacimiento'),
                                    salario=request.POST.get('txtsalario'), rh=request.POST.get('txtrh'), idDocumentoEmp=persona,
                                    idarl=arl, ideps=eps, idFondoPension=pension, idCargoEmpleado=cargo, iduser=usuario, idrol=rol)

    cargos = CargoEmpleado.objects.all()
    genero = Genero.objects.all()
    empleados = Empleado.objects.all()
    personas = Persona.objects.all()
    fondo = Fondopension

    return render(request, "novedadesPersonal.html", {"cargos": cargos, "genero": genero, "empleados":empleados, "personas": personas})



def edicionEmpleado(request, idempleado):
    empleado=Empleado.objects.get(idempleado=idempleado)
    return render(request, "edicionEmpleado.html", {"empleado":empleado})

def editarEmpleado(request, idempleado):
    # Obtener el empleado que se va a editar
    empleado = Empleado.objects.get(idempleado=idempleado)

    if request.method == 'POST':
        # Actualizar los campos del empleado con los datos del formulario
        idempleado.fechaingreso = datetime.strptime(request.POST.get('txtfechaingreso'), '%Y-%m-%d').date()
        empleado.fechanacimiento = datetime.strptime(request.POST.get('txtfechanacimiento'), '%Y-%m-%d').date()

        # Acceder a los atributos del modelo relacionado
        empleado.iddocumento.primernombre = request.POST.get('txtprimernombre')
        empleado.iddocumento.segundonombre = request.POST.get('txtsegundonombre')
        empleado.iddocumento.primerapellido = request.POST.get('txtprimerapellido')
        empleado.iddocumento.segundoapellido = request.POST.get('txtsegundoapellido')

        # Guardar el contacto asociado al empleado
        empleado.iddocumento.idcontacto.telefono = request.POST.get('txttelefono')
        empleado.iddocumento.idcontacto.correo = request.POST.get('txtcorreo')

        # Guardar la dirección asociada al empleado
        empleado.iddocumento.iddireccion.direccion = request.POST.get('txtdireccion')
        empleado.iddocumento.iddireccion.barrio = request.POST.get('txtbarrio')
        empleado.iddocumento.iddireccion.idciudad.ciudad = request.POST.get('txtciudad')

        empleado.idcargoempleado.cargoempleado = request.POST.get('txtcargo')
        empleado.salario = request.POST.get('txtsalario')
        empleado.rh = request.POST.get('txtrh')
        empleado.ideps.eps = request.POST.get('txteps')
        empleado.idarl.arl = request.POST.get('txtarl')
        empleado.ifondopension.fondopension = request.POST.get('txtpension')
        empleado.iduser.user = request.POST.get('txtuser')
        empleado.iduser.password = request.POST.get('txtpassword')
        empleado.idrol.rol = request.POST.get('txtrolus')

        # Guardar los cambios
        empleado.save()
        empleado.iddocumento.save() # Guardar el documento relacionado
        empleado.iddocumento.idcontacto.save() # Guardar el contacto relacionado
        empleado.iddocumento.iddireccion.save() # Guardar la dirección relacionada
        empleado.idcargoempleado.save() # Guardar el cargo del empleado
        empleado.ideps.save() # Guardar la EPS
        empleado.idarl.save() # Guardar la ARL
        empleado.ifondopension.save() # Guardar el fondo de pensiones
        empleado.iduser.save() # Guardar el usuario relacionado
        empleado.idrol.save() # Guardar el rol

        return redirect('/')  # Redirige a la página principal

    # Si no es una solicitud POST, renderiza la página de edición con los datos del empleado
    return render(request, 'edicionEmpleado.html', {'empleado': empleado})


def eliminarEmpleado(request, idEmpleado):
    empleado=Empleado.objects.get(idEmpleado=idEmpleado)
    empleado.delete()
    
    return redirect('/')



# -------------------------------------INVENTARIO---------------------------------------
def inventarioss(request):
    inventarios=Inventario.objects.all()
    productos = Producto.objects.all()
    empleado = Empleado.objects.all()
    categoriaproductos=Categoriaproducto.objects.all()
    tallas=Talla.objects.all()
    inventarios=Inventario.objects.all()
    ubicacionesinventario=Ubicacioninventario.objects.all()
    tipo=Tipomovimiento.objects.all()
    talla=Talla.objects.all()
    categoria=Categoriaproducto.objects.all()
    context = {
        "productos": productos,
        "categoriaproductos": categoriaproductos,    
        "inventarios": inventarios,
        "ubicacionesinventario": ubicacionesinventario,
        "empleados": empleado,
        "tipo":tipo,
        "talla":talla,
        "categoria":categoria,
    }
    
    return render(request, "gestionInventario.html", context)

def vistaInventario(request):

    if request.method == "GET":
        # Obtener todos los productos, empleados e inventarios
        productos = Producto.objects.all()
        empleados = Empleado.objects.all()
        inventarios = Inventario.objects.all()
        ubicacionesinventario=Ubicacioninventario.objects.all()
        tipo=Tipomovimiento.objects.all()
        talla=Talla.objects.all()
        categoria=Categoriaproducto.objects.all()

        
        # Renderizar la plantilla con los datos obtenidos
        return render(request, "gestionInventario.html", {
            "productos": productos,
            "empleados": empleados,
            "inventarios": inventarios,
            "ubicacionesinventario": ubicacionesinventario,
            "tipo":tipo,
            "talla":talla,
            "categoria":categoria,

        })
    else:
        
        return registrarInventario(request)
        
        


def registrarInventario(request):
  

    if request.method == 'POST':
        # Obtener datos del formulario
        fechainventario = request.POST.get('txtfechainventario')
        cantidadproductos = request.POST.get('txtcantidadproductos')
        nombreproducto = request.POST.get('txtnombreproducto')
        precioventa = request.POST.get('txtprecioventa')
        descripcionproducto = request.POST.get('txtdescripcionproducto')
        categoriaproducto = request.POST.get('txtcategoriaproducto')
        talla = request.POST.get('txttalla')
        tipomovimiento = request.POST.get('txttipomovimiento')
        ubicacioninventario = request.POST.get('txtubicacioninventario')
        idEmpleado = request.POST.get('txtidempleado')

        # Validar datos
        errores = {}
        if not fechainventario:
            errores['txtfechainventario'] = 'La fecha es obligatoria.'
        if not cantidadproductos:
            errores['txtcantidadproductos'] = 'La cantidad es obligatoria.'
        if not nombreproducto:
            errores['txtnombreproducto'] = 'El nombre del producto es obligatorio.'
        if not precioventa:
            errores['txtprecioventa'] = 'El precio de venta es obligatorio.'
        if not categoriaproducto:
            errores['txtcategoriaproducto'] = 'La categoría del producto es obligatoria.'
        if not talla:
            errores['txttalla'] = 'La talla del producto es obligatoria.'
        if not tipomovimiento:
            errores['txttipomovimiento'] = 'El tipo de movimiento es obligatorio.'
        if not ubicacioninventario:
            errores['txtubicacioninventario'] = 'La ubicación del inventario es obligatoria.'
        if not idEmpleado:
            errores['txtidempleado'] = 'El ID del empleado es obligatorio.'

        if errores:
            # Mostrar errores en la vista
            context = {'errores': errores}
            return render(request, "gestionInventario.html", context)

        # Obtener o crear objetos relacionados
        try:
            categoria = Categoriaproducto.objects.get(categoriaproducto=categoriaproducto)
        except Categoriaproducto.DoesNotExist:
            categoria = Categoriaproducto.objects.create(categoriaproducto=categoriaproducto)

        try:
            talla = Talla.objects.get(talla=talla)
        except Talla.DoesNotExist:
            talla = Talla.objects.create(talla=talla)

        try:
            ubicacioninventario = Ubicacioninventario.objects.get(ubicacioninventario=ubicacioninventario)
        except Ubicacioninventario.DoesNotExist:
            ubicacioninventario = Ubicacioninventario.objects.create(ubicacioninventario=ubicacioninventario)

        try:
            empleado = Empleado.objects.get(idEmpleado=idEmpleado)
        except Empleado.DoesNotExist:
            empleado = Empleado.objects.create(idEmpleado=idEmpleado)

        try:
            # Intenta recuperar el Tipomovimiento
            tipomovimiento_obj = Tipomovimiento.objects.get(tipomovimiento=tipomovimiento)
        except Tipomovimiento.DoesNotExist:
            # Si no existe, crea uno nuevo
            tipomovimiento_obj = Tipomovimiento.objects.create(tipomovimiento=tipomovimiento)
        except MultipleObjectsReturned:
            # Si se devuelve más de un objeto, maneja el caso aquí
            # Por ejemplo, puedes tomar el primero de la lista
            tipomovimiento_obj = Tipomovimiento.objects.filter(tipomovimiento=tipomovimiento).first()

        # Crear el producto
        try:
            producto = Producto.objects.get(nombreproducto=nombreproducto)
        except Producto.DoesNotExist:
            # Producto no encontrado, mostrar mensaje de error o manejar de otra manera
            messages.error(request, 'El producto no existe.')
            return redirect('ruta_de_la_vista_de_inventario')  # Redirigir a la página de inventario o a donde sea necesario

        # Crear el inventario
        inventario = Inventario.objects.create(fechainventario=fechainventario, cantidadproductos=cantidadproductos, 
                                        idproductoinv=producto, idtipomovimientoinv=tipomovimiento_obj, idEmpleado=empleado, 
                                        idubicacioninventarioinv=ubicacioninventario)


        # Obtener datos para la vista
    inventarios=Inventario.objects.all()
    productos = Producto.objects.all()
    empleado = Empleado.objects.all()
    categoriaproductos=Categoriaproducto.objects.all()
    tallas=Talla.objects.all()
    inventarios=Inventario.objects.all()
    ubicacionesinventario=Ubicacioninventario.objects.all()
    tipo=Tipomovimiento.objects.all()
    talla=Talla.objects.all()
    categoria=Categoriaproducto.objects.all()
    context = {
        "productos": productos,
        "categoriaproductos": categoriaproductos,    
        "inventarios": inventarios,
        "ubicacionesinventario": ubicacionesinventario,
        "empleados": empleado,
        "tipo":tipo,
        "talla":talla,
        "categoria":categoria,
    }
    
    return render(request, "gestionInventario.html", context)
    

def edicionInventario(request, idinventario):
    inventario=Inventario.objects.get(idinventario=idinventario)
    
    productos = Producto.objects.all()
    empleado = Empleado.objects.all()
    categoriaproductos=Categoriaproducto.objects.all()
    talla=Talla.objects.all()
    
    ubicacionesinventario=Ubicacioninventario.objects.all()
    tipo=Tipomovimiento.objects.all()
    talla=Talla.objects.all()
    categoria=Categoriaproducto.objects.all()
    context = {
        "productos": productos,
        "categoriaproductos": categoriaproductos,    
        "inventarios": inventario,
        "ubicacionesinventario": ubicacionesinventario,
        "empleados": empleado,
        "tipo":tipo,
        "talla":talla,
        "categoria":categoria,
    }
    
    return render(request, "edicionInventario.html", context)


def editarInventario(request, idinventario):
    # Obtener el inventario que se va a editar
    inventario = Inventario.objects.get(idinventario=idinventario)

    if request.method == 'POST':
        # Actualizar los campos del inventario con los datos del formulario
        inventario.fechainventario = datetime.strptime(request.POST.get('txtfechainventario'), '%Y-%m-%d').date()
        
        # Acceder a los atributos del modelo relacionado Producto
        inventario.idproductoinv.nombreproducto = request.POST.get('txtnombreproducto')
        precio_venta_str = request.POST.get('txtprecioventa')
        if precio_venta_str:
            # Reemplazar la coma por un punto y convertir a flotante
            precio_venta = float(precio_venta_str.replace(',', '.'))

            # Asignar el valor convertido al campo
            inventario.idproductoinv.precioventa = precio_venta
        inventario.idproductoinv.descripcionproducto = request.POST.get('txtdescripcionproducto')
        
        # Guardar el contacto asociado al empleado
        inventario.idproductoinv.idcategoriaproducto.categoriaproducto = request.POST.get('txtcategoriaproducto')
        tipo_movimiento = request.POST.get('txttipomovimiento')
        tipo_movimiento_instancia, created = Tipomovimiento.objects.get_or_create(tipomovimiento=tipo_movimiento)
        inventario.idtipomovimientoinv = tipo_movimiento_instancia
        
        ubicacion_inventario = request.POST.get("txtubicacioninventario")
        ubicacion_inventario_instancia, created = Ubicacioninventario.objects.get_or_create(ubicacioninventario=ubicacion_inventario)
        inventario.idubicacioninventarioinv = ubicacion_inventario_instancia
        # Guardar la dirección asociada al empleado
        inventario.idproductoinv.idtalla.talla = request.POST.get('txttalla')

        inventario.cantidadproductos = request.POST.get('txtcantidadproductos')

        # Obtener el id del empleado del formulario
        idEmpleado = request.POST.get('txtidempleado')

        # Obtener o crear el objeto Empleado
        empleado_obj, created = Empleado.objects.get_or_create(idEmpleado=idEmpleado)

        # Asignar el objeto Empleado al inventario
        inventario.idempleado = empleado_obj

        # Guardar los cambios
        inventario.save()
        inventario.idproductoinv.save() # Guardar el producto relacionado
        inventario.idproductoinv.idcategoriaproducto.save() # Guardar la categoría de producto relacionada
        inventario.idtipomovimientoinv.save()
        inventario.idproductoinv.idtalla.save() # Guardar la talla relacionada

        return redirect('vistaInventario')  # Redirige a la página principal

    # Si no es una solicitud POST, renderiza la página de edición con los datos del inventario
    

    return render(request, "gestionInventario.html")




def eliminarInventario(request, idinventario):
    inventario = Inventario.objects.get(idinventario=idinventario)
    inventario.delete()
    
    messages.success(request, '¡Inventario eliminado correctamente!')

    # Redirigir a la página anterior
    return redirect('vistaInventario') 

    