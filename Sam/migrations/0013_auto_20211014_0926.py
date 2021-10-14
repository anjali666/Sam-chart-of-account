# Generated by Django 3.2.7 on 2021-10-14 09:26
# to seed static categories

from django.db import migrations

def seed_static_categories(apps, schema_editor):
    # We can't import the Category model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Category = apps.get_model('Sam', 'Category')
    # Category(name="Assets", type="static", status=True).save()
    # Category(name="Liabilities", type="static", status=True).save()
    # Category(name="Income", type="static", status=True).save()
    # Category(name="Expenses", type="static", status=True).save()

class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0012_auto_20211014_0921'),
    ]

    operations = [
        migrations.RunPython(seed_static_categories),
    ]