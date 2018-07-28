from django.contrib import admin

from .models import Lfcategory, Legfruccategory
# Register your models here.

class LfcategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

class LegfruccategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


admin.site.register(Lfcategory, LfcategoryAdmin)
admin.site.register(Legfruccategory, LegfruccategoryAdmin)