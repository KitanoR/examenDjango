from django.shortcuts import render
from .models import Maestro, Grado, Alumno, Materia, MateriasCursadas,MateriasGrados
from .forms import GradoForm


def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], aula = formulario.cleaned_data['aula'],capacidad=formulario.cleaned_data['capacidad'], estado = formulario.cleaned_data['estado'])
            for Materia_id in request.POST.getlist('materias'):
                materia = Materia(materia_id=materia_id, grado_id = grado.id)
                materia.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'alumnos/ingresar.html', {'formulario': formulario})
# Create your views here.
