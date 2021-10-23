from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

def home(request):
    
    return render(request,"ProyectowebApp/home.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"ProyectowebApp/catalogo.html", {"servicios": servicios})

def tienda(request):
    
    return render(request,"ProyectowebApp/tienda.html")

def blog(request):
    
    return render(request,"ProyectowebApp/blog.html")

def contacto(request):
    
    return render(request,"ProyectowebApp/contacto.html")

# Create your views here.
