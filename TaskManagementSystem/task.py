
import threading
from uuid import uuid4
from concreteState import ToDoState
from user import User
from priorityEnum import PriorityLevel
from state import State
class Task:

    def __init__(self, title: str, description: str, due_date: str, priority: PriorityLevel, created_by: User):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.state = ToDoState(self)
        self.priority = priority
        self.lock = threading.Lock()
        self.created_by = created_by
        self.assigned_to = None
        
    def set_state(self, state: State):
        self.state = state

    def get_state(self):
        return self.state
    
    def start_progress(self):
        with self.lock:
            new_state = self.state.start_progress()
            if new_state:
                self.state = new_state

    def complete_task(self):
        with self.lock:
            new_state = self.state.complete_task()
            if new_state:
                self.state = new_state

    def set_priority(self, prioirty: PriorityLevel):
        with self.lock:
            self.priority = prioirty

    def get_priority(self):
        with self.lock:
            return self.priority

    def reopen_task(self):
        with self.lock:
            new_state = self.state.reopen_task()
            if new_state:
                self.state = new_state

    def assign_user(self, user: User):
        with self.lock:
            self.assigned_to = user