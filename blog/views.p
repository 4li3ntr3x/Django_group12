from django.shortcuts import render, redirect
from .forms import PostForm

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio o donde quieras después de crear la publicación
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'crear_post.html', context)
