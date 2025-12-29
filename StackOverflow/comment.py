
from uuid import uuid4
from user import User
from commentable import Commentable
from votable import Votable

class Comment(Votable, Commentable):

    def __init__(self, content: str, user: User):
        super().__init__()
        self._id = str(uuid4())
        self._content = content
        self._user = user

    @property
    def get_id(self):
        return self._id
    
    @property
    def get_question(self):
        return self._question
    
    @property
    def get_user(self):
        return self._user

    def upvote(self, user: User, votable: Votable):
        return self.vote_service.upvote(user, votable)
    
    def downvote(self, user: User, votable: Votable):
        return self.vote_service.downvote(user, votable)

    def comment(self, content: str, user: User):
        return self.comment_service.comment(content, user, self)