"""
Customications for the django admin
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as translate

from core import models

# we should really visit the Django admin site to learn how this works:
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        (
            translate('permissions'),
            {
                'fields' : (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (translate('important dates'), {'fields': ('last_login',)}),
    ]
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )


admin.site.register(models.User, UserAdmin)