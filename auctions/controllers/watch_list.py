from auctions.models import Watchlist

def get_watchlists():
    watchlists = Watchlist.objects.all()
    return watchlists

def get_watchlist(watchlist_id):
    watchlist = Watchlist.objects.get(pk=watchlist_id, watchlist_is_deleted=False)
    return watchlist

def my_watchlists(user_id):
    my_watchlist = Watchlist.objects.filter(watchlist_owner = user_id, watchlist_is_deleted=False)
    return my_watchlist

def is_watchlist_added(watchlist_owner, watchlist_listing):
    try:
        check = Watchlist.objects.get(watchlist_owner= watchlist_owner, watchlist_listing = watchlist_listing)
        if check.watchlist_is_deleted == True:
            check.watchlist_is_deleted = False
            check.save()
        return True
    except Watchlist.DoesNotExist:
        return False

def add_watchlist(watchlist_owner, watchlist_listing):
    new_watchlist = Watchlist(watchlist_owner = watchlist_owner, watchlist_listing = watchlist_listing)
    new_watchlist.save()
    return True


