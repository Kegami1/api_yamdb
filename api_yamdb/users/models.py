from django.contrib.auth.models import AbstractUser
from django.db import models


USERS_ROLE_CHOICES = [
    ('ANONYMOUS', 'anonymous'),
    ('USER', 'user'),
    ('MODERATOR','moderator'),
    ('ADMIN','admin'),
]

class User(AbstractUser):
    user_role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=16,
        choices=USERS_ROLE_CHOICES,
        blank=False,
        null=False,
        default='USER',
    ) 