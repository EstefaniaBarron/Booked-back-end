# Generated by Django 3.2.18 on 2023-03-15 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20230315_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=5000),
            preserve_default=False,
        ),
    ]