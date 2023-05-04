from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre')
    direccion = models.CharField(max_length=45, verbose_name='Direccion')
    telefono = models.CharField(max_length=20, verbose_name='Telefono')
    DPI = models.CharField(max_length=45, verbose_name='DPI')
    NIT = models.CharField(max_length=45, verbose_name='NIT')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='especialidad', default='descarga.png', )
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion


class Tipo(models.Model):
    tipo = models.CharField(max_length=25, verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    especialidad_id = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.especialidad_id.categoria_id, self.especialidad_id, self.tipo)


class CuadreCaja(models.Model):
    disponible = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(verbose_name='Fecha')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.fecha)


class Gasto(models.Model):
    cantidad = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=45, verbose_name='Descripcion')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    colaborador_id = models.ForeignKey(User, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.descripcion)


class Orden(models.Model):
    tipo = models.CharField(max_length=45, verbose_name='Tipo')
    estado = models.CharField(max_length=20, verbose_name="Estado")
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    colaborador_id = models.ForeignKey(User, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s %s %s' % (self.id, self.cliente_id, self.creacion)


class DetalleOrden(models.Model):
    # idDetalleOrden=models.IntegerField
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    orden_id = models.ForeignKey(Orden, on_delete=models.CASCADE)
    tipo_id = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.cantidad, self.sub_total)

# class Usuario(models.Model):
#     # idUsuario =models.IntegerField
#     perfil = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.perfil.username
#
#
# @receiver(post_save, sender=User)
# def crear_usuario(sender, instance, created, **kwargs):
#     if created:
#         Usuario.objects.create(perfil=instance)
#
#
# @receiver(post_save, sender=User)
# def guardar_usuario(sender, instance, created, **kwargs):
#     instance.usuario.save()
