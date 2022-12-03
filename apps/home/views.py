from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.template import Template, Context
from .models import Colaborador, CuadreCaja, Gasto, Orden, Platillo, TipoPlatillo, Cliente, DetalleOrden, Puesto, Usuario
from .forms import OrdenForm, PlatilloForm, TipoPlatilloForm, ColaboradorForm, GastoForm, PuestoForm, RegistroForm
from django.contrib.auth.views import LoginView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class MainView(TemplateView):
    template_name = 'main.html'


class OrdenesView(TemplateView):
    template_name = 'ordenes.html'


class OrdenesProgresoView(CreateView, ListView):
    template_name = 'ordenes_progreso.html'
    form_class = OrdenForm
    success_url = reverse_lazy('home:ordenesapp')
    model = Orden

    def get_query(self):

        return {"orden":Orden.objects.all(), "cliente":Cliente.objects.all(), "colaborador":Colaborador.objects.all(), "cuadrecaja":CuadreCaja.objects.all()}


    def get_queryset(self):
        vEstado = self.request.GET.get('estado')
        if(vEstado):
            return {"orden":Orden.objects.filter(estado__icontains=vEstado), "cliente":Cliente.objects.all(), "colaborador":Colaborador.objects.all(), "cuadrecaja":CuadreCaja.objects.all()}
        else:
            return {"orden":Orden.objects.all(), "cliente":Cliente.objects.all(), "colaborador":Colaborador.objects.all(), "cuadrecaja":CuadreCaja.objects.all()}


def ordenNueva(request):
    tipo= request.POST['tipo']
    #estado= request.POST['estado'] Se asigna directamente
    cliente_id= Cliente.objects.get(pk=request.POST['cliente'])
    colaborador_id= Colaborador.objects.get(pk=request.POST['colaborador_id'])

    if(CuadreCaja.objects.filter(fecha=datetime.now().date()).count() == 0):
        try:
            ultimo = CuadreCaja.objects.filter(fecha__isnull=False).latest('fecha')
            nuevoCuadre = CuadreCaja(disponible=ultimo.disponible, fecha=datetime.now().date())
        except CuadreCaja.DoesNotExist:
            nuevoCuadre = CuadreCaja(disponible=0, fecha=datetime.now().date())

        nuevoCuadre.save()

    cuadrecaja_id = CuadreCaja.objects.get(fecha=datetime.now().date())
    orden = Orden(tipo=tipo, estado='Creada', cliente_id=cliente_id, colaborador_id=colaborador_id, cuadreCaja_id=cuadrecaja_id)
    orden.save()

    orden = Orden.objects.latest('creacion')

    return redirect('home:tomar_orden', orden.id)


def ordenEliminar(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()

    return redirect('home:ordenes_progreso')


def tomarOrden(request, id):
    modeloPlatillo = Platillo.objects.all()
    modeloOrden = Orden.objects.get(pk=id)
    modeloCliente = Cliente.objects.get(pk=modeloOrden.cliente_id.id)

    templateExterno = open('./apps/home/templates/ordenes_tomar_platillos.html')
    template = Template(templateExterno.read())
    contexto = Context({'orden':modeloOrden, 'platillos':modeloPlatillo, 'cliente':modeloCliente})
    documento = template.render(contexto)
    return HttpResponse(documento)


def agregarDetalleOrden(request):
    id_orden = Orden.objects.get(pk=request.POST['id_orden'])
    cantidad = request.POST['cantidad']
    tipo_platillo = TipoPlatillo.objects.get(pk=request.POST['tipoPlatillo'])
    sub_total = cantidad * tipo_platillo.PrimerPrecio

    detalle = DetalleOrden(cantidad=cantidad, sub_total=sub_total, orden_id=id_orden, tipoPlatillo_id=tipo_platillo)
    detalle.save()
    return redirect('home:tomar_orden', id_orden)


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


def ProductosView(request):
    model = Platillo
    return render(request, 'product.html' ,{'platillo':Platillo.objects.all()})


def producto_Nuevo(request):
    tipo = request.POST['tipo']
    descripcion = request.POST['descripcion']
    precio1 = request.POST['precio1']
    precio2 = request.POST['precio2']
    precio3 = request.POST['precio3']
    id_platillo = Platillo.objects.get(pk=request.POST['platillo_id'])

    plat = TipoPlatillo(tipo=tipo, descripcion=descripcion, PrimerPrecio=precio1, SegundoPrecio=precio2, TercerPrecio=precio3, platillo_id=id_platillo)
    plat.save()

    return redirect('home:productoapp')


def platillo_Formulario(request):
    return render(request, 'platillo_formulario.html')


def platillo_Nuevo(request):
    nombre_platillo = request.POST['nombrePlatillo']
    platillo = Platillo(nombre=nombre_platillo)
    platillo.save()
    return redirect('home:productoapp')


class ServiceView(TemplateView):
    template_name = 'service.html'


class TeamView(CreateView, ListView):
    template_name = 'team.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('home:teamapp')
    model = Colaborador


    def get_query(self):
        return Colaborador.objects.all()
    
def usuariodelete (request,id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect('home:teamapp')


class EditarUsuarioView(UpdateView):
    template_name = 'editarusuario.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('home:teamapp')
    model = Colaborador

class PuestoView (CreateView):
    template_name = "puesto.html"
    form_class= PuestoForm
    success_url = reverse_lazy('home:teamapp')
    model= Puesto

    def get_query(self):
        return Puesto.objects.all()

class GastoView(CreateView, ListView):
    template_name = 'gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('home:gastoapp')
    model = Gasto
    
    def get_queryset(self):
        vDescripcion =self.request.GET.get('descripcion')
        if(vDescripcion):
            return Gasto.objects.filter(descripcion__icontains=vDescripcion)
        else:
            return Gasto.objects.all()

def gastodelete (request,pk):
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
    model = TipoPlatillo
    form_class = TipoPlatilloForm
    success_url = reverse_lazy('home:productoapp')

def platillodelete (request,pk):
    Platillo = TipoPlatillo.objects.get(id=pk)
    Platillo.delete()
    return redirect('home:productoapp')

   
class PlatillosView(ListView):
    template_name = 'product.html'
    form_class = PlatilloForm
    success_url = reverse_lazy('home:gastoapp')
    model = Platillo

    def get_query(self):
        return Platillo.objects.all()



def plantillaParametros(request):
    modeloGastos = Gasto
    modeloPlatillos = TipoPlatillo
    nombre = "Curso Django"
    fechaActual = datetime.now()
    lenguajes = ["Python", "Ruby", "JavaScript"]

    #Se abri el documento que contiene la plantilla
    plantillaExterna = open('./apps/home/templates/plantillaparametros.html')

    #Se carga el documento en una variable de tipo template
    template = Template(plantillaExterna.read())
    
    #Se cierra el documento por seguridad y optimización
    plantillaExterna.close()

    #Se crea un contexto para pasarle parámetros
    contexto = Context({"nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes, "gastos": modeloGastos.objects.all(), "platillos": modeloPlatillos.objects.all()})

    #Se renderiza el documento con el contexto
    documento = template.render(contexto)
    return HttpResponse(documento)


class RegistroView (CreateView):
    model= Usuario
    form_class = RegistroForm
    success_url =reverse_lazy('home:teamapp')

class LoginView(LoginView):
    template_name = 'index.html'