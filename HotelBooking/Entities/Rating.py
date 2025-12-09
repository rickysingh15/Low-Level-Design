from Entities.User import User

class Rating:

    def __init__(self, user: User, rating: float, comment: str = ""):
        self.user = user
        self.rating = rating
        self.comment = comment
