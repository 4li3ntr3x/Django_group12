from django.shortcuts import render, redirect
from datetime import date
from .models import Post
from .forms import PostForm
from .forms import CommentForm
from datetime import date
from datetime import datetime
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):

    ultimos_post = Post.obtener_ultimos_x(3)

    context = {
            'home': home,
            'lastPosts':ultimos_post
        }
    return render(request, 'homepage.html', context)

def index(request):
    posts = Post.objects.all()  # Recupera todos los objetos de tipo Post
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def quienes_somos(request):

    context = {
        'fecha' : date.today(),
        'nombres' : [
            'Alejandro',
            'Marcelo',
            'Leandro',
            'Daniel',
            'Horacio',
        ]
    }
    return render(request, 'quienesSomos.html', context)

def nosotros(request, nombre=''):
    
    context = {
        'nombre_usuario' : nombre,
    }
    return render(request, 'trabajaConNosotros.html', context)

def perfil(request, nombre):
    context = {'nombre' : nombre}
    return render(request, 'perfil.html', context)


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Crea una instancia del modelo Post con los datos del formulario
            nuevo_post = Post(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                contenido=form.cleaned_data['contenido']
                
            )
            nuevo_post.save()  # Guarda el nuevo post en la base de datos
            return redirect('index')  # Redirige a la página de inicio después de crear la publicación
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'crear_post.html', context)

def convertirFecha(date):
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    return "{} de {} del {}".format(date.day, meses[date.month - 1], date.year)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
    }

    return render(request, 'post_detail.html', context)

