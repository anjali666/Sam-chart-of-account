# Generated by Django 3.2.7 on 2021-10-14 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0010_auto_20211013_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ('name',), 'verbose_name_plural': 'Assets'},
        ),
    ]
