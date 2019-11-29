from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'date_create',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('first_name', 'last_name', 'email', 'state', 'date_create',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Autor, AutorAdmin)