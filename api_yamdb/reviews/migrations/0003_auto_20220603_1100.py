# Generated by Django 2.2.16 on 2022-06-03 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220601_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_titles', to='reviews.Genre')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre_titles', to='reviews.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(default=1, help_text='Рассматриваемое произведение', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title', verbose_name='Рассматриваемое произведение'),
            preserve_default=False,
        ),
    ]
