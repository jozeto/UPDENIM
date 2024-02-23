from django.db import models






    
    
    

class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return f"{self.rol}"
    
    


    
class Arl(models.Model):
    id_arl = models.AutoField(primary_key=True)
    arl = models.CharField(max_length=45)
    def __str__(self):
        return self.arl
    
    
class Eps(models.Model):
    idEps = models.AutoField(primary_key=True)
    eps = models.CharField(max_length=255)
    def __str__(self):
        return self.eps
    
    

class CargoEmpleado(models.Model):
    idCargoEmpleado = models.AutoField(primary_key=True)
    cargoEmpleado = models.CharField(max_length=255)
    def __str__(self):
        return self.cargoEmpleado
    
    


class Fondopension(models.Model):
    idFondoPension = models.AutoField(primary_key=True)
    fondoPension = models.CharField(max_length=255)
    def __str__(self):
        return self.fondoPension
    
class Contacto(models.Model):
    idcontacto = models.AutoField(primary_key=True)
    telefono = models.IntegerField(null=False, blank=False)
    correo = models.CharField(max_length=60)

    def __str__(self):
        texto = '{0} {1} {2}'
        return texto.format(self.idcontacto, self.telefono, self.correo)
    
class Ciudad(models.Model):
    idciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        texto = '{0} {1}'
        return texto.format(self.idciudad, self.ciudad)

class Direccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=60, null=False, blank=False)
    barrio = models.CharField(max_length=45, null=False, blank=False)
    idciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        texto = '{0} {1} {2} {3}'
        return texto.format(self.iddireccion, self.direccion, self.barrio, self.idciudad,)
    
class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=15, null=False, blank=False)
    
    def __str__(self):
        return self.genero
    
    
class Persona(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    primernombre = models.CharField(max_length=45, null=False, blank=False)
    segundonombre = models.CharField(max_length=45, blank=True, null=True)
    primerapellido = models.CharField(max_length=45, null=False, blank=False)
    segundoapellido = models.CharField(max_length=45, blank=True, null=True)
    idcontacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    iddireccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    idgenero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    

    def __str__(self):
        texto = '{0}'
        return texto.format(self.iddocumento)
    
        
class Usuario(models.Model):
    iduser = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=10, null=False, blank=False)
    password = models.CharField(max_length=10, null=False, blank=False)
    def __str__(self):
        return f"{self.usuario}"


class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    idDocumentoEmp = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fechaIngreso = models.DateField()
    salario = models.FloatField()
    fechaNacimiento = models.DateField()
    rh = models.CharField(max_length=5)
    idarl = models.ForeignKey(Arl, on_delete=models.CASCADE)
    ideps = models.ForeignKey(Eps, on_delete=models.CASCADE)
    idFondoPension = models.ForeignKey(Fondopension, on_delete=models.CASCADE)
    idCargoEmpleado = models.ForeignKey(CargoEmpleado, on_delete=models.CASCADE)
    iduser = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idrol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idEmpleado}"
    
class Tipocliente(models.Model):
    idtipocliente = models.AutoField(primary_key=True)
    tipocliente = models.CharField(max_length=45, null=False, blank=False)

class Tipocomercio(models.Model):
    idtipocomercio = models.AutoField(primary_key=True)
    tipocomercio = models.CharField(max_length=45, null=False, blank=False)
    def __str__(self):
        return f"{self.tipocomercio}"
    
    
    
class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    cupocredito = models.IntegerField()
    iddocumento = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idtipocomercio = models.ForeignKey(Tipocomercio, on_delete=models.CASCADE)
    idtipocliente = models.ForeignKey(Tipocliente,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.iddocumento}" 
    
    
class Ventas(models.Model):
    idVenta = models.AutoField(primary_key=True)
    cantidadProductos = models.CharField(max_length=50)
    descuentoVenta = models.CharField(max_length=50)
    precioProducto = models.CharField(max_length=50)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  # Corrección aquí
    idProducto = models.CharField(max_length=50)
    TotalVenta = models.CharField(max_length=50)

    def __str__(self):
        return f"Venta ID: {self.idVenta} - Cantidad Productos: {self.cantidadProductos}"
    
    
class Categoriaproducto(models.Model):
    idcategoriaproducto = models.AutoField(primary_key=True)
    categoriaproducto = models.CharField(max_length=45, blank=False, null=False)
    def __str__(self):
        return f"{self.categoriaproducto}"




class Estadocomprobante(models.Model):
    idestadocomprobante = models.AutoField(primary_key=True)
    estadocomprobante = models.CharField(max_length=45, null=False, blank=False)

class Estadopqr(models.Model):
    idestadopqr = models.AutoField(primary_key=True)
    estadopqr = models.CharField(max_length=45, null=False, blank=False)

