from django.shortcuts import render
from .models import datos_family

   
#def crear_familiares(request):
#   familiar1=datos_family.objects.create(nombre="Facundo", apellido="Pelayo", familiar="Hermano", edad=8, nacimiento='2013-12-13')
#   contexto={"familiar":familiar1}
#   return render(request,'Home.html',contexto)

def ver_familiares(request):
    familiares = datos_family.objects.all()
    contexto = { 'familia': familiares }
    return render(request, "Home.html", contexto)

