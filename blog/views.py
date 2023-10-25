from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from .models import Post
from .forms import PostForm
from .forms import CommentForm
from .models import Comentario, Etiqueta
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
    posts = Post.objects.all()
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

def etiquetas(request, etiqueta_id):

    etiqueta = Etiqueta.objects.filter(id=etiqueta_id).get() # Recupera todos los objetos de tipo Post
    posts = etiqueta.post_set.all()
    context = {
        'posts': posts,
        'desc': etiqueta.desc
    }
    return render(request, 'etiquetas.html', context)

def crear_post(request):

    if request.method == 'GET':
            form = PostForm()


    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            messages.success(request, 'Hemos recibido tus datos')

            # Crea una instancia del modelo Post con los datos del formulario
            
            nNuevasEtiquetas =  int(request.POST.get('etiquetaNewCount'))
            
            if nNuevasEtiquetas > 0:
                nuevasEtiquetas = []
                # Tenemos que revisar si las nuevas etiquetas estan o no..
                for i in range(0, nNuevasEtiquetas):
                     nuevaEtiqueta = request.POST.get('inewEtiqueta' + str(i + 1))
                     newEtiqueta = Etiqueta.objects.filter(desc=nuevaEtiqueta)

                     if not newEtiqueta:
                        print(nuevaEtiqueta)
                        newEtiqueta = Etiqueta(desc = nuevaEtiqueta)
                        nuevasEtiquetas.append(newEtiqueta)
                        newEtiqueta.save()
                     else:
                        nuevasEtiquetas.append(newEtiqueta.get())


            nuevo_post = Post(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                contenido=form.cleaned_data['contenido']
            )
            nuevo_post.save()  # Guarda el nuevo post en la base de datos
            nuevo_post.etiquetas.set(form.cleaned_data['etiquetas'])
            form = PostForm()

            if nNuevasEtiquetas > 0:
                for j in range(0, nNuevasEtiquetas):
                    print(j)
                    print(len(nuevasEtiquetas))
                    nuevo_post.etiquetas.add(nuevasEtiquetas[j])

            #return redirect('index')  # Redirige a la página de inicio después de crear la publicación
        
        else:    
            messages.warning(request, 'Por favor revisa los errores en el formulario')



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

    if request.method == 'POST':
        comentario = CommentForm(request.POST)
        if comentario.is_valid():
            comentario_modelo = comentario.save(commit=False)
            comentario_modelo.post = post
            comentario_modelo.save()

    comentarios = post.comentario_set.all()
    
    etiquetas = post.etiquetas.all()

    print(etiquetas)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comentarios': comentarios,
        'comment_form': comment_form,
        'etiquetas': etiquetas
    }

    return render(request, 'post_detail.html', context)


