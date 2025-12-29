
from uuid import uuid4
from question import Question
from user import User
from commentable import Commentable
from votable import Votable
from subject import Subject
from observer import Observer
from typing import List

class Answer(Votable, Commentable, Subject):

    def __init__(self, question: Question, user: User, content: str):
        super().__init__()
        self._id = str(uuid4())
        self._content = content
        self._question = question
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
    def get_content(self):
        return self._content
    
    @property
    def get_question(self):
        return self._question
    
    @property
    def get_user(self):
        return self._user
    
    def upvote(self, user: User):
        return self.vote_service.upvote(user, self)
    
    def downvote(self, user: User):
        return self.vote_service.downvote(user, self)

    def comment(self, content: str, user: User):
        return self.comment_service.comment(content, user, self)