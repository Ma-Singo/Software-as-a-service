from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Customer

admin.site.register(Customer)
admin.site.unregister(Group)