from django.shortcuts import render, redirect
from .models import Maestro, Grado, Alumno, Materia, MateriasCursadas,MateriasGrados2, MateriasGrados
from .forms import GradoForm


def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], aula = formulario.cleaned_data['aula'],capacidad=formulario.cleaned_data['capacidad'], estado = formulario.cleaned_data['estado'])
            for materia_id in request.POST.getlist('materia'):
                materia = MateriasGrados(materias_id=materia_id, grado_id = grado.id)
                materia.save()
            return redirect('admin/')
    else:
        formulario = GradoForm()
    return render(request, 'alumnos/ingresar.html', {'formulario': formulario})
# Create your views here.
