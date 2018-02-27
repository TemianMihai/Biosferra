from django.contrib import admin
from models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'details', 'delivery_time', 'cantity', 'price']

admin.site.register(PostModel, PostModelAdmin)