from entities.user import User

class Rating():

    def __init__(self, user: User, rating: int, comment: str = None):
        self.user = user
        self.rating = rating
        self.comment = comment or ""
    