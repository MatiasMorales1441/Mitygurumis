# Generated by Django 3.0.7 on 2021-10-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_auto_20211025_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
