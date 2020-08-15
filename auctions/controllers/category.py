from auctions.models import Category 

def get_categories():
    categories = Category.objects.all()
    return categories

def get_category(category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return False
        
    return category

def get_category_listing(category):
    try:
        listing = category.listing.all()
        return listing
    except:
        return False

