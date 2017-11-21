from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Maestro(models.Model):
    nombre = models.CharField(max_length=200)
    dpi = models.CharField(max_length=200, unique=True)
    nocuenta = models.CharField(max_length=200)
    direccion = models.TextField(max_length=255)
    especialidad = models.TextField()
    salario = models.TextField()
    estado = models.BooleanField(default = True)
    def guardar(self):
        self.save()

    def __str__(self):
        return self.nombre



class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    periodos = models.CharField(max_length=200)
    maestro = models.ForeignKey(Maestro, on_delete = models.CASCADE)
    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre
class Grado(models.Model):
    nombre = models.CharField(max_length=200)
    aula = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    materias = models.ManyToManyField(Materia, through = 'MateriasGrados')
    estado = models.BooleanField(default = True)
    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nocarnet = models.CharField(max_length=200)
    encargado = models.CharField(max_length=200)
    numencargado = models.CharField(max_length=200)
    grado = models.ForeignKey(Grado, on_delete = models.CASCADE)
    estado = models.BooleanField(default = True)
    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre
class MateriasCursadas(models.Model):
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete= models.CASCADE)
    punteo = models.TextField()
    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre

class MateriasGrados(models.Model):
    materias = models.ForeignKey(Materia, on_delete = models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete = models.CASCADE)

class materiasLinea(admin.TabularInline):
    model = Grado
    extra = 1

class GradoAdmin(admin.ModelAdmin):
    inlines = (materiasLinea,)
class MateriaAdmin(admin.ModelAdmin):
    inlines = (materiasLinea,)
