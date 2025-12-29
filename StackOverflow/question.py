
from uuid import uuid4
from user import User
from commentable import Commentable
from votable import Votable
from tag import Tag
from subject import Subject
from observer import Observer

class Question(Votable, Commentable, Subject):

    def __init__(self, content: str, user: User, tag: Tag):
        super().__init__()
        self._id = str(uuid4())
        self._tag = tag
        self._content = content
        self._user = user
        self.observer = user

    def notify(self):
        self.observer.update()

    def update_observers(self):
        self.notify()

    @property
    def get_id(self):
        return self._id
    
    @property
    def get_tag(self):
        return self._tag
    
    @property
    def get_content(self):
        return self._content
    
    @property
    def get_user(self):
        return self._user
    
    def upvote(self, user: User):
        return self.vote_service.upvote(user, self)
    
    def downvote(self, user: User):
        return self.vote_service.downvote(user, self)

    def comment(self, content: str, user: User):
        return self.comment_service.comment(content, user, self)
        

