from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.controllers import listing, category, user, watch_list, bidding, comment
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import User, Listing, Category


def index(request):
    listings = listing.get_listings()
    return render(request, "auctions/index.html", {
        "listings": listings
    })

def categories(request):
    categories = category.get_categories()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category_view(request, category_id):
    category_item = category.get_category(category_id)
    category_listing = category.get_category_listing(category_item)
    # return HttpResponse(category_listing)
    return render(request, "auctions/category.html", {
        "listing": category_listing
    })

@login_required
def bid(request, user_id, listing_id):
    if request.method == "POST":
        current_user = user.get_user(user_id)
        current_listing = listing.get_listing(listing_id)
        bidding_price = int(request.POST["bidding_price"])

        if bidding.add_bid(current_user, current_listing, bidding_price):
            return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

    return HttpResponse("status")

@login_required
def watchlist(request, user_id):
    current_user = user.get_user(user_id)
    my_lists = watch_list.my_watchlists(current_user)
    return render(request, "auctions/watchlist.html", {
        "watchlists": my_lists
    })

@login_required
def add_watchlist(request, user_id, listing_id):
    current_user = user.get_user(user_id)
    current_listing = listing.get_listing(listing_id)

    if watch_list.is_watchlist_added(current_user, current_listing):

        return HttpResponseRedirect(reverse("watchlist", args=(user_id,)))
    else:
        watch_list.add_watchlist(current_user, current_listing)

    return HttpResponseRedirect(reverse("watchlist", args=(user_id,)))

@login_required
def del_watchlist(request, watchlist_id, user_id):
    current_watchlist = watch_list.get_watchlist(watchlist_id)
    current_watchlist.watchlist_is_deleted = True
    current_watchlist.save()

    return HttpResponseRedirect(reverse("watchlist", args=(user_id, )))

@login_required
def close_bidding(request, listing_id):
    current_listing = listing.get_listing(listing_id)
    current_listing.listing_bid_is_active = False
    current_listing.save()

    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

@login_required
def add_comment(request, listing_id):
    current_listing = listing.get_listing(listing_id)
    current_comment = request.GET["comment"]
    if comment.add_comment(current_listing, current_comment):
        return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

@login_required
def create_listing(request):
    if request.method == "POST":
        try:
            user_id = int(request.POST["listing_owner"])
            this_user = user.get_user(user_id)
            # return HttpResponse(this_user)
        except:
            return HttpResponseRedirect(reverse("error"))

        try:
            listing_title = request.POST["listing_title"]
            listing_description = request.POST["listing_description"]
            listing_starting_price = int(request.POST["listing_starting_price"])
            # listing_closing_date = request.POST["listing_closing_date"]
            listing_category = int(request.POST["listing_category"])
            listing_picture = request.POST["listing_picture"]
        except:
            return HttpResponseRedirect(reverse("error"))

        try:
            listing_category = category.get_category(listing_category)
        except:
            return HttpResponseRedirect(reverse("error"))

        listing_dict = {
            "owner": this_user,
            "title": listing_title,
            "desc": listing_description, 
            "starting_price": listing_starting_price, 
            # "closing_date": listing_closing_date, 
            "category": listing_category,
            "listing_picture": listing_picture
            }
        

        new_listing = Listing(
            listing_title = listing_dict["title"],
            listing_description = listing_dict["desc"],
            listing_price = listing_dict["starting_price"],
            listing_owner = listing_dict["owner"],
            # listing_category = listing_dict["category"],
            # listing_creation_date,
            # listing_bid_close = listing_dict["closing_date"],
            listing_picture = listing_dict["listing_picture"]
        )
        new_listing.save()

        listing_dict["category"].listing.add(new_listing)

        return HttpResponseRedirect(reverse("index"))
    
    categories = category.get_categories()
    return render(request, "auctions/new_listing.html", {
        "categories": categories
    })



def listing_page(request, listing_id):
    listing_res = listing.get_listing(listing_id)
    comments = listing.get_listing_comments(listing_id)

    if not listing_res.listing_bid_is_active:
        winner = bidding.get_bid_winner(listing_res)

        if winner == None or not winner:
            winner = "No bids"

    else:
        winner = "Bidding is Active"

    if bidding.get_listing_bids(listing_res):
        last_bid = bidding.get_last_bid(listing_res)
    else:
        last_bid = 0
    
    if listing_res != False:
        return render(request, "auctions/listing.html", {
            "listing": listing_res,
            "comments": comments,
            "last_bid": last_bid,
            "bid_winner": winner
        })
    else:
        return HttpResponseRedirect(reverse("error"))

def error():
    return HttpResponse("Error !")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
