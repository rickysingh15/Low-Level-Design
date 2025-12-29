
from abc import ABC, abstractmethod
from voteService import VoteService

class Votable(ABC):

    def __init__(self):
        super().__init__()
        self.vote_service = VoteService()

    @abstractmethod
    def upvote(self):
        pass

    @abstractmethod
    def downvote(self):
        pass