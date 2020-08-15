from auctions.models import Comment


def add_comment(listing, comment):
    new_comment = Comment(comment_listing = listing, comment_text = comment)
    new_comment.save()
    return True