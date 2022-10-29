from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView,UpdateView
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
    success_url = reverse_lazy('home:mainapp')
    model = Colaborador


    def get_query(self):
        return Colaborador.objects.all()


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

class EditarGastoView(UpdateView):
    template_name = 'editargasto.html'
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('home:gastoapp')
   

class PlatillosView(CreateView,ListView):
    template_name = 'product.html'
    form_class = PlatilloForm
    success_url = reverse_lazy('home:gastoapp')
    model = Platillo

    def get_query(self):
        return Platillo.objects.all()

