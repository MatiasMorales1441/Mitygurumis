from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="titulo")
<<<<<<< HEAD
    contenido =models.TextField(max_length=1000, verbose_name='contenido')
=======
    contenido =models.CharField(max_length=200, verbose_name='contenido')
>>>>>>> d09a9454c6ae7f6bdc8008ff03d3854608b6079d
    imagen = models.ImageField(upload_to = 'servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
