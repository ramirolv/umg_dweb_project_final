from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'groups']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'

class CuadreCajaForm(forms.ModelForm):
    class Meta:
        model = CuadreCaja
        fields = '__all__'

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

class RegistroForm(UserCreationForm):
       class Meta:
        model=User
        fields =(
            'username',
            'password1',
            'password2',
            )


