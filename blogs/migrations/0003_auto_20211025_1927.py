# Generated by Django 3.0.7 on 2021-10-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20211022_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=models.TextField(max_length=1000, verbose_name='contenido'),
        ),
    ]
