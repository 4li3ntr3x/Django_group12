from django.contrib import admin
from blog.models import Etiqueta
from blog.models import Post
from blog.models import Comentario

admin.site.register(Etiqueta)
admin.site.register(Post)
admin.site.register(Comentario)
