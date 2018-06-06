from django.contrib import admin
from .models import Account2


class Account2Admin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Account2, Account2Admin)
