# Generated by Django 2.1.15 on 2023-02-28 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singleBookData', '0004_book_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Location',
            new_name='BookStore',
        ),
    ]
