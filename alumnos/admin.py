from django.contrib import admin
from .models import Maestro, Grado, Alumno, Materia, MateriasCursadas,MateriasGrados

admin.site.register(Maestro)
admin.site.register(Grado)
admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(MateriasCursadas)
admin.site.register(MateriasGrados)
# Register your models here.
