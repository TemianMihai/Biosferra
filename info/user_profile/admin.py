from django.contrib import admin
from .models import Mesaje, Report, Favorit

class MesajeAdmin(admin.ModelAdmin):
    list_display = ['titlu', 'autor', 'destinatar']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['titluu', 'autor', 'destinatar']

class FavoritAdmin(admin.ModelAdmin):
    list_display = ['alegator', 'ales']

admin.site.register(Mesaje, MesajeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Favorit, FavoritAdmin)