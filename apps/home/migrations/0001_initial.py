# Generated by Django 4.1.3 on 2023-05-08 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=45, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('DPI', models.CharField(max_length=45, verbose_name='DPI')),
                ('NIT', models.CharField(max_length=45, verbose_name='NIT')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuadreCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('imagen', models.ImageField(default='descarga.png', upload_to='especialidad')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('especialidad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45, verbose_name='Tipo')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente')),
                ('colaborador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripcion')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('colaborador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.orden')),
                ('tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipo')),
            ],
        ),
    ]
