# Generated by Django 4.2 on 2023-04-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_especialidad_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='imagen',
            field=models.ImageField(default='descarga.png', null=True, upload_to='especialidad'),
        ),
    ]
