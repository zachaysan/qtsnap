from fhp.models.user import User

class UserComments(object):
    def __init__(self, username):
        self.username = username

    def get_comment_count(self):
        self.comment_counter = defaultdict(int)
        user = User(username=username)
        for photo in user.photos:
            self.analze_photo(photo)

    def analyze_photo(self, photo):
        for comment in photo.comments:
            self.comment_count[comment.user.username] += 1

class AuthorizedUser(object):
    pass
