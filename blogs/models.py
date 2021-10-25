from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="titulo")
    contenido =models.TextField(max_length=1000, verbose_name='contenido')
    imagen = models.ImageField(upload_to = 'blogs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs" 

    def __str__(self):
        return self.titulo
