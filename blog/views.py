from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienesSomos.html')

def nosotros(request):
    return render(request, 'trabajaConNosotros.html')