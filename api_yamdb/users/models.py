from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class UserRole:
    ANONYMOUS = 'anonymous'
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    def max_len_role(self):
        return len(max(
            (self.ANONYMOUS, self.USER, self.MODERATOR, self.ADMIN),
            key=len)
        )


USERS_ROLE_CHOICES = [
    (UserRole.ANONYMOUS, 'anonymous'),
    (UserRole.USER, 'user'),
    (UserRole.MODERATOR, 'moderator'),
    (UserRole.ADMIN, 'admin'),
]


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        validators=[username_validator],
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=254,
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
        max_length=UserRole.max_len_role(UserRole),
        choices=USERS_ROLE_CHOICES,
        default=UserRole.USER,
    )
    bio = models.TextField(blank=True, null=True)
