from django.contrib.auth.models import AbstractUser
from django.db import models


USERS_ROLE_CHOICES = [
    ('anonymous', 'anonymous'),
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
]


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Почта',
        blank=False,
        null=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
        null=True,
    )
    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=16,
        choices=USERS_ROLE_CHOICES,
        blank=False,
        null=False,
        default='user',
    )
    bio = models.TextField(blank=True, null=True)
