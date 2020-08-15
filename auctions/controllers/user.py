from auctions.models import User

def get_user(user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return False

    return user