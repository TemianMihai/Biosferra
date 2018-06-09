from django.contrib import admin
from .models import Mesaje, Report

class MesajeAdmin(admin.ModelAdmin):
    list_display = ['titlu', 'autor', 'destinatar']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['titlu', 'autor', 'destinatar']

admin.site.register(Mesaje, MesajeAdmin)
admin.site.register(Report, ReportAdmin)