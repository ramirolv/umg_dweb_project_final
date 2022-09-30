from django import forms
from .models import Cliente, Platillo, TipoPlatillo, CuadreCaja, Gasto, Puesto, Colaborador, Orden, DetalleOrden, Usuario

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

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__'

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrden
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
