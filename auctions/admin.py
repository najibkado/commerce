from django.contrib import admin
from .models import User, Listing, Category, Bid, Comment, Watchlist
# Register your models here.

admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Watchlist)