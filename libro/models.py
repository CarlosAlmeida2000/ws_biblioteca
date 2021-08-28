from django.db import models

class libro(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=450)
    ruta_foto = models.ImageField(upload_to="portada_libro", null=True, blank=False)

