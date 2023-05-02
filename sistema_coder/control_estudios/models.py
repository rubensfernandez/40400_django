from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=64) # Equivalente de str
    comision = models.IntegerField()  # Equivalente de int (numero entero)

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=158)
    bio = models.TextField()  # es un archivo de texto

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False) # equivalente a un boogleano
