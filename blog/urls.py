from django.urls import path
from blog import views as blog_views

urlpatterns = [
   path('', blog_views.index, name='index')
]
