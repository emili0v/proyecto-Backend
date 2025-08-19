from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    direccion = models.CharField(max_length=250,null=False)

class lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250,null=False)
    rut = models.IntegerField(null=False)
    dig_verificador = models.CharField(max_length=1,null=False)

class autor(models.Model):
    nombre = models.CharField(max_length=250,null=False)
    