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


@login_required
def vistaVentas(request): 
   
    cliente = Cliente.objects.all()
    vistaVentas = Ventas.objects.all()
    empleado = Empleado.objects.all()
    
    return render(request, "gestionVentas.html", {"cliente": cliente, "ventas": vistaVentas, "empleado": empleado} )

@login_required
def home(request):
    return render(request,"home.html")

@login_required
def registrarVenta(request):
    if request.method == 'POST':
        idVenta = request.POST.get('txtIdVenturas')
        
        idProducto = request.POST.get('txtProducto')
        cantidadProductos = request.POST.get('txtNombre')
        descuentoVenta = request.POST.get('txtCategoria')
        precioProducto = request.POST.get('txtPrecio')
        TotalVenta = request.POST.get('txtVenta')
        
        idCliente = request.POST.get('txtClientela') 
        cliente = get_object_or_404(Cliente, pk=idCliente)
        
        idEmpleado = request.POST.get('txtEmpleados')
        empleado = get_object_or_404(Empleado, pk=idEmpleado)
        
        
        try:
            venta = Ventas.objects.create(idVenta=idVenta, idEmpleado=empleado, idCliente=cliente,
                                           idProducto=idProducto, cantidadProductos=cantidadProductos, 
                                           descuentoVenta=descuentoVenta, precioProducto=precioProducto, 
                                           TotalVenta=TotalVenta)
            messages.success(request, '¡Venta registrada!')
        except Exception as e:
            messages.error(request, f'Error al registrar la venta: {str(e)}')

    eliminarVentass = Ventas.objects.all()
    cliente = Cliente.objects.all()
    empleado = Empleado.objects.all()
    return render(request, "gestionVentas.html", {"ventas": eliminarVentass, "cliente": cliente, "empleado": empleado} )


@login_required
def eliminarVenta(request, idVenta):
    venta = Ventas.objects.get(idVenta=idVenta)
    eliminarVenta = Ventas.objects.all()
    venta.delete()
    messages.success(request, '¡Venta eliminada!')
    return render(request, "gestionVentas.html", {"ventas": eliminarVenta})
@login_required
def eliminarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    Clientesss = Cliente.objects.all()
    cliente.delete()
    messages.success(request, '¡Cliente eliminadao!') 
    return render(request, "gestionCliente.html", {"cliente": Clientesss})




@login_required
def edicionVenta(request, idVenta):
    venta = Ventas.objects.get(idVenta=idVenta)
    messages.success(request, '¡Venta actualizada!')
    return render(request, "edicionVenta.html", {"ventas": venta})
@login_required
def edicionCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    messages.success(request, '¡Cliente actualizado!')
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
def editarVenta(request):
    idVenta = request.POST['txtIdEditar']
    idEmpleado_id = request.POST['txtEmpleado']  # Obtener el ID del empleado del formulario
    idCliente_id = request.POST['txtClientes']  # Obtener el ID del cliente del formulario
    idProducto = request.POST['txtProducto']
    cantidadProductos = request.POST['txtCantidad']
    descuentoVenta = request.POST['txtDescuento']
    precioProducto = request.POST['txtPrecio']
    TotalVenta = request.POST['txtVenta']
   
    # Obtener la instancia del cliente correspondiente
    cliente = get_object_or_404(Cliente, idCliente=idCliente_id)

    # Obtener la instancia del empleado correspondiente
    empleado = get_object_or_404(Empleado, idEmpleado=idEmpleado_id)

    # Obtener la instancia de la venta que se va a editar
    venta = Ventas.objects.get(idVenta=idVenta)
    
    # Actualizar los campos de la venta con los nuevos valores
    venta.idEmpleado = empleado
    venta.idCliente = cliente
    venta.idProducto = idProducto
    venta.cantidadProductos = cantidadProductos
    venta.descuentoVenta = descuentoVenta
    venta.precioProducto = precioProducto
    venta.TotalVenta = TotalVenta
    
    # Guardar los cambios en la venta
    venta.save()
    
    # Obtener todas las ventas después de la edición
    eliminarVenta = Ventas.objects.all()
    
    return render(request, "gestionVentas.html", {"ventas": eliminarVenta})


@login_required
def vistaCliente(request): 
    Clientesss = Cliente.objects.all()
    if not request.user.is_staff:
        # Redirigir a otra página o mostrar un mensaje de error
        return render(request,"home.html")
    
    return render(request, "gestionCliente.html", {"cliente": Clientesss})


@login_required
def registrarCliente(request):
    idCliente = request.POST.get('idCliente', None)

   
    cupoCredito = request.POST['txtCupo']
    idDocumentoCli = request.POST['txtDocumento']
    idTipoComercio = request.POST['txtComercio']
    idTipoCliente = request.POST['txtTipo']
    
    
    cliente = Cliente.objects.create(idCliente=idCliente,cupoCredito=cupoCredito, idDocumentoCli=idDocumentoCli,
                                  idTipoComercio=idTipoComercio, idTipoCliente=idTipoCliente)
    Clientesss = Cliente.objects.all()
    messages.success(request, '¡Cliente registrado!')
    
    return render(request, "gestionCliente.html", {"cliente": Clientesss})




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



# Lo que hizo el mario.
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

from django.contrib.auth.models import User
from django.db import transaction

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
        usuario = request.POST.get('txtuser')
        usuario, created = Usuario.objects.get_or_create(usuario=usuario)
        if created:
            usuario.password(request.POST.get('txtpassword'))
            usuario.save()

        # Crear persona y empleado
        persona, _ = Persona.objects.get_or_create(iddocumento=request.POST.get('txtdocumento'), primernombre=request.POST.get('txtprimernombre'),
                                         segundonombre=request.POST.get('txtsegundonombre'), primerapellido=request.POST.get('txtprimerapellido'),
                                         segundoapellido=request.POST.get('txtsegundoapellido'), idcontacto=contacto, iddireccion=direccion,
                                         idgenero=genero)

        empleado = Empleado.objects.create(fechaIngreso=request.POST.get('txtfechaingreso'), fechaNacimiento=request.POST.get('txtfechanacimiento'),
                                    salario=request.POST.get('txtsalario'), rh=request.POST.get('txtrh'), idDocumentoEmp=persona,
                                    idarl=arl, ideps=eps, idFondoPension=pension, idCargoEmpleado=cargo, usuario=usuario, idrol=rol)

    cargos = CargoEmpleado.objects.all()
    genero = Genero.objects.all()
    empleados = Empleado.objects.all()
    personas = Persona.objects.all()
    fondo = Fondopension

    return render(request, "novedadesPersonal.html", {"cargos": cargos, "genero": genero, "empleados":empleados, "personas": persona})



def edicionEmpleado(request, idempleado):
    empleado=Empleado.objects.get(idempleado=idempleado)
    return render(request, "edicionEmpleado.html", {"empleado":empleado})

def editarEmpleado(request, idempleado):
    # Obtener el empleado que se va a editar
    empleado = Empleado.objects.get(idempleado=idempleado)

    if request.method == 'POST':
        # Actualizar los campos del empleado con los datos del formulario
        empleado.fechaingreso = datetime.strptime(request.POST.get('txtfechaingreso'), '%Y-%m-%d').date()
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


def eliminarEmpleado(request, idempleado):
    empleado=Empleado.objects.get(idempleado=idempleado)
    empleado.delete()
    
    return redirect('/')