# Generated by Django 3.0.7 on 2021-12-09 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0007_auto_20211125_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='file',
            new_name='pdf',
        ),
    ]