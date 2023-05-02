import os
from django.conf import settings
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, \
    user_passes_test  # Add the following line to the top of your code
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.template import Template, Context

from .forms import *


# Funciones para saber a qué grupo pertenece un usuario
def is_member(user):
    return user.groups.filter(name='Administrador').exists()


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['group1', 'group2']).exists()


# Vistas para inicio y cierre de sesión
class LoginView(LoginView):
    template_name = 'registration/login.html'


def LogoutView(request):
    logout(request)
    return redirect('home:login')


# MainView.
@login_required
def MainView(request):
    return render(request, 'main.html')


class OrdenesView(TemplateView):
    template_name = 'ordenes.html'


class OrdenesProgresoView(CreateView, ListView):
    template_name = 'ordenes_progreso.html'
    form_class = OrdenForm
    success_url = reverse_lazy('home:ordenesapp')
    model = Orden

    def get_query(self):

        return {"orden": Orden.objects.all(), "cliente": Cliente.objects.all(),
                "colaborador": User.objects.all(), "cuadrecaja": CuadreCaja.objects.all()}

    def get_queryset(self):
        vEstado = self.request.GET.get('estado')
        if (vEstado):
            return {"orden": Orden.objects.filter(estado__icontains=vEstado), "cliente": Cliente.objects.all(),
                    "colaborador": User.objects.all(), "cuadrecaja": CuadreCaja.objects.all()}
        else:
            return {"orden": Orden.objects.all(), "cliente": Cliente.objects.all(),
                    "colaborador": User.objects.all(), "cuadrecaja": CuadreCaja.objects.all()}


def ordenNueva(request):
    tipo = request.POST['tipo']
    # estado= request.POST['estado'] Se asigna directamente
    cliente_id = Cliente.objects.get(pk=request.POST['cliente'])
    colaborador_id = User.objects.get(pk=request.POST['colaborador_id'])

    if (CuadreCaja.objects.filter(fecha=datetime.now().date()).count() == 0):
        try:
            ultimo = CuadreCaja.objects.filter(fecha__isnull=False).latest('fecha')
            nuevoCuadre = CuadreCaja(disponible=ultimo.disponible, fecha=datetime.now().date())
        except CuadreCaja.DoesNotExist:
            nuevoCuadre = CuadreCaja(disponible=0, fecha=datetime.now().date())

        nuevoCuadre.save()

    cuadrecaja_id = CuadreCaja.objects.get(fecha=datetime.now().date())
    orden = Orden(tipo=tipo, estado='Creada', cliente_id=cliente_id, colaborador_id=colaborador_id,
                  cuadreCaja_id=cuadrecaja_id)
    orden.save()

    orden = Orden.objects.latest('creacion')

    return redirect('home:tomar_orden', orden.id)


