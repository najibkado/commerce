# Generated by Django 3.0.8 on 2020-07-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200725_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_picture',
            field=models.CharField(default='https://pixabay.com/get/52e9d2474d51a414f6da8c7dda79357d133edae44e50744070287dd29448c7_1280.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
