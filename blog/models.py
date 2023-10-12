from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)