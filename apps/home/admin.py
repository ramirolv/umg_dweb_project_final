from django.contrib import admin

# Register your models here.
from .models import Gasto
from .models import Cliente
from .models import Categoria
from .models import Especialidad
from .models import Tipo
from .models import CuadreCaja
from .models import Orden
from .models import DetalleOrden



admin.site.register(Gasto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Especialidad)
admin.site.register(Tipo)
admin.site.register(CuadreCaja)
admin.site.register(Orden)
admin.site.register(DetalleOrden)



