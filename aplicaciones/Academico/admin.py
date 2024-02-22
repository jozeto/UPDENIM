from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import  *





admin.site.register(Genero)
admin.site.register(Rol)
admin.site.register(Arl)
admin.site.register(Eps)
admin.site.register(Fondopension)
admin.site.register(CargoEmpleado)
admin.site.register(Categoriaproducto)
admin.site.register(Ciudad)
admin.site.register(Tipocliente)
admin.site.register(Tipocomercio)
admin.site.register(Estadocomprobante)
admin.site.register(Estadopqr)
admin.site.register(Formapago)
admin.site.register(Tipomovimiento)
admin.site.register(Tiponovedadpersonal)
admin.site.register(Tiponovedadproducto)
admin.site.register(Tipopqr)
admin.site.register(Ubicacioninventario)
admin.site.register(Talla)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Novedadpersonal)
admin.site.register(Pqr)
admin.site.register(Cotizaciones)
admin.site.register(Inventario)
admin.site.register(Ventas)
admin.site.register(Comprobanteventa)
admin.site.register(Novedadproducto)


class VentasResource(resources.ModelResource):
    class Meta:
        model = Ventas
        
class VentaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = VentasResource