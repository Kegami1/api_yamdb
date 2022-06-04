# Generated by Django 2.2.16 on 2022-06-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220603_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('anonymous', 'anonymous'), ('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='USER', max_length=16, verbose_name='Пользовательская роль'),
        ),
    ]
