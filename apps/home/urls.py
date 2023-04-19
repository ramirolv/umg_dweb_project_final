from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

app_name='home'

urlpatterns = [
    #Inicio y cierre de sesión
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    #path('', LoginView.as_view(), name='indexapp'),

    # CRUD Usuarios
    path('registro/', RegistroView, name='registro'),

    path('main/', MainView, name='mainapp'),
    path('ordenes/', OrdenesView.as_view(), name='ordenesapp'),
    path('ordenes/nueva/', ordenNueva, name='ordenes_nueva'),
    path('ordenes/progreso/', OrdenesProgresoView.as_view(), name='ordenes_progreso'),
    path('ordenes/eliminar/<int:id>', ordenEliminar, name='ordenes_eliminar'),
    path('ordenes/platillos/<int:id>', tomarOrden, name='tomar_orden'),
    path('ordenes/detalle/eliminar/<int:id>', detalleOrdenEliminar, name='detalle_eliminar'),
    path('cliente/formulario/', clienteFormulario, name='cliente_formulario'),
    path('cliente/nuevo/', clienteNuevo, name='cliente_nuevo'),
    path('producto/', ProductosView, name='productoapp'),
    path('producto/nuevo/', producto_Nuevo, name='producto_nuevo'),
    path('producto/formulario/', platillo_Formulario, name='platillo_formulario'),
    path('producto/nuevo/tipo/', platillo_Nuevo, name='platillo_nuevo'),
    #Ejemplo: producto/5/
    # path('producto/<int:product_id>/', views.list_product, name='productoapp'),
    path('service/', ServiceView.as_view(), name='serviceapp'),
    path('team/', TeamView, name='teamapp'),
    path('gasto/', GastoView.as_view(), name='gastoapp'),
    path('editargastos/<int:pk>', EditarGastoView.as_view(), name='editargastoapp'),
    path('eliminargastos/<int:pk>', gastodelete, name='eliminargasto'),
    path('editar_platillo/<int:pk>', EditarPlatilloView.as_view(), name='editarplatilloapp'),
    path('eliminar_platillo/<int:pk>', platillodelete, name='eliminarplatillo'),
    path('plantilla/', plantillaParametros, name='plantilla'),
    path('editar_usuario/<int:pk>', EditarUsuarioView.as_view(), name='editarusuarioapp'),
    path('eliminar_usuario/<int:id>', usuariodelete, name='eliminarusuario'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
