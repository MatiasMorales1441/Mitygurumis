from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="titulo")  
    nombre = models.CharField(max_length= 60)
    contenido =models.TextField(max_length=1000, verbose_name='contenido')
    imagen = models.ImageField(upload_to = 'servicios')
    procedencia = models.CharField( max_length=60)
    precio = models.IntegerField()

    file = models.FileField(upload_to= 'servicios/files')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
