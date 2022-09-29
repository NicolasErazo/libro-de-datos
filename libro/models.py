from secrets import choice
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Afiliado(models.Model):
    
    nombres = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100)
    numero_documento = models.IntegerField(blank=True)
    sexo = models.CharField(max_length=2)
    telefono = models.IntegerField(blank=True)
    email = models.EmailField(max_length=100)
    direccion = models.TextField(blank=True, max_length=100)
    nacimiento = models.DateField(blank=True)
    educacion = models.TextField(blank=True, max_length=100)
    ocupacion = models.TextField(blank=True, max_length=100)
    discapacidad = models.TextField(blank=True, max_length=100)
    grupo_etnico = models.TextField(blank=True, max_length=100)
    comision_trabajo = models.TextField(blank=True, max_length=100)
    observaciones = models.TextField(blank=True, max_length=100)      
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombres + '- by: ' + self.user.username