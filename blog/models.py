from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    
    def obtener_ultimos_x(cantidad):
        return Post.objects.order_by("-fecha", "-id").all()[:cantidad]

class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    contenido = models.TextField(max_length=140)
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

