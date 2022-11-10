from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("", inicio, name="coder-inicio"),
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("profesores/", profesores, name="coder-profesores"),
    path("cursos/", cursos, name="coder-cursos"),
    path("curso/crear/", creacion_curso, name="coder-cursos-crear"),
    path("entregables/", entregables, name="coder-entregables"),
]