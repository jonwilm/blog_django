from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'date_create',)
    resources_class = CategoryResources

class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('first_name', 'last_name', 'email', 'state', 'date_create',)
    resources_class = AutorResources

admin.site.register(Category, CategoryAdmin)
admin.site.register(Autor, AutorAdmin)