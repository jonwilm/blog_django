from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    state = models.BooleanField('Categoría Activada/Desactivada', default=True)
    date_create = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('Nombre del Autor', max_length=255, null=False, blank=False)
    last_name = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    state = models.BooleanField('Autor Activado/Desactivado', default=True)
    date_create = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['last_name']

    def __str__(self):
        return "{0},{1}".format(self.last_name, self.first_name)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo', max_length=90, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    description = models.CharField('Descripción', max_length=110, null=False, blank=False)
    content = RichTextField()
    image = models.URLField('Imagen', max_length=255, null=False, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.BooleanField('Publicado/No Publicado', default=True)
    date_create = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['date_create']

    def __str__(self):
        return self.title