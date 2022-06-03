from django.contrib.auth.models import AbstractUser
from django.db import models


USERS_ROLE_CHOICES = [
    ('ANONYMOUS', 'anonymous'),
    ('USER', 'user'),
    ('MODERATOR','moderator'),
    ('ADMIN','admin'),
]

class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
        null=True
    )
    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=16,
        choices=USERS_ROLE_CHOICES,
        blank=False,
        null=False,
        default='USER',
    )
    bio = models.TextField(blank=True, null=True)

