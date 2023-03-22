# Generated by Django 3.2.18 on 2023-03-16 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_address_phone_number'),
        ('singleBookData', '0005_auto_20230228_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Binding',
            new_name='binding',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='BookStore',
        ),
        migrations.RemoveField(
            model_name='book',
            name='LinkUrl',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Price',
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.URLField(max_length=5000)),
                ('price', models.FloatField(max_length=300)),
                ('book_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.booksellersite')),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singleBookData.book')),
            ],
        ),
    ]