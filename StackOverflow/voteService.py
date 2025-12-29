
import threading
from vote import Vote
from user import User
from userService import UserService
from typing import TYPE_CHECKING, Dict, List
from voteType import VoteType

if TYPE_CHECKING:
    from votable import Votable

class VoteService:

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
            self.votes = dict()
            self.user_service = UserService()
            self.question_to_votes: Dict[str, Dict[str, Vote]] = {}
            self.answer_to_votes: Dict[str, Dict[str, Vote]] = {}

    def insert_into_question_to_vote_mapping(self, question, vote):
        if question.get_id in self.question_to_votes:
            dct = self.question_to_votes[question.get_id]
            if vote.get_user.get_id not in dct or dct[vote.get_user.get_id].get_type != vote.get_type:
                dct[vote.get_user.get_id] = vote
                return True
            else:
                return False
        else:
            self.question_to_votes[question.get_id] = {}
            self.question_to_votes[question.get_id][vote.get_user.get_id] = vote
            return True

    def insert_into_answer_to_vote_mapping(self, answer, vote):
        if answer.get_id in self.question_to_votes:
            dct = self.answer_to_votes[answer.get_id]
            if vote.get_user.get_id not in dct or dct[vote.get_user.get_id].get_type != vote.get_type:
                dct[vote.get_user.get_id] = vote
                return True
            else:
                return False
        else:
            self.answer_to_votes[answer.get_id] = {}
            self.answer_to_votes[answer.get_id][vote.get_user.get_id] = vote
            return True


    def upvote(self, user: User, votable: "Votable"):
        from question import Question
        from answer import Answer
        
        owner_user = votable.get_user
        print("owner of votable is ", owner_user.get_name)
        vote = Vote(user, VoteType.UP.value)
        insert_status = False
        if isinstance(votable, Question):
            insert_status = self.insert_into_question_to_vote_mapping(votable, vote)
        elif isinstance(votable, Answer):
            insert_status = self.insert_into_answer_to_vote_mapping(votable, vote)
        else:
            print("votable is of undefined type")

        print("insert staus is ", insert_status)
        if insert_status:
            status = self.user_service.add_upvote_to_user(owner_user)
            print("adding vote status is ", status)
        return vote
    

    def downvote(self, user: User, votable: "Votable"):
        from question import Question
        from answer import Answer
        
        owner_user = votable.get_user
        print("owner of votable is ", owner_user.get_name)
        vote = Vote(user, VoteType.DOWN.value)
        insert_status = False
        if isinstance(votable, Question):
            insert_status = self.insert_into_question_to_vote_mapping(votable, vote)
        elif isinstance(votable, Answer):
            insert_status = self.insert_into_answer_to_vote_mapping(votable, vote)
        else:
            print("votable is of undefined type")

        print("insert staus is ", insert_status)
        if insert_status:
            status = self.user_service.add_downvote_to_user(owner_user)
            print("adding vote status is ", status)

        return vote
