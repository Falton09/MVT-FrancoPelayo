from django.db import models

# Create your models here.

class datos_family(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    familiar=models.CharField(max_length=30)
    edad=models.IntegerField()
    nacimiento=models.DateField()
    