from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.db import models

from temp_project.user_and_pass.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
