# Generated by Django 4.1.1 on 2022-10-01 01:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True)),
                ('original', models.ImageField(blank=True, null=True, upload_to='galeria/original')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='galeria/thumbnail')),
                ('publicacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BD_imagens.album')),
            ],
            options={
                'ordering': ('album', 'titulo'),
            },
        ),
    ]
