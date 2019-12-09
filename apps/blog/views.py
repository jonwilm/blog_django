from django.shortcuts import render
from .models import Post, Category

def Home(request):
    posts = Post.objects.filter(state = True)
    return render(request, 'index.html', {'posts': posts})

def Generales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'General')
    )
    return render(request, 'generales.html', {'posts': posts})

def Programacion(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Programacion')
    )
    return render(request, 'programacion.html', {'posts': posts})

def Videojuegos(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Videojuegos')
    )
    return render(request, 'videojuegos.html', {'posts': posts})

def Tecnologia(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Tecnologia')
    )
    return render(request, 'tecnologia.html', {'posts': posts})

def Tutoriales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name = 'Tutoriales')
    )
    return render(request, 'tutoriales.html', {'posts': posts})