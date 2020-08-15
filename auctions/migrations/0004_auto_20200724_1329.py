# Generated by Django 3.0.8 on 2020-07-24 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200724_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='watchlist_listing',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='watchlist_listing',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='my_watchlist_listing', to='auctions.Listing'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='watchlist_owner',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='watchlist_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
