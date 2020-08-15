from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_title = models.CharField(max_length=64)
    category_description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} : {self.category_title}, {self.category_description}"

class Listing(models.Model):
    listing_title = models.CharField(max_length=64)
    listing_description = models.CharField(max_length=255)
    listing_price = models.IntegerField()
    listing_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_products")
    listing_category = models.ManyToManyField(Category, blank=True, related_name="listing")
    listing_creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    listing_bid_is_active = models.BooleanField(default=True, blank=False)
    # listing_bid_close = models.DateTimeField(auto_now=False)
    listing_picture = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} : {self.listing_title}, {self.listing_description}, {self.listing_price}, {self.listing_owner}"

class Bid(models.Model):
    bid_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bid_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_biddings")
    bid_price = models.IntegerField()

class Comment(models.Model):
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=255)

class Watchlist(models.Model):
    watchlist_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_owner")
    watchlist_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="my_watchlist_listing")
    watchlist_is_deleted = models.BooleanField(blank=False, default=False)
