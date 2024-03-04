from django.urls import path
from . import views
from .views import exit

urlpatterns = [
    
    path('home/', views.home),
    path('gestionCliente/', views.vistaCliente),
    path('gestionVentas/', views.vistaVentas,name='vistaVentas'),
    path('registrarVenta/', views.registrarVenta),
    path('eliminarVenta/<int:idVenta>', views.eliminarVenta, name='eliminarVenta'),
    path('editarVenta/<int:idVenta>/', views.editarVenta, name='editarVenta'),
    path('edicionVenta/<int:idVenta>/', views.edicionVenta, name='edicionVenta'),
    
    #-------------------------------CLIENTE----------------------------------------------
    path('eliminarCliente/<int:idcliente>', views.eliminarCliente, name='eliminarCliente'),
    path('edicionCliente/<int:idcliente>', views.edicionCliente, name='edicionCliente'), 
    path('editarCliente/', views.editarCliente),
    path('registrarCliente/',views.registrarCliente, name='registrarCliente'),
    
    #---------------------------EXPORTAR E IMPORTAR---------------------------------
    path('contacto/', views.contacto, name='contacto'),
    path('exportar/', views.exportar_a_xls, name='exportar_a_xls'),
    path('exportarClientes/', views.exportar_clientes, name='exportar_clientes'),
    path('importar_excel/', views.importar_excel, name='importar_excel'),
    
#-------------------------EMPLEADO-----------------------------------------------------
    path('registrarEmpleado/', views.registrarEmpleado),
    path('edicionEmpleado/<idEmpleado>', views.edicionEmpleado),
    path('editarEmpleado/<int:idEmpleado>/', views.editarEmpleado, name='editarEmpleado'),
    path('eliminarEmpleado/<idEmpleado>', views.eliminarEmpleado),
    path('personal/', views.personal, name ='personal'),
    
    
#---------------------------------INVENTARIO-----------------------
    path('registrarInventario/', views.vistaInventario, name='vistaInventario'),
    path('edicionInventario/<idinventario>', views.edicionInventario, name='edicionInventario'),
    path('editarInventario/<int:idinventario>/', views.editarInventario, name='editarInventario'),
    path('eliminarInventario/<idinventario>', views.eliminarInventario, name='eliminarInventario'),

    
 
  
    
    path('logout/', exit, name="exit"),
   
    
    
    ]
