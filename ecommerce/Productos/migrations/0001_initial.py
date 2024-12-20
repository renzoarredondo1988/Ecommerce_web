# Generated by Django 5.0.7 on 2024-11-30 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('arma', 'Arma'), ('armadura', 'Armadura')], default='arma', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.BinaryField(blank=True, null=True)),
                ('plataforma', models.CharField(max_length=45, null=True)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('url_pagina', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250, null=True)),
                ('stock', models.IntegerField(null=True)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.categoria')),
                ('juego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.juego')),
            ],
        ),
    ]
