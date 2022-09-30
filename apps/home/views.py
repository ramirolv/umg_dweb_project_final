from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import OrdenForm, PlatilloForm, ColaboradorForm, GastoForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class MainView(TemplateView):
    template_name = 'main.html'

class OrdenesView(CreateView):
    template_name = 'ordenes.html'
    form_class = OrdenForm
    success_url = reverse_lazy('home:mainapp')

class ProductosView(CreateView):
    template_name = 'product.html'
    form_class = PlatilloForm
    success_url = reverse_lazy('home:mainapp')

class ServiceView(TemplateView):
    template_name = 'service.html'

class TeamView(CreateView):
    template_name = 'team.html'
    form_class = ColaboradorForm
    success_url = reverse_lazy('home:mainapp')

class GastoView(CreateView):
    template_name = 'gasto.html'
    form_class = GastoForm
    success_url = reverse_lazy('home:mainapp')