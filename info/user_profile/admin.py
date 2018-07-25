from django.contrib import admin
from .models import Message, Report, Favourite, Profile

class MesajeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'receiver']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'receiver']

class FavoritAdmin(admin.ModelAdmin):
    list_display = ['author', 'receiver']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'product1', 'product2', 'product3', 'product4', 'product5', 'cover_image', 'profile_image', 'description']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MesajeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Favourite, FavoritAdmin)