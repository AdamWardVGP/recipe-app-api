"""
Database models.
"""
from django.conf import settings
from django.db import models
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

    def create_superuser(self, email, password=None, **extra_fields):
        """Builds, stores and returns a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
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

class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    time_minutes=models.IntegerField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    link=models.CharField(max_length=255,blank=True)

    def __str__(self) -> str:
        return self.title