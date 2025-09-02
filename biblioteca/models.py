from django.db import models

# Create your models here.
from django.db import models

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)
    detalles = models.TextField(null=True)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=255, null=False)
    nacionalidad = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=250, null=False)

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=255, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lector(models.Model):
    rut = models.IntegerField(null=False)
    digito_verificador = models.CharField(max_length=1, null=False)
    nombre_lector = models.CharField(max_length=255, null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=False)
    fecha_entrega = models.DateTimeField(auto_now=True)

