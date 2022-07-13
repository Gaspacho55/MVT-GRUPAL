from django.urls import path
from .views import *


urlpatterns = [
   path('deporte/', deporte),
   path('profesores/', profesores, name='profesores'),
   path('socios/', socios, name='socios'),
   path('deportes/', deportes, name='deportes'),
   path('', inicio, name='inicio'),
   path('deporteFormulario/', deporteFormulario, name='deporteFormulario'),
   path('profeFormulario/', profeFormulario, name='profeFormulario'),
   path('busquedaCategoria/', busquedaCategoria, name='busquedaCategoria'),
   path('buscar/', buscar, name='buscar'),
]