# Generated by Django 2.1.15 on 2023-02-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookSellerSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StoreName', models.CharField(max_length=5000)),
                ('Address', models.CharField(max_length=5000)),
                ('StoreSite', models.URLField(max_length=5000)),
            ],
        ),
    ]
