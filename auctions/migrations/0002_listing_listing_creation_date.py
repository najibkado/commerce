# Generated by Django 3.0.8 on 2020-07-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_creation_date',
            field=models.DateTimeField(default='2020-07-20 10:00'),
            preserve_default=False,
        ),
    ]
