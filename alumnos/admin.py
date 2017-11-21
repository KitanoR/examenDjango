from django.contrib import admin
from .models import Maestro, Grado, Alumno, Materia, MateriasCursadas,MateriasGrados,MateriasGrados2

admin.site.register(Maestro)
admin.site.register(Grado)
admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(MateriasCursadas)
admin.site.register(MateriasGrados)
admin.site.register(MateriasGrados2)
# Register your models here.
