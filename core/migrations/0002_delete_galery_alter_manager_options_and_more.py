# Generated by Django 4.0.5 on 2022-06-21 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Galery',
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