def ordenEliminar(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()

    return redirect('home:ordenes_progreso')


def tomarOrden(request, id):
    modeloPlatillo = Categoria.objects.all()
    modeloOrden = Orden.objects.get(pk=id)
    totalOrden = 0

    for subtotal in modeloOrden.detalleorden_set.all():
        totalOrden = totalOrden + subtotal.sub_total
        
    modeloCliente = Cliente.objects.get(pk=modeloOrden.cliente_id.id)

    return render(request, 'ordenes_tomar_platillos.html', {'orden': modeloOrden, 'platillos': modeloPlatillo, 'cliente': modeloCliente, 'total': totalOrden})


def detalleordenAgregar(request):
    id_orden = Orden.objects.get(pk=request.POST['id_orden'])
    id_tipo = Tipo.objects.get(pk=request.POST['id_tipo'])
    cantidad = request.POST['inputCantidad']

    sub_total = float(cantidad) * float(id_tipo.precio)

    detalle = DetalleOrden(cantidad=cantidad, precio=id_tipo.precio, sub_total=sub_total, orden_id=id_orden, tipo_id=id_tipo)
    detalle.save()

    return redirect('home:tomar_orden', id_orden.pk)


def detalleOrdenEliminar(request, id):
    detalleOrden = DetalleOrden.objects.get(id=id)
    orden = Orden.objects.get(pk=detalleOrden.orden_id.id)
    detalleOrden.delete()

    return redirect('home:tomar_orden', orden.id)


def clienteFormulario(request):
    return render(request, './cliente_nuevo.html')


def clienteNuevo(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    dpi = request.POST['dpi']
    nit = request.POST['nit']

    cliente = Cliente(nombre=nombre, telefono=telefono, direccion=direccion, DPI=dpi, NIT=nit)
    cliente.save()

    return redirect('home:ordenes_progreso')


@login_required
def ProductosView(request):
    model = Categoria
    form = EspecialidadForm()
    return render(request, 'product.html', {'platillo': Categoria.objects.all(), 'form': form})


# ----------------- Views of Categoria -----------------
def categoria_nueva(request):
    nuevaCategoria = Categoria(nombre=request.POST['categoria'])
    nuevaCategoria.save()
    if nuevaCategoria.pk is None:
        messages.error(request, f'La categoría no se pudo crear')
    else:
        messages.success(request, f'Categoria {nuevaCategoria.nombre} creada correctamente')
    return redirect('home:productoapp')


def categoria_eliminar(request, id):
    eliminarCategoria = Categoria.objects.get(pk=id)
    eliminarCategoria.delete()
    if eliminarCategoria.pk is None:
        messages.success(request, f'Categoria {eliminarCategoria.nombre} eliminada correctamente')
    else:
        messages.error(request, f'La categoría no se pudo eliminar')
    return redirect('home:productoapp')


# ----------------- Views of Especialidad -----------------
def especialidad_nueva(request):
    form = EspecialidadForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        descripcion = form.cleaned_data['descripcion']
        messages.success(request, f'Especialidad {descripcion} creada correctamente')
    else:
        messages.error(request, f'La especialidad no se pudo crear')
    return redirect('home:productoapp')


def especialidad_eliminar(request, id):
    eliminarEspecialidad = Especialidad.objects.get(pk=id)

    rutapartes = (eliminarEspecialidad.imagen.url).split("/")
    # mi lista queda asi ['', 'media', 'peliculas', 'mi_imagen.jpg']

    try:
        # crear la ruta faltante cambiando / por \\ como el media_root
        # y no considerando el index 0 y 1 de la lista
        rutaok = "\\" + str(rutapartes[2]) + "\\" + str(rutapartes[3])

        # eliminando con la ruta correcta
        os.remove(os.path.join(settings.MEDIA_ROOT + rutaok))
    except:
        messages.error(request, 'No se encontró la imagen')
    # luego eliminar y redirigir
    eliminarEspecialidad.delete()

    if eliminarEspecialidad.pk is None:
        messages.success(request, f'Especialidad {eliminarEspecialidad.descripcion} eliminada correctamente')
    else:
        messages.error(request, f'La especialidad no se pudo eliminar')
    return redirect('home:productoapp')


class especialidad_editar(UpdateView):
    template_name = 'especialidad_editar.html'
    form_class = EspecialidadForm
    model = Especialidad
    success_url = reverse_lazy('home:productoapp')


# ----------------- Views of Tipo -----------------
def tipo_nuevo(request):
    tipo = request.POST['tipo']
    precio = request.POST['precio']
    idEspecialidad = request.POST['id_especialidad']
    especialidad = Especialidad.objects.get(pk=idEspecialidad)
    tipo_nuevo = Tipo(tipo=tipo, precio=precio, especialidad_id=especialidad)
    tipo_nuevo.save()

    if tipo_nuevo.pk is None:
        messages.success(request, f'El tipo no se pudo crear')
    else:
        messages.success(request, f'Tipo {tipo_nuevo.tipo} creado correctamente')

    return redirect('home:productoapp')


class ServiceView(TemplateView):
    template_name = 'service.html'


@login_required
@user_passes_test(is_member)  # or @user_passes_test(is_in_multiple_groups)
def TeamView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            return redirect('home:teamapp')
    else:
        form = UserRegisterForm()

    context = {'form': form, 'usuario': User.objects.all()}
    return render(request, 'team.html', context)


def usuariodelete(request, id):
    colaborador = User.objects.get(id=id)
    colaborador.delete()
    messages.success(request, f'Usuario {colaborador.first_name} eliminado correctamente')
    return redirect('home:teamapp')


class EditarUsuarioView(UpdateView):
    template_name = 'editarusuario.html'
    form_class = UserForm
    success_url = reverse_lazy('home:teamapp')
    model = User


class GastoView(CreateView, ListView):
    template_name = 'gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('home:gastoapp')
    model = Gasto

    def get_queryset(self):
        vDescripcion = self.request.GET.get('descripcion')
        if (vDescripcion):
            return Gasto.objects.filter(descripcion__icontains=vDescripcion)
        else:
            return Gasto.objects.all()


def gastodelete(request, pk):
    gasto = Gasto.objects.get(id=pk)
    gasto.delete()
    return redirect('home:gastoapp')


class EditarGastoView(UpdateView):
    template_name = 'editargasto.html'
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('home:gastoapp')


class EditarPlatilloView(UpdateView):
    template_name = 'editarplatillo.html'
    model = Tipo
    form_class = TipoForm
    success_url = reverse_lazy('home:productoapp')


def platillodelete(request, pk):
    Platillo = Tipo.objects.get(id=pk)
    Platillo.delete()
    return redirect('home:productoapp')


class PlatillosView(ListView):
    template_name = 'product.html'
    form_class = EspecialidadForm
    success_url = reverse_lazy('home:gastoapp')
    model = Especialidad

    def get_query(self):
        return Platillo.objects.all()


def plantillaParametros(request):
    modeloGastos = Gasto
    modeloPlatillos = TipoPlatillo
    nombre = "Curso Django"
    fechaActual = datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript"]

    # Se abri el documento que contiene la plantilla
    plantillaExterna = open('./apps/home/templates/plantillaparametros.html')

    # Se carga el documento en una variable de tipo template
    template = Template(plantillaExterna.read())

    # Se cierra el documento por seguridad y optimización
    plantillaExterna.close()

    # Se crea un contexto para pasarle parámetros
    contexto = Context(
        {"nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes, "gastos": modeloGastos.objects.all(),
         "platillos": modeloPlatillos.objects.all()})

    # Se renderiza el documento con el contexto
    documento = template.render(contexto)
    return HttpResponse(documento)


def RegistroView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
        else:
            form = UserCreationForm()

        context = {'form': form, 'usuario': User.objects.all()}
    return render(request, 'team.html', context)
