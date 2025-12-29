

import threading
from question import Question
from tag import Tag
from user import User
from typing import TYPE_CHECKING, Dict, List

class QuestionService:

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
            self.questions: Dict[str, Question] = {}
            self.tag_to_question: Dict[str, Dict[str, Question]] = {}

    def get_all_questions(self):
        return self.questions
    
    def get_tag_to_questions_map(self):
        return self.tag_to_question

    def insert_question(self, question: Question):
        self.questions[question.get_id] = question

    def insert_question_through_tag(self, question):
        tag = question.get_tag
        if tag not in self.tag_to_question:
            self.tag_to_question[tag] = {}
        self.tag_to_question[tag][question.get_id] = question

    def create_question(self, content: str, user: User, tag: Tag):
        question = Question(content, user, tag)
        self.insert_question(question)
        self.insert_question_through_tag(question)
        return question
