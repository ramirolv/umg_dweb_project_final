# Generated by Django 4.2 on 2023-04-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='imagen',
            field=models.ImageField(default='img/pizza-deluxe.png', null=True, upload_to='especialidad'),
        ),
    ]