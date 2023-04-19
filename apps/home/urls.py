from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

app_name='home'

urlpatterns = [
    #Main View
    path('', MainView, name='mainapp'),
    
    #Inicio y cierre de sesión
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    #path('', LoginView.as_view(), name='indexapp'),

    #CRUD Usuarios
    path('team/', TeamView, name='teamapp'),
    path('usuario/nuevo/', RegistroView, name='registro'),
    path('usuario/editar/<int:pk>', EditarUsuarioView.as_view(), name='editarusuarioapp'),
    path('usuario/eliminar/<int:id>', usuariodelete, name='eliminarusuario'),

    #CRUD Categorias
    path('producto/', ProductosView, name='productoapp'), #View of List Categoria and Especialidad
    path('categoria/nueva', categoria_nueva, name='categoria_nueva'),
    path('categoria/eliminar/<int:id>', categoria_eliminar, name='categoria_eliminar'),

    #CRUD Especialidad
    path('especialidad/nueva', especialidad_nueva, name='especialidad_nueva'),
    path('especialidad/eliminar/<int:id>', especialidad_eliminar, name='especialidad_eliminar'),
    path('especialidad/editar/<int:pk>', especialidad_editar.as_view(), name='especialidad_editar'),

    
    path('ordenes/', OrdenesView.as_view(), name='ordenesapp'),
    path('ordenes/nueva/', ordenNueva, name='ordenes_nueva'),
    path('ordenes/progreso/', OrdenesProgresoView.as_view(), name='ordenes_progreso'),
    path('ordenes/eliminar/<int:id>', ordenEliminar, name='ordenes_eliminar'),
    path('ordenes/platillos/<int:id>', tomarOrden, name='tomar_orden'),
    path('ordenes/detalle/eliminar/<int:id>', detalleOrdenEliminar, name='detalle_eliminar'),
    path('cliente/formulario/', clienteFormulario, name='cliente_formulario'),
    path('cliente/nuevo/', clienteNuevo, name='cliente_nuevo'),

    #Ejemplo: producto/5/
    # path('producto/<int:product_id>/', views.list_product, name='productoapp'),
    path('service/', ServiceView.as_view(), name='serviceapp'),
    
    

    path('gasto/', GastoView.as_view(), name='gastoapp'),
    path('editargastos/<int:pk>', EditarGastoView.as_view(), name='editargastoapp'),
    path('eliminargastos/<int:pk>', gastodelete, name='eliminargasto'),
    path('editar_platillo/<int:pk>', EditarPlatilloView.as_view(), name='editarplatilloapp'),
    path('eliminar_platillo/<int:pk>', platillodelete, name='eliminarplatillo'),
    path('plantilla/', plantillaParametros, name='plantilla'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
