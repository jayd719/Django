"""-------------------------------------------------------
Django: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    Django
Version:  1.0.8
__updated__ = Sat Jan 04 2025
-------------------------------------------------------
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return super().__str__()
