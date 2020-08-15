from auctions.models import Listing
    
def get_listings():
    return Listing.objects.all()

def get_listing(listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return False
    return listing

def get_listing_comments(listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
        comments = listing.comments.all()
    except Listing.DoesNotExist:
        return False
    
    return comments

def add_listing(listing):
    try:
        new_listing = Listing(listing_title = listing['title'], listing_description = listing['desc'], listing_price = listing['starting_price'], listing_owner = listing['owner'], listing_category = listing['category'], listing_bid_close = listing['closing_date'])
        new_listing.save()
    except:
        return False
        
    return True

def verify_listing(listing):
    try:
        listing = Listing(listing_title = listing['title'], listing_description = listing['desc'], listing_price = listing['starting_price'], listing_owner = listing['owner'], listing_category = listing['category'], listing_bid_close = listing['closing_date'])
    except:
        pass

    if isinstance(listing, Listing):
        return True
    else:
        return False

def delete_listing(listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return "Unsuccessfull, It does not exist"

    listing.delete()
    return "Successfull"