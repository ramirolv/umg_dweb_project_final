"""umg_dweb_project_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from apps.home import views
from .views import *

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='indexapp'),
    path('main/', MainView.as_view(), name='mainapp'),
    path('ordenes/', OrdenesView.as_view(), name='ordenesapp'),
    path('ordenes/nueva/', ordenNueva, name='ordenes_nueva'),
    path('ordenes/progreso/', OrdenesProgresoView.as_view(), name='ordenes_progreso'),
    path('ordenes/eliminar/<int:id>', ordenEliminar, name='ordenes_eliminar'),
    path('ordenes/platillos/<int:id>', tomarOrden, name='tomar_orden'),
    path('ordenes/detalle/eliminar/<int:id>', detalleOrdenEliminar, name='detalle_eliminar'),
    path('cliente/formulario/', clienteFormulario, name='cliente_formulario'),
    path('cliente/nuevo/', clienteNuevo, name='cliente_nuevo'),
    path('producto/', ProductosView.as_view(), name='productoapp'),
    #Ejemplo: producto/5/
    # path('producto/<int:product_id>/', views.list_product, name='productoapp'),
    path('service/', ServiceView.as_view(), name='serviceapp'),
    path('team/', TeamView.as_view(), name='teamapp'),
    path('gasto/', GastoView.as_view(), name='gastoapp'),
    path('editargastos/<int:pk>', EditarGastoView.as_view(), name='editargastoapp'),
    path('eliminargastos/<int:pk>', gastodelete, name='eliminargasto'),
    path('editar_platillo/<int:pk>', EditarPlatilloView.as_view(), name='editarplatilloapp'),
    path('eliminar_platillo/<int:pk>', views.delete, name='eliminarplatillo'),
    path('plantilla/', plantillaParametros, name='plantilla'),    
    path('puesto/', PuestoView.as_view(), name='puestoapp'),
    path('editar_usuario/<int:pk>', EditarUsuarioView.as_view(), name='editarusuarioapp'),
    path('eliminar_usuario/<int:id>', usuariodelete, name='eliminarusuario'),
]

