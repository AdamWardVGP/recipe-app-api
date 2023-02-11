"""
Customications for the django admin
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

# we should really visit the Django admin site to learn how this works:
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)