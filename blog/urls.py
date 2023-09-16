from django.urls import path
from blog import views as blog_views

urlpatterns = [
   path('', blog_views.index, name='index'),
   path('somos/', blog_views.quienes_somos, name='somos'),
   path('nosotros/', blog_views.nosotros, name='nosotros')
]