class Formapago(models.Model):
    idformapago = models.AutoField(primary_key=True)
    formapago = models.CharField(max_length=45, null=False, blank=False)

class Tipomovimiento(models.Model):
    idtipomovimiento = models.AutoField(primary_key=True)
    tipomovimiento = models.CharField(max_length=45, null=False, blank=False)
    def __str__(self):
        return f"{self.tipomovimiento}"

class Tiponovedadpersonal(models.Model):
    idtiponovedadpersonal = models.AutoField(primary_key=True)
    novedadpersonal = models.CharField(max_length=45, null=False, blank=False)

class Tiponovedadproducto(models.Model):
    idtiponovedadproducto = models.AutoField(primary_key=True)
    novedadproducto = models.CharField(max_length=45, null=False, blank=False)

class Tipopqr(models.Model):
    idtipopqr = models.AutoField(primary_key=True)
    tipopqr = models.CharField(max_length=45, null=False, blank=False)

class Ubicacioninventario(models.Model):
    idubicacioninventario = models.AutoField(primary_key=True)
    ubicacioninventario = models.CharField(max_length=45, null=False, blank=False)
    def __str__(self):
        return f"{self.ubicacioninventario}"

class Talla(models.Model):
    idtalla = models.AutoField(primary_key=True)
    talla = models.CharField(max_length=45, null=False, blank=False)






    
class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombreproducto = models.CharField(max_length=45, null=False)
    precioventa = models.FloatField(null=False, blank=False)
    descripcionproducto = models.CharField(max_length=45)
    idcategoriaproducto = models.ForeignKey(Categoriaproducto, on_delete=models.CASCADE)
    idtalla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombreproducto}"

class Novedadpersonal(models.Model):
    idnovedadpersonal = models.AutoField(primary_key=True)
    fechainicio = models.DateField(null=False, blank=False)
    fechafin = models.DateField()
    descripcion = models.CharField(max_length=60, null=False, blank=False)
    idtiponovedadpersonal = models.ForeignKey(Tiponovedadpersonal, on_delete=models.CASCADE, related_name='novedades_personales')
    idempleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)


class Pqr(models.Model):
    idpqr = models.AutoField(primary_key=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    motivopqr = models.CharField(max_length=250, null=False, blank=False)  # Field name made lowercase.
    fechacierre = models.DateTimeField(default=None)  # Field name made lowercase.
    iddocumentopqr = models.ForeignKey(Persona, on_delete=models.CASCADE)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Field name made lowercase.
    idtipopqr = models.ForeignKey(Tipopqr, on_delete=models.CASCADE)  # Field name made lowercase.
    idestadopqr = models.ForeignKey(Estadopqr, on_delete=models.CASCADE)  # Field name made lowercase.

class Cotizaciones(models.Model):
    idcotizacion = models.AutoField(primary_key=True)  # Field name made lowercase.
    fechacotizacion = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    cantidadproductos = models.IntegerField(null=False, blank=False)  # Field name made lowercase.
    valortotalproductos = models.FloatField(null=False, blank=False)  # Field name made lowercase.
    descuento = models.IntegerField()
    idcliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)  # Field name made lowercase.
    idempleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  # Field name made lowercase.
    idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # 
    
class Inventario(models.Model):
    idinventario = models.AutoField(primary_key=True)  # Field name made lowercase.
    fechainventario = models.DateField(auto_now_add=True)  # Field name made lowercase.
    cantidadproductos = models.IntegerField(null=False, blank=False)  # Field name made lowercase.
    idproductoinv = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Field name made lowercase.
    idtipomovimientoinv = models.ForeignKey(Tipomovimiento, on_delete=models.CASCADE)  # Field name made lowercase.
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  # Field name made lowercase.
    idubicacioninventarioinv = models.ForeignKey(Ubicacioninventario, on_delete=models.CASCADE)  # Field name made lowercase.
    def __str__(self):
        return f"{self.idinventario}"

class Comprobanteventa(models.Model):
    idcomprobanteventa = models.AutoField(primary_key=True)  # Field name made lowercase.
    idventa = models.ForeignKey(Ventas, null=False,on_delete=models.CASCADE)  # Field name made lowercase.
    fechacomprobante = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    idformapago = models.ForeignKey(Formapago, on_delete=models.CASCADE)  # Field name made lowercase.
    idestadocomprobante = models.ForeignKey(Estadocomprobante, on_delete=models.CASCADE)  # Field name made lowercase.

class Novedadproducto(models.Model):
    idnovedadproducto = models.AutoField(primary_key=True)
    fechanovedad = models.DateField(auto_now_add=True, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False)
    cantidadproductos = models.IntegerField(null=False)
    tiponovedadproducto = models.ForeignKey(
        'Tiponovedadproducto',
        on_delete=models.CASCADE,
        related_name='novedades_producto'  # Cambia 'novedades_producto' a un nombre único
    )