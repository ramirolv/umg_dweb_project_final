from django.shortcuts import render, redirect
from django import forms 
from .models import UserProfile
from django.contrib.auth.models import User 
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView



class UserForm (forms.ModelForm):
    class Meta:
        model= User
        fields = ("username", "password")

class UserProfileForm (forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ("nombres", "apellidos", "edad", "direccion", "telefono")

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("home:mainapp")
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {"u_form":user_form, "p_form": user_profile_form})


class ListarColaboradoresView(ListView):
    template_name= 'listarestudiantes.html'
    model = UserProfile

    def get_query(self):
        return UserProfile.objects.all()