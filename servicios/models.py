from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="titulo")
    contenido =models.CharField(max_length=50, verbose_name='contenido')
    imagen = models.ImageField(upload_to = 'servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
