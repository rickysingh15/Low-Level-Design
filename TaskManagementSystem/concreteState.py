
from state import State
from statusEnum import StatusType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from task import Task

class ToDoState(State):

    def __init__(self, task: 'Task'):
        self.status_name = StatusType.PENDING.value
        self.task = task

    def start_progress(self):
        print("State changed from ToDo ---> InProgress")
        return InProgressState(self.task)
    
    def complete_task(self):
        print("Task not in progress")
    
    def reopen_task(self):
        print("Task in to do state")


class InProgressState(State):

    def __init__(self, task: 'Task'):
        self.status_name = StatusType.INPROGRESS.value
        self.task = task

    def start_progress(self):
        print("Task already in progress")
    
    def complete_task(self):
        print("State changed from InProgress ---> Complete")
        return DoneState(self.task)
    
    def reopen_task(self):
        print("Task already in progress")



class DoneState(State):

    def __init__(self, task: 'Task'):
        self.status_name = StatusType.COMPLETE.value
        self.task = task

    def start_progress(self):
        print("Task already completed")
    
    def complete_task(self):
        print("Task already completed")
    
    def reopen_task(self):
        print("State changed from Complete ---> ToDo")
        return ToDoState(self.task)