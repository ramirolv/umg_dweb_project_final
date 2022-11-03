# Generated by Django 4.1.3 on 2022-11-03 09:13

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
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=45, verbose_name='Direccion')),
                ('DPI', models.CharField(max_length=45, verbose_name='DPI')),
                ('NIT', models.CharField(max_length=45, verbose_name='NIT')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripcion')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPlatillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45, verbose_name='Tipo')),
                ('PrimerPrecio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SegundoPrecio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TercerPrecio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('platillo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.platillo')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45, verbose_name='Tipo')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente')),
                ('colaborador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.colaborador')),
                ('cuadreCaja_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cuadrecaja')),
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
                ('cuadreCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cuadrecaja')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.orden')),
                ('tipoPlatillo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipoplatillo')),
            ],
        ),
    ]
