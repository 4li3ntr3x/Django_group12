from django.db import models

class Etiqueta(models.Model):
    desc = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.id} - {self.desc}'
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def obtener_ultimos_x(cantidad):
        return Post.objects.order_by("-fecha", "-id").all()[:cantidad]
    def __str__(self) -> str:
        return f'{self.id} - Autor: {self.autor} - Título: {self.titulo}'
    
class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, verbose_name="Email", null=True)
    contenido = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    


