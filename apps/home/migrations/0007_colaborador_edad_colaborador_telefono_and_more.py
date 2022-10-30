# Generated by Django 4.1.2 on 2022-10-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_colaborador_puesto_id_delete_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='nombre',
            field=models.CharField(max_length=45, null=True),
        ),
    ]