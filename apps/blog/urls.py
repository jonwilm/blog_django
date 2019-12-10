from django.urls import path
from .views import Home, Generales, Programacion, Videojuegos, Tecnologia, Tutoriales, DetailPost

urlpatterns = [
    path('', Home, name = 'index'),
    path('generales/', Generales, name = 'generales'),
    path('programacion/', Programacion, name = 'programacion'),
    path('videojuegos/', Videojuegos, name = 'videojuegos'),
    path('tecnologia/', Tecnologia, name = 'tecnologia'),
    path('tutoriales/', Tutoriales, name = 'tutoriales'),
    path('<slug:slug>', DetailPost, name = 'detail_post')
]