from django.urls import path
from blog import views as blog_views

urlpatterns = [
   path('', blog_views.index, name='index'),
   path('somos/', blog_views.quienes_somos, name='somos'),
   path('nosotros/', blog_views.nosotros, name='nosotros'),
   path('nosotros/<str:nombre>', blog_views.nosotros, name='nosotros'),
   path('perfil/<str:nombre>', blog_views.perfil, name='perfil'),
   path('crear_post/', blog_views.crear_post, name='crear_post')  # Agrega esta línea para la nueva ruta
]
