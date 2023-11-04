from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display= ['email','is_staff','is_superuser','is_verified','is_active']
    list_filter = ['is_verified']
    search_fields = ['email']
    ordering = ['email']

    fieldsets = (
        ('Basic data', {'fields': ('email','username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_verified', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        )
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)