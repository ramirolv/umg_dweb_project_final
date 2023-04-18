from django import forms
from .models import Cliente, Platillo, TipoPlatillo, CuadreCaja, Gasto, Orden, DetalleOrden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = '__all__'

class TipoPlatilloForm(forms.ModelForm):
    class Meta:
        model = TipoPlatillo
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


