# Generated by Django 3.2.18 on 2023-04-02 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_address_store_name'),
        ('singleBookData', '0006_auto_20230316_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='book_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_at', to='seller.booksellersite'),
        ),
    ]
