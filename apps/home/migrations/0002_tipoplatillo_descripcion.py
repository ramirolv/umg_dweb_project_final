# Generated by Django 4.1.2 on 2022-10-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoplatillo',
            name='descripcion',
            field=models.CharField(default=1, max_length=45, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
