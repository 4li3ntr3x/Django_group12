from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    contenido = models.TextField(max_length=200, null=True)
    autor = models.CharField(verbose_name="Autor", max_length=100, null=True)
    fecha = models.DateField(null=True)

    """def __str__(self):
        return self.titulo"""