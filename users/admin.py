from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets= (
        (None,{'fields':('email', 'init_email', 'stripe_id', 'password')}),
        ('Personalinfo',{'fields':('username' ,'phone_number', 'image')}),
    )
    
    # Fields to display when creating a new user
    add_fieldsets =(
        (None,{
        'classes':('wide',),
        'fields':('email','username','password1','password2'),
        }),
        ('Personalinfo',{'fields':('phone_number', 'image')}),
    )

    list_display = ['username', 'email', 'is_staff']
    list_filter = ['is_staff', ]
    search_fields = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
