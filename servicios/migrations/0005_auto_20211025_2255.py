# Generated by Django 3.0.7 on 2021-10-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_auto_20211025_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='file',
            field=models.FileField(default=1, upload_to='servicios/files'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='procedencia',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
