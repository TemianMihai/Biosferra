from django.contrib import admin
from .models import PostModel, Comment, AdresaDeFacturare , CosulMeu

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'details', 'quantity', 'price']

class AdresaDeFacturareAdmin(admin.ModelAdmin):
    list_display = ['nume', 'prenume']

class CosulMeuAdmin(admin.ModelAdmin):
    list_display = ['anunturi', 'vanzator', 'cumparator']

admin.site.register(CosulMeu, CosulMeuAdmin)
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(AdresaDeFacturare, AdresaDeFacturareAdmin)
admin.site.register(Comment)