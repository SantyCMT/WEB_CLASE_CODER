from django.http import HttpResponse
from appcoder.models import Curso, Profesor
from django.shortcuts import render
from appcoder.forms import ProfesorFormularios


def inicio(request):
    return render(request, "appcoder/index.html")

    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")
    
def profesores(request):
    return render(request, "appcoder/profesores.html")

def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormularios(request.POST)

        # validamos formulario
        if formulario.is_valid():
            # recuperamos los datos
            data    = formulario.cleaned_data

        profesor = Profesor(nombre= data["nombre"], apellido= data["apellido"],email= data["email"],
        profesion= data["profesion"])
        profesor.save()

        
        formulario = ProfesorFormularios()
    contexto = {"formulario" : formulario} 
    return render(request, "appcoder/profesores_formularios.html", contexto )


def entregables(request):
    return render(request, "appcoder/entregables.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def creacion_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = int(request.POST["camada"])
        
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
        
    return render(request, "appcoder/formularios_curso.html")
    
def buscar_curso(request):
    return render(request, "appcoder/buscar_curso.html")

def resultados_busquedas_cursos(request):

    nombre_curso = request.GET["nombre_curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder/resultados_busquedas_cursos.html", {"cursos": cursos})
   




# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     # Respuesta casera
#     cadena_respuesta = "<ul>"
#     for curso in cursos:
#         cadena_respuesta += f"<li>({curso.nombre},{curso.camada}) </li>"
#     cadena_respuesta += "</ul>"

#     return HttpResponse(cadena_respuesta)
