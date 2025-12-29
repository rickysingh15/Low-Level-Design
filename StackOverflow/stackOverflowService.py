
from questionService import QuestionService
from answerService import AnswerService
from commentService import CommentService
from userService import UserService
from voteService import VoteService
from tag import Tag
from user import User
from question import Question
from commentable import Commentable
from votable import Votable
from searchStrategy import SearchStrategy

class StackOverflowService:

    def __init__(self):
        self.question_service = QuestionService()
        self.answer_service = AnswerService()
        self.comment_service = CommentService()
        self.vote_service = VoteService()
        self.user_service = UserService()

    def post_question(self, content: str, user: User, tag: Tag):
        return self.question_service.create_question(content, user, tag)

    def answer_question(self, question: Question, user: User, content: str):
        question.update_observers()
        return self.answer_service.create_answer(question, user, content)

    def comment(self, content: str, user: User, commentable: Commentable):
        commentable.update_observers()
        commentable.comment(content, user)

    def upvote(self, user: User, votable: Votable):
        votable.update_observers()
        return votable.upvote(user)
    
    def downvote(self, user: User, votable: Votable):
        votable.update_observers()
        return votable.downvote(user)
        
    def create_user(self, name: str, email: str):
        return self.user_service.create_user(name, email)
    
    def search(self, keyword: str, search_strategy: SearchStrategy):
        return search_strategy.search(keyword, self.question_service)