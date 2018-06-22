from django.contrib import admin
from .models import PostModel, Comment, CosulMeu

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'details', 'delivery_time', 'cantity', 'price']

class CosulMeuAdmin(admin.ModelAdmin):
    list_display = ['anunturi', 'vanzator', 'cumparator']

admin.site.register(CosulMeu, CosulMeuAdmin)
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)