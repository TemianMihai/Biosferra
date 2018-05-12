from django.contrib import admin

from .models import Lfcategory
# Register your models here.

class LfcategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


admin.site.register(Lfcategory, LfcategoryAdmin)
