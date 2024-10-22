from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from custom_user.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=None)
    locale = models.CharField(max_length=64, null=True, blank=True)
    sex = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        db_table = 'user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователь'