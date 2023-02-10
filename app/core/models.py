"""
Database models.
"""
from django.db import models  # noqa
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Custom manager extending."""

    def create_user(self, email, password=None, **extra_fields):
        """Method to create, and store a user. New user is returned"""
        if not email:
            raise ValueError('User must have a vailid email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
        

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user object for our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'