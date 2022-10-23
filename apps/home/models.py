from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.
class Cliente(models.Model):
    #idCliente=models.IntegerField
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre')
    telefono=models.IntegerField
    direccion=models.CharField(max_length=45, verbose_name = 'Direccion')
    DPI=models.CharField(max_length=45, verbose_name = 'DPI')
    NIT=models.CharField(max_length=45, verbose_name = 'NIT')
    creacion =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    #idPlatillo=models.IntegerField
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre')
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class TipoPlatillo(models.Model):
    # idPlatillo=models.IntegerField
    tipo =models.CharField(max_length=45, verbose_name = 'Tipo')
    precio =models.DecimalField(max_digits=5, decimal_places=2)
    creacion =models.DateTimeField(auto_now_add=True)
    platillo_id = models.ForeignKey(Platillo,on_delete =models.CASCADE)
    def __str__(self):
        return self.tipo

class CuadreCaja(models.Model):
    # idCaja =models.IntegerField
    disponible =models.DecimalField(max_digits=5, decimal_places=2)
    fecha =models.DateField(verbose_name = 'Fecha')  
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.disponible

class Gasto(models.Model):
     #idGasto =models.IntegerField
    fecha =models.DateField(verbose_name = 'Fecha') 
    cantidad =models.IntegerField(default =0)
    descripcion =models.CharField(max_length=45, verbose_name = 'Descripcion') 
    monto =models.DecimalField(max_digits=5, decimal_places=2)
    total =models.DecimalField(max_digits=5, decimal_places=2)
    cuadreCaja = models.ForeignKey(CuadreCaja,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)


class Puesto(models.Model):
    #idPuesto =models.IntegerField
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre') 
    descripcion=models.CharField(max_length=45, verbose_name = 'Descripcion')
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre


class Colaborador(models.Model):
    #idColaborador=models.IntegerField
    perfil = models.OneToOneField (User, null= True, on_delete=models.CASCADE)
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre') 
    direccion= models.CharField(max_length=45, verbose_name = 'Direccion')
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
        
@receiver ( post_save, sender = User)
def crear_colaborador(sender, instance, created, **kwargs):
        if created:
            Colaborador.objects.create(perfil=instance)

@receiver ( post_save, sender = User)
def guardar_colaborador(sender, instance, created, **kwargs):
       instance.colaborador.save()


class Orden(models.Model):
    tipo_estado=(
        ('C', 'Creada'),
        ('T', 'Terminada'),
        ('E', 'Entregada'),   
      )
    #idOrden=models.IntegerField
    fecha =models.DateField(verbose_name = 'Fecha')  
    tipo=models.CharField(max_length=45, verbose_name = 'Tipo')
    estado = models.CharField(
        max_length=1,
        choices = tipo_estado,
        default = 'C',
      )

    cliente_id = models.ForeignKey(Cliente,on_delete =models.CASCADE)
    colaborador_id = models.ForeignKey(Colaborador,on_delete =models.CASCADE)
    cuadreCaja_id = models.ForeignKey(CuadreCaja,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)

class DetalleOrden(models.Model):
    #idDetalleOrden=models.IntegerField
    cantidad=models.IntegerField
    sub_total =models.DecimalField(max_digits=5, decimal_places=2)
    orden_id = models.ForeignKey(Orden,on_delete =models.CASCADE)
    platillo_id = models.ForeignKey(Platillo,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)

