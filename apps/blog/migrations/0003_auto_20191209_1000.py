# Generated by Django 2.2.7 on 2019-12-09 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['last_name'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_create'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
