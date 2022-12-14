from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.
class Cliente(models.Model):
    #idCliente=models.IntegerField
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre')
    direccion=models.CharField(max_length=45, verbose_name = 'Direccion')
    telefono=models.CharField(max_length=20, verbose_name = 'Telefono')
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
        return '%s' % (self.nombre)
 
class TipoPlatillo(models.Model):
    # idPlatillo=models.IntegerField
    tipo =models.CharField(max_length=45, verbose_name = 'Tipo')
    PrimerPrecio =models.DecimalField(max_digits=10, decimal_places=2)
    SegundoPrecio =models.DecimalField(max_digits=10, decimal_places=2, null=True, blank =True)
    TercerPrecio =models.DecimalField(max_digits=10, decimal_places=2, null=True, blank =True)
    descripcion =models.CharField(max_length=200, verbose_name = 'Descripcion') 
    creacion =models.DateTimeField(auto_now_add=True)
    platillo_id = models.ForeignKey(Platillo,on_delete =models.CASCADE)
    def __str__(self):
        return self.tipo



class CuadreCaja(models.Model):
    # idCaja =models.IntegerField
    disponible =models.DecimalField(max_digits=10,decimal_places=2)
    fecha =models.DateField(verbose_name = 'Fecha')
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.fecha)

class Gasto(models.Model):
     #idGasto =models.IntegerField
    #fecha =models.DateField(verbose_name = 'Fecha') 
    cantidad =models.IntegerField(default =0)
    descripcion =models.CharField(max_length=45, verbose_name = 'Descripcion') 
    monto =models.DecimalField(max_digits=10, decimal_places=2)
    total =models.DecimalField(max_digits=10, decimal_places=2)
    cuadreCaja = models.ForeignKey(CuadreCaja,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.descripcion)

class Puesto(models.Model):
    #idPuesto =models.IntegerField
    nombre =models.CharField(max_length=45, verbose_name = 'Nombre') 
    descripcion=models.CharField(max_length=45, verbose_name = 'Descripcion')
    creacion =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre


class Colaborador(models.Model):
    #idColaborador=models.IntegerField
    nombre =models.CharField(max_length=45, null= True) 
    edad= models.IntegerField (null=True, blank=True)
    direccion= models.CharField (max_length=100, null=True, blank =True)
    telefono = models.CharField (max_length=20, null=True, blank =True)
    creacion = models.DateTimeField(auto_now_add=True)
    puesto= models.ForeignKey (Puesto,null=True,on_delete=models.CASCADE)
    perfil = models.OneToOneField (User, null= True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)
        

class Orden(models.Model):
    #idOrden=models.IntegerField
    tipo=models.CharField(max_length=45, verbose_name = 'Tipo')
    estado = models.CharField(max_length=20, verbose_name="Estado")
    cliente_id = models.ForeignKey(Cliente,on_delete =models.CASCADE)
    colaborador_id = models.ForeignKey(Colaborador,on_delete =models.CASCADE)
    cuadreCaja_id = models.ForeignKey(CuadreCaja,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s %s %s' % (self.id, self.cliente_id, self.creacion)

class DetalleOrden(models.Model):
    #idDetalleOrden=models.IntegerField
    cantidad=models.IntegerField()
    sub_total =models.DecimalField(max_digits=10, decimal_places=2)
    orden_id = models.ForeignKey(Orden,on_delete =models.CASCADE)
    tipoPlatillo_id = models.ForeignKey(TipoPlatillo,on_delete =models.CASCADE)
    creacion =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.cantidad, self.tipoPlatillo_id, self.sub_total)


class Usuario(models.Model):
    #idUsuario =models.IntegerField
    perfil = models.OneToOneField (User, on_delete=models.CASCADE)

    def __str__(self):
        return self.perfil.username 
        
@receiver (post_save, sender = User)
def crear_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(perfil=instance)

@receiver (post_save, sender = User)
def guardar_usuario(sender, instance, created, **kwargs):
       instance.usuario.save()
    