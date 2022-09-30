from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class MainView(TemplateView):
    template_name = 'main.html'

class OrdenesView(TemplateView):
    template_name = 'ordenes.html'

class ProductosView(TemplateView):
    template_name = 'product.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'