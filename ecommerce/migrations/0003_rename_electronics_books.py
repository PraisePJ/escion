# Generated by Django 4.1.4 on 2023-01-01 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_rename_cosmetics_shoes_rename_hairgrooming_watches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Electronics',
            new_name='Books',
        ),
    ]
