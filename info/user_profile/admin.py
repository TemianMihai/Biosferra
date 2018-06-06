from django.contrib import admin
from .models import Mesaje

class MesajeAdmin(admin.ModelAdmin):
    list_display = ['titlu', 'autor', 'destinatar']

admin.site.register(Mesaje, MesajeAdmin)