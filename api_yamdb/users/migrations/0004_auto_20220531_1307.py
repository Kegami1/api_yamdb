# Generated by Django 2.2.6 on 2022-05-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220531_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ANONYMOUS', 'anonymous'), ('USER', 'user'), ('MODERATOR', 'moderator'), ('ADMIN', 'admin')], default='user', max_length=16, verbose_name='Пользовательская роль'),
        ),
    ]
