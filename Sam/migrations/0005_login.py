# Generated by Django 3.2.7 on 2021-09-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
            ],
        ),
    ]