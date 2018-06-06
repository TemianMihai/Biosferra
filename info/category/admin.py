from django.contrib import admin

# Register your models here.
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Category, CategoryAdmin)