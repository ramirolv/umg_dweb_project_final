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
from .views import HomeView, MainView, OrdenesView, ProductosView, ServiceView, TeamView, TestimonialView

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='indexapp'),
    path('main/', MainView.as_view(), name='mainapp'),
    path('ordenes/', OrdenesView.as_view(), name='ordenesapp'),
    path('producto/', ProductosView.as_view(), name='productoapp'),
    path('service/', ServiceView.as_view(), name='serviceapp'),
    path('team/', TeamView.as_view(), name='teamapp'),
    path('testimonial/', TestimonialView.as_view(), name='testimonialapp')
]
