from auctions.models import Bid

def get_bids():
    bids = Bid.objects.all()
    return bids

def get_listing_bids(listing):
    try:
        bid = Bid.objects.filter(bid_listing = listing)
    except Bid.DoesNotExist:
        return False
    return bid

def get_last_bid(listing):
    bid = Bid.objects.filter(bid_listing = listing).last()
    bid = bid.bid_price
    return bid

def get_bid_winner(listing):
    winner = Bid.objects.filter(bid_listing = listing).last()
    try:
        winner = winner.bid_bidder
    except AttributeError:
        return False
    return winner

def add_bid(user, listing, price):
    listing_start_price = listing.listing_price
    if price > listing_start_price:
        new_bid = Bid(bid_listing = listing, bid_bidder=user, bid_price=price)
        new_bid.save()
        return True
    else:
        return False