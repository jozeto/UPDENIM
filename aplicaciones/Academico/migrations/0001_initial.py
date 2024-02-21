# Generated by Django 5.0.1 on 2024-02-21 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arl',
            fields=[
                ('id_arl', models.AutoField(primary_key=True, serialize=False)),
                ('arl', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('idCargoEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('cargoEmpleado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categoriaproducto',
            fields=[
                ('idcategoriaproducto', models.AutoField(primary_key=True, serialize=False)),
                ('categoriaproducto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idciudad', models.AutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('cupoCredito', models.IntegerField()),
                ('idDocumentoCli', models.IntegerField()),
                ('idTipoComercio', models.IntegerField()),
                ('idTipoCliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idcontacto', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('idEps', models.AutoField(primary_key=True, serialize=False)),
                ('eps', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estadocomprobante',
            fields=[
                ('idestadocomprobante', models.AutoField(primary_key=True, serialize=False)),
                ('estadocomprobante', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Estadopqr',
            fields=[
                ('idestadopqr', models.AutoField(primary_key=True, serialize=False)),
                ('estadopqr', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Fondopension',
            fields=[
                ('idFondoPension', models.AutoField(primary_key=True, serialize=False)),
                ('fondoPension', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Formapago',
            fields=[
                ('idformapago', models.AutoField(primary_key=True, serialize=False)),
                ('formapago', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgenero', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('idtalla', models.AutoField(primary_key=True, serialize=False)),
                ('talla', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipocliente',
            fields=[
                ('idtipocliente', models.AutoField(primary_key=True, serialize=False)),
                ('tipocliente', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipocomercio',
            fields=[
                ('idtipocomercio', models.AutoField(primary_key=True, serialize=False)),
                ('tipocomercio', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipomovimiento',
            fields=[
                ('idtipomovimiento', models.AutoField(primary_key=True, serialize=False)),
                ('tipomovimiento', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tiponovedadpersonal',
            fields=[
                ('idtiponovedadpersonal', models.AutoField(primary_key=True, serialize=False)),
                ('novedadpersonal', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tiponovedadproducto',
            fields=[
                ('idtiponovedadproducto', models.AutoField(primary_key=True, serialize=False)),
                ('novedadproducto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipopqr',
            fields=[
                ('idtipopqr', models.AutoField(primary_key=True, serialize=False)),
                ('tipopqr', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacioninventario',
            fields=[
                ('idubicacioninventario', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacioninventario', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('iddireccion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=60)),
                ('barrio', models.CharField(max_length=45)),
                ('idciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('fechaIngreso', models.DateField()),
                ('salario', models.FloatField()),
                ('fechaNacimiento', models.DateField()),
                ('rh', models.CharField(max_length=5)),
                ('idDocumentoEmp', models.CharField(max_length=150, unique=True)),
                ('idCargoEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.cargoempleado')),
                ('idarl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.arl')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ideps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.eps')),
                ('idFondoPension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.fondopension')),
                ('idrol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('primernombre', models.CharField(max_length=45)),
                ('segundonombre', models.CharField(blank=True, max_length=45, null=True)),
                ('primerapellido', models.CharField(max_length=45)),
                ('segundoapellido', models.CharField(blank=True, max_length=45, null=True)),
                ('idcontacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.contacto')),
                ('iddireccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.direccion')),
                ('idgenero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreproducto', models.CharField(max_length=45)),
                ('precioventa', models.FloatField()),
                ('descripcionproducto', models.CharField(max_length=45)),
                ('idcategoriaproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.categoriaproducto')),
                ('idtalla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.talla')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('idcotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('fechacotizacion', models.DateTimeField(auto_now_add=True)),
                ('cantidadproductos', models.IntegerField()),
                ('valortotalproductos', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('idcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.cliente')),
                ('idempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.empleado')),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idinventario', models.AutoField(primary_key=True, serialize=False)),
                ('fechainventario', models.DateField(auto_now_add=True)),
                ('cantidadproductos', models.IntegerField()),
                ('idempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.empleado')),
                ('idproductoinv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.producto')),
                ('idtipomovimientoinv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.tipomovimiento')),
                ('idubicacioninventarioinv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.ubicacioninventario')),
            ],
        ),
        migrations.CreateModel(
            name='Novedadpersonal',
            fields=[
                ('idnovedadpersonal', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('descripcion', models.CharField(max_length=60)),
                ('idempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.empleado')),
                ('idtiponovedadpersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='novedades_personales', to='Academico.tiponovedadpersonal')),
            ],
        ),
        migrations.CreateModel(
            name='Novedadproducto',
            fields=[
                ('idnovedadproducto', models.AutoField(primary_key=True, serialize=False)),
                ('fechanovedad', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidadproductos', models.IntegerField()),
                ('idempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.empleado')),
                ('idinventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.inventario')),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.producto')),
                ('tiponovedadproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='novedades_producto', to='Academico.tiponovedadproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Pqr',
            fields=[
                ('idpqr', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateTimeField(auto_now_add=True)),
                ('motivopqr', models.CharField(max_length=250)),
                ('fechacierre', models.DateTimeField(default=None)),
                ('idcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.cliente')),
                ('iddocumentopqr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.persona')),
                ('idestadopqr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.estadopqr')),
                ('idtipopqr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.tipopqr')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioExtendido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.rol')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadProductos', models.CharField(max_length=50)),
                ('descuentoVenta', models.CharField(max_length=50)),
                ('precioProducto', models.CharField(max_length=50)),
                ('idProducto', models.CharField(max_length=50)),
                ('TotalVenta', models.CharField(max_length=50)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.cliente')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Comprobanteventa',
            fields=[
                ('idcomprobanteventa', models.AutoField(primary_key=True, serialize=False)),
                ('fechacomprobante', models.DateTimeField(auto_now_add=True)),
                ('idestadocomprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.estadocomprobante')),
                ('idformapago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.formapago')),
                ('idventa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.ventas')),
            ],
        ),
    ]