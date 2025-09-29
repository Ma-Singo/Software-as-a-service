from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer

class CustomerAdmin(UserAdmin):
    list_display = ['username', 'email']

admin.site.register(Customer)