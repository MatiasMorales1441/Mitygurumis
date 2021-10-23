from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.home, name="home"),
    path('catalogo/', views.servicios, name="catalogo"),
    path('productos/', views.tienda, name="productos"),
  
    path('contacto/', views.contacto, name="contacto"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)