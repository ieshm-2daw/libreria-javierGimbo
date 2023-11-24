from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Usuario(AbstractUser):
    dni= models.TextField(max_length=10)
    direccion= models.TextField()
    telefono= models.IntegerField()


    def __str__(self):
        return self.dni



class Libro(models.Model):
    titulo= models.TextField(max_length=200)
    autor= models.CharField()
    editorial= models.TextField()
    fechaPublicacion= models.DateField()
    genero= models.CharField()
    isbn= models.IntegerField()
    resumen= models.TextField()
    '''disponibilidad='''

    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    nombre= models.TextField(max_length=100)
    biografia= models.TextField()
    foto= models.ImageField()

    def __str__(self):
        return self.nombre
    
