

import threading
from tag import Tag
from user import User
from typing import TYPE_CHECKING, Dict, List
if TYPE_CHECKING:
    from commentable import Commentable
    from comment import Comment

class CommentService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.comments = dict()
            self.comment_mapping: Dict[str, List["Comment"]] = {}

    def enter_comment(self, comment, commentable: "Commentable"):
        self.comments[commentable.get_id] = comment
        self.comments[comment.get_id] = comment


    def comment(self, content: str, user: User, commentable: "Commentable"):
        from comment import Comment
        comment = Comment(content, user)
        self.enter_comment(comment, commentable)
        return comment
        