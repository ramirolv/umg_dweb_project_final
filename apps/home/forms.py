from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={"class":"form-control"}))

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
    descripcion = forms.CharField(label='Especialidad', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=200, required=True)
    imagen = forms.ImageField(label='Imagen', widget=forms.FileInput(attrs={"class":"form-control"}), required=False)
    categoria_id = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), required=True)
    
    class Meta:
        model = Especialidad
        fields = ['descripcion', 'imagen', 'categoria_id']

class TipoForm(forms.ModelForm):
    tipo = forms.CharField(label='Tipo o sabor', widget=forms.TextInput(attrs={"class":"form-control"}), max_length=200, required=True)
    precio = forms.DecimalField(label='Precio', widget=forms.NumberInput(attrs={"class":"form-control"}), max_digits=10, required=True)
    especialidad_id = forms.ModelChoiceField(queryset=Especialidad.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), required=True)
    class Meta:
        model = Tipo
        fields = ['tipo', 'precio']

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


