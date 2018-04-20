from django.contrib import admin

# Register your models here.
from models import Categorie


class CategorieAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Categorie, CategorieAdmin)