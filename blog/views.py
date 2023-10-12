from django.shortcuts import render, redirect
from datetime import date
from .models import Post
from .forms import PostForm
from datetime import date
from datetime import datetime

blogs = [
    {'titulo':'La Pesca durante el més de junio.',
    'fecha':'20 de Junio del 2023', 
    'autor':'Marcelo', 
    'contenido':'''Mayo es un mes excepcional para la pesca. Con la temporada de desove en pleno apogeo y un clima perfecto, los pescadores tienen todas las razones para emocionarse.

Temporada de Desove: En mayo, los peces como el lucio y el bass están en su momento de reproducción, lo que significa que están hambrientos y activos. Es el momento ideal para lanzar el anzuelo y disfrutar de una pesca deportiva emocionante.

Clima Perfecto: Las temperaturas agradables y días más largos hacen que pasar tiempo en el agua sea un placer. No hay preocupaciones por el frío o el calor extremo, lo que hace que mayo sea ideal para la pesca.

Variedad de Especies: Desde truchas en ríos fríos hasta lucios en aguas cálidas, mayo ofrece una amplia variedad de especies para pescar. Investiga las especies locales y adapta tus técnicas para tener éxito.

Ética de Pesca: Recuerda siempre respetar las regulaciones locales de pesca y practicar la pesca sostenible. Captura y suelta con cuidado para preservar nuestros recursos naturales.

En resumen, mayo es un mes emocionante para los amantes de la pesca. Aprovecha la temporada de desove, disfruta del clima y sé un pescador ético. ¡Buena pesca en mayo!'''},
     {'titulo':'La caza en primavera',
    'fecha':'20 de Septiembre del 2022',
    'autor':'Alejandro', 
     'contenido':'''La primavera es una temporada mágica para los cazadores. A medida que la naturaleza se despierta y se renueva, los cazadores encuentran una renovada emoción en sus aventuras en el campo. En este artículo, exploraremos por qué la caza en primavera es una experiencia única y apasionante.

Renovación de la Naturaleza: Con la llegada de la primavera, la naturaleza comienza a despertar después del invierno. Los bosques se llenan de vida, los árboles florecen y las aves migratorias regresan a sus áreas de reproducción. Para los cazadores, esto significa que hay una mayor actividad de la fauna, lo que hace que la caza sea más emocionante y gratificante.

Temporada de Caza Específica: La primavera suele ser la temporada de caza de ciertas especies, como el pavo y el faisán. Estos animales son especialmente activos y visibles durante esta época del año, lo que brinda a los cazadores la oportunidad perfecta para perseguirlos. La caza de pavos, por ejemplo, es una tradición popular de primavera en muchas regiones.

Caza Responsable: Siempre es importante practicar la caza responsable y respetar las regulaciones locales. Con la primavera también vienen nuevas responsabilidades, como el cuidado de los nidos y la cría de las aves. Asegúrate de conocer y cumplir con todas las leyes de caza y conservación.

Condiciones Meteorológicas Agradables: La primavera suele ofrecer condiciones meteorológicas más agradables para la caza. Los días son más largos, las temperaturas son suaves y el entorno es más cómodo para los cazadores. Esta es una temporada perfecta para disfrutar del aire libre y la caza.

Énfasis en la Observación: La primavera también es un momento excelente para la observación de la fauna. Los cazadores pueden disfrutar de la belleza de la naturaleza mientras buscan su presa. Observar la vida silvestre en su entorno natural es una experiencia enriquecedora que va más allá de la caza en sí.

En conclusión, la caza en primavera ofrece una oportunidad única para conectarse con la naturaleza, experimentar la emoción de la caza y ser testigo de la renovación de la vida silvestre. Si eres un apasionado cazador, no te pierdas la oportunidad de disfrutar de todo lo que la primavera tiene para ofrecer en tus aventuras cinegéticas. ¡Buena caza en primavera!'''}]
# Create your views here.

def home(request):

    context = {
            'home': home
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