# Generated by Django 4.1.2 on 2022-11-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleorden',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tipoplatillo',
            name='SegundoPrecio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tipoplatillo',
            name='TercerPrecio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
