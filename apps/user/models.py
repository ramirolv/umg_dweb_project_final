from django.db import models
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserProfile (models.Model):
    user= models.OneToOneField ( User,on_delete=models.CASCADE)
    nombres =models.CharField(max_length=50, null= True) 
    apellidos = models.CharField(max_length=50, null= True)
    edad= models.IntegerField (null=True, blank=True)
    direccion= models.CharField (max_length=200, null=True, blank =True)
    telefono = models.CharField (max_length=20, null=True, blank =True)
    
    
    def __str__(self):
        return self.user.username
        
@receiver ( post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)