from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def Home(request):
    posts = Post.objects.filter(state = True)
    return render(request, 'index.html', {'posts': posts})

def Generales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact = 'general')
    )
    return render(request, 'generales.html', {'posts': posts})

def Programacion(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact = 'programación')
    )
    return render(request, 'programacion.html', {'posts': posts})

def Videojuegos(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact = 'videojuegos')
    )
    return render(request, 'videojuegos.html', {'posts': posts})

def Tecnologia(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact = 'tecnología')
    )
    return render(request, 'tecnologia.html', {'posts': posts})

def Tutoriales(request):
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact = 'tutoriales')
    )
    return render(request, 'tutoriales.html', {'posts': posts})

def DetailPost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detail_post': post})