# Generated by Django 4.0.5 on 2022-06-21 19:50

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modifiy_at', models.DateTimeField(auto_now=True)),
                ('active_at', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='galery', variations={'thumbnail': {'crop': True, 'height': 600, 'width': 600}}, verbose_name='Imagem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modifiy_at', models.DateTimeField(auto_now=True)),
                ('active_at', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('bio', models.TextField(max_length=1000, verbose_name='Texto')),
                ('photo', stdimage.models.StdImageField(force_min_size=False, upload_to='manager', variations={'thumbnail': {'crop': True, 'height': 600, 'width': 600}}, verbose_name='Photo')),
                ('facebook', models.CharField(max_length=100, verbose_name='Face')),
                ('twitter', models.CharField(max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(max_length=100, verbose_name='Insta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modifiy_at', models.DateTimeField(auto_now=True)),
                ('active_at', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('text', models.TextField(max_length=1000, verbose_name='Texto')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='post', variations={'thumbnail': {'crop': True, 'height': 600, 'width': 600}}, verbose_name='Imagem')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.manager')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
