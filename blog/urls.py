from django.urls import path
from blog import views as blog_views
from . import views

urlpatterns = [
   path('', blog_views.home, name='home'),
   path('index', blog_views.index, name='index'),  # Ruta para mostrar la lista de posts en la página de inicio
   path('somos/', blog_views.quienes_somos, name='somos'),
   path('nosotros/', blog_views.nosotros, name='nosotros'),
   path('nosotros/<str:nombre>', blog_views.nosotros, name='nosotros'),
   path('perfil/<str:nombre>', blog_views.perfil, name='perfil'),
   path('crear_post/', blog_views.crear_post, name='crear_post'),
   path('post/<int:post_id>/', views.post_detail, name='post_detail'),# Ruta para entran en detalle al post
   path('etiquetas/<int:etiqueta_id>/', views.etiquetas, name='etiquetas')
]
