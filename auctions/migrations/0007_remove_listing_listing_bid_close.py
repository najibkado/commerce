# Generated by Django 3.0.8 on 2020-07-26 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_listing_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listing_bid_close',
        ),
    ]
