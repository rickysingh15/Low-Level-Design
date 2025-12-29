
from abc import ABC, abstractmethod
from commentService import CommentService
from user import User

class Commentable(ABC):

    def __init__(self):
        super().__init__()
        self.comment_service = CommentService()

    @abstractmethod
    def comment(self, content: str, user: User):
        pass