from contextvars import Context
from datetime import datetime
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from .models import Colaborador, Gasto, Platillo, TipoPlatillo
from .forms import PlatilloForm, TipoPlatilloForm, ColaboradorForm, GastoForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class MainView(TemplateView):
    template_name = 'main.html'


class OrdenesView(TemplateView):
    template_name = 'ordenes.html'


class ProductosView(CreateView, ListView):
    template_name = 'product.html'
    form_class = TipoPlatilloForm
    success_url = reverse_lazy('home:productoapp')
    model = TipoPlatillo


    def get_query(self):
        return TipoPlatillo.objects.all()


""" def list_product(request, product_id):
    return HttpResponse(f"El producto seleccionado es: {product_id}") """


class ServiceView(TemplateView):
    template_name = 'service.html'


class TeamView(CreateView, ListView):
    template_name = 'team.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('home:teamapp')
    model = Colaborador


    def get_query(self):
        return Colaborador.objects.all()


class GastoView(CreateView, ListView):
    template_name = 'gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('home:gastoapp')
    model = Gasto

    def get_query(self):
        return Gasto.objects.all()

class PlatillosView(CreateView,ListView):
    template_name = 'product.html'
    form_class = PlatilloForm
    success_url = reverse_lazy('home:gastoapp')
    model = Platillo

    def get_query(self):
        return Platillo.objects.all()

"""
def plantillaParametros(request):
    nombre = "Ramiro"
    fechaActual = datetime.now()

    #Abrimos el documento de la plantilla
    plantillaExterna = open("./templates.main.html")

    #Se carga el documento en una variable de tipo plantillal
    template = Template(plantillaExterna.read())

    #Se cierra el documento por seguridad y optimización
    plantillaExterna.close()

    #Se crea un contexto - Recepción de parámetros
    contexto = Context({"nombreCanal": nombre, "fechaActual": fechaActual})

    #Se renderiza el documento
    documento = template.render(contexto)
    return HttpResponse(documento)
    """

