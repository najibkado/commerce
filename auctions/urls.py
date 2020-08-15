from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("close/<int:listing_id>", views.close_bidding, name="close_biding"),
    path("comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("bid/<int:user_id>/<int:listing_id>", views.bid, name="bid_view"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("delete/<int:watchlist_id>/<int:user_id>", views.del_watchlist, name="del_watchlist"),
    path("add_watchlist/<int:user_id>/<int:listing_id>", views.add_watchlist, name="add_watchlist"),
    path("category/<int:category_id>", views.category_view, name="category_view"),
    path("newlisting", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("error", views.error, name="error")
]
