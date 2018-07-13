from django.contrib import admin
from .models import Account2, Account


class Account2Admin(admin.ModelAdmin):
    list_display = ['user']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Account2, Account2Admin)
admin.site.register(Account, AccountAdmin)

