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
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q


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

@login_required(login_url='/login/')
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Hemos recibido tus datos')

            nNuevasEtiquetas = int(request.POST.get('etiquetaNewCount'))
            nuevasEtiquetas = []

            if nNuevasEtiquetas > 0:
                for i in range(0, nNuevasEtiquetas):
                    nuevaEtiqueta = request.POST.get('inewEtiqueta' + str(i + 1))
                    newEtiqueta, created = Etiqueta.objects.get_or_create(desc=nuevaEtiqueta)
                    nuevasEtiquetas.append(newEtiqueta)

            nuevo_post = Post(
                titulo=form.cleaned_data['titulo'],
                #autor=form.cleaned_data['autor'],
                autor=request.user.username,
                contenido=form.cleaned_data['contenido']
            )
            nuevo_post.save()
            nuevo_post.etiquetas.set(form.cleaned_data['etiquetas'])

            if nNuevasEtiquetas > 0:
                for nueva_etiqueta in nuevasEtiquetas:
                    nuevo_post.etiquetas.add(nueva_etiqueta)

            return redirect('index')

        else:
            messages.warning(request, 'Por favor revisa los errores en el formulario')
    else:
        form = PostForm()

    etiquetas = Etiqueta.objects.all()  # Obtener todas las etiquetas

    context = {
        'form': form,
        'etiquetas': etiquetas,
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

def loginUser(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            #return redirect('home')  # Redirige al usuario a la página de inicio después del inicio de sesión exitoso
            return redirect('home')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
            #return render(request, "login.html")
        # Lógica de inicio de sesión
       

    # Si la solicitud no es POST, simplemente muestra el formulario de inicio de sesión
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    #messages.info(request, "desconectado del blog")
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_c = request.POST.get("password-c")
        if (password == password_c):
            try:
                user = User.objects.create_user(username, email, password);
                user.save()
                login(request, user)
                messages.success(request, "Login correcto")
                return redirect("home")
            except IntegrityError:
                messages.info(request, "prueba con un usuario diferente")
                return render(request, "signup.html")
        messages.error(request, "Password no coincide confirma la Password")
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "signup.html")


class BuscarResultado(generic.ListView):

    model = Post
    template_name = "buscar.html"

    def get_queryset(self):

        query = self.request.GET.get('Buscar')
      
        post_list = Post.objects.filter(
            Q(titulo__icontains=query)).distinct()
        return post_list

