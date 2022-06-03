from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.TextField(max_length=256)
    slug = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField
    description = models.TextField(
        blank=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name='title',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='title',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Рассматриваемое произведение',
        help_text='Рассматриваемое произведение',
    )
    text = models.TextField(
        verbose_name='Текст рецензии',
        help_text='Оставьте свою рецензию',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор рецензии',
        help_text='Автор рецензии',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=(MinValueValidator(1),
                    MaxValueValidator(10)),
        blank=False,
        null=False
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата рецензии',
        help_text='Дата рецензии',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'

    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Рецензия',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField('Текст')
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата комментария',
        help_text='Дата комментария',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]
