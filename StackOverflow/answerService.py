
from question import Question
from answer import Answer
import threading
from typing import TYPE_CHECKING, Dict, List
from user import User

class AnswerService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.answers: Dict[str, Answer] = {}
            self.question_to_answer_mapping: Dict[str, List[Answer]] = {}

    def insert_answer_to_mapping(self, question, answer):
        if question.get_id in self.question_to_answer_mapping:
            self.question_to_answer_mapping[question.get_id].append(answer)
        else:
            self.question_to_answer_mapping[question.get_id] = [answer]

    def create_answer(self, question: Question, user: User, content: str):
        answer = Answer(question, user, content)
        self.insert_answer_to_mapping(question, answer)
        return answer