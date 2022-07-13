from django import http
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from Appclub.forms import DeporteForm, ProfeForm

# Create your views here.
"""  """

def deporte(self):
    
    deporte= Deporte(nombre="Futbol", categoria="Infantil")
    deporte.save()
    texto= f"Deporte creado: {deporte.nombre} {deporte.categoria}"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "Appclub/inicio.html")

def deportes(request):
    return render(request, "Appclub/deportes.html")

def profesores(request):
    return render(request, "Appclub/profesores.html")

def socios(request):
    return render(request, "Appclub/socios.html")


""" def cursoFormulario(request):

    if (request.method=="POST"):
        nombre= request.POST.get("curso")
        comision= request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "Appcoder/inicio.html")





    return render(request, "Appclub/cursoFormulario.html")   VISTA PARA FORMULARIO HTML"""


def deporteFormulario(request):

    if (request.method=="POST"):
        form= DeporteForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            categoria= info["categoria"]
            deporte= Deporte(nombre=nombre, categoria=categoria)
            deporte.save()
            return render (request, "Appclub/inicio.html")
    else:
        form= DeporteForm()
    return render(request, "Appclub/deporteFormulario.html", {"formulario":form})


def profeFormulario(request):

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            deporte= info["deporte"]
            categoria= info["categoria"]
            nacimiento= info["nacimiento"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, deporte=deporte, categoria=categoria)
            profe.save()
            return render (request, "Appclub/inicio.html")
    else:
        form= ProfeForm()
    return render(request, "Appclub/profeForm.html", {"formulario":form})



def busquedaCategoria(request):
    
    return render(request, "Appclub/busquedaCategoria.html")

def buscar(request):
    if request.GET["categoria"]:
        comi= request.GET["categoria"]
        deportes= Deporte.objects.filter(categoria__icontains=comi)
        return render(request, "Appclub/resultadosBusqueda.html", {"deportes":deportes})
    else:
        return render(request, "Appclub/busquedaCategoria.html", {"error":"No se ingreso ninguna categoria"})

        
    
