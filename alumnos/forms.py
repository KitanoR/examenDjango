from django import forms
from .models import Maestro, Grado, Alumno, Materia, MateriasCursadas,MateriasGrados

class GradoForm(forms.ModelForm):
    class Meta:
        model= Grado
        fields = ('nombre','aula','capacidad','materia','estado',)
