from django.contrib import admin
from blog.models import Etiqueta
from blog.models import Post
from blog.models import Comentario
class EtiquetasInline(admin.TabularInline):
    model = Post.etiquetas.through

class EtiquetaAdmin (admin.ModelAdmin):
    inlines = [
        EtiquetasInline
    ]
    pass
admin.site.register(Etiqueta, EtiquetaAdmin)

class PostAdmin(admin.ModelAdmin):
    inlines = [
        EtiquetasInline
    ]
    list_filter = ('autor',)
    exclude = ('etiquetas',)
    pass
admin.site.register(Post, PostAdmin)


admin.site.register(Comentario)
