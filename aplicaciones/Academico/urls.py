from django.urls import path
from . import views
from .views import exit

urlpatterns = [
    
    path('home/', views.home),
    path('gestionCliente/', views.vistaCliente),
    path('gestionVentas/', views.vistaVentas),
    path('registrarVenta/', views.registrarVenta),
    path('eliminarVenta/<int:idVenta>', views.eliminarVenta, name='eliminarVenta'),
    path('eliminarCliente/<int:idCliente>', views.eliminarCliente, name='eliminarCliente'),
    path('edicionCliente/<int:idCliente>', views.edicionCliente, name='edicionCliente'),
    path('edicionVenta/<int:idVenta>',views.edicionVenta, name='edicionVenta'),
    path('editarCliente/', views.editarCliente),
    path('editarVenta/', views.editarVenta),
    path('registrarCliente/',views.registrarCliente),
    path('contacto/', views.contacto, name='contacto'),
    path('exportar/', views.exportar_a_xls, name='exportar_a_xls'),
    path('exportarClientes/', views.exportar_clientes, name='exportar_clientes'),
    path('importar_excel/', views.importar_excel, name='importar_excel'),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('edicionEmpleado/<idempleado>', views.edicionEmpleado),
    path('editarEmpleado/<int:idempleado>/', views.editarEmpleado, name='editarEmpleado'),
    path('eliminarEmpleado/<idempleado>', views.eliminarEmpleado),
    path('personal/', views.personal, name ='personal'),
    
 
  
    
    path('logout/', exit, name="exit"),
   
    
    
    ]
