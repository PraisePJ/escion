# Generated by Django 4.1.4 on 2023-01-11 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_rename_shoes_book_rename_phones_clothe_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Clothe',
        ),
        migrations.DeleteModel(
            name='Laptop',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
        migrations.DeleteModel(
            name='Watche',
        ),
    ]
