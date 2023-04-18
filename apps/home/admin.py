from django.contrib import admin

# Register your models here.
from .models import Gasto
from .models import Cliente
from .models import Platillo
from .models import TipoPlatillo
from .models import CuadreCaja
from .models import Orden
from .models import DetalleOrden



admin.site.register(Gasto)
admin.site.register(Cliente)
admin.site.register(Platillo)
admin.site.register(TipoPlatillo)
admin.site.register(CuadreCaja)
admin.site.register(Orden)
admin.site.register(DetalleOrden)



