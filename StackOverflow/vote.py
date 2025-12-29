
from uuid import uuid4
from user import User
from voteType import VoteType

class Vote:

    def __init__(self, user: User, type: VoteType):
        self._id = str(uuid4())
        self._user = user
        self._type = type

    @property
    def get_id(self):
        return self._id
    
    @property
    def get_user(self):
        return self._user
    
    @property
    def get_type(self):
        return self._type

