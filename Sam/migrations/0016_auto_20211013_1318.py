# Generated by Django 3.0.3 on 2021-10-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0015_asset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_child', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='new_child',
        ),
    ]
